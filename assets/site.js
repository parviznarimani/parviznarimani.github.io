'use strict';
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
function closeMenu() { toggle?.setAttribute('aria-expanded', 'false'); nav?.classList.remove('open'); }
toggle?.addEventListener('click', () => { const open = toggle.getAttribute('aria-expanded') !== 'true'; toggle.setAttribute('aria-expanded', String(open)); nav.classList.toggle('open', open); });
nav?.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', event => { if (event.key === 'Escape' && nav?.classList.contains('open')) { closeMenu(); toggle.focus(); } });
const reduced = matchMedia('(prefers-reduced-motion: reduce)');
if (!reduced.matches && 'IntersectionObserver' in window) {
 const observer = new IntersectionObserver(entries => entries.forEach(entry => { if (entry.isIntersecting) { entry.target.animate([{opacity: .35, transform: 'translateY(18px)'}, {opacity: 1, transform: 'none'}], {duration: 650, easing: 'ease-out'}); observer.unobserve(entry.target); } }), {threshold: .08});
 document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
}
if (!reduced.matches && matchMedia('(pointer:fine)').matches) {
 const glow = document.querySelector('.cursor-glow');
 window.addEventListener('pointermove', event => { if (glow) { glow.style.left = event.clientX+'px'; glow.style.top = event.clientY+'px'; } }, {passive:true});
 document.querySelectorAll('[data-tilt]').forEach(card => { card.addEventListener('pointermove', event => { const rect=card.getBoundingClientRect(); card.style.transform=`perspective(1000px) rotateX(${-(event.clientY-rect.top-rect.height/2)/80}deg) rotateY(${(event.clientX-rect.left-rect.width/2)/80}deg)`; }); card.addEventListener('pointerleave',()=>card.style.transform=''); });
}
const search = document.querySelector('#paper-search');
if (search) {
 document.querySelector('.filters').hidden = false;
 const year = document.querySelector('#paper-year'); const rows = [...document.querySelectorAll('[data-paper]')];
 function filter() { const query = search.value.trim().toLocaleLowerCase(); let count=0; rows.forEach(row => { row.hidden = !row.textContent.toLocaleLowerCase().includes(query) || (year.value !== '' && row.dataset.year !== year.value); if (!row.hidden) count++; }); document.querySelector('#result-count').textContent=`${count} of ${rows.length} papers`; document.querySelector('#no-results').hidden=count>0; }
 search.addEventListener('input',filter); year.addEventListener('change',filter); filter();
}

// Jewelry carousel: centered selection, circular navigation and touch gestures.
const carousel = document.querySelector('.jewelry-carousel');
if (carousel) {
 const stage = carousel.querySelector('.jewelry-stage');
 const slides = [...stage.querySelectorAll('.jewel')];
 const dots = [...carousel.querySelectorAll('[data-slide]')];
 let active = 1;
 function showSlide(index) {
  active = (index + slides.length) % slides.length;
  slides.forEach((slide, i) => {
   const offset = (i - active + slides.length) % slides.length;
   slide.dataset.position = offset === 0 ? 'center' : offset === 1 ? 'right' : 'left';
  });
  dots.forEach((dot, i) => dot.setAttribute('aria-pressed', String(i === active)));
  carousel.querySelector('.jewelry-status').textContent = `${slides[active].querySelector('h3').textContent}, slide ${active + 1} of ${slides.length}`;
 }
 carousel.querySelector('.jewelry-controls').hidden = false;
 carousel.querySelector('.jewelry-prev').addEventListener('click', () => showSlide(active - 1));
 carousel.querySelector('.jewelry-next').addEventListener('click', () => showSlide(active + 1));
 dots.forEach((dot, i) => dot.addEventListener('click', () => showSlide(i)));
 stage.addEventListener('keydown', event => {
  if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') { event.preventDefault(); showSlide(active + (event.key === 'ArrowRight' ? 1 : -1)); }
 });
 let start = null, suppressClick = false;
 stage.addEventListener('pointerdown', event => { start = {x:event.clientX,y:event.clientY}; suppressClick = false; });
 stage.addEventListener('pointerup', event => {
  if (!start) return;
  const dx = event.clientX-start.x, dy = event.clientY-start.y;
  if (Math.abs(dx)>45 && Math.abs(dx)>Math.abs(dy)) { suppressClick = true; showSlide(active + (dx<0 ? 1 : -1)); }
  start = null;
 });
 stage.addEventListener('pointercancel', () => { start = null; });
 slides.forEach((slide, i) => slide.addEventListener('click', () => { if (!suppressClick) showSlide(i); suppressClick = false; }));
}

// Keep the editable biography current; static generated text remains for crawlers
// and when JavaScript or the text request is unavailable.
document.querySelectorAll('.hero-biography[data-source], .about-description[data-source], .strategy-description[data-source], .research-description[data-source], .jewelry-description[data-source], .projects-description[data-source]').forEach(biography => {
 fetch(biography.dataset.source, {cache:'no-store'})
  .then(response => { if (!response.ok) throw new Error('Biography unavailable'); return response.text(); })
  .then(text => {
   const fragment = document.createDocumentFragment();
   text.trim().split(/(\*\*.*?\*\*)/g).forEach(part => {
    if (part.startsWith('**') && part.endsWith('**')) { const strong=document.createElement('strong'); strong.textContent=part.slice(2,-2); fragment.append(strong); }
    else fragment.append(document.createTextNode(part));
   });
   if (biography.classList.contains('research-description')) {
    const walker = document.createTreeWalker(fragment, NodeFilter.SHOW_TEXT);
    let node;
    while ((node = walker.nextNode())) {
     const match = /\bpublications\b/.exec(node.textContent);
     if (!match) continue;
     const word = node.splitText(match.index);
     word.splitText(match[0].length);
     const glow = document.createElement('span');
     glow.className = 'publication-glow';
     glow.textContent = word.textContent;
     word.replaceWith(glow);
     break;
    }
   }
   biography.replaceChildren(fragment);
  }).catch(() => { /* Preserve the statically rendered biography. */ });
});

// Read each project field independently, retaining the generated fallback on failure.
document.querySelectorAll('[data-project-source]').forEach(field => {
 fetch(field.dataset.projectSource, {cache:'no-store'})
 .then(response => { if (!response.ok) throw new Error('Project field unavailable'); return response.text(); })
 .then(text => {
  const value=text.trim();
  if (field.hasAttribute('data-progress')) {
   if (!/^\d+$/.test(value) || Number(value)<1 || Number(value)>99) return;
   field.querySelector('.progress-number').textContent=Number(value);
   field.setAttribute('aria-label', 'Project progress: '+Number(value)+'%');
  } else field.textContent=value;
 }).catch(() => {});
});
