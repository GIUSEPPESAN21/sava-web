(function(){
  var C = window.CFG, P = C.prices, t = C.t;
  var loc = t.locale || 'es-CO';
  var state = {k:'subscription', setup:false, care:true};
  function fmt(n){ return '$' + Math.round(n).toLocaleString(loc); }
  function $(id){ return document.getElementById(id); }
  var shown = {today:0, month:0, year:0};
  function anim(id, key, to, suffix){
    var el = $(id), from = shown[key], t0 = performance.now(), dur = 550;
    shown[key] = to;
    el.classList.remove('bump'); void el.offsetWidth; el.classList.add('bump');
    function step(now){
      var p = Math.min(1, (now - t0) / dur), e = 1 - Math.pow(1 - p, 3);
      var v = from + (to - from) * e;
      el.innerHTML = (to === 0 && key === 'month') ? t.none : fmt(v) + '<span class="code">COP</span>' + (suffix || '');
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  function render(){
    document.querySelectorAll('.opt').forEach(function(b){ b.classList.toggle('on', b.dataset.k === state.k); });
    var careForced = state.k !== 'license';
    if (careForced) state.care = true;
    $('care').checked = state.care; $('care').disabled = careForced;
    $('tg-care').classList.toggle('locked', careForced);
    $('req').textContent = careForced ? t.care_req : '';
    $('setup').checked = state.setup;
    $('p-setup').textContent = '+ ' + fmt(P.setup);
    $('p-care').textContent = '+ ' + fmt(P.care) + (loc === 'es-CO' ? '/mes' : '/mo');
    var base = P[state.k], today = base + (state.setup ? P.setup : 0), month = state.care ? P.care : 0;
    var year = today + month * 11;
    anim('r-today', 'today', today, state.k === 'flow' ? ' <small style="font-size:12px;color:#93A3BC">' + t.from + '</small>' : '');
    anim('r-month', 'month', month, '');
    anim('r-year', 'year', year, '');
    var name = '';
    t.opts.forEach(function(o){ if (o[0] === state.k) name = o[1]; });
    var msg = t.wa.replace('{plan}', name)
                  .replace('{setup}', state.setup ? t.with_setup : '')
                  .replace('{care}', (state.care && state.k === 'license') ? t.with_care : '')
                  .replace('{today}', fmt(today))
                  .replace('{month}', month ? t.monthly_txt.replace('{m}', fmt(month)) : '');
    $('cta').href = 'https://wa.me/' + C.wa + '?text=' + encodeURIComponent(msg);
  }
  document.querySelectorAll('.opt').forEach(function(b){
    b.addEventListener('click', function(){ state.k = b.dataset.k; if (state.k === 'license') state.care = false; render(); });
  });
  $('setup').addEventListener('change', function(e){ state.setup = e.target.checked; render(); });
  $('care').addEventListener('change', function(e){ if (state.k === 'license') state.care = e.target.checked; render(); });
  render();
  function fit(){ try { var f = window.frameElement; if (f) { f.style.height = (document.documentElement.scrollHeight + 4) + 'px'; } } catch(e){} }
  window.addEventListener('resize', fit); setTimeout(fit, 50); setTimeout(fit, 600);
  if (window.ResizeObserver) new ResizeObserver(fit).observe(document.body);
})();
