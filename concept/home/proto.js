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

  // Стрелка карусели на десктопе: следующий слайд, с последнего — на первый
  document.querySelectorAll('.arw').forEach(function (btn) {
    var track = btn.parentElement.querySelector('.track');
    if (!track) return;
    btn.addEventListener('click', function () {
      var slide = track.querySelector('.sl'); if (!slide) return;
      var step = slide.getBoundingClientRect().width + parseFloat(getComputedStyle(track).columnGap || 16);
      var end = track.scrollWidth - track.clientWidth - 2;
      track.scrollTo({ left: track.scrollLeft >= end ? 0 : track.scrollLeft + step, behavior: 'smooth' });
    });
  });
})();
