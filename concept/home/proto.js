// Прототип главной: перетаскивание мышью у горизонтальных лент и стрелка карусели.
// Свайп, привязка к слайдам и бегущая строка работают на CSS; здесь только то, чего CSS не умеет.
(function () {
  var SCROLLERS = '.car, .track, .row, .g6, .g6r, .tkr.top';

  // Перетаскивание мышью: на тачпадах и телефонах лента листается нативно
  document.querySelectorAll(SCROLLERS).forEach(function (el) {
    var down = false, moved = false, startX = 0, startLeft = 0, snap = '';
    el.addEventListener('pointerdown', function (e) {
      if (e.pointerType !== 'mouse' || e.button !== 0) return;
      down = true; moved = false; startX = e.clientX; startLeft = el.scrollLeft;
      snap = el.style.scrollSnapType; el.style.scrollSnapType = 'none';
    });
    window.addEventListener('pointermove', function (e) {
      if (!down) return;
      var dx = e.clientX - startX;
      if (Math.abs(dx) > 4) { moved = true; el.style.cursor = 'grabbing'; }
      el.scrollLeft = startLeft - dx;
    });
    window.addEventListener('pointerup', function () {
      if (!down) return;
      down = false; el.style.cursor = ''; el.style.scrollSnapType = snap;
      // доводка до ближайшего слайда
      var kid = nearest(el); if (kid) el.scrollTo({ left: kid.offsetLeft - el.firstElementChild.offsetLeft, behavior: 'smooth' });
    });
    // клик после перетаскивания не открывает карточку
    el.addEventListener('click', function (e) { if (moved) { e.preventDefault(); e.stopPropagation(); moved = false; } }, true);
    el.addEventListener('dragstart', function (e) { e.preventDefault(); });
  });

  function nearest(el) {
    var kids = Array.prototype.slice.call(el.children), best = null, bd = Infinity, base = el.firstElementChild ? el.firstElementChild.offsetLeft : 0;
    kids.forEach(function (k) { var d = Math.abs(k.offsetLeft - base - el.scrollLeft); if (d < bd) { bd = d; best = k; } });
    return best;
  }

  // Карусель по кругу: копии слайдов до и после, на копиях — незаметный перескок к оригиналу
  document.querySelectorAll('.car, .track').forEach(function (track) {
    var slides = Array.prototype.slice.call(track.querySelectorAll(':scope > .sl'));
    var n = slides.length; if (n < 2) return;
    function copy(s) { var c = s.cloneNode(true); c.setAttribute('aria-hidden', 'true'); c.inert = true; c.classList.add('clone'); return c; }
    slides.forEach(function (s) { track.insertBefore(copy(s), slides[0]); });
    slides.forEach(function (s) { track.appendChild(copy(s)); });
    var all = function () { return track.querySelectorAll(':scope > .sl'); };
    var step = function () { return slides[1].offsetLeft - slides[0].offsetLeft; };
    var base = function () { return all()[0].offsetLeft; };
    function jump(x) { var sn = track.style.scrollSnapType; track.style.scrollSnapType = 'none'; track.scrollLeft = x; void track.offsetHeight; track.style.scrollSnapType = sn; }
    jump(slides[0].offsetLeft - base());
    function settle() {
      var idx = Math.round(track.scrollLeft / step());
      if (idx < n) jump(track.scrollLeft + n * step());
      else if (idx >= 2 * n) jump(track.scrollLeft - n * step());
    }
    var t = null;
    if ('onscrollend' in window) track.addEventListener('scrollend', settle);
    else track.addEventListener('scroll', function () { clearTimeout(t); t = setTimeout(settle, 150); });
    track._step = step;
  });

  // Стрелка карусели на десктопе: следующий слайд, по кругу
  document.querySelectorAll('.arw').forEach(function (btn) {
    var track = btn.parentElement.querySelector('.track');
    if (!track) return;
    btn.addEventListener('click', function () {
      var step = track._step ? track._step() : track.querySelector('.sl').getBoundingClientRect().width;
      track.scrollBy({ left: step, behavior: 'smooth' });
    });
  });

  // Плитки категорий: подсветка выбранной (переход к полке — обычная ссылка #id)
  document.querySelectorAll('.tiles, .bar').forEach(function (nav) {
    nav.addEventListener('click', function (e) {
      var a = e.target.closest('.tile'); if (!a) return;
      nav.querySelectorAll('.tile').forEach(function (x) { x.classList.toggle('on', x === a); });
    });
  });
})();
