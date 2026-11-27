(function(){
  var W = window.parent, D;
  try { D = W.document; } catch (e) { return; }   // sin acceso: la página queda sin animaciones, pero completa
  if (D.documentElement.dataset.savaFx) return;
  D.documentElement.dataset.savaFx = '1';
  var reduce = W.matchMedia && W.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var root = D.querySelector('.stApp') || D.body;
  if (!reduce) root.classList.add('js-anim');

  // Aparición al bajar
  var io = new W.IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
    });
  }, {threshold: 0.12, rootMargin: '0px 0px -40px 0px'});

  // Contadores
  function countUp(el){
    if (el.dataset.done) return; el.dataset.done = '1';
    var to = parseFloat(el.dataset.count), pre = el.dataset.prefix || '', loc = el.dataset.locale || 'es-CO';
    var t0 = performance.now(), dur = 1600;
    function step(now){
      var p = Math.min(1, (now - t0) / dur), e = 1 - Math.pow(1 - p, 4);
      el.textContent = pre + Math.round(to * e).toLocaleString(loc);
      if (p < 1) W.requestAnimationFrame(step);
    }
    W.requestAnimationFrame(step);
  }
  var cio = new W.IntersectionObserver(function(entries){
    entries.forEach(function(en){ if (en.isIntersecting) { countUp(en.target); cio.unobserve(en.target); } });
  }, {threshold: 0.4});

  // Luz que sigue el cursor en las tarjetas
  function spot(el){
    if (el.dataset.spot) return; el.dataset.spot = '1';
    el.addEventListener('mousemove', function(ev){
      var r = el.getBoundingClientRect();
      el.style.setProperty('--mx', (ev.clientX - r.left) + 'px');
      el.style.setProperty('--my', (ev.clientY - r.top) + 'px');
    });
  }

  function scan(){
    D.querySelectorAll('[data-reveal]:not([data-obs]), .timeline:not([data-obs])').forEach(function(el){
      el.dataset.obs = '1'; if (reduce) el.classList.add('in'); else io.observe(el);
    });
    D.querySelectorAll('[data-count]:not([data-obs])').forEach(function(el){ el.dataset.obs = '1'; if (!reduce) cio.observe(el); });
    D.querySelectorAll('.spot').forEach(spot);
  }
  scan();
  new W.MutationObserver(function(){ scan(); }).observe(D.body, {childList: true, subtree: true});

  // Barra superior más sólida al bajar
  D.addEventListener('scroll', function(ev){
    var nav = D.querySelector('.nav'); if (!nav) return;
    var y = (ev.target && ev.target.scrollTop !== undefined) ? ev.target.scrollTop : W.scrollY;
    nav.classList.toggle('scrolled', y > 30);
  }, true);

  // Seguridad: si algo queda oculto, mostrarlo a los 4 segundos
  W.setTimeout(function(){
    D.querySelectorAll('[data-reveal]').forEach(function(el){
      var r = el.getBoundingClientRect();
      if (r.top < W.innerHeight) el.classList.add('in');
    });
  }, 4000);
})();
