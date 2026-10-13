"""Rebuild static, crawler-readable pages using only Python's standard library."""
from pathlib import Path
from html import escape as e
import json
import runpy
import re
from urllib.parse import quote
ROOT=Path(__file__).resolve().parent
BASE='https://parviznarimani.github.io'
SECTIONS=['hero','about','strategy','research','jewelry','projects','contact']
PAPERS=json.loads((ROOT/'pages/publications/papers.json').read_text())
URLS=[]
def page(path,title,body,description,extra='',home=False):
 if home:
  extra='<meta name="google-site-verification" content="rbT0Tn673XAQ6Pl55nEKZC76ianaJTlekB-ycvQNLEU" />'+extra
 depth=len(Path(path).parts)-1; prefix='../'*depth
 styles=['assets/site.css']+([f'sections/{s}/style.css' for s in SECTIONS] if home else [])+['assets/enhancements.css']
 canonical=BASE+'/'+quote(path.removesuffix('index.html'), safe='/');URLS.append(canonical)
 nav=''.join(f'<a href="{prefix}{url}">{label}</a>' for label,url in [('About','index.html#about'),('Strategy','index.html#strategy'),('Jewelry','index.html#jewelry'),('Publications','pages/publications/index.html'),('Projects','index.html#projects'),('Contacts','index.html#contact')])
 footer='' if home else '<footer class="subpage-footer"><span>Born curious. Building with ❤️ since 1991.</span><span>© Parviz Narimani</span></footer>'
 html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#07090d"><title>{e(title)}</title><link rel="icon" type="image/png" sizes="70x70" href="{prefix}parviznarimaniMainLogo70X.png"><meta name="description" content="{e(description)}"><link rel="canonical" href="{canonical}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{canonical}"><meta property="og:type" content="website">{''.join(f'<link rel="stylesheet" href="{prefix}{s}?v={(ROOT/s).stat().st_mtime_ns}">' for s in styles)}{extra}</head><body><a class="skip-link" href="#main">Skip to content</a><div class="cursor-glow" aria-hidden="true"></div><header class="site-nav"><a class="brand" href="{prefix}index.html"><img class="brand-logo" src="{prefix}parviznarimaniMainLogo70X.png" alt="" width="32" height="32">Parviz Narimani</a><button class="menu-toggle" aria-expanded="false" aria-controls="navigation" aria-label="Toggle navigation"><span class="menu-bar" aria-hidden="true"></span><span class="menu-bar" aria-hidden="true"></span><span class="menu-bar" aria-hidden="true"></span></button><nav id="navigation" aria-label="Primary">{nav}</nav></header><main id="main" class="{'home' if home else 'page-main'}">{body}</main>{footer}<script src="{prefix}assets/site.js?v={(ROOT/"assets/site.js").stat().st_mtime_ns}" defer></script></body></html>'''
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
    if field == 'Progress' and (not value.isdigit() or not 1 <= int(value) <= 100):
     raise ValueError(f'project{i} progress must be an integer from 1 to 100')
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
 progress=(ROOT/f'sections/projects/project{i}/projectProgress.txt').read_text().strip()
 if not progress.isdigit() or not 1 <= int(progress) <= 100: raise ValueError('Project progress must be 1–100')
 if i == 1:
  continue
 page(f'pages/project-{i}/index.html',title+' — Parviz Narimani',f'<a class="back" href="../../index.html#projects">← All projects</a><header class="page-head"><span class="section-label">Independent project / {status}</span><h1>{title}</h1><p class="lead">{desc}</p></header><section class="content-panel"><h2>Direction</h2><p>{focus}</p><h2>Project updates</h2><p>A detailed methodology, milestones and release information will be added here as the project develops.</p><a class="btn" href="../../index.html#contact">Connect about this project ↗</a></section>',desc)
 (ROOT/f'pages/project-{i}/medias').mkdir(exist_ok=True);(ROOT/f'pages/project-{i}/medias/.gitkeep').touch()
