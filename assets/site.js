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
document.querySelectorAll('[data-project-source], [data-publication-source]').forEach(field => {
 fetch(field.dataset.projectSource || field.dataset.publicationSource, {cache:'no-store'})
 .then(response => { if (!response.ok) throw new Error('Project field unavailable'); return response.text(); })
 .then(text => {
  const value=text.trim();
  if (field.hasAttribute('data-progress')) {
   if (!/^\d+$/.test(value) || Number(value)<1 || Number(value)>100) return;
   field.querySelector('.progress-number').textContent=Number(value);
   field.setAttribute('aria-label', (field.dataset.publicationSource ? 'Publication' : 'Project')+' progress: '+Number(value)+'%');
  } else field.textContent=value;
 }).catch(() => {});
});

// Original dotted-sphere backdrop inspired by Jakub Antalik's thinking-orbs.
(() => {
 const canvas=document.querySelector('.portrait-thinking-orb, .publications-thinking-orb');
 if (!canvas) return;
 const ctx=canvas.getContext('2d');
 if (!ctx) return;
 const motion=matchMedia('(prefers-reduced-motion: reduce)');
 const points=Array.from({length:1100},(_,i)=>{
  const y=1-2*(i+.5)/1100, radius=Math.sqrt(1-y*y), angle=i*Math.PI*(3-Math.sqrt(5));
  return [Math.cos(angle)*radius,y,Math.sin(angle)*radius];
 });
 let size=0, visible=false, frame=0, previous=0, phase=0;
 function draw() {
  const dpr=Math.min(devicePixelRatio||1,2);
  ctx.setTransform(dpr,0,0,dpr,0,0); ctx.clearRect(0,0,size,size);
  // Adapted from thinking-orbs engine/ribbon.ts (MIT, Jakub Antalik).
  // The demo's large “Thinking” example uses the composing/ribbon state.
  const radius=size*.46, t=phase*.25, dots=[];
  function project(x,y,z,r,alpha) {
   const spin=canvas.classList.contains('publications-thinking-orb') ? phase*.12 : 0;
   const rx=x*Math.cos(spin)+z*Math.sin(spin), rz=z*Math.cos(spin)-x*Math.sin(spin);
   x=rx; z=rz;
   const tilt=.3, py=y*Math.cos(tilt)-z*Math.sin(tilt), pz=y*Math.sin(tilt)+z*Math.cos(tilt);
   dots.push({x:size/2+x*radius,y:size/2+py*radius,z:pz,r,alpha});
  }
  for (let i=0;i<points.length;i+=4) {
   const [x,y,z]=points[i]; project(x,y,z,.7*size/500,.12);
  }
  const tilt=.55, lanes=9, segments=140;
  for(let w=0;w<lanes;w++) {
   const laneOff=(w-(lanes-1)/2)*.045;
   const edge=Math.abs(w-(lanes-1)/2)/((lanes-1)/2);
   for(let k=0;k<segments;k++) {
    const a=k/segments*Math.PI*2;
    const wob=.16*Math.sin(a*3-t*1.7+w*.22)+.07*Math.sin(a*5+t*1.1);
    const off=laneOff+wob;
    const x=Math.cos(a), y=Math.cos(tilt)*Math.sin(a)-Math.sin(tilt)*off,
          z=Math.sin(tilt)*Math.sin(a)+Math.cos(tilt)*off;
    const length=Math.hypot(x,y,z), depth=(z/length+1)/2;
    project(x/length,y/length,z/length,(.85+depth*.9)*(1-.25*edge)*size/500,.3+.5*depth);
   }
  }
  dots.sort((a,b)=>a.z-b.z);
  for(const dot of dots) {
   ctx.beginPath(); ctx.arc(dot.x,dot.y,dot.r,0,Math.PI*2);
   ctx.fillStyle=`rgba(190,225,233,${dot.alpha})`; ctx.fill();
  }
 }
 function tick(now) {
  frame=0;
  if (previous) phase+=Math.min((now-previous)/1000,.05);
  previous=now; draw();
  if (visible&&!document.hidden&&!motion.matches) frame=requestAnimationFrame(tick);
 }
 function sync() {
  cancelAnimationFrame(frame); frame=0; previous=0;
  draw();
  if (visible&&!document.hidden&&!motion.matches) frame=requestAnimationFrame(tick);
 }
 new ResizeObserver(()=>{
  size=canvas.getBoundingClientRect().width;
  const dpr=Math.min(devicePixelRatio||1,2);
  canvas.width=Math.round(size*dpr); canvas.height=Math.round(size*dpr); draw();
 }).observe(canvas);
 new IntersectionObserver(([entry])=>{ visible=entry.isIntersecting; sync(); }).observe(canvas);
 document.addEventListener('visibilitychange',sync);
 motion.addEventListener('change',sync);
})();

// Automatic product gallery, with manual controls and accessible pause behavior.
(() => {
 const gallery=document.querySelector('.product-slideshow'); if(!gallery) return;
 const slides=[...gallery.querySelectorAll('.product-slide')], stage=gallery.querySelector('.product-stage');
 const dots=[...gallery.querySelectorAll('[data-product-dot]')];
 let active=0, paused=reduced.matches, hover=false, focused=false, visible=false, timer;
 function show(index,announce=false) {
  active=(index+slides.length)%slides.length;
  slides.forEach((slide,i)=>{
   const offset=(i-active+slides.length)%slides.length;
   slide.dataset.position=offset===0?'center':offset===1?'right':offset===slides.length-1?'left':'hidden';
   slide.setAttribute('aria-hidden',String(offset!==0));
  });
  dots.forEach((dot,i)=>dot.setAttribute('aria-pressed',String(i===active)));
  if(announce) gallery.querySelector('.product-status').textContent=`Image ${active+1} of ${slides.length}`;
 }
 function schedule() {
  clearInterval(timer);
  if(!paused&&!hover&&!focused&&visible&&!document.hidden) timer=setInterval(()=>show(active+1),5500);
 }
 gallery.querySelector('.product-controls').hidden=false;
 gallery.querySelector('[data-product-prev]').onclick=()=>{show(active-1,true);schedule();};
 gallery.querySelector('[data-product-next]').onclick=()=>{show(active+1,true);schedule();};
 dots.forEach((dot,i)=>dot.addEventListener('click',()=>{show(i,true);schedule();}));
 stage.addEventListener('keydown',e=>{if(['ArrowLeft','ArrowRight'].includes(e.key)){e.preventDefault();show(active+(e.key==='ArrowRight'?1:-1),true);schedule();}});
 gallery.addEventListener('mouseenter',()=>{hover=true;schedule();});
 gallery.addEventListener('mouseleave',()=>{hover=false;schedule();});
 gallery.addEventListener('focusin',()=>{focused=true;schedule();});
 gallery.addEventListener('focusout',e=>{if(!gallery.contains(e.relatedTarget)){focused=false;schedule();}});
 document.addEventListener('visibilitychange',schedule);
 reduced.addEventListener('change',()=>{paused=reduced.matches;schedule();});
 new IntersectionObserver(([entry])=>{visible=entry.isIntersecting;schedule();}).observe(gallery);
 show(0);
})();
