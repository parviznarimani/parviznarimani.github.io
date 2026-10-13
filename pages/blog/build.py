"""Build the blog through the shared site renderer; no third-party dependencies."""
from pathlib import Path
from datetime import date
from html import escape
from urllib.parse import quote
import re
import runpy
import json

BLOG = Path(__file__).resolve().parent

def inline(text):
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escape(text))

def article_text(text):
    blocks = []
    for block in re.split(r'\n\s*\n', text.strip()):
        if block.startswith('### '):
            blocks.append('<h3>'+inline(block[4:])+'</h3>')
        elif block.startswith('## '):
            blocks.append('<h2>'+inline(block[3:])+'</h2>')
        else:
            blocks.append('<p>'+inline(block).replace('\n', '<br>')+'</p>')
    return '\n'.join(blocks)

def build_blog(page, base):
    posts = []
    for folder in BLOG.iterdir():
        if not folder.is_dir() or folder.name.startswith(('_', '.')):
            continue
        match = re.fullmatch(r'Post\d+\[(\d{4}-\d{2}-\d{2})\]', folder.name)
        if not match:
            raise ValueError(f'Blog folder must use Post1[YYYY-MM-DD]: {folder.name}')
        published = date.fromisoformat(match[1])
        fields = {}
        for name in ('title', 'metadescription', 'mainText'):
            fields[name] = (folder / (name+'.txt')).read_text().strip()
            if not fields[name]:
                raise ValueError(f'{folder.name}/{name}.txt must not be empty')
        images = sorted(p for p in (folder/'medias').iterdir() if p.suffix.lower() in ('.png','.jpg','.jpeg','.webp','.avif','.svg'))
        cover = next((p for p in images if p.stem.lower()=='cover'), images[0] if images else None)
        if cover is None:
            raise ValueError(f'Add a cover image to {folder.name}/medias/')
        posts.append((published, folder, fields, cover))
    posts.sort(key=lambda row:(row[0], row[1].name), reverse=True)
    cards=[]
    for published, folder, fields, cover in posts:
        slug=quote(folder.name, safe='')
        cover_name=quote(cover.name, safe='')
        url=base+'/pages/blog/'+slug+'/'
        title=escape(fields['title'])
        desc=escape(fields['metadescription'])
        cards.append(f'<article class="blog-card"><a class="blog-cover" href="{slug}/index.html" aria-label="Read {title}"><img src="{slug}/medias/{cover_name}" alt="" loading="lazy"></a><div class="blog-card-copy"><time datetime="{published}">{published}</time><h2><a href="{slug}/index.html">{title}</a></h2><p>{desc}</p><a class="read-link" href="{slug}/index.html">Read more →</a></div></article>')
        sources_path=folder/'sources.json'
        source_html=''
        if sources_path.exists():
            sources=json.loads(sources_path.read_text())
            source_html='<section class="blog-sources"><h2>Sources and further reading</h2><ul>'
            for source in sources:
                if not source['url'].startswith('https://'):
                    raise ValueError('Source URLs must use HTTPS')
                source_html+='<li><a href="'+escape(source['url'],quote=True)+'">'+escape(source['title'])+'</a></li>'
            source_html+='</ul></section>'
        body=f'<a class="back" href="../index.html">← Blog</a><article class="blog-article"><header class="page-head"><time datetime="{published}">{published}</time><h1>{title}</h1><p class="lead">{desc}</p></header><img class="blog-article-cover" src="medias/{cover_name}" alt=""><div class="blog-prose">{article_text(fields["mainText"])}{source_html}</div></article>'
        schema={'@context':'https://schema.org','@type':'BlogPosting','headline':fields['title'],'description':fields['metadescription'],'datePublished':str(published),'author':{'@type':'Person','name':'Parviz Narimani','url':base+'/'},'mainEntityOfPage':url,'image':url+'medias/'+cover_name}
        extra='<script type="application/ld+json">'+json.dumps(schema).replace('<','\\u003c')+'</script>'
        page('pages/blog/'+folder.name+'/index.html',fields['title']+' — Parviz Narimani',body,fields['metadescription'],extra)
    body='<a class="back" href="../../index.html">← Home</a><header class="page-head"><h1>Blog</h1></header><div class="blog-list">'+(''.join(cards) if cards else '<p class="lead">Articles will appear here when the first post is published.</p>')+'</div>'
    page('pages/blog/index.html','Blog — Parviz Narimani',body,'Articles by Parviz Narimani on strategy, machine learning, research, and gold and jewelry.')

if __name__ == '__main__':
    # The shared build calls build_blog, then writes one complete site sitemap.
    runpy.run_path(str(BLOG.parents[1]/'build.py'), run_name='__main__')