ongoing=''
for i in range(1,4):
 directory=ROOT/f'pages/publications/ongoing/paper{i}'
 title=e((directory/'publicationTitle.txt').read_text().strip())
 status=e((directory/'publicationStatus.txt').read_text().strip())
 progress=(directory/'publicationProgress.txt').read_text().strip()
 if not progress.isdigit() or not 1 <= int(progress) <= 100:
  raise ValueError('Publication progress must be 1–100')
 source=f'ongoing/paper{i}'
 ongoing+=f'<tr><td>0{i}</td><th scope="row"><span data-publication-source="{source}/publicationTitle.txt">{title}</span></th><td><span data-publication-source="{source}/publicationStatus.txt">{status}</span><div class="table-project-progress" data-publication-source="{source}/publicationProgress.txt" data-progress aria-label="Publication progress: {progress}%"><span class="progress-number">{progress}</span><span class="progress-unit">%</span></div></td></tr>'
rows=''
for p in sorted(PAPERS,key=lambda x:x['date'],reverse=True):
 slug=p['slug']; local=f'../../pages/publications/papers/{slug}/index.html';pdf=f'../../pages/publications/papers/{slug}/medias/paper.pdf'
 target='https://doi.org/'+p['doi'] if p['kind']=='journal' and p['doi'] else local
 status='<span class="published" aria-label="Published">✓ <span>Published</span></span>' if p['kind']=='journal' else '<span class="preprint">Preprint</span>'
 rows+=f'<tr data-paper data-year="{p["date"][:4]}"><td>{p["date"][:4]}</td><th scope="row"><a class="paper-title" href="{target}">{e(p["title"])} ↗</a><p>{e(p["journal"])} · {e(", ".join(p["authors"]))}</p><a class="read-link" href="{local}">Read this paper now →</a></th><td><div class="paper-actions"><a class="btn silver-download" download href="{pdf}">Download paper ↓</a>{status}</div></td></tr>'
 tags={'citation_title':p['title'],'citation_publication_date':p['date'],'citation_pdf_url':BASE+f'/pages/publications/papers/{slug}/medias/paper.pdf'}
 if p['kind']=='journal':tags['citation_journal_title']=p['journal']
 for key in ['volume','issue','firstpage']:
  if p[key]:tags['citation_'+key]=p[key]
 if p['doi']:tags['citation_doi']=p['doi']
 extra=''.join(f'<meta name="{key}" content="{e(value)}">' for key,value in tags.items())+''.join(f'<meta name="citation_author" content="{e(a)}">' for a in p['authors'])
 journal=f'<a class="btn" href="https://doi.org/{p["doi"]}">{"View journal" if p["kind"]=="journal" else "View Preprint"} ↗</a>' if p['doi'] else ''
 prompt_url=BASE+'/pages/publications/universalScholarlyAnalysisPrompt.md'
 message='Read the paper file fully and follow exactly the instructions in the accompanying Markdown prompt file.\n\nPaper: '+BASE+f'/pages/publications/papers/{slug}/medias/paper.pdf'+'\nAnalysis prompt: '+prompt_url+'\n\nThese are links, not attachments. If either file cannot be accessed in full, ask me to upload it before analyzing.'
 gpt_url='https://chatgpt.com/?q='+quote(message,safe='')
 handoff=f'<details class="gpt-help"><summary>Files and instructions for ChatGPT</summary><p>Opens ChatGPT in a new tab with a prepared message. Files are linked, not automatically uploaded. If needed, download the paper and <a href="../../universalScholarlyAnalysisPrompt.md" download>analysis prompt (.md)</a>, then attach both in ChatGPT. If the message does not appear, copy it below.</p><label for="gpt-message">Prepared message</label><textarea id="gpt-message" readonly rows="7">{e(message)}</textarea></details>'
 body=f'<a class="back" href="../../../../pages/publications/index.html">← Publications</a><article><header class="paper-head"><span class="section-label">{e(p["journal"])} · {p["date"]}</span><h1>{e(p["title"])}</h1><p>{e(", ".join(p["authors"]))}</p>{status}</header><section class="abstract"><h2>Abstract</h2><p>{e(p["abstract"])}</p></section><div class="reader-actions"><a class="btn paper-download" href="medias/paper.pdf" download>Download paper ↓</a><a class="btn gpt-open" href="{e(gpt_url)}" target="_blank" rel="noopener noreferrer">Open on GPT ↗</a>{journal}</div>{handoff}<h2>Full paper</h2><object class="pdf-reader" data="medias/paper.pdf" type="application/pdf"><p>Your browser can’t display the PDF inline. <a href="medias/paper.pdf">Open the full paper</a>.</p></object></article>'
 page(f'pages/publications/papers/{slug}/index.html',p['title']+' — Parviz Narimani',body,p['title'],extra)
