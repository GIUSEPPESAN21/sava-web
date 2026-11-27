/* SAVA Software · animaciones y cotizador (mejora progresiva).
   Corre dentro de un iframe invisible de Streamlit y actúa sobre la página principal.
   Si el navegador lo bloquea, la página se ve completa: solo faltan las animaciones y el cálculo en vivo. */
(function(){
  var W = window.parent, D;
  try { D = W.document; if (!D || !D.body) return; } catch (e) { return; }
  if (D.documentElement.dataset.savaFx) return;
  D.documentElement.dataset.savaFx = '1';
  var reduce = W.matchMedia && W.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var root = D.querySelector('.stApp') || D.body;
  if (!reduce) root.classList.add('js-anim');

  /* ---------- Aparición al bajar ---------- */
  var io = new W.IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
    });
  }, {threshold: 0.12, rootMargin: '0px 0px -40px 0px'});

  /* ---------- Contadores ---------- */
  function countUp(el){
    if (el.dataset.done) return; el.dataset.done = '1';
    var to = parseFloat(el.dataset.count), pre = el.dataset.prefix || '', loc = el.dataset.locale || 'es-CO';
    var t0 = W.performance.now(), dur = 1600;
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

  /* ---------- Luz que sigue el cursor y maqueta que se inclina ---------- */
  function spot(el){
    if (el.dataset.spot) return; el.dataset.spot = '1';
    el.addEventListener('mousemove', function(ev){
      var r = el.getBoundingClientRect();
      el.style.setProperty('--mx', (ev.clientX - r.left) + 'px');
      el.style.setProperty('--my', (ev.clientY - r.top) + 'px');
    });
  }
  function tilt(el){
    if (el.dataset.tiltOn) return; el.dataset.tiltOn = '1';
    var box = el.parentNode;
    box.addEventListener('mousemove', function(ev){
      if (W.innerWidth < 1000) return;
      var r = box.getBoundingClientRect();
      var x = (ev.clientX - r.left) / r.width - .5, y = (ev.clientY - r.top) / r.height - .5;
      el.style.setProperty('--ry', (x * 12).toFixed(2) + 'deg');
      el.style.setProperty('--rx', (-y * 10).toFixed(2) + 'deg');
    });
    box.addEventListener('mouseleave', function(){ el.style.removeProperty('--ry'); el.style.removeProperty('--rx'); });
  }

  /* ---------- Cotizador ---------- */
  function calc(box){
    if (box.dataset.ready) return; box.dataset.ready = '1';
    var C; try { C = JSON.parse(box.dataset.calc); } catch (e) { return; }
    var P = C.prices, t = C.t, loc = t.locale || 'es-CO';
    var state = {k: 'subscription', setup: false, care: true};
    var shown = {today: null, month: null, year: null};
    function q(s){ return box.querySelector(s); }
    function fmt(n){ return '$' + Math.round(n).toLocaleString(loc); }
    function paint(el, key, to, extra){
      var from = shown[key] === null ? to : shown[key];
      shown[key] = to;
      el.classList.remove('bump'); void el.offsetWidth; el.classList.add('bump');
      var t0 = W.performance.now(), dur = reduce ? 0 : 550;
      function step(now){
        var p = dur ? Math.min(1, (now - t0) / dur) : 1, e = 1 - Math.pow(1 - p, 3), v = from + (to - from) * e;
        el.innerHTML = (to === 0 && key === 'month') ? t.none : fmt(v) + '<span class="code">COP</span>' + (extra || '');
        if (p < 1) W.requestAnimationFrame(step);
      }
      W.requestAnimationFrame(step);
    }
    function render(){
      box.querySelectorAll('.opt').forEach(function(b){ b.classList.toggle('on', b.dataset.k === state.k); });
      var forced = state.k !== 'license';
      if (forced) state.care = true;
      var care = q('.c-care'), setup = q('.c-setup');
      care.checked = state.care; care.disabled = forced;
      care.closest('.tg').classList.toggle('locked', forced);
      q('.req').textContent = forced ? t.care_req : '';
      setup.checked = state.setup;
      var today = P[state.k] + (state.setup ? P.setup : 0), month = state.care ? P.care : 0, year = today + month * 12;
      var from = state.k === 'flow' ? '<span class="from">' + t.from + '</span>' : '';
      paint(q('.r-today'), 'today', today, from);
      paint(q('.r-month'), 'month', month, '');
      paint(q('.r-year'), 'year', year, from);
      var name = ''; t.opts.forEach(function(o){ if (o[0] === state.k) name = o[1]; });
      var msg = t.wa.replace('{plan}', name)
        .replace('{setup}', state.setup ? t.with_setup : '')
        .replace('{care}', (state.care && state.k === 'license') ? t.with_care : '')
        .replace('{today}', (state.k === 'flow' ? t.from + ' ' : '') + fmt(today))
        .replace('{month}', month ? t.monthly_txt.replace('{m}', fmt(month)) : '');
      q('.c-cta').href = 'https://wa.me/' + C.wa + '?text=' + encodeURIComponent(msg);
    }
    box.querySelectorAll('.opt').forEach(function(b){
      b.addEventListener('click', function(){ state.k = b.dataset.k; if (state.k === 'license') state.care = false; render(); });
    });
    q('.c-setup').addEventListener('change', function(e){ state.setup = e.target.checked; render(); });
    q('.c-care').addEventListener('change', function(e){ if (state.k === 'license') state.care = e.target.checked; render(); });
    render();
  }

  function scan(){
    D.querySelectorAll('[data-reveal]:not([data-obs])').forEach(function(el){
      el.dataset.obs = '1'; if (reduce) el.classList.add('in'); else io.observe(el);
    });
    D.querySelectorAll('[data-count]:not([data-obs])').forEach(function(el){ el.dataset.obs = '1'; if (!reduce) cio.observe(el); });
    D.querySelectorAll('.spot').forEach(spot);
    if (!reduce) D.querySelectorAll('[data-tilt]').forEach(tilt);
    D.querySelectorAll('[data-calc]').forEach(calc);
  }
  scan();
  new W.MutationObserver(function(){ scan(); }).observe(D.body, {childList: true, subtree: true});

  /* ---------- Barra superior, progreso de lectura y botón flotante ---------- */
  function onScroll(ev){
    var el = ev && ev.target && ev.target.scrollTop !== undefined ? ev.target : (D.scrollingElement || D.documentElement);
    var y = el.scrollTop || 0, max = (el.scrollHeight - el.clientHeight) || 1;
    var nav = D.querySelector('.nav'); if (nav) nav.classList.toggle('scrolled', y > 30);
    var bar = D.querySelector('.progress'); if (bar) bar.style.setProperty('--p', Math.min(1, y / max).toFixed(4));
    var hero = D.querySelector('.hero'), cta = D.querySelector('.cta-box');
    if (hero) root.classList.toggle('past-hero', hero.getBoundingClientRect().bottom < 80);
    if (cta) { var r = cta.getBoundingClientRect(); root.classList.toggle('at-cta', r.top < W.innerHeight && r.bottom > 0); }
  }
  D.addEventListener('scroll', onScroll, true);
  W.addEventListener('scroll', onScroll);
  onScroll();

  /* ---------- Seguridad: si algo queda oculto, mostrarlo ---------- */
  W.setTimeout(function(){
    D.querySelectorAll('[data-reveal]').forEach(function(el){
      var r = el.getBoundingClientRect();
      if (r.top < W.innerHeight) el.classList.add('in');
    });
  }, 3500);
})();
