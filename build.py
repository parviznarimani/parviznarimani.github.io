"""Rebuild static, crawler-readable pages using only Python's standard library."""
from pathlib import Path
from html import escape as e
import json
import re
ROOT=Path(__file__).resolve().parent
BASE='https://parviznarimani.github.io'
SECTIONS=['hero','about','strategy','research','jewelry','projects','contact']
PAPERS=json.loads((ROOT/'sections/publications/papers.json').read_text())
URLS=[]
def page(path,title,body,description,extra='',home=False):
 depth=len(Path(path).parts)-1; prefix='../'*depth
 styles=['assets/site.css']+([f'sections/{s}/style.css' for s in SECTIONS] if home else [])+['assets/enhancements.css']
 canonical=BASE+'/'+path.removesuffix('index.html');URLS.append(canonical)
 nav=''.join(f'<a href="{prefix}{url}">{label}</a>' for label,url in [('About','index.html#about'),('Strategy','index.html#strategy'),('Jewelry','index.html#jewelry'),('Publications','pages/publications/index.html'),('Projects','index.html#projects'),('Contacts','index.html#contact')])
 html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#07090d"><title>{e(title)}</title><meta name="description" content="{e(description)}"><link rel="canonical" href="{canonical}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{canonical}"><meta property="og:type" content="website">{''.join(f'<link rel="stylesheet" href="{prefix}{s}?v={(ROOT/s).stat().st_mtime_ns}">' for s in styles)}{extra}</head><body><a class="skip-link" href="#main">Skip to content</a><div class="cursor-glow" aria-hidden="true"></div><header class="site-nav"><a class="brand" href="{prefix}index.html"><i></i>Parviz Narimani</a><button class="menu-toggle" aria-expanded="false" aria-controls="navigation" aria-label="Toggle navigation"><span class="menu-bar" aria-hidden="true"></span><span class="menu-bar" aria-hidden="true"></span><span class="menu-bar" aria-hidden="true"></span></button><nav id="navigation" aria-label="Primary">{nav}</nav></header><main id="main" class="{'home' if home else 'page-main'}">{body}</main><script src="{prefix}assets/site.js?v={(ROOT/"assets/site.js").stat().st_mtime_ns}" defer></script></body></html>'''
 dest=ROOT/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(html)
def section_html(name):
 html=(ROOT/f'sections/{name}/section.html').read_text()
 sources={'projects':('ongoingProjectsAbout.txt','{{PROJECTS_DESCRIPTION}}'),'jewelry':('jewelryDirectionAbout.txt','{{JEWELRY_DESCRIPTION}}'),'research':('researchDirections.txt','{{RESEARCH_DESCRIPTION}}'),'strategy':('aboutStartegy.txt','{{STRATEGY_DESCRIPTION}}'),'hero':('aboutMe.txt','{{ABOUT_ME}}'),'about':('aboutDescription.txt','{{ABOUT_DESCRIPTION}}')}
 if name in sources:
  filename,placeholder=sources[name]
  biography=e((ROOT/f'sections/{name}'/filename).read_text().strip())
  biography=re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', biography)
  if name == 'research':
   biography=re.sub(r'\bpublications\b', '<span class="publication-glow">publications</span>', biography, count=1)
  html=html.replace(placeholder, biography)
 if name == 'projects':
  for i in range(1,4):
   for field in ['Status','Name','Description','Progress']:
    value=(ROOT/f'sections/projects/project{i}/project{field}.txt').read_text().strip()
    if field == 'Progress' and (not value.isdigit() or not 1 <= int(value) <= 99):
     raise ValueError(f'project{i} progress must be an integer from 1 to 99')
    html=html.replace('{{PROJECT_'+str(i)+'_'+field+'}}',e(value))
 return html

page('index.html','Parviz Narimani — Strategy · Research · Design', '\n'.join(section_html(s) for s in SECTIONS),'Strategy, engineering research, machine learning and jewelry design. Explore Parviz Narimani’s work, publications and independent projects.', '<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@type':'Person','name':'Parviz Narimani','url':BASE,'sameAs':['https://github.com/parviznarimani']})+'</script>',True)
projects=[]
for i in range(1,4):
 directory=ROOT/f'sections/projects/project{i}'
 read=lambda field: (directory/f'project{field}.txt').read_text().strip()
 projects.append((e(read('Name')),e(read('Description')),e(read('Status'))))
ongoing=''
for i,(title,desc,status) in enumerate(projects,1):
 focus=desc
 ongoing+=f'<tr><td>0{i}</td><th scope="row"><a href="../project-{i}/index.html">{title} ↗</a><p>{desc}</p></th><td>{status}</td></tr>'
 page(f'pages/project-{i}/index.html',title+' — Parviz Narimani',f'<a class="back" href="../../index.html#projects">← All projects</a><header class="page-head"><span class="section-label">Independent project / {status}</span><h1>{title}</h1><p class="lead">{desc}</p></header><section class="content-panel"><h2>Direction</h2><p>{focus}</p><h2>Project updates</h2><p>A detailed methodology, milestones and release information will be added here as the project develops.</p><a class="btn" href="../../index.html#contact">Connect about this project ↗</a></section>',desc)
 (ROOT/f'pages/project-{i}/medias').mkdir(exist_ok=True);(ROOT/f'pages/project-{i}/medias/.gitkeep').touch()