body=f'''<a class="back" href="../../index.html#research">← Research</a><header class="page-head publications-head"><span class="section-label">Latest Research &amp; Development</span><div class="publications-title-row"><h1>Knowledge at the Edge of <span class="discovery-glow">Discovery</span></h1><canvas class="publications-thinking-orb" aria-hidden="true"></canvas></div><p class="lead">Publications and ongoing research advancing machine learning, data analysis and intelligent systems for engineering and business managements</p><div class="publication-stats"><span><b>07</b> Journal articles</span><span><b>01</b> Preprint</span><span><b>03</b> Ongoing publications</span></div></header><section><h2>Ongoing publications</h2><p class="ongoing-publications-note">We work on just three publications at a time.</p><div class="table-wrap"><table><caption class="sr-only">Ongoing publications and concepts</caption><thead><tr><th>No.</th><th>Publication</th><th>Status</th></tr></thead><tbody>{ongoing}</tbody></table></div></section><section class="publications"><div class="table-heading"><h2>Published papers & preprints</h2><div class="filters" hidden><label>Search papers<input id="paper-search" type="search" placeholder="Title, author, journal…"></label><label>Year<select id="paper-year"><option value="">All years</option>{''.join(f'<option>{y}</option>' for y in sorted(set(p['date'][:4] for p in PAPERS),reverse=True))}</select></label></div></div><p class="table-note">Journal titles link to the publisher where available. Read every paper here using its reading link.</p><p id="result-count" role="status" aria-live="polite"></p><div class="table-wrap"><table><caption class="sr-only">Published research and preprints with downloads</caption><thead><tr><th>Year</th><th>Paper / Authors</th><th>Resources / Status</th></tr></thead><tbody>{rows}</tbody></table></div><p id="no-results" hidden>No papers match. Try another title, author or year.</p></section>'''
page('pages/publications/index.html','Publications — Parviz Narimani',body,'Journal articles, preprints and ongoing projects by Parviz Narimani. Read papers, download PDFs and explore datasets.')
jewelry_description=e((ROOT/'pages/jewelry/jewelryDescription.txt').read_text().strip())
jewelry_description=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',jewelry_description)
gallery='<section class="product-gallery" aria-labelledby="imagery-title"><h2 id="imagery-title">Professional Imaginary</h2><p class="lead">Professional gold and jewelry imagery brings craftsmanship into focus, connecting digital branding with the digital transformation of the industry.</p><div class="product-slideshow" aria-roledescription="carousel" aria-label="Gold and jewelry product imagery"><div class="product-stage" tabindex="0" aria-label="Product images. Use left and right arrow keys to browse.">'
for i in range(1,7):
 gallery+=f'<figure class="product-slide" data-position="{ "center" if i==1 else "right" if i==2 else "left" if i==6 else "hidden" }" aria-label="Image {i} of 6"><img src="medias/Image{i}.png" alt="Gold and jewelry product imagery, photograph {i}" loading="lazy"></figure>'
