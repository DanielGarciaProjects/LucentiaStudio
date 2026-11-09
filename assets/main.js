(()=>{const q=(s,c=document)=>[...c.querySelectorAll(s)],rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
const mt=q('.mt')[0],nav=q('#nav')[0];
mt?.addEventListener('click',()=>{const o=nav.classList.toggle('open');mt.setAttribute('aria-expanded',o)});
q('#nav a').forEach(a=>a.addEventListener('click',()=>nav.classList.remove('open')));
if(!rm){ // transição suave entre páginas
 q('a[href^="/"]').forEach(a=>a.addEventListener('click',e=>{const u=new URL(a.href);if(e.metaKey||e.ctrlKey||a.target||u.pathname===location.pathname)return;e.preventDefault();document.body.classList.add('out');setTimeout(()=>location.href=a.href,300)}));
 addEventListener('pageshow',()=>document.body.classList.remove('out'));
 // luz que acompanha o cursor no hero
 const h=q('.hero')[0],g=q('.glow')[0];h&&g&&h.addEventListener('pointermove',e=>{const r=h.getBoundingClientRect();g.style.setProperty('--mx',e.clientX-r.left+'px');g.style.setProperty('--my',e.clientY-r.top+'px')});
 // entrada sutil de títulos
 const io=new IntersectionObserver(es=>es.forEach(x=>{if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}}),{threshold:.2});
 q('.big,.steps li,.pc').forEach(el=>{if(el.closest('.hero'))return;el.setAttribute('data-r','');io.observe(el)});
}
// filtro de projetos
const fb=q('.flt button');fb.forEach(b=>b.addEventListener('click',()=>{fb.forEach(x=>x.setAttribute('aria-pressed',x===b));let n=0;q('.pc').forEach(c=>{const s=b.dataset.f==='todos'||c.dataset.kind===b.dataset.f;c.hidden=!s;n+=s});q('.empty')[0].hidden=n>0}));
// formulário (Netlify Forms via fetch, com fallback)
const f=q('.fm')[0];if(f){const p=new URLSearchParams(location.search).get('servico');if(p&&f.servico.querySelector(`[value="${p}"]`))f.servico.value=p;
 f.addEventListener('submit',async e=>{e.preventDefault();const st=q('.st',f)[0],btn=q('button',f)[0];btn.disabled=true;st.className='st sm';st.textContent='Enviando…';
  try{const r=await fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams(new FormData(f)).toString()});if(!r.ok)throw 0;location.href='/obrigado/'}
  catch{st.className='st sm err';st.textContent='Não foi possível enviar agora. Tente novamente ou use outro canal de contato.';btn.disabled=false}})}
})();