rows=''
for p in sorted(PAPERS,key=lambda x:x['date'],reverse=True):
 slug=p['slug']; local=f'../../sections/publications/papers/{slug}/index.html';pdf=f'../../sections/publications/papers/{slug}/medias/paper.pdf'
 target='https://doi.org/'+p['doi'] if p['kind']=='journal' and p['doi'] else local
 status='<span class="published" aria-label="Published">✓ <span>Published</span></span>' if p['kind']=='journal' else '<span class="preprint">Preprint</span>'
 dataset=f'<a class="btn" href="{e(p["dataset_url"])}">Dataset ↗</a>' if p['dataset_url'] else '<button class="btn" disabled title="Dataset repository has not been supplied">Dataset unavailable</button>'
 rows+=f'<tr data-paper data-year="{p["date"][:4]}"><td>{p["date"][:4]}</td><th scope="row"><a class="paper-title" href="{target}">{e(p["title"])} ↗</a><p>{e(p["journal"])} · {e(", ".join(p["authors"]))}</p><a class="read-link" href="{local}">Read paper on this website →</a></th><td><div class="paper-actions"><a class="btn" download href="{pdf}">Download paper ↓</a>{dataset}{status}</div></td></tr>'
 tags={'citation_title':p['title'],'citation_publication_date':p['date'],'citation_pdf_url':BASE+f'/sections/publications/papers/{slug}/medias/paper.pdf'}
 if p['kind']=='journal':tags['citation_journal_title']=p['journal']
 for key in ['volume','issue','firstpage']:
  if p[key]:tags['citation_'+key]=p[key]
 if p['doi']:tags['citation_doi']=p['doi']
 extra=''.join(f'<meta name="{key}" content="{e(value)}">' for key,value in tags.items())+''.join(f'<meta name="citation_author" content="{e(a)}">' for a in p['authors'])
 journal=f'<a class="btn" href="https://doi.org/{p["doi"]}">{"View journal" if p["kind"]=="journal" else "View preprint source"} ↗</a>' if p['doi'] else ''
 body=f'<a class="back" href="../../../../pages/publications/index.html">← Publications</a><article><header class="paper-head"><span class="section-label">{e(p["journal"])} · {p["date"]}</span><h1>{e(p["title"])}</h1><p>{e(", ".join(p["authors"]))}</p>{status}</header><section class="abstract"><h2>Abstract</h2><p>{e(p["abstract"])}</p></section><div class="reader-actions"><a class="btn primary" href="medias/paper.pdf" download>Download paper ↓</a><a class="btn" href="medias/paper.pdf">Open PDF ↗</a>{journal}</div><h2>Full paper</h2><object class="pdf-reader" data="medias/paper.pdf" type="application/pdf"><p>Your browser can’t display the PDF inline. <a href="medias/paper.pdf">Open the full paper</a>.</p></object></article>'
 page(f'sections/publications/papers/{slug}/index.html',p['title']+' — Parviz Narimani',body,p['title'],extra)
body=f'''<a class="back" href="../../index.html#research">← Research</a><header class="page-head"><span class="section-label">Research & development / Index</span><h1>Ideas, tested<br><span>Knowledge, shared</span></h1><p class="lead">Ongoing systems and published research in machine learning, manufacturing and engineering.</p><div class="publication-stats"><span><b>07</b> Journal articles</span><span><b>01</b> Preprint</span><span><b>03</b> Development tracks</span></div></header><section><h2>Ongoing projects</h2><div class="table-wrap"><table><caption class="sr-only">Ongoing projects and concepts</caption><thead><tr><th>No.</th><th>Project</th><th>Status</th></tr></thead><tbody>{ongoing}</tbody></table></div></section><section class="publications"><div class="table-heading"><h2>Published papers & preprints</h2><div class="filters" hidden><label>Search papers<input id="paper-search" type="search" placeholder="Title, author, journal…"></label><label>Year<select id="paper-year"><option value="">All years</option>{''.join(f'<option>{y}</option>' for y in sorted(set(p['date'][:4] for p in PAPERS),reverse=True))}</select></label></div></div><p class="table-note">Journal titles link to the publisher where available. Read every paper here using its reading link.</p><p id="result-count" role="status" aria-live="polite"></p><div class="table-wrap"><table><caption class="sr-only">Published research and preprints with downloads</caption><thead><tr><th>Year</th><th>Paper / Authors</th><th>Resources / Status</th></tr></thead><tbody>{rows}</tbody></table></div><p id="no-results" hidden>No papers match. Try another title, author or year.</p></section>'''
page('pages/publications/index.html','Publications — Parviz Narimani',body,'Journal articles, preprints and ongoing projects by Parviz Narimani. Read papers, download PDFs and explore datasets.')
page('pages/jewelry/index.html','Gold & Jewelry — Parviz Narimani','<a class="back" href="../../index.html#jewelry">← Gold &amp; Jewelry</a><header class="page-head"><span class="section-label">Gold &amp; Jewelry Profession</span><h1>Eternal Light</h1><p class="lead">More about my work in gold and jewelry is coming soon.</p></header>','Explore the gold and jewelry work of Parviz Narimani.')
page('404.html','Page not found — Parviz Narimani','<section class="error-page"><div class="error-code" aria-hidden="true">404</div><h1><span class="sr-only">404: </span>Page not found!</h1><a class="btn error-return" href="index.html">Return →</a></section>','The requested page could not be found.')
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{u}</loc></url>' for u in URLS if not u.endswith('404.html'))+'</urlset>')
(ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')
(ROOT/'.nojekyll').touch()
print(f'Built {len(URLS)} static pages.')