gallery+='</div><div class="product-controls" hidden><button type="button" data-product-prev aria-label="Previous product image">←</button><div class="product-dots" aria-label="Choose a product image"><button type="button" data-product-dot="0" aria-label="Show product image 1" aria-pressed="false"></button><button type="button" data-product-dot="1" aria-label="Show product image 2" aria-pressed="false"></button><button type="button" data-product-dot="2" aria-label="Show product image 3" aria-pressed="false"></button><button type="button" data-product-dot="3" aria-label="Show product image 4" aria-pressed="false"></button><button type="button" data-product-dot="4" aria-label="Show product image 5" aria-pressed="false"></button><button type="button" data-product-dot="5" aria-label="Show product image 6" aria-pressed="false"></button></div><button type="button" data-product-next aria-label="Next product image">→</button></div><p class="sr-only product-status" aria-live="polite"></p></div></section>'
transformation=(ROOT/'pages/jewelry/digitalTransformation.html').read_text()
jewelry_connect='<section class="jewelry-connect" aria-labelledby="jewelry-connect-title"><h2 id="jewelry-connect-title">Let’s have a conversation about how we could collaborate</h2><div class="jewelry-connect-links"><a href="https://wa.me/989363084896" target="_blank" rel="noopener" aria-label="Chat with Parviz Narimani on WhatsApp">WhatsApp</a><a href="mailto:parviznarimani91@gmail.com" aria-label="Email Parviz Narimani">Email</a></div></section>'
page('pages/jewelry/index.html','Gold & Jewelry — Parviz Narimani',f'<a class="back" href="../../index.html#jewelry">← Gold &amp; Jewelry</a><header class="page-head jewelry-page-hero"><div class="jewelry-page-copy"><span class="section-label">Gold &amp; Jewelry Profession</span><h1>Eternal Light</h1><p class="lead jewelry-description" data-source="jewelryDescription.txt">{jewelry_description}</p></div><div class="jewelry-model-frame"><img src="medias/modelNumber12Final.png" alt="Model wearing a gold leaf-shaped earring and a gold sequined outfit" width="1600" height="2477" fetchpriority="high"></div></header>{gallery}{transformation}{jewelry_connect}','Gold and jewelry manufacturing, craftsmanship, digital transformation and artificial intelligence in the work of Parviz Narimani.')
page('404.html','Page not found — Parviz Narimani','<section class="error-page"><div class="error-code" aria-hidden="true">404</div><h1><span class="sr-only">404: </span>Page not found!</h1><a class="btn error-return" href="index.html">Return →</a></section>','The requested page could not be found.')
runpy.run_path(str(ROOT/'pages/blog/build.py'))['build_blog'](page, BASE)
# Index complete public pages and paper PDFs, not section fragments or error pages.
# Homepage sections are already included in the crawlable homepage HTML.
from xml.etree import ElementTree as ET
sitemap_urls=[u for u in URLS if not u.endswith('404.html')]
for paper in PAPERS:
 pdf_path=f"pages/publications/papers/{paper['slug']}/medias/paper.pdf"
 if not (ROOT/pdf_path).is_file():
  raise FileNotFoundError(f'Missing sitemap paper: {pdf_path}')
 sitemap_urls.append(BASE+'/'+quote(pdf_path, safe='/'))
namespace='http://www.sitemaps.org/schemas/sitemap/0.9'
ET.register_namespace('', namespace)
urlset=ET.Element(f'{{{namespace}}}urlset')
for url in dict.fromkeys(sitemap_urls):
 entry=ET.SubElement(urlset, f'{{{namespace}}}url')
 ET.SubElement(entry, f'{{{namespace}}}loc').text=url
ET.indent(urlset, space='  ')
ET.ElementTree(urlset).write(ROOT/'sitemap.xml', encoding='utf-8', xml_declaration=True)
(ROOT/'robots.txt').write_text(f'''# Parviz Narimani - robots.txt
# Website: {BASE}/

# General search engine crawlers
User-agent: *
Allow: /

# ChatGPT Search
User-agent: OAI-SearchBot
Allow: /

# OpenAI GPTBot
User-agent: GPTBot
Allow: /

# Google Search
User-agent: Googlebot
Allow: /

# Google Image Search
User-agent: Googlebot-Image
Allow: /

# Bing Search and Microsoft Copilot
User-agent: Bingbot
Allow: /

# Sitemap
Sitemap: {BASE}/sitemap.xml
''', encoding='utf-8')
(ROOT/'.nojekyll').touch()
print(f'Built {len(URLS)} static pages.')
