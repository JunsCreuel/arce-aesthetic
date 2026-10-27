const CONFIG = {
  phone: '055-903-3002',
  kakaoUrl: 'https://pf.kakao.com/',
  address: '경남 김해시 율하숲길 21 303호',
  mapUrl: 'https://map.naver.com/p/search/' + encodeURIComponent('경남 김해시 율하숲길 21'),
  formEndpoint: ''
};

(() => {
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  if (!location.hash) { document.documentElement.style.scrollBehavior = 'auto'; window.scrollTo(0, 0); document.documentElement.style.scrollBehavior = ''; }
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const io = (el, fn, opt) => { if (el) new IntersectionObserver(fn, opt).observe(el); };

  $$('.js-tel').forEach(a => a.href = 'tel:' + CONFIG.phone.replace(/\D/g, ''));
  $$('.js-tel-text').forEach(el => el.textContent = CONFIG.phone);
  $$('.js-kakao').forEach(a => { a.href = CONFIG.kakaoUrl; a.target = '_blank'; a.rel = 'noopener'; });
  $$('.js-addr').forEach(el => el.textContent = CONFIG.address);
  $$('.js-map').forEach(a => a.href = CONFIG.mapUrl);
  $$('.js-kakao').forEach(a => a.addEventListener('click', () => { if (window.fbq) fbq('track', 'Contact'); }));
  requestAnimationFrame(() => document.body.classList.add('loaded'));
  $$('.ps__art path').forEach(p => { try { p.style.setProperty('--len', Math.ceil(p.getTotalLength()) + 1); } catch (e) {} });

  if (!reduce) {
    const once = (el, cls = 'is-in', th = .3) => io(el, ([e], o) => { if (e.isIntersecting) { el.classList.add(cls); o.disconnect(); } }, { threshold: th });
    $$('.split__img, .resv__photo, .dir__photo').forEach(el => { el.classList.add('ph'); once(el, 'is-in', .25); });

    const par = $$('.split__img img, .resv__photo img, .phero__bg img');
    const rows = $$('.mq__row');
    rows.forEach(row => { const sp = row.firstElementChild; sp.innerHTML += sp.innerHTML; });
    const tick = () => {
      const vh = innerHeight;
      par.forEach(img => {
        const r = img.parentElement.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) return;
        const p = (r.top + r.height / 2 - vh / 2) / vh;
        img.style.transform = `translate3d(0,${(p * -6).toFixed(2)}%,0) scale(1.12)`;
      });
      rows.forEach(row => {
        const r = row.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        const x = (vh - r.top) * .35 * row.dataset.dir - row.scrollWidth * .3;
        row.firstElementChild.style.transform = `translate3d(${x.toFixed(1)}px,0,0)`;
      });
    };
    let raf = 0;
    addEventListener('scroll', () => { if (!raf) raf = requestAnimationFrame(() => { raf = 0; tick(); }); }, { passive: true });
    addEventListener('resize', tick); tick();

    const count = el => {
      const node = [...el.childNodes].find(n => n.nodeType === 3 && /\d/.test(n.textContent));
      if (!node) return;
      const end = parseInt(node.textContent, 10), t0 = performance.now(), dur = 1400;
      const step = now => {
        const k = Math.min(1, (now - t0) / dur), e = 1 - Math.pow(1 - k, 3);
        node.textContent = String(Math.round(end * e));
        if (k < 1) requestAnimationFrame(step);
      };
      node.textContent = '0'; requestAnimationFrame(step);
    };
    $$('.big26, .rvs__head .num').forEach(el => io(el, ([e], o) => { if (e.isIntersecting) { count(el); o.disconnect(); } }, { threshold: .6 }));
  }

  const hdr = $('#hdr'), hero = $('#top'), drawer = $('#drawer'), burger = $('#burger');
  let lastY = 0;
  const heroH = () => hero ? hero.offsetHeight - 80 : 0;
  const setDrawer = open => {
    drawer.classList.toggle('open', open); drawer.setAttribute('aria-hidden', !open);
    burger.setAttribute('aria-expanded', open); burger.setAttribute('aria-label', open ? '메뉴 닫기' : '메뉴 열기');
    document.body.style.overflow = open ? 'hidden' : '';
    hdr.classList.toggle('solid', open || scrollY > heroH());
  };
  burger.addEventListener('click', () => setDrawer(!drawer.classList.contains('open')));
  $$('a', drawer).forEach(a => a.addEventListener('click', () => setDrawer(false)));
  addEventListener('keydown', e => { if (e.key === 'Escape') setDrawer(false); });

  const hs = $('#hs');
  if (hs) {
    const slides = $$('.hs__slide', hs), txts = $$('.hs__txt', hs), dots = $$('.hs__dot', hs), num = $('#hsNum');
    let hi = 0, ht = null;
    const show = i => {
      hi = i;
      slides.forEach((s, k) => s.classList.toggle('on', k === i));
      txts.forEach((t, k) => t.classList.toggle('on', k === i));
      dots.forEach((d, k) => { d.classList.toggle('on', k === i); d.classList.toggle('is-done', k < i); d.setAttribute('aria-current', k === i); const b = $('i', d); b.style.animation = 'none'; void b.offsetWidth; b.style.animation = ''; });
      if (num) num.textContent = `${String(i + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;
      clearTimeout(ht); if (!reduce) ht = setTimeout(() => show((hi + 1) % slides.length), 6000);
    };
    dots.forEach((d, i) => d.addEventListener('click', () => show(i)));
    show(0);
  }

  const sayT = $('#sayT');
  let sayUpd = () => {};
  if (sayT) {
    sayT.innerHTML = sayT.textContent.split(' ').map(w => `<span class="w">${w}</span>`).join(' ');
    const words = $$('.w', sayT);
    sayUpd = () => {
      const r = sayT.getBoundingClientRect();
      const p = Math.min(1, Math.max(0, (innerHeight * .85 - r.top) / (innerHeight * .55)));
      const n = reduce ? words.length : Math.round(p * words.length);
      words.forEach((w, i) => w.classList.toggle('on', i < n));
    };
  }

  const method = $('#method');
  if (method) {
    const STEPS = [
      ['진단', '얼굴 비율과 좌우 균형, 저작근과 근막의 긴장도를 대표원장이 직접 분석합니다.'],
      ['이완', '습관과 자세로 굳어진 저작근·광대 주변·목 근막을 손기술로 섬세하게 이완합니다.'],
      ['정돈', '해부학적 구조를 따라 턱선과 얼굴 외곽 라인을 정돈하고, 순환의 흐름을 바로잡습니다.'],
      ['유지', '목·어깨 순환 관리와 맞춤 홈케어 가이드로 정돈된 라인이 오래 유지되도록 돕습니다.']
    ];
    const sBtns = $$('#steps button'), face = $('#face'), stepT = $('#stepT'), stepD = $('#stepD'), copy = $('#stepCopy');
    let si = 0, timer = null, inView = false, manual = false;
    const DUR = 5000; method.style.setProperty('--dur', DUR + 'ms');
    const schedule = () => { clearTimeout(timer); if (reduce) { method.classList.add('paused'); return; } if (inView && !manual) timer = setTimeout(() => setStep((si + 1) % 4), DUR); };
    const setStep = i => {
      si = i;
      sBtns.forEach((b, k) => { b.setAttribute('aria-selected', k === i); b.tabIndex = k === i ? 0 : -1; b.classList.toggle('is-done', k < i); const bar = $('.bar i', b); bar.style.animation = 'none'; void bar.offsetWidth; bar.style.animation = ''; });
      face.dataset.s = i; stepT.textContent = STEPS[i][0]; stepD.textContent = STEPS[i][1];
      copy.classList.remove('swap'); void copy.offsetWidth; copy.classList.add('swap');
      schedule();
    };
    sBtns.forEach((b, i) => {
      b.addEventListener('click', () => { manual = true; method.classList.add('paused'); setStep(i); });
      b.addEventListener('keydown', e => { const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0; if (!d) return; manual = true; method.classList.add('paused'); const n = (i + d + 4) % 4; setStep(n); sBtns[n].focus(); });
    });
    io(method, ([e]) => { inView = e.isIntersecting; method.classList.toggle('paused', !inView || manual); if (inView) setStep(si); else clearTimeout(timer); }, { threshold: .35 });
  }

  io($('#dirPhoto'), ([e], o) => { if (e.isIntersecting) { e.target.classList.add('in'); o.disconnect(); } }, { threshold: .3 });

  const eqTabs = $$('#eqTabs .eq__tab');
  if (eqTabs.length) {
    const EQ = [
      { img: 'assets/eq-lpg.webp', w: 530, h: 852, brand: 'LPG® · FRANCE', name: 'LPG® 알리안스', alt: 'LPG 알리안스 장비',
        one: '롤러와 음압으로 피부와 피하 조직을 부드럽게 자극해, 뭉친 조직을 풀고 순환을 돕는 엔더몰로지 장비입니다.',
        facts: [['방식', '롤러 + 음압(흡입)을 이용한 기계적 자극, 엔더몰로지'], ['관리 부위', '바디 라인, 셀룰라이트, 얼굴 탄력'], ['이런 분께', '붓기와 뭉침이 잦고 바디 라인이 고민인 분']] },
      { img: 'assets/eq-thermawave.webp', w: 228, h: 802, brand: 'LPHYSIO · WELLNESS DEVICE', name: '써마웨이브™', alt: '써마웨이브 장비',
        one: '따뜻한 열감을 이용해 얼굴과 바디의 라인, 탄력을 함께 관리하는 장비입니다.',
        facts: [['방식', '열감을 이용한 관리'], ['관리 부위', '얼굴 라인, 바디 라인'], ['이런 분께', '탄력 저하와 처짐이 고민인 분']] },
      { img: 'assets/eq-zionic.webp', w: 1027, h: 1000, brand: 'TERMOSALUD · SPAIN', name: '자이오닉', alt: '자이오닉 핸드피스',
        one: '깊게 회전하는 마사지와 고주파 열을 동시에 전달하는 바디 컨투어링 장비입니다.',
        facts: [['방식', '회전 마사지(MARP) + 470kHz 모노폴라 고주파'], ['관리 부위', '복부, 허벅지, 엉덩이 등 바디'], ['이런 분께', '셀룰라이트, 붓기, 처진 바디 라인이 고민인 분']] }
    ];
    const eqImg = $('#eqImg'), eqText = $('#eqText');
    const setEq = i => {
      const d = EQ[i];
      eqTabs.forEach((t, k) => { t.setAttribute('aria-selected', k === i); t.tabIndex = k === i ? 0 : -1; });
      eqImg.style.animation = 'none'; void eqImg.offsetWidth; eqImg.style.animation = '';
      eqImg.src = d.img; eqImg.width = d.w; eqImg.height = d.h; eqImg.alt = d.alt;
      $('#eqBrand').textContent = d.brand; $('#eqName').textContent = d.name; $('#eqOne').textContent = d.one;
      $('#eqFacts').innerHTML = d.facts.map(([k, v]) => `<div><dt>${k}</dt><dd>${v}</dd></div>`).join('');
      eqText.classList.remove('eq__text'); void eqText.offsetWidth; eqText.classList.add('eq__text');
    };
    eqTabs.forEach((t, i) => {
      t.addEventListener('click', () => setEq(i));
      t.addEventListener('keydown', e => { const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0; if (!d) return; const n = (i + d + EQ.length) % EQ.length; setEq(n); eqTabs[n].focus(); });
    });
    const start = Math.max(0, ['lpg', 'thermawave', 'zionic'].indexOf(location.hash.slice(1)));
    setEq(start);
  }

  const cv = $('#cv');
  if (cv) {
    $('#cvOpen').addEventListener('click', () => { if (cv.showModal) cv.showModal(); else cv.setAttribute('open', ''); });
    $('#cvClose').addEventListener('click', () => cv.close ? cv.close() : cv.removeAttribute('open'));
    cv.addEventListener('click', e => { if (e.target === cv) cv.close(); });
  }

  const dragScroll = el => {
    if (!el) return;
    let d = null;
    el.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse' || e.target.closest('a, button, .ba')) return; d = { x: e.clientX, s: el.scrollLeft }; el.style.scrollSnapType = 'none'; });
    addEventListener('pointermove', e => { if (d) el.scrollLeft = d.s - (e.clientX - d.x); });
    addEventListener('pointerup', () => { if (!d) return; d = null; el.style.scrollSnapType = ''; });
  };
  dragScroll($('#rvTrack')); dragScroll($('#gal'));

  $$('.rv').forEach(c => { const b = $('.rv__body', c), m = $('.rv__more', c); if (b && m && b.scrollHeight > b.clientHeight + 4) { m.hidden = false; m.addEventListener('click', () => { const o = c.classList.toggle('open'); m.textContent = o ? '접기' : '더보기'; }); } });
  io($('#kw'), ([e], o) => { if (e.isIntersecting) { e.target.classList.add('in'); o.disconnect(); } }, { threshold: .4 });

  const vids = $$('.care__v video');
  if (!reduce) {
    vids.forEach(v => io(v, ([e]) => { if (e.isIntersecting) { v.preload = 'auto'; v.play().catch(() => {}); } else v.pause(); }, { threshold: .4 }));
  } else vids.forEach(v => v.controls = true);

  $$('.ba').forEach(ba => { const r = $('input', ba); r.addEventListener('input', () => ba.style.setProperty('--p', r.value + '%')); });

  const area = $('#area');
  if (area) { const q = new URLSearchParams(location.search).get('care'); if (q && !area.value) area.value = q; }

  const cImg = $('#clinicImg');
  const cUpd = () => {
    if (!cImg || reduce) return;
    const r = cImg.closest('section').getBoundingClientRect();
    if (r.bottom < 0 || r.top > innerHeight) return;
    const p = (r.top + r.height / 2 - innerHeight / 2) / innerHeight;
    cImg.style.transform = `translateY(${(-8 + p * 8).toFixed(2)}%)`;
  };

  const mcta = $('#mcta'); let pastHero = !hero, inResv = false;
  const mUpd = () => mcta && mcta.classList.toggle('show', pastHero && !inResv);
  io(hero, ([e]) => { pastHero = !e.isIntersecting; mUpd(); }, { threshold: .1 });
  io($('#reserve'), ([e]) => { inResv = e.isIntersecting; mUpd(); }, { threshold: .2 });
  mUpd();

  const onScroll = () => {
    const y = scrollY;
    hdr.classList.toggle('solid', y > heroH() || drawer.classList.contains('open'));
    hdr.classList.toggle('hide', y > lastY && y > 400 && !drawer.classList.contains('open'));
    lastY = y; sayUpd(); cUpd();
  };
  addEventListener('scroll', () => requestAnimationFrame(onScroll), { passive: true });
  onScroll();

  const form = $('#form');
  if (form) {
    const phone = $('#phone');
    phone.addEventListener('input', () => {
      const d = phone.value.replace(/\D/g, '').slice(0, 11);
      phone.value = d.length < 4 ? d : d.length < 8 ? `${d.slice(0, 3)}-${d.slice(3)}` : `${d.slice(0, 3)}-${d.slice(3, d.length - 4)}-${d.slice(-4)}`;
    });
    form.addEventListener('submit', async e => {
      e.preventDefault();
      const name = $('#name').value.trim(), tel = phone.value.replace(/\D/g, ''), agree = $('#agree').checked;
      $('#fName').classList.toggle('err', !name);
      $('#fPhone').classList.toggle('err', !/^01\d{8,9}$/.test(tel));
      $('#fAgree').classList.toggle('err', !agree);
      const bad = $('.f.err', form); if (bad) { $('input', bad).focus(); return; }
      const data = { name, phone: phone.value, area: area ? area.value.trim() : '', page: location.href };
      if (CONFIG.formEndpoint) { try { await fetch(CONFIG.formEndpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) }); } catch (err) {} }
      if (window.fbq) fbq('track', 'Lead');
      $('#resvBox').classList.add('sent');
    });
  }
})();
