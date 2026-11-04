import re
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://arceaesthetic.com'
VER = __import__('time').strftime('%y%m%d%H%M')
REVIEWS = json.loads((ROOT / 'src' / 'reviews.json').read_text(encoding='utf-8'))

WRAP = 'w-full max-w-site mx-auto px-gutter'
SERIF = 'font-sans font-semibold tracking-[-.03em] leading-[1.38]'
DISP = 'font-display font-normal leading-[1.05] tracking-[.01em]'
PILL = 'inline-flex items-center gap-2 h-11 px-6 rounded-full border border-current text-[14px] font-medium tracking-[.02em] transition-colors duration-200 hover:bg-ink hover:text-ivory hover:border-ink'
EN = 'font-mark text-[12px] tracking-[.36em]'
SUB_TEXT = 'text-sub text-[clamp(15px,.6vw+12px,18px)]'
EASE = 'ease-soft'

ARROW = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 8 H13 M9 4 L13 8 L9 12"/></svg>'
KAKAO = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 3.5c-5 0-9 3.1-9 7 0 2.5 1.7 4.7 4.2 6l-1 3.6c-.1.3.3.6.6.4l4.2-2.8h1c5 0 9-3.1 9-7s-4-7.2-9-7.2z"/></svg>'

BTN_BASE = f'inline-flex items-center justify-center gap-2.5 rounded-[2px] font-medium tracking-[.04em] transition-[background-color,color,transform] duration-150 {EASE} active:scale-[.97] [-webkit-tap-highlight-color:transparent] [&_svg]:w-5 [&_svg]:h-5 [&_svg]:flex-none'
BTN_SIZE = {
    'md': 'h-[54px] px-[30px] text-[15px]',
    'sm': 'h-[42px] px-[22px] text-[14px]',
    'bar': 'h-[52px] px-3 text-[15px]',
    'dir': 'h-[52px] px-[30px] text-[15px]',
}
BTN_KIND = {
    'kakao': 'bg-ink text-ivory hover:bg-bronze',
    'kakao-light': 'bg-ivory text-ink hover:bg-white',
    'ink': 'bg-ink text-white hover:bg-bronze',
    'line': 'border border-current hover:bg-text hover:text-white hover:border-text',
}


def btn_cls(kind, size='md', extra=''):
    return f'{BTN_BASE} {BTN_SIZE[size]} {BTN_KIND[kind]} {extra}'.strip()


def kakao_btn(light=False, size='md', extra='', icon=True):
    return f'<a class="{btn_cls("kakao-light" if light else "kakao", size, extra)} js-kakao" href="#">{KAKAO if icon else ""}카카오톡 상담</a>'


MORE = f'inline-flex items-center gap-2 font-medium tracking-[.04em] min-h-12 border-b border-current [&_svg]:transition-transform [&_svg]:duration-200 [&_svg]:{EASE} [&:hover_svg]:translate-x-1'

MENU = [
    ('ARCÉ', 'brand.html', 'brand', [('브랜드 소개', 'brand.html#about', 'ABOUT'), ('원장 약력', 'director.html', 'DIRECTOR'), ('공간', 'brand.html#space', 'SPACE'), ('관리 현장', 'brand.html#care', 'IN CARE')]),
    ('조막얼굴메소드®', 'method.html', 'method', [('메소드 소개', 'method.html', 'SIGNATURE METHOD'), ('관리 전후', 'method.html#result', 'BEFORE & AFTER')]),
    ('관리 프로그램', 'program-face.html', 'program', [('페이스 윤곽 케어', 'program-face.html', 'FACE CONTOUR'), ('안티에이징 케어', 'program-aging.html', 'ANTI-AGING'), ('바디 밸런스 케어', 'program-body.html', 'BODY BALANCE'), ('산전·산후 케어', 'program-mom.html', 'PRENATAL & POSTPARTUM')]),
    ('장비', 'equipment.html', 'equipment', [('LPG® 알리안스', 'equipment.html#lpg', 'LPG'), ('써마웨이브™', 'equipment.html#thermawave', 'THERMAWAVE'), ('자이오닉', 'equipment.html#zionic', 'ZIONIC')]),
    ('고객후기', 'review.html', 'review', [('방문자 리뷰', 'review.html', 'REVIEW')]),
    ('상담·오시는 길', 'contact.html', 'contact', [('상담 문의', 'contact.html#reserve', 'CONTACT'), ('오시는 길', 'contact.html#clinic', 'LOCATION')]),
]


def header(cur):
    items = ''
    for label, href, key, subs in MENU:
        weight = 'font-medium' if key == cur else 'font-normal'
        links = ''.join(
            f'<a class="relative block py-2.5 px-3.5 rounded-[10px] text-[14px] font-medium whitespace-nowrap hover:bg-beige" href="{h}">{t}<small class="block font-mark text-[11px] tracking-[.12em] text-sub mt-0.5">{e}</small></a>'
            for t, h, e in subs)
        items += (
            f'<div class="group relative">'
            f'<a class="relative flex items-center gap-1.5 py-3 px-4 min-h-12 text-[15px] tracking-[.04em] {weight} max-[1180px]:px-2.5 max-[1180px]:text-[14px]" href="{href}">{label}</a>'
            f'<div class="absolute top-full left-1/2 min-w-[200px] p-3 bg-ivory text-text rounded-2xl shadow-[0_12px_32px_rgba(52,41,32,.14)] opacity-0 invisible -translate-x-1/2 translate-y-1.5 transition-[opacity,transform,visibility] duration-200 {EASE} group-hover:opacity-100 group-hover:visible group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:visible group-focus-within:translate-y-0">{links}</div>'
            f'</div>')
    groups = ''.join(
        f'<div class="border-b border-line py-3"><a class="{SERIF} text-[24px] block py-1.5" href="{href}">{label}</a>'
        f'<div class="flex flex-wrap gap-x-4 gap-y-1 mt-1.5">'
        + ''.join(f'<a class="text-[15px] text-sub py-2 min-h-10 inline-flex items-center" href="{h}">{t}</a>' for t, h, _ in subs)
        + '</div></div>'
        for label, href, key, subs in MENU)
    return f'''<header id="hdr" class="fixed inset-x-0 top-0 z-50 h-[calc(var(--hh)+env(safe-area-inset-top,0px))] pt-[env(safe-area-inset-top,0px)] bg-ivory text-text shadow-[0_1px_0_#E2D6C4] transition-[background-color,transform,box-shadow] duration-300 {EASE} [&.hide]:-translate-y-full">
  <div class="{WRAP} h-hh flex items-center justify-between gap-6">
    <a href="index.html" class="flex items-center min-h-12" aria-label="아르쎄에스테틱 홈"><img class="block w-auto h-[38px] sm:h-[46px]" src="assets/logo-header.png" width="152" height="56" alt="ARCÉ 아르쎄에스테틱"></a>
    <nav class="hidden xl:flex gap-1" aria-label="주요 메뉴">{items}</nav>
    <a href="contact.html#reserve" class="{btn_cls('ink', 'sm', 'hidden xl:flex !text-ivory')}">상담 예약</a>
    <button class="group grid xl:hidden w-12 h-12 place-items-center -mr-3" id="burger" aria-label="메뉴 열기" aria-expanded="false" aria-controls="drawer"><span class="flex flex-col"><i class="block w-6 h-[1.5px] bg-text transition-transform duration-[250ms] {EASE} group-aria-expanded:translate-y-[4.25px] group-aria-expanded:rotate-45"></i><i class="block w-6 h-[1.5px] mt-[7px] bg-text transition-transform duration-[250ms] {EASE} group-aria-expanded:-translate-y-[4.25px] group-aria-expanded:-rotate-45"></i></span></button>
  </div>
</header>
<div id="drawer" class="fixed inset-0 z-[49] flex flex-col gap-2 overflow-y-auto bg-ivory pt-[calc(var(--hh)+32px+env(safe-area-inset-top,0px))] px-gutter pb-[calc(32px+env(safe-area-inset-bottom,0px))] opacity-0 invisible transition-[opacity,visibility] duration-200 {EASE} [&.open]:opacity-100 [&.open]:visible" aria-hidden="true">
  {groups}
  <div class="mt-8 flex flex-wrap gap-x-8 gap-y-2">
    <a class="{MORE} js-kakao" href="#">카카오톡 상담 {ARROW}</a>
    <a class="{MORE} js-tel" href="#">전화 문의 {ARROW}</a>
  </div>
</div>'''


FOOTER = f'''<footer class="bg-paper text-ink pt-[72px] pb-[calc(120px+env(safe-area-inset-bottom,0px))] lg:pb-[72px] text-[13px]">
  <div class="{WRAP}">
    <p class="mb-10 leading-[0]"><img class="block w-auto h-[clamp(120px,14vw,190px)]" src="assets/logo.webp" width="260" height="267" alt="ARCÉ" loading="lazy"></p>
    <dl class="flex flex-wrap gap-x-8 gap-y-2">
      <div class="flex gap-2"><dt class="font-medium">상호</dt><dd>아르쎄에스테틱</dd></div>
      <div class="flex gap-2"><dt class="font-medium">대표</dt><dd>조외현</dd></div>
      <div class="flex gap-2"><dt class="font-medium">사업자등록번호</dt><dd class="tabular-nums">641-43-00735</dd></div>
      <div class="flex gap-2"><dt class="font-medium">전화</dt><dd class="js-tel-text tabular-nums"></dd></div>
      <div class="flex gap-2"><dt class="font-medium">주소</dt><dd class="js-addr"></dd></div>
    </dl>
    <p class="mt-8">© ARCÉ AESTHETIC</p>
  </div>
</footer>
<aside id="quick" class="fixed right-0 z-40 bottom-[calc(16px+env(safe-area-inset-bottom,0px))] xl:bottom-auto xl:top-1/2 xl:-translate-y-1/2" aria-label="빠른 연락">
  <div class="rounded-l-2xl bg-white/60 backdrop-blur-md shadow-[0_8px_30px_rgba(52,41,32,.12)] overflow-hidden">
    <a class="flex items-center justify-center xl:justify-start gap-3 w-12 h-12 xl:w-auto xl:h-auto xl:px-5 xl:py-3.5 text-[13px] text-text transition-colors duration-200 hover:bg-white/70 js-kakao" href="#" aria-label="카카오톡 상담"><svg class="w-[22px] h-[22px] flex-none" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 3.5c-5 0-9 3.1-9 7 0 2.5 1.7 4.7 4.2 6l-1 3.6c-.1.3.3.6.6.4l4.2-2.8h1c5 0 9-3.1 9-7s-4-7.2-9-7.2z"/></svg><span class="hidden xl:inline">카톡 상담</span></a>
    <a class="flex items-center justify-center xl:justify-start gap-3 w-12 h-12 xl:w-auto xl:h-auto xl:px-5 xl:py-3.5 text-[13px] text-text transition-colors duration-200 hover:bg-white/70 js-tel" href="#" aria-label="전화 문의"><svg class="w-[22px] h-[22px] flex-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg><span class="hidden xl:inline">전화 문의</span></a>
    <a class="flex items-center justify-center xl:justify-start gap-3 w-12 h-12 xl:w-auto xl:h-auto xl:px-5 xl:py-3.5 text-[13px] text-text transition-colors duration-200 hover:bg-white/70" href="contact.html#clinic" aria-label="오시는 길"><svg class="w-[22px] h-[22px] flex-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg><span class="hidden xl:inline">오시는 길</span></a>
    <button class="block w-full h-11 xl:h-12 border-t border-line/80 font-mark text-[12px] xl:text-[14px] tracking-[.12em] text-text transition-colors duration-200 hover:bg-white/70" id="toTop" type="button" aria-label="맨 위로">TOP</button>
  </div>
</aside>'''


def page(fn, title, desc, cur, body, og='assets/corridor.webp'):
    html = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<script>if('scrollRestoration' in history)history.scrollRestoration='manual'</script>
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="{SITE}/{"" if fn == "index.html" else fn}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#1E3A4C">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Noto+Serif+KR:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="icon" href="assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="stylesheet" href="assets/css/site.css?v={VER}">
</head>
<body>
{header(cur)}
<main>
{body}
</main>
{FOOTER}
<script src="assets/js/site.js?v={VER}"></script>
</body>
</html>
'''
    (ROOT / fn).write_text(html, encoding='utf-8')


def sh(en, title, desc=''):
    p = f'<p class="mt-4 {SUB_TEXT} max-w-[36em] leading-[1.75]">{desc}</p>' if desc else ''
    return f'<div class="mb-[clamp(32px,4vw,56px)]"><h2 class="{SERIF} text-[clamp(28px,3vw,44px)]">{title}</h2>{p}</div>'


def phero(img, en, title, desc, crumbs, pos='50% 50%'):
    trail = '<a class="underline underline-offset-[3px] decoration-white/35" href="index.html">홈</a>'
    for label, href in crumbs:
        trail += ' <span aria-hidden="true">/</span> '
        trail += f'<a class="underline underline-offset-[3px] decoration-white/35" href="{href}">{label}</a>' if href else f'<span>{label}</span>'
    return f'''<section id="top" class="relative isolate flex items-end min-h-[min(62svh,560px)] overflow-hidden bg-ink text-white before:content-[''] before:absolute before:inset-0 before:-z-[1] before:bg-[linear-gradient(180deg,rgba(52,41,32,.45)_0%,rgba(52,41,32,.35)_40%,rgba(52,41,32,.88)_100%)]">
  <div class="absolute inset-0 -z-[2]" aria-hidden="true" data-par><img class="w-full h-full object-cover will-change-transform" src="assets/{img}" alt="" style="object-position:{pos}"></div>
  <div class="{WRAP} pt-[calc(var(--hh)+48px)] pb-[clamp(40px,6vw,72px)]">
    <nav class="flex gap-2 text-[13px] text-white/75 mb-5" aria-label="현재 위치">{trail}</nav>
    <h1 class="{SERIF} text-[clamp(32px,4vw,56px)]">{title}</h1>
    <p class="mt-4 text-[clamp(15px,.8vw+11px,19px)] font-light text-white/85 max-w-[34em] leading-[1.7]">{desc}</p>
  </div>
</section>'''


def ctaband(title, desc, care=None):
    href = f'contact.html?care={care}#reserve' if care else 'contact.html#reserve'
    return f'''<section class="bg-ivory border-t border-line py-[clamp(72px,8vw,112px)]">
  <div class="{WRAP} flex flex-wrap justify-between items-center gap-x-10 gap-y-6">
    <div><h2 class="{SERIF} text-[clamp(22px,2.2vw,32px)] text-ink">{title}</h2><p class="mt-2.5 text-ink opacity-80">{desc}</p></div>
    <div class="flex flex-wrap gap-2">
      <a class="{btn_cls('ink')}" href="{href}">상담 예약</a>
    </div>
  </div>
</section>'''


CHK = 'grid gap-3.5 [&>li]:grid [&>li]:grid-cols-[20px_minmax(0,1fr)] [&>li]:gap-3.5 [&>li]:items-start [&>li]:text-[clamp(16px,.4vw+14px,18px)] [&>li]:leading-[1.6] [&>li]:before:content-[\'\'] [&>li]:before:w-5 [&>li]:before:h-px [&>li]:before:mt-[.85em] [&>li]:before:bg-bronze'
LEAD = 'text-[clamp(18px,1vw+13px,24px)] leading-[1.75] font-light max-w-[30em] [&+&]:mt-5'
SPLIT = 'grid gap-10 items-center lg:grid-cols-[6fr_5fr] lg:gap-24'
SPLIT_IMG = 'aspect-[4/5] overflow-hidden rounded-[4px] max-w-[520px] w-full bg-beige'
SEC = 'py-[clamp(96px,11vw,160px)]'

HS = [
    ('corridor.webp', '50% 40%', 'FACE CONTOUR, REBALANCED', '얼굴을 더하지 않고,<br>흩어진 균형을 바로잡습니다', '26년간 윤곽관리 한 분야에 집중해 온 대표원장이 해부학을 바탕으로 직접 진단하고 관리합니다.'),
    ('hero-2.webp', '60% 20%', '1:1 PERSONAL CONSULTATION', '관리 전, 원장이<br>직접 진단합니다', '얼굴 비율과 좌우 균형, 근육의 긴장도를 먼저 분석하고 지금 필요한 관리만 제안합니다.'),
    ('stock-hero3.webp', '60% 45%', 'HAND TECHNIQUE × PREMIUM DEVICE', '정교한 손기술 위에<br>엄선한 정품 장비', '프랑스 LPG®, 스페인 Termosalud 등 검증된 장비를 손기술과 함께 설계해 관리의 깊이를 더합니다.'),
]


def hero_slider():
    slides = ''.join(
        f'<div class="group absolute inset-0 -z-[2] opacity-0 [&>img]:will-change-transform transition-opacity duration-[1200ms] {EASE} [&.on]:opacity-100{" on" if i == 0 else ""}" aria-hidden="true" data-hs="slide">'
        f'<img class="w-full h-full object-cover scale-[1.08] transition-transform duration-[7000ms] ease-linear group-[.on]:scale-100" src="assets/{img}" alt="" style="object-position:{pos}"{" fetchpriority=high" if i == 0 else " loading=lazy"}></div>'
        for i, (img, pos, *_r) in enumerate(HS))
    txts = ''.join(
        f'<div class="hidden [&.on]:block [&.on]:animate-swap-slow{" on" if i == 0 else ""}" data-hs="txt">'
        f'<p class="font-sans font-semibold tracking-[-.03em] leading-[1.35] text-[clamp(30px,4vw,56px)]">{t}</p>'
        f'<p class="mt-6 text-[clamp(15px,1vw+10px,19px)] text-white/85 max-w-[34em] mx-auto leading-[1.7]">{d}</p></div>'
        for i, (_img, _pos, en, t, d) in enumerate(HS))
    dots = ''.join(
        f'<button class="group w-10 h-6 flex items-center{" on" if i == 0 else ""}" type="button" aria-label="{i + 1}번째 슬라이드" data-hs="dot">'
        f'<i class="relative block w-full h-px bg-white/35 overflow-hidden after:content-[\'\'] after:absolute after:inset-0 after:bg-white after:scale-x-0 after:origin-left group-[.on]:after:animate-fill-6 group-[.is-done]:after:scale-x-100"></i></button>'
        for i in range(len(HS)))
    return f'''<section id="hs" class="relative isolate flex items-center justify-center min-h-[100svh] overflow-hidden bg-ink text-white text-center before:content-[''] before:absolute before:inset-0 before:-z-[1] before:bg-[rgba(46,38,33,.42)]">
  <h1 class="sr-only">아르쎄에스테틱 김해 장유 윤곽관리 · 조막얼굴메소드®</h1>
  {slides}
  <div class="{WRAP} pt-hh">
    <div id="top" class="absolute inset-0 pointer-events-none"></div>
    {txts}
    <div class="flex items-center justify-center gap-5 mt-12 text-[13px] text-white/80">
      <button class="font-display text-[15px] tracking-[.06em] hover:text-white" type="button" data-hs="prev">Prev</button>
      <div class="flex gap-1.5">{dots}</div>
      <button class="font-display text-[15px] tracking-[.06em] hover:text-white" type="button" data-hs="next">Next</button>
    </div>
    <span class="sr-only" id="hsNum">01 / 03</span>
  </div>
  <div class="absolute left-1/2 bottom-8 -translate-x-1/2 flex flex-col items-center gap-2 text-white/70" aria-hidden="true"><span class="font-display text-[14px] tracking-[.08em]">Scroll down</span><span class="block w-px h-10 bg-white/50"></span></div>
</section>'''


METHOD_IMGS = [
    ('consult.webp', 1080, 1186, '대표원장이 상담실에서 고객과 마주 앉아 상담하는 모습', '70% 50%'),
    ('method-2.webp', 900, 1600, '원장이 목과 쇄골 라인을 이완하는 관리 장면', '50% 45%'),
    ('method-3.webp', 900, 1600, '원장이 얼굴 라인을 정돈하는 관리 장면', '50% 58%'),
    ('lounge-masks.webp', 900, 1600, '홈케어 제품이 진열된 아르쎄에스테틱 라운지', '60% 50%'),
]
STEP_NAMES = ['진단', '이완', '정돈', '유지']


def method_sec():
    steps = ''.join(
        f'<li><button class="group w-full text-left tracking-normal pt-4 pb-2 min-h-16 text-linen opacity-40 cursor-pointer transition-opacity duration-200 {EASE} hover:opacity-75 aria-selected:opacity-100" role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-controls="stepCopy" data-i="{i}"{"" if i == 0 else " tabindex=-1"}>'
        f'<span class="block h-0.5 bg-[rgba(243,235,221,.16)] overflow-hidden mb-4"><i class="block h-full bg-champagne scale-x-0 origin-left group-[.is-done]:scale-x-100 group-aria-selected:animate-fill-step [.paused_[aria-selected=true]_&]:animate-none [.paused_[aria-selected=true]_&]:scale-x-100" data-bar></i></span>'
        f'<span class="block text-[13px] tabular-nums tracking-[.08em]">0{i + 1}</span><span class="block text-[17px] font-medium mt-0.5">{t}</span></button></li>'
        for i, t in enumerate(STEP_NAMES))
    imgs = ''.join(
        f'<img class="absolute inset-0 w-full h-full object-cover opacity-0 scale-[1.06] transition-[opacity,transform] duration-[700ms,5000ms] ease-[var(--ease),linear] motion-reduce:transition-none [&.on]:opacity-100 [&.on]:scale-100{" on" if i == 0 else ""}" src="assets/{src}" width="{w}" height="{h}" alt="{alt}" loading="lazy" style="object-position:{pos}">'
        for i, (src, w, h, alt, pos) in enumerate(METHOD_IMGS))
    return f'''<section id="method" class="bg-espresso text-linen py-[clamp(96px,11vw,160px)] overflow-hidden" aria-labelledby="methodT">
  <div class="{WRAP} grid gap-12 items-center lg:grid-cols-[7fr_5fr] lg:gap-20">
    <div>
      <h2 id="methodT" class="{SERIF} text-[clamp(28px,3vw,44px)] [&_sup]:text-[.4em] [&_sup]:font-normal [&_sup]:align-top [&_sup]:ml-0.5">조막얼굴메소드<sup>®</sup></h2>
      <p class="mt-4 text-[rgba(243,235,221,.66)] text-[clamp(15px,.6vw+12px,18px)] max-w-[24em]">해부학을 바탕으로 직접 개발하고 상표로 등록한, 아르쎄의 윤곽관리입니다.</p>
      <ol class="mt-12 grid grid-cols-4 gap-2" role="tablist" aria-label="관리 단계" id="steps">{steps}</ol>
      <div class="mt-10 min-h-[150px]" id="stepCopy" role="tabpanel" aria-live="polite">
        <p class="{SERIF} text-[clamp(40px,4.6vw,68px)] !leading-[1.1]" id="stepT">진단</p>
        <p class="mt-5 text-[clamp(16px,.8vw+12px,20px)] text-[rgba(243,235,221,.66)] max-w-[22em]" id="stepD">좌우 비율과 근육의 긴장을 원장이 직접 확인합니다.</p>
      </div>
    </div>
    <figure class="relative w-full max-w-[480px] justify-self-center aspect-[4/5] overflow-hidden rounded-[4px] bg-ink" id="face" data-reveal>{imgs}</figure>
  </div>
</section>'''


EQ_TAB = f'flex-none min-h-12 px-[22px] rounded-[2px] border border-line bg-transparent text-[15px] font-medium tracking-[.02em] text-sub transition-[background-color,color,border-color] duration-200 {EASE} aria-selected:bg-ink aria-selected:border-ink aria-selected:text-ivory'
EQ_FACTS = 'mt-8 grid border-t border-line [&>div]:grid [&>div]:grid-cols-[88px_minmax(0,1fr)] [&>div]:gap-4 [&>div]:py-4 [&>div]:border-b [&>div]:border-line [&>div]:text-[15px] [&_dt]:text-bronze [&_dt]:font-medium [&_dd]:text-sub'


def eq_sec(head=True):
    tabs = ''.join(
        f'<button class="{EQ_TAB}" role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-controls="eqPanel" data-i="{i}"{"" if i == 0 else " tabindex=-1"}>{n}</button>'
        for i, n in enumerate(['LPG® 알리안스', '써마웨이브™', '자이오닉']))
    head_html = f'''<div>
      <h2 id="eqT" class="{SERIF} text-[clamp(28px,3vw,44px)]">손기술 위에,<br>정품 장비</h2>
      <p class="mt-4 {SUB_TEXT} max-w-[28em]">엄선한 프리미엄 장비로 관리의 깊이를 더합니다.</p>
    </div>''' if head else '<h2 id="eqT" class="sr-only">장비 소개</h2>'
    return f'''<section id="equipment" class="py-[clamp(120px,14vw,200px)] bg-mist" aria-labelledby="eqT">
  <div class="{WRAP}">
    {head_html}
    <div class="flex gap-2 {"mt-10" if head else ""} overflow-x-auto [scrollbar-width:none] [&::-webkit-scrollbar]:hidden" role="tablist" aria-label="장비 선택" id="eqTabs">{tabs}</div>
    <div class="grid gap-8 mt-8 items-center lg:grid-cols-[6fr_5fr] lg:gap-20" id="eqPanel" role="tabpanel" aria-live="polite">
      <div class="relative aspect-square max-h-[640px] w-full overflow-hidden [perspective:900px] bg-[radial-gradient(closest-side,#EEE3D2_0%,#EEE3D2_62%,rgba(210,237,233,0)_100%)]" id="eqStage" data-reveal><div class="absolute inset-0 transition-transform duration-500 ease-soft [transform-style:preserve-3d]" id="eqTilt"><div class="absolute inset-0 motion-safe:animate-float"><img class="absolute inset-0 m-auto w-[72%] h-[84%] object-contain drop-shadow-[0_24px_32px_rgba(52,41,32,.16)] animate-rise" id="eqImg" src="assets/eq-lpg.webp" alt="LPG 알리안스 장비" width="530" height="852" loading="lazy"></div></div></div>
      <div class="animate-swap" id="eqText">
        <p class="my-3 font-mark text-[12px] tracking-[.24em] text-bronze" id="eqBrand">LPG® · 프랑스</p>
        <h3 class="mt-2 {SERIF} text-[clamp(30px,3vw,44px)] !leading-[1.2]" id="eqName">LPG® 알리안스</h3>
        <p class="mt-4 text-[clamp(17px,.8vw+13px,22px)] leading-[1.6] max-w-[24em]" id="eqOne">롤러와 음압으로 피부를 부드럽게 집어 올리고 굴려, 뭉친 조직을 풀고 순환을 돕는 엔더몰로지 장비입니다.</p>
        <dl class="{EQ_FACTS}" id="eqFacts"></dl>
      </div>
    </div>
  </div>
</section>'''


def review_title(body):
    t = re.sub(r'<br\s*/?>', '\n', body)
    t = re.sub(r'<[^>]+>', '', t).strip()
    first = re.split(r'(?<=[.!?~])\s|\n', t)[0].strip()
    first = re.sub(r'[\s~.!]+$', '', first)
    return first if len(first) <= 34 else first[:32].rstrip() + '…'


def review_card(r, extra=''):
    kw = ''.join(f'<span class="text-[12px] py-1 px-2.5 rounded-full bg-mist text-ink">{k}</span>' for k in r['kw'])
    return f'''<article class="group flex flex-col rounded-xl border border-line bg-white overflow-hidden {extra}" data-rv data-reveal>
        <div class="flex-1 flex flex-col p-6">
          <h3 class="text-[17px] font-semibold tracking-[-.02em] leading-[1.45] line-clamp-2">{review_title(r['body'])}</h3>
          <p class="mt-3 text-[14px] text-sub leading-[1.75] line-clamp-4 group-[.open]:line-clamp-none" data-rv-body>{r['body']}</p>
          <button class="self-start mt-2 text-[13px] font-medium text-bronze min-h-8" type="button" hidden data-rv-more>더보기</button>
          <div class="mt-auto pt-5 flex flex-wrap gap-1.5">{kw}</div>
        </div>
        <div class="flex justify-between items-center gap-3 px-6 py-3.5 bg-mist text-[13px] text-sub"><span class="font-medium text-text">{r['who']}</span><span>{r['when']}</span></div>
      </article>'''


NAVER = 'https://m.place.naver.com/place/2088530746/review/visitor'


MAP_Q = '%EA%B2%BD%EB%82%A8%20%EA%B9%80%ED%95%B4%EC%8B%9C%20%EC%9C%A8%ED%95%98%EC%88%B2%EA%B8%B8%2021'
LOC_BTN = 'inline-flex items-center gap-2 h-11 px-5 rounded-full border border-line bg-white text-[14px] font-medium transition-colors duration-200 hover:bg-ink hover:text-ivory hover:border-ink'


def location_sec(sid='clinic', title_tag='h2'):
    rows = [
        ('주소', '<span class="js-addr"></span>'),
        ('영업시간', '월요일 – 토요일 10:00 – 21:00'),
        ('휴무', '일요일 정기휴무'),
        ('주차', '건물 지하주차장 이용'),
        ('전화', '<a class="js-tel js-tel-text underline underline-offset-4 decoration-line" href="#"></a>'),
        ('상담', '<a class="js-kakao underline underline-offset-4 decoration-line" href="#">카카오톡 상담</a> · <a class="underline underline-offset-4 decoration-line" href="contact.html#reserve">상담 예약 신청</a>'),
    ]
    dl = ''.join(f'<div class="grid grid-cols-[88px_minmax(0,1fr)] gap-4 py-4 border-b border-line"><dt class="text-[14px] font-semibold text-bronze">{k}</dt><dd class="text-[15px] leading-[1.7]">{v}</dd></div>' for k, v in rows)
    return f"""<section id="{sid}" class="{SEC} bg-mist" aria-labelledby="{sid}T">
  <div class="{WRAP}">
    <div class="text-center mb-[clamp(40px,5vw,64px)]">
      <{title_tag} id="{sid}T" class="{DISP} text-[clamp(44px,5vw,72px)] text-ink">Location</{title_tag}>
      <p class="mt-4 text-[clamp(16px,1vw+10px,19px)] text-sub">오시는 길</p>
    </div>
    <div class="grid gap-8 lg:grid-cols-[7fr_5fr] lg:gap-14 items-stretch">
      <div class="relative min-h-[320px] lg:min-h-[480px] overflow-hidden rounded-2xl bg-beige border border-line" data-reveal>
        <iframe class="absolute inset-0 w-full h-full border-0" src="https://maps.google.com/maps?q={MAP_Q}&z=17&output=embed" title="아르쎄에스테틱 위치 지도" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
      <div class="flex flex-col" data-reveal>
        <img class="w-auto h-[64px] self-start" src="assets/logo.webp" width="260" height="267" alt="" loading="lazy">
        <p class="mt-4 text-[clamp(22px,2vw,28px)] font-semibold tracking-[-.02em]">아르쎄에스테틱</p>
        <dl class="mt-5 border-t border-text">{dl}</dl>
        <div class="mt-6 flex flex-wrap gap-2">
          <a class="{LOC_BTN} js-map" href="#" target="_blank" rel="noopener">네이버 지도 {ARROW}</a>
          <a class="{LOC_BTN}" href="https://map.kakao.com/link/search/{MAP_Q}" target="_blank" rel="noopener">카카오맵 {ARROW}</a>
          <a class="{LOC_BTN}" href="https://www.google.com/maps/search/?api=1&query={MAP_Q}" target="_blank" rel="noopener">구글 지도 {ARROW}</a>
        </div>
      </div>
    </div>
  </div>
</section>"""


def ba_solo():
    tag = 'absolute top-3 z-[2] text-[11px] font-bold tracking-[.12em] py-1.5 px-2.5 rounded-full bg-white/90 text-ink'
    return f'''<div class="grid justify-items-center gap-2">
      <div class="relative w-full max-w-[360px] mx-auto aspect-[346/639] overflow-hidden rounded-[4px] bg-ivory touch-pan-y select-none [--p:50%]" data-ba>
        <img class="absolute inset-0 w-full h-full object-cover pointer-events-none" src="assets/ba-after.webp" width="346" height="639" alt="조막얼굴 윤곽관리 후 얼굴 라인" loading="lazy">
        <img class="absolute inset-0 w-full h-full object-cover pointer-events-none [clip-path:inset(0_calc(100%-var(--p))_0_0)]" src="assets/ba-before.webp" width="346" height="639" alt="조막얼굴 윤곽관리 전 얼굴 라인" loading="lazy">
        <span class="{tag} left-3">BEFORE</span><span class="{tag} right-3">AFTER</span>
        <span class="absolute inset-y-0 left-[var(--p)] w-0.5 -ml-px bg-white z-[2] pointer-events-none" aria-hidden="true"><span class="absolute top-1/2 left-1/2 w-11 h-11 -mt-[22px] -ml-[22px] rounded-full bg-white grid place-items-center text-ink shadow-[0_2px_10px_rgba(52,41,32,.25)]"><svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M7 5 L2 10 L7 15 M13 5 L18 10 L13 15"/></svg></span></span>
        <input class="absolute inset-0 w-full h-full m-0 opacity-0 cursor-ew-resize z-[3]" type="range" min="0" max="100" value="50" aria-label="관리 전후 비교, 좌우로 움직여 보세요">
      </div>
      <p class="mt-2 text-[12px] text-sub text-center">실제 고객 관리 전후 사진입니다. 개인에 따라 결과는 다를 수 있습니다.</p>
    </div>'''


PCARDS = [
    ('program-face.html', 'stock-face.webp', '35% 45%', 'FACE CONTOUR', '페이스 윤곽 케어', '붓기·비대칭·턱선을 정돈하는 시그니처'),
    ('program-aging.html', 'stock-aging.webp', '65% 45%', 'ANTI-AGING', '안티에이징 케어', '시술 없이 탄력과 결을 회복하는 웰에이징'),
    ('program-body.html', 'stock-body.webp', '55% 55%', 'BODY BALANCE', '바디 밸런스 케어', '목·어깨·승모근부터 이어지는 체형 균형'),
    ('program-mom.html', 'lounge.webp', '40% 60%', 'PRENATAL &amp; POSTPARTUM', '산전·산후 케어', '시기에 맞춘 안전한 회복 관리'),
]

HOME_FIND = [
    ('붓기 · 비대칭 · 턱선', 'program-face.html'), ('탄력과 피부결', 'program-aging.html'), ('목 · 어깨 · 승모근', 'program-body.html'),
    ('산전 · 산후 회복', 'program-mom.html'), ('조막얼굴메소드®', 'method.html'), ('정품 장비', 'equipment.html'),
]

home = f'''{hero_slider()}

<section class="grid lg:grid-cols-2">
  <div class="bg-beige flex flex-col items-center justify-center text-center px-gutter py-[clamp(80px,9vw,140px)] lg:min-h-[640px]" data-reveal>
    <h2 class="{DISP} text-[clamp(48px,5.4vw,80px)] text-ink">About Us</h2>
    <p class="mt-8 text-[clamp(17px,1.2vw+10px,21px)] font-semibold tracking-[-.02em] leading-[1.6] max-w-[22em]">윤곽관리 26년 경력의 조외현 대표원장이<br>직접 진단하고 관리합니다.</p>
    <p class="mt-5 text-[15px] text-sub leading-[1.8] max-w-[30em]">유행하는 시술 대신, 얼굴과 몸이 가진 본래의 균형을 해부학적으로 읽어내고 정돈하는 것. 처음에는 느리지만 시간이 갈수록 가속도가 붙는 변화를 지향합니다.</p>
    <a class="{PILL} mt-10" href="brand.html">View More {ARROW}</a>
  </div>
  <figure class="relative min-h-[360px] overflow-hidden" data-par><img class="absolute inset-0 w-full h-full object-cover" src="assets/interior-hero.webp" alt="아르쎄에스테틱 리셉션" loading="lazy" style="object-position:50% 50%"></figure>
</section>

<section class="{SEC}">
  <div class="{WRAP}">
    <div class="text-center mb-[clamp(40px,5vw,64px)]">
      <h2 class="{DISP} text-[clamp(44px,5vw,72px)] text-ink">Care Program</h2>
      <p class="mt-4 text-[clamp(16px,1vw+10px,19px)] text-sub">고민에 맞춘 네 가지 관리 프로그램</p>
    </div>
    <div class="grid grid-cols-2 gap-x-4 gap-y-10 sm:gap-x-6 sm:gap-y-12 2xl:grid-cols-4">
''' + '\n'.join(
    f'''      <a class="group block" href="{href}" data-reveal><figure class="aspect-[4/3] overflow-hidden rounded-xl bg-beige"><img class="w-full h-full object-cover transition-transform duration-[600ms] {EASE} group-hover:scale-[1.05]" src="assets/{img}" alt="" loading="lazy" style="object-position:{pos}"></figure><p class="mt-4 sm:mt-5 text-[16px] sm:text-[20px] font-semibold tracking-[-.02em]">{t}</p><p class="mt-1.5 text-[14px] text-sub">{d}</p><span class="{PILL} mt-5 h-10 px-5 text-[13px] group-hover:bg-ink group-hover:text-ivory group-hover:border-ink">View More {ARROW}</span></a>'''
    for href, img, pos, en, t, d in PCARDS) + f'''
    </div>
  </div>
</section>

<section id="reviews" class="{SEC} bg-mist" aria-labelledby="rvT">
  <div class="{WRAP}">
    <div class="text-center mb-[clamp(40px,5vw,64px)]">
      <h2 id="rvT" class="{DISP} text-[clamp(44px,5vw,72px)] text-ink">Review</h2>
      <p class="mt-4 text-[clamp(16px,1vw+10px,19px)] text-sub">네이버 플레이스에 고객님들이 직접 남겨주신 후기입니다.</p>
    </div>
    <div class="flex justify-between items-end gap-4 mb-5 text-[14px] text-sub"><p>Total <b class="text-bronze tabular-nums" data-count>133</b>건</p><a class="inline-flex items-center gap-1.5 hover:text-text" href="{NAVER}" target="_blank" rel="noopener">네이버에서 보기 {ARROW}</a></div>
    <div class="grid grid-flow-col auto-cols-[82%] gap-4 overflow-x-auto snap-x snap-mandatory [scrollbar-width:none] [&::-webkit-scrollbar]:hidden -mx-gutter px-gutter scroll-px-gutter md:mx-0 md:px-0 md:grid-flow-row md:auto-cols-auto md:grid-cols-2 xl:grid-cols-4 md:overflow-visible">
      {''.join(review_card(r, 'snap-start') for r in REVIEWS[:4])}
    </div>
    <div class="mt-12 text-center"><a class="{PILL}" href="review.html">후기 모두 보기 {ARROW}</a></div>
  </div>
</section>

{location_sec('location')}

<section class="pt-[clamp(80px,9vw,140px)] pb-[clamp(96px,11vw,160px)] bg-mist">
  <div class="{WRAP} text-center">
    <h2 class="text-[clamp(24px,2.4vw,34px)] font-semibold tracking-[-.03em]">나에게 맞는 관리 찾기</h2>
    <div class="mt-10 grid gap-3 grid-cols-2 lg:grid-cols-3 max-w-[960px] mx-auto">
''' + ''.join(
    f'''      <a class="flex items-center justify-between gap-3 min-h-[56px] px-5 rounded-md border border-line bg-ivory text-[15px] text-left transition-colors duration-200 hover:border-ink hover:bg-white" href="{h}">{t}{ARROW}</a>
''' for t, h in HOME_FIND) + '''    </div>
  </div>
</section>
'''
page('index.html', '아르쎄에스테틱 | 김해 장유 윤곽관리 · 조막얼굴메소드®', '윤곽관리 26년, 조외현 대표원장이 직접 진단하고 관리하는 김해 장유 아르쎄에스테틱. 해부학 기반 조막얼굴메소드®.', 'home', home)

VALS = [
    ('진단이 먼저입니다', '모든 관리는 대표원장의 1:1 진단에서 시작합니다. 얼굴 비율과 근육의 긴장, 생활 습관까지 살핀 뒤 필요한 관리만 제안합니다.'),
    ('해부학에 근거합니다', '한방피부미용학 석사, 국제 CIDESCO 자격을 바탕으로 근육과 근막의 구조를 따라 관리하는 조막얼굴메소드®를 개발했습니다.'),
    ('시술 없이 아름답게', '무언가를 더하기보다 본래의 균형을 회복하는 방식으로, 건강하고 자연스럽게 나이 드는 웰에이징을 지향합니다.'),
]
CV_EDU = ['대구한의대학교 대학원 한방피부미용학 석사', '마산대학교 뷰티케어학과 학사', '마산대학교 뷰티케어학과 겸임교수', '아르쎄 에스테틱 대표 · 트로이아르케 김해점 원장']
CV_CAREER = ['에스테틱 업계 26년 · 누적 관리 고객 5만 명 이상', '전) 스파현 대표원장, 윤곽전문에스테틱 (창원·김해·장유)', '2022–2025 경남기능경기대회 채점감독', '조막얼굴메소드® 개발']
CV_CERT = [
    '국제 시데스코(CIDESCO) 자격증',
    '영국 치체스터 대학교(University of Chichester) 단기 연수 수료',
    '상해대학교 학부학 실습 수료',
    'Prenatal &amp; Postpartum Care (산전·산후 회복관리 과정) 국제 디플로마',
    '브레인 리웨이브 프로그램 수료 (국제 뉴로아로마콜로지 연구소 / 연 80시간 과정)',
    'LaStone Therapy (핫&amp;콜드 스톤 마사지) 수료',
    'Power Tree SPA Treatment 과정 수료 (Nouvelle Esthetic Academy)',
    '국제 트리콜로지스트 자격 (KCT / International Trichologists Federation)',
    ('World Atopy Association', ['아토피 상담사 (Atopy Counselor)', '아토피 디톡스 코디네이터 (Detox Coordinator)']),
    ('대한 자격기관 소아디톡스 전문가', ['리커버리 스트레칭 지도자', '바디케어 전문가', '발모관리 상담지도자']),
    '약석약회 발건강 강사 자격',
]
CV_UL = 'grid gap-2 text-[15px] text-sub'


def cv_list(items):
    out = ''
    for it in items:
        if isinstance(it, tuple):
            out += f'<li>{it[0]}<ul class="grid gap-1 mt-1.5 pl-4 text-[14px]">' + ''.join(f'<li>{x}</li>' for x in it[1]) + '</ul></li>'
        else:
            out += f'<li>{it}</li>'
    return f'<ul class="{CV_UL}">{out}</ul>'


GAL = [
    ('interior-hero.webp', 1500, 2000, '민트색 리셉션 데스크와 아르쎄 간판', '리셉션', False),
    ('lounge.webp', 1500, 2000, '핑크 벨벳 소파가 놓인 라운지', '라운지', False),
    ('mirror.webp', 2000, 1500, '조명이 들어간 타원형 거울과 화장대', '파우더룸', True),
    ('lounge-masks.webp', 1500, 2000, '얼굴 모형이 진열된 선반과 라운지', '라운지 · 얼굴 모형 선반', False),
]
CARE = [
    ('care-1', '원장이 장비로 목과 쇄골 라인을 관리하는 영상'),
    ('care-2', '원장이 장비로 어깨와 목을 관리하는 영상'),
    ('care-3', '원장이 얼굴 라인을 관리하는 영상'),
]
H4 = 'mb-3 text-[14px] font-bold text-bronze'

FEED = [('consult.webp', '60% 50%', '관리 전, 원장이', '직접 진단합니다', '얼굴 비율과 좌우 균형, 근육의 긴장도를 먼저 분석하고 지금 필요한 관리만 제안합니다.'), ('stock-drop.webp', '50% 45%', '정교한 손기술 위에', '엄선한 정품 장비', '프랑스 LPG®, 스페인 Termosalud 등 검증된 장비를 손기술과 함께 설계해 관리의 깊이를 더합니다.'), ('stock-serum.webp', '50% 60%', '대표원장이 직접,', '처음부터 끝까지.', '상담부터 관리, 사후 홈케어 가이드까지 한 분이 책임집니다.')]
CIRCLES = [('diag', 'DIAGNOSIS FIRST', '진단이 먼저입니다', '대표원장의 1:1 진단 후<br>필요한 관리만 제안합니다.'), ('anat', 'ANATOMY BASED', '해부학에 근거합니다', '근육과 근막의 구조를 따라<br>관리하는 조막얼굴메소드®'), ('well', 'WELL AGEING', '시술 없이 아름답게', '본래의 균형을 회복하는<br>웰에이징 관리'), ('one', 'ONE DIRECTOR', '처음부터 끝까지', '상담부터 관리, 홈케어 가이드까지<br>대표원장이 직접')]
CIRCLE_ICON = {'diag': '<path d="M12 4a4 4 0 0 1 4 4c0 3-4 5-4 5s-4-2-4-5a4 4 0 0 1 4-4z"/><path d="M6 20c1-3 3.5-4.5 6-4.5s5 1.5 6 4.5"/><path d="M17 8h3M18.5 6.5v3"/>', 'anat': '<path d="M12 3v18"/><path d="M8 6c-2 2-2 5 0 7M16 6c2 2 2 5 0 7"/><path d="M6 17c2 1.5 4 2 6 2s4-.5 6-2"/>', 'well': '<path d="M12 21c-4-3-7-6.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 3.5-3 7-7 10z"/><path d="M9 12h6M12 9v6"/>', 'one': '<circle cx="12" cy="8" r="3.5"/><path d="M5 20c1.2-3.5 3.8-5.5 7-5.5s5.8 2 7 5.5"/><path d="M4 4l2 2M20 4l-2 2"/>'}
FIND = [('붓기 · 비대칭 · 턱선', 'program-face.html'), ('탄력과 피부결', 'program-aging.html'), ('목 · 어깨 · 승모근', 'program-body.html'), ('산전 · 산후 회복', 'program-mom.html'), ('조막얼굴메소드®', 'method.html'), ('정품 장비', 'equipment.html')]
HL = 'bg-[linear-gradient(transparent_55%,#E6D3B8_55%)] px-1 -mx-1'


def feed_row(i, img, pos, t1, t2, d):
    rev = i % 2 == 1
    return f"""    <article class="grid items-center lg:grid-cols-2">
      <div class="px-gutter py-12 lg:py-0 {'lg:order-2 lg:pl-20' if rev else 'lg:pl-[max(var(--gutter),calc((100vw-1360px)/2+var(--gutter)))] lg:pr-20'}" data-reveal>
        <h3 class="text-[clamp(24px,2.2vw,34px)] font-semibold tracking-[-.03em] leading-[1.45]">{t1}<br><span class="{HL}">{t2}</span></h3>
        <p class="mt-6 text-sub text-[15px] leading-[1.85] max-w-[26em]">{d}</p>
      </div>
      <figure class="relative aspect-[4/3] lg:aspect-auto lg:h-[min(46vw,560px)] overflow-hidden bg-beige {'lg:order-1' if rev else ''}" data-par><img class="w-full h-full object-cover" src="assets/{img}" alt="" loading="lazy" style="object-position:{pos}"></figure>
    </article>"""


brand = f"""<section id="about" class="relative isolate overflow-hidden bg-espresso text-linen pt-[calc(var(--hh)+clamp(96px,12vw,180px))] pb-[clamp(120px,15vw,220px)] min-h-[100svh] flex items-center text-center before:content-[''] before:absolute before:inset-0 before:-z-[1] before:bg-[rgba(46,38,33,.62)]" aria-label="아르쎄의 철학">
  <div id="top" class="absolute inset-0 pointer-events-none"></div>
  <div class="absolute inset-0 -z-[2]" aria-hidden="true" data-par><img class="w-full h-full object-cover" src="assets/corridor.webp" alt="" loading="lazy" style="object-position:50% 40%"></div>
  <div class="{WRAP}">
    <h1 class="sr-only">아르쎄에스테틱 브랜드 소개</h1>
    <p class="{DISP} text-[clamp(40px,6vw,92px)] text-ivory">Arcé Aesthetic</p>
    <p class="mt-10 text-[clamp(15px,1vw+10px,18px)] text-ivory/85 leading-[2]">같은 골격이라도 씹는 습관, 자세, 순환 상태에 따라<br class="max-sm:hidden"> 얼굴의 윤곽은 달라집니다.<br><br>아르쎄는 무언가를 더하기보다<br class="max-sm:hidden"> 흩어진 균형을 제자리로 돌려놓습니다.</p>
    <p class="mt-10 text-[clamp(17px,1.2vw+10px,22px)] font-semibold text-champagne leading-[1.7]">처음에는 느리지만,<br>시간이 갈수록 가속도가 붙는 변화.</p>
  </div>
</section>
<section class="{SEC}">
  <div class="{WRAP}">
    <div class="grid grid-cols-2 lg:grid-cols-4 max-w-[1240px] mx-auto border-t border-text">
""" + ''.join(
    f"""      <div class="group relative pt-8 pb-10 px-5 sm:px-7 border-b border-line {'lg:border-r' if i < 3 else ''} {'max-lg:border-r' if i % 2 == 0 else ''} transition-colors duration-300 hover:bg-white" data-reveal><span class="absolute top-0 left-0 h-[2px] w-0 bg-bronze transition-[width] duration-500 ease-soft group-hover:w-full"></span><div class="flex items-start justify-between"><span class="font-display text-[clamp(36px,3.4vw,52px)] leading-none text-champagne">0{i + 1}</span><svg class="w-8 h-8 sm:w-9 sm:h-9 text-bronze" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{CIRCLE_ICON[ic]}</svg></div><p class="mt-8 font-mark text-[10px] sm:text-[11px] tracking-[.2em] text-bronze">{en}</p><p class="mt-2 text-[16px] sm:text-[19px] font-semibold tracking-[-.02em]">{t}</p><p class="mt-3 text-[13px] sm:text-[14px] text-sub leading-[1.7]">{d.replace('<br>', ' ')}</p></div>
""" for i, (ic, en, t, d) in enumerate(CIRCLES)) + f"""    </div>
  </div>
</section>
<section id="space" class="py-[clamp(96px,10vw,140px)] bg-mist" aria-labelledby="spaceT">
  <div class="{WRAP} text-center mb-10">
    <h2 id="spaceT" class="{SERIF} text-[clamp(26px,2.6vw,38px)]">아르쎄의 공간</h2>
    <p class="mt-3 {SUB_TEXT}">밝고 깨끗한 공간에서, 관리에만 집중하세요.</p>
  </div>
  <div class="{WRAP} max-w-[1100px]">
    <div class="relative" id="gal" aria-roledescription="carousel" aria-label="매장 사진">
      <div class="relative aspect-[4/3] md:aspect-[16/9] overflow-hidden rounded-2xl bg-beige">
""" + ''.join(
    f"""        <figure class="group absolute inset-0 opacity-0 transition-opacity duration-700 {EASE} [&.on]:opacity-100{' on' if i == 0 else ''}" data-slide aria-hidden="{'false' if i == 0 else 'true'}"><img class="w-full h-full object-cover scale-[1.03] transition-transform duration-[4000ms] ease-out group-[.on]:scale-100" src="assets/{src}" width="{w}" height="{h}" alt="{alt}" loading="lazy"><figcaption class="absolute left-1/2 bottom-5 -translate-x-1/2 rounded-full bg-[rgba(58,48,41,.72)] text-ivory text-[14px] px-6 py-1.5 backdrop-blur-sm">{cap}</figcaption></figure>
""" for i, (src, w, h, alt, cap, wide) in enumerate(GAL)) + f"""      </div>
      <button class="absolute left-2 md:-left-6 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-white/80 backdrop-blur grid place-items-center text-ink shadow-[0_4px_16px_rgba(52,41,32,.12)]" type="button" data-gal="prev" aria-label="이전 사진"><svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M11 3 L5 9 L11 15"/></svg></button>
      <button class="absolute right-2 md:-right-6 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-white/80 backdrop-blur grid place-items-center text-ink shadow-[0_4px_16px_rgba(52,41,32,.12)]" type="button" data-gal="next" aria-label="다음 사진"><svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M7 3 L13 9 L7 15"/></svg></button>
      <div class="flex justify-center gap-2 mt-6">""" + ''.join(
    f'<button class="h-1.5 rounded-full bg-mute transition-all duration-300 w-1.5 [&.on]:w-6 [&.on]:bg-bronze{" on" if i == 0 else ""}" type="button" data-gal-dot aria-label="{i + 1}번째 사진"></button>'
    for i in range(len(GAL))) + f"""</div>
    </div>
  </div>
</section>
<section class="py-[clamp(48px,6vw,96px)]">
  <div class="grid gap-[clamp(24px,4vw,64px)]">
""" + '\n'.join(feed_row(i, *r) for i, r in enumerate(FEED)) + f"""
  </div>
</section>
<section id="care" class="py-[clamp(96px,10vw,140px)] bg-mist" aria-labelledby="careT">
  <div class="{WRAP} flex flex-wrap justify-between items-end gap-x-10 gap-y-3 mb-10">
    <h2 id="careT" class="{SERIF} text-[clamp(26px,2.6vw,38px)]">관리 현장</h2>
    <p class="{SUB_TEXT}">원장이 직접, 처음부터 끝까지 관리합니다.</p>
  </div>
  <div class="flex gap-4 overflow-x-auto snap-x snap-mandatory [scrollbar-width:none] [&::-webkit-scrollbar]:hidden px-gutter scroll-px-gutter lg:max-w-site lg:mx-auto lg:justify-center lg:overflow-visible" id="careRow">
""" + ''.join(
    f"""    <figure data-reveal class="flex-[0_0_min(64vw,300px)] snap-start aspect-[9/16] rounded-[4px] overflow-hidden bg-beige lg:flex-[1_1_0] lg:max-w-[340px]"><video class="block w-full h-full object-cover" poster="assets/{n}.jpg" muted loop playsinline preload="none" aria-label="{a}"><source src="assets/{n}.mp4" type="video/mp4"><source src="assets/{n}.webm" type="video/webm"></video></figure>
""" for n, a in CARE) + f"""  </div>
</section>
<section class="{SEC}">
  <div class="{WRAP} text-center">
    <h2 class="{SERIF} text-[clamp(26px,2.6vw,38px)]">고민에 맞춘 관리 프로그램</h2>
    <div class="mt-10 grid gap-3 grid-cols-2 lg:grid-cols-3 max-w-[960px] mx-auto">
""" + ''.join(
    f"""      <a class="flex items-center justify-between gap-3 min-h-[56px] px-5 rounded-md border border-line bg-ivory text-[15px] text-left transition-colors duration-200 hover:border-ink hover:bg-white" href="{h}">{t}{ARROW}</a>
""" for t, h in FIND) + f"""    </div>
  </div>
</section>
{ctaband('대표원장이 직접, 처음부터 끝까지.', '상담부터 관리, 사후 홈케어 가이드까지 한 분이 책임집니다.')}
"""
page('brand.html', '브랜드 소개 | 아르쎄에스테틱', '얼굴을 더하지 않고 흩어진 균형을 바로잡는 김해 장유 윤곽 전문 에스테틱, 아르쎄. 대표원장 조외현 소개와 공간.', 'brand', brand)

STATS = [('26', 'YEARS', '에스테틱 업계 경력'), ('50,000+', 'CLIENTS', '누적 관리 고객'), ('CIDESCO', 'LICENSE', '국제 시데스코 자격')]
CV_BLOCKS = [('EDUCATION', '학력 · 직위', CV_EDU), ('CAREER', '경력', CV_CAREER), ('LICENSE', '자격 · 연수', CV_CERT)]


def cv_rows(items):
    out = ''
    for it in items:
        if isinstance(it, tuple):
            out += f'<li class="py-4 border-b border-line">{it[0]}<ul class="mt-2 grid gap-1 pl-4 text-[14px] text-sub">' + ''.join(f'<li>· {x}</li>' for x in it[1]) + '</ul></li>'
        else:
            out += f'<li class="py-4 border-b border-line">{it}</li>'
    return out


director = phero('interior-hero.webp', 'DIRECTOR', '원장 약력', '시술 없이 자연스럽게, 건강하고 아름답게 나이 드는 관리.', [('ARCÉ', 'brand.html'), ('원장 약력', None)], '50% 50%') + f"""
<section class="{SEC}">
  <div class="{WRAP}">
    <div class="text-center">
      <p class="font-mark text-[13px] tracking-[.3em] text-bronze">JO OE HYUN</p>
      <h2 class="mt-4 {SERIF} text-[clamp(30px,3vw,44px)]">조외현 <span class="text-[.5em] text-sub tracking-normal">대표원장</span></h2>
      <p class="mt-6 {SERIF} text-[clamp(18px,1.4vw,22px)] text-sub">“시술 없이 자연스럽게,<br>건강하고 아름답게 나이 드는 관리.”</p>
    </div>
    <div class="mt-[clamp(56px,7vw,96px)] grid gap-4 md:grid-cols-3 max-w-[1080px] mx-auto">
""" + ''.join(
    f"""      <div class="text-center py-10 rounded-2xl bg-mist" data-reveal><p class="font-display text-[clamp(44px,5vw,72px)] leading-none text-bronze tabular-nums"{' data-count' if n.isdigit() else ''}>{n}</p><p class="mt-3 font-mark text-[11px] tracking-[.3em] text-text">{en}</p><p class="mt-2 text-[14px] text-sub">{d}</p></div>
""" for n, en, d in STATS) + f"""    </div>
  </div>
</section>
<section class="{SEC} bg-mist">
  <div class="{WRAP} grid gap-[clamp(64px,7vw,104px)] max-w-[1080px]">
""" + ''.join(
    f"""    <div class="grid gap-6 lg:grid-cols-[280px_minmax(0,1fr)] lg:gap-16" data-reveal>
      <div><p class="font-mark text-[12px] tracking-[.3em] text-bronze">{en}</p><h3 class="mt-3 {SERIF} text-[clamp(22px,2vw,30px)]">{t}</h3></div>
      <ul class="border-t border-text text-[16px]">{cv_rows(items)}</ul>
    </div>
""" for en, t, items in CV_BLOCKS) + f"""  </div>
</section>
{ctaband('대표원장이 직접, 처음부터 끝까지.', '상담부터 관리, 사후 홈케어 가이드까지 한 분이 책임집니다.')}
"""
page('director.html', '원장 약력 | 아르쎄에스테틱', '아르쎄에스테틱 조외현 대표원장 약력. 에스테틱 업계 26년, 국제 시데스코(CIDESCO) 자격, 한방피부미용학 석사.', 'brand', director)

METHOD_WHY = [('진단', '대표원장의 1:1 얼굴 진단으로 시작합니다'), ('흐름', '저작근·광대 주변·목까지 이어지는 흐름을 함께 관리합니다'), ('설계', '필요한 경우 정품 장비를 더해 관리의 깊이를 설계합니다')]
method = f"""<section id="top" class="relative isolate flex items-center justify-center text-center min-h-[min(70svh,620px)] overflow-hidden bg-ink text-white before:content-[''] before:absolute before:inset-0 before:-z-[1] before:bg-[rgba(46,38,33,.5)]">
  <div class="absolute inset-0 -z-[2]" aria-hidden="true" data-par><img class="w-full h-full object-cover will-change-transform" src="assets/method-3.webp" alt="" style="object-position:50% 50%"></div>
  <div class="{WRAP} pt-hh">
    <p class="{DISP} text-[clamp(44px,6vw,88px)]">Signature Method</p>
    <h1 class="mt-3 text-[clamp(18px,1.4vw+10px,24px)] font-semibold tracking-[-.02em]">조막얼굴메소드<sup class="text-[.55em]">®</sup></h1>
    <p class="mt-3 text-[clamp(14px,.6vw+11px,17px)] text-white/80 max-w-[34em] mx-auto leading-[1.7]">해부학을 기반으로 대표원장이 직접 개발하고 상표로 등록한 아르쎄만의 윤곽관리 프로토콜입니다.</p>
  </div>
  <div class="absolute left-1/2 bottom-6 -translate-x-1/2 flex flex-col items-center gap-2 text-white/70" aria-hidden="true"><span class="font-display text-[14px] tracking-[.08em]">Scroll down</span><span class="block w-px h-8 bg-white/50"></span></div>
</section>
<section class="{SEC}">
  <div class="{WRAP} grid gap-10 items-center lg:grid-cols-2 lg:gap-20">
    <figure class="aspect-[4/5] max-h-[620px] w-full overflow-hidden rounded-2xl bg-beige" data-reveal data-par><img class="w-full h-full object-cover" src="assets/consult.webp" alt="대표원장이 상담실에서 고객과 마주 앉아 상담하는 모습" loading="lazy" style="object-position:60% 50%"></figure>
    <div data-reveal>
      <h2 class="text-[clamp(26px,2.6vw,38px)] font-semibold tracking-[-.03em] leading-[1.4]">얼굴 라인은<br><span class="{HL}">근육과 근막이 만듭니다</span></h2>
      <p class="mt-6 font-display text-[48px] leading-[.5] text-champagne" aria-hidden="true">“</p>
      <p class="mt-3 text-[16px] leading-[1.85] max-w-[32em]">같은 골격이라도 씹는 습관, 자세, 순환 상태에 따라 얼굴의 윤곽은 달라집니다. 조막얼굴메소드®는 윤곽을 흐트러뜨리는 원인을 해부학적으로 찾아 근육과 근막의 균형을 바로잡는 데 집중합니다.</p>
      <ol class="mt-10 border-t border-text">""" + ''.join(
    f'<li class="grid grid-cols-[56px_64px_minmax(0,1fr)] items-baseline gap-2 py-5 border-b border-line"><span class="font-display text-[22px] text-champagne">0{i + 1}</span><b class="text-[16px] font-semibold text-bronze">{k}</b><span class="text-[15px] leading-[1.7]">{v}</span></li>'
    for i, (k, v) in enumerate(METHOD_WHY)) + f"""</ol>
    </div>
  </div>
</section>
{method_sec().replace('<h2 id="methodT" class="' + SERIF + ' text-[clamp(28px,3vw,44px)] [&_sup]:text-[.4em] [&_sup]:font-normal [&_sup]:align-top [&_sup]:ml-0.5">조막얼굴메소드<sup>®</sup></h2>', '<h2 id="methodT" class="' + DISP + ' text-[clamp(44px,5vw,72px)] text-ivory">Program Order</h2>')}
<section class="{SEC} bg-mist" id="result">
  <div class="{WRAP}">
    <div class="text-center mb-[clamp(40px,5vw,64px)]">
      <h2 class="{DISP} text-[clamp(44px,5vw,72px)] text-ink">Before &amp; After</h2>
      <p class="mt-4 text-[clamp(16px,1vw+10px,19px)] text-sub">가운데 손잡이를 좌우로 움직여 관리 전후의 얼굴 라인을 비교해 보세요.</p>
    </div>
    {ba_solo()}
  </div>
</section>
<section class="{SEC} text-center">
  <div class="{WRAP}">
    <img class="mx-auto w-auto h-[72px]" src="assets/logo.webp" width="260" height="267" alt="" loading="lazy">
    <h2 class="mt-8 text-[clamp(22px,2.2vw,32px)] font-semibold tracking-[-.03em]">내 얼굴의 균형, 진단부터 받아보세요.</h2>
    <p class="mt-3 text-sub">조막얼굴메소드® 상담은 대표원장이 직접 진행합니다.</p>
    <a class="{PILL} mt-8 bg-ink text-ivory border-ink hover:bg-bronze hover:border-bronze" href="contact.html?care=조막얼굴 윤곽관리#reserve">상담 예약 {ARROW}</a>
  </div>
</section>
"""
page('method.html', '조막얼굴메소드® | 아르쎄에스테틱', '해부학 기반으로 대표원장이 직접 개발하고 상표 등록한 아르쎄의 윤곽관리 프로토콜, 조막얼굴메소드®.', 'method', method, 'assets/interior-hero.webp')


PROGRAM_TABS = [('program-face.html', '페이스 윤곽 케어'), ('program-aging.html', '안티에이징 케어'), ('program-body.html', '바디 밸런스 케어'), ('program-mom.html', '산전·산후 케어')]
PROGRAM_EXTRA = {
    'program-face.html': ('Face Contour', 'method-3.webp', '50% 55%'),
    'program-aging.html': ('Anti-Aging', 'consult.webp', '60% 50%'),
    'program-body.html': ('Body Balance', 'method-2.webp', '50% 45%'),
    'program-mom.html': ('Prenatal Care', 'interior-hero.webp', '50% 50%'),
}
DEVICES = {
    'lpg': ('eq-lpg.webp', 'LPG® · FRANCE', 'LPG® 알리안스', '롤러와 음압으로 피부와 피하 조직을 부드럽게 자극해, 뭉친 조직을 풀고 순환을 돕는 엔더몰로지 장비입니다.', ['롤러 + 음압(흡입)을 이용한 기계적 자극', '바디 라인, 셀룰라이트, 얼굴 탄력']),
    'thermawave': ('eq-thermawave.webp', 'LPHYSIO · WELLNESS DEVICE', '써마웨이브™', '따뜻한 열감을 이용해 얼굴과 바디의 라인, 탄력을 함께 관리하는 장비입니다.', ['열감을 이용한 관리', '얼굴 라인, 바디 라인']),
    'zionic': ('eq-zionic.webp', 'TERMOSALUD · SPAIN', '자이오닉', '깊게 회전하는 마사지와 고주파 열을 동시에 전달하는 바디 컨투어링 장비입니다.', ['회전 마사지(MARP) + 470kHz 모노폴라 고주파', '복부, 허벅지, 엉덩이 등 바디']),
}
CHECK = '<svg class="w-4 h-4 mt-1 flex-none text-bronze" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 8.5l3 3 7-7"/></svg>'


def program(fn, img, pos, en, title, desc, intro, recs, steps, devices, note, care):
    disp, oimg, opos = PROGRAM_EXTRA[fn]
    tabs = ''.join(
        f'<a class="inline-flex items-center h-10 px-5 rounded-full text-[14px] border transition-colors duration-200 {"bg-ink text-ivory border-ink" if h == fn else "bg-ivory border-line text-sub hover:border-ink hover:text-text"}" href="{h}"{" aria-current=page" if h == fn else ""}>{t}</a>'
        for h, t in PROGRAM_TABS)
    dev_names = ' · '.join(DEVICES[h][2] for _, h in devices) if devices else '손기술 중심'
    info = [('진행', '대표원장 1:1'), ('과정', f'{len(steps)} Steps'), ('장비', dev_names)]
    info_html = ''.join(
        f'<div class="px-3 text-center"><p class="font-display text-[15px] text-bronze">{k}</p><p class="mt-1 text-[14px] font-medium">{v}</p></div>'
        for k, v in info)
    rec = ''.join(f'<li class="flex gap-3 py-3.5 border-b border-line last:border-b-0">{CHECK}<span>{r}</span></li>' for r in recs)
    st = ''.join(
        f'<li class="flex gap-4 items-start" data-reveal><span class="flex-none inline-flex items-center h-7 px-3 rounded-full border border-champagne/60 font-display text-[13px] tracking-[.06em] text-champagne">STEP {i + 1}</span><div><p class="text-[17px] font-semibold">{t}</p><p class="mt-1 text-[14px] text-linen/70 leading-[1.7]">{d}</p></div></li>'
        for i, (t, d) in enumerate(steps))
    dev_cards = ''.join(
        f'''<article class="grid sm:grid-cols-[200px_minmax(0,1fr)] gap-6 items-center rounded-2xl bg-white p-6" data-reveal>
          <div class="aspect-[16/10] sm:aspect-square rounded-xl bg-mist grid place-items-center p-4 overflow-hidden"><img class="max-h-full max-w-full object-contain" src="assets/{DEVICES[h][0]}" alt="{DEVICES[h][2]}" loading="lazy"></div>
          <div><p class="font-mark text-[12px] tracking-[.14em] text-bronze">{DEVICES[h][1]}</p><h3 class="mt-1.5 text-[20px] font-semibold tracking-[-.02em]">{DEVICES[h][2]}</h3><p class="mt-2 text-[14px] text-sub leading-[1.7]">{DEVICES[h][3]}</p>
            <ul class="mt-3 grid gap-1 text-[14px]">{''.join(f'<li class="flex gap-2">{CHECK}<span>{x}</span></li>' for x in DEVICES[h][4])}</ul>
            <a class="{PILL} mt-4 h-9 px-4 text-[13px]" href="equipment.html#{h}">장비 자세히 {ARROW}</a></div>
        </article>''' for _, h in devices)
    devsec = f'''<section class="{SEC} bg-mist">
  <div class="{WRAP}">
    <div class="text-center mb-[clamp(40px,5vw,64px)]">
      <h2 class="{DISP} text-[clamp(44px,5vw,72px)] text-ink">Knowhow</h2>
      <p class="mt-4 text-[clamp(16px,1vw+10px,19px)] text-sub">상태에 따라 손기술에 정품 장비를 더해 관리합니다.</p>
    </div>
    <div class="grid gap-4 lg:grid-cols-2">{dev_cards}</div>
  </div>
</section>''' if devices else ''
    notep = f'<p class="mt-5 text-[13px] text-sub leading-[1.7] text-center">{note}</p>' if note else ''
    body = f'''<section id="top" class="relative isolate flex items-center justify-center text-center min-h-[min(70svh,620px)] overflow-hidden bg-ink text-white before:content-[''] before:absolute before:inset-0 before:-z-[1] before:bg-[rgba(46,38,33,.45)]">
  <div class="absolute inset-0 -z-[2]" aria-hidden="true" data-par><img class="w-full h-full object-cover will-change-transform" src="assets/{img}" alt="" style="object-position:{pos}"></div>
  <div class="{WRAP} pt-hh">
    <p class="{DISP} text-[clamp(44px,6vw,88px)]">{disp}</p>
    <h1 class="mt-3 text-[clamp(18px,1.4vw+10px,24px)] font-semibold tracking-[-.02em]">{title}</h1>
    <p class="mt-3 text-[clamp(14px,.6vw+11px,17px)] text-white/80 max-w-[34em] mx-auto leading-[1.7]">{desc}</p>
  </div>
  <div class="absolute left-1/2 bottom-6 -translate-x-1/2 flex flex-col items-center gap-2 text-white/70" aria-hidden="true"><span class="font-display text-[14px] tracking-[.08em]">Scroll down</span><span class="block w-px h-8 bg-white/50"></span></div>
</section>
<nav class="flex flex-wrap justify-center gap-2 px-gutter pt-10" aria-label="관리 프로그램">{tabs}</nav>
<section class="{SEC}">
  <div class="{WRAP} grid gap-10 items-center lg:grid-cols-2 lg:gap-20">
    <figure class="aspect-[4/5] max-h-[620px] w-full overflow-hidden rounded-2xl bg-beige" data-reveal data-par><img class="w-full h-full object-cover" src="assets/{img}" alt="" loading="lazy" style="object-position:{pos}"></figure>
    <div data-reveal>
      <h2 class="text-[clamp(26px,2.6vw,38px)] font-semibold tracking-[-.03em] text-bronze">{title}</h2>
      <p class="mt-6 font-display text-[48px] leading-[.5] text-champagne" aria-hidden="true">“</p>
      {''.join(f'<p class="mt-3 text-[16px] leading-[1.85] max-w-[32em]">{x}</p>' for x in intro)}
      <div class="mt-10 grid grid-cols-3 divide-x divide-line border-y border-line py-5">{info_html}</div>
    </div>
  </div>
</section>
<section class="pb-[clamp(96px,11vw,160px)]">
  <div class="{WRAP} max-w-[760px]">
    <h2 class="text-center text-[clamp(22px,2vw,30px)] font-semibold tracking-[-.03em]">이런 분께 추천해요</h2>
    <ul class="mt-8 rounded-2xl bg-white px-6 sm:px-10 py-3 text-[16px]" data-reveal>{rec}</ul>
    {notep}
  </div>
</section>
<section class="{SEC} bg-espresso text-linen overflow-hidden">
  <div class="{WRAP} grid gap-12 items-center lg:grid-cols-[5fr_6fr] lg:gap-20">
    <figure class="aspect-[4/3] lg:aspect-[4/5] overflow-hidden rounded-2xl bg-ink" data-reveal data-par><img class="w-full h-full object-cover" src="assets/{oimg}" alt="" loading="lazy" style="object-position:{opos}"></figure>
    <div>
      <h2 class="{DISP} text-[clamp(44px,5vw,72px)] text-ivory">Program Order</h2>
      <ol class="mt-10 grid gap-7">{st}</ol>
    </div>
  </div>
</section>
{devsec}
<section class="{SEC} text-center">
  <div class="{WRAP}">
    <img class="mx-auto w-auto h-[72px]" src="assets/logo.webp" width="260" height="267" alt="" loading="lazy">
    <h2 class="mt-8 text-[clamp(22px,2.2vw,32px)] font-semibold tracking-[-.03em]">{title}, 상담으로 시작하세요.</h2>
    <p class="mt-3 text-sub">현재 상태를 진단한 뒤 필요한 관리와 회차를 안내해 드립니다.</p>
    <a class="{PILL} mt-8 bg-ink text-ivory border-ink hover:bg-bronze hover:border-bronze" href="contact.html?care={care}#reserve">상담 예약 {ARROW}</a>
  </div>
</section>
'''
    page(fn, f'{title} | 아르쎄에스테틱', desc, 'program', body, 'assets/' + img)


program('program-face.html', 'stock-face.webp', '35% 40%', 'FACE CONTOUR CARE', '페이스 윤곽 케어',
        '조막얼굴메소드®로 붓기와 비대칭, 턱선을 정돈하는 아르쎄의 시그니처 관리입니다.',
        ['얼굴이 커 보이는 원인은 골격만이 아닙니다. 굳은 저작근, 정체된 순환, 좌우 근육의 불균형이 윤곽을 흐트러뜨립니다.',
         '페이스 윤곽 케어는 조막얼굴메소드®를 바탕으로 원인을 진단하고, 근육과 근막의 균형을 바로잡아 얼굴 본래의 라인을 정돈합니다.'],
        ['사진 속 얼굴이 커 보여 고민인 분', '아침 붓기가 오래 지속되는 분', '좌우 비대칭, 각진 턱선이 신경 쓰이는 분', '웨딩·촬영 등 중요한 일정을 앞둔 분'],
        [('진단', '정면·측면 비율과 좌우 균형, 근육의 긴장도를 분석합니다.'), ('이완', '저작근과 광대 주변, 목 근막의 긴장을 손기술로 풉니다.'), ('정돈', '턱선과 얼굴 외곽 라인을 해부학적 구조에 따라 정돈합니다.'), ('유지', '순환 관리와 홈케어 가이드로 정돈된 라인을 이어갑니다.')],
        [('써마웨이브™', 'thermawave'), ('LPG® 알리안스', 'lpg')], '관리 결과는 개인의 얼굴 구조와 생활 습관에 따라 다를 수 있습니다.', '페이스 윤곽 케어')

program('program-aging.html', 'stock-aging.webp', '65% 40%', 'NATURAL ANTI-AGING CARE', '안티에이징 케어',
        '시술에 의존하지 않고, 피부와 근막의 탄력을 단계적으로 회복하는 웰에이징 관리입니다.',
        ['나이가 들며 생기는 처짐은 피부 표면만의 문제가 아니라, 근막의 탄력과 순환이 함께 떨어지면서 나타납니다.',
         '안티에이징 케어는 처짐의 방향과 피부 상태를 진단한 뒤, 탄력 중심의 손기술과 장비를 더해 건강하고 자연스럽게 나이 드는 피부를 만듭니다.'],
        ['볼살과 턱선의 처짐이 신경 쓰이기 시작한 분', '반복된 시술로 피부가 예민해진 분', '자연스러운 변화를 원하는 분', '꾸준한 관리 루틴이 필요한 분'],
        [('피부 진단', '피부 결, 탄력, 처짐의 방향을 확인합니다.'), ('탄력 케어', '처짐 방향을 고려한 손기술로 근막과 피부의 탄력을 끌어올립니다.'), ('장비 케어', '필요에 따라 열감 장비로 관리의 깊이를 더합니다.'), ('홈케어', '관리 효과가 이어지도록 생활 습관과 홈케어를 안내합니다.')],
        [('써마웨이브™', 'thermawave'), ('LPG® 알리안스', 'lpg')], '', '안티에이징 케어')

program('program-body.html', 'stock-body.webp', '50% 60%', 'BODY BALANCE CARE', '바디 밸런스 케어',
        '목·어깨·승모근부터 바디 라인까지, 체형의 균형과 순환을 함께 다루는 관리입니다.',
        ['얼굴 라인은 목과 어깨에서 시작됩니다. 뭉친 승모근과 굽은 자세는 순환을 막아 얼굴 붓기와 바디 실루엣에까지 영향을 줍니다.',
         '바디 밸런스 케어는 체형의 불균형을 진단하고, 손기술과 정품 장비를 함께 사용해 뭉친 조직을 풀고 순환을 정돈합니다.'],
        ['목·어깨·승모근이 늘 뭉쳐 있는 분', '오래 앉아서 일하는 분', '몸의 좌우 균형이 틀어진 느낌이 드는 분', '셀룰라이트와 붓기가 고민인 분'],
        [('체형 진단', '자세와 좌우 균형, 뭉침 부위를 확인합니다.'), ('이완', '목·어깨·등의 긴장을 손기술로 풉니다.'), ('장비 케어', 'LPG®·자이오닉으로 순환과 바디 라인을 관리합니다.'), ('홈케어', '스트레칭과 생활 습관 가이드를 안내합니다.')],
        [('LPG® 알리안스', 'lpg'), ('자이오닉', 'zionic')], '', '바디 밸런스 케어')

program('program-mom.html', 'lounge.webp', '40% 60%', 'PRENATAL &amp; POSTPARTUM CARE', '산전·산후 케어',
        '국제 산전·산후 회복관리 디플로마를 수료한 대표원장이 시기와 컨디션에 맞춰 진행합니다.',
        ['임신과 출산 시기의 몸은 매주 달라집니다. 같은 관리라도 시기와 컨디션에 따라 강도와 방식이 달라져야 합니다.',
         '산전·산후 케어는 Prenatal &amp; Postpartum Care 국제 디플로마를 수료한 대표원장이 시기별 상태를 확인하며, 붓기와 뭉침을 부드럽게 관리하고 출산 후 얼굴과 바디의 균형 회복을 돕습니다.'],
        ['임신 중 붓기와 뭉침으로 불편한 분', '출산 후 컨디션 회복이 필요한 분', '출산 후 달라진 얼굴·바디 라인이 고민인 분'],
        [('상담', '임신 주수, 출산 시기, 현재 컨디션을 확인합니다.'), ('순환 케어', '부드러운 손기술로 붓기와 뭉침을 관리합니다.'), ('균형 회복', '출산 후 얼굴과 바디의 균형 회복을 돕습니다.'), ('생활 가이드', '시기에 맞는 홈케어와 생활 습관을 안내합니다.')],
        [], '임신 중 관리는 주수와 건강 상태를 상담으로 확인한 뒤 진행하며, 필요한 경우 담당 의료진과 먼저 상의해 주세요.', '산전·산후 케어')

EQ_ORDER = [('lpg', '붓기와 뭉침이 잦고 바디 라인이 고민인 분'), ('thermawave', '탄력 저하와 처짐이 고민인 분'), ('zionic', '셀룰라이트, 붓기, 처진 바디 라인이 고민인 분')]


def eq_slide(i, key):
    img, brand_, name, one, facts = DEVICES[key]
    return f"""<li class="group/eq absolute top-0 left-1/2 w-[64%] sm:w-[44%] lg:w-[34%] h-full -translate-x-1/2 transition-[transform,opacity,filter] duration-700 ease-soft opacity-0 pointer-events-none data-[pos=c]:opacity-100 data-[pos=c]:pointer-events-auto data-[pos=l]:opacity-50 data-[pos=r]:opacity-50 data-[pos=l]:blur-[3px] data-[pos=r]:blur-[3px] data-[pos=l]:-translate-x-[150%] data-[pos=r]:translate-x-[50%] data-[pos=l]:scale-[.82] data-[pos=r]:scale-[.82] data-[pos=l]:pointer-events-auto data-[pos=r]:pointer-events-auto data-[pos=l]:cursor-pointer data-[pos=r]:cursor-pointer" data-eqs="{i}" data-pos="{'c' if i == 0 else 'r' if i == 1 else 'l'}" role="group" aria-roledescription="slide" aria-label="{name}">
        <div class="relative h-full rounded-3xl bg-white shadow-[0_20px_50px_rgba(52,41,32,.08)]"><img class="absolute inset-[9%] w-[82%] h-[82%] object-contain drop-shadow-[0_18px_24px_rgba(52,41,32,.14)]" src="assets/{img}" alt="{name}" loading="lazy"></div>
      </li>"""


def eq_detail(i, key, who):
    img, brand_, name, one, facts = DEVICES[key]
    tags = ''.join(f'<span class="inline-flex items-center h-8 px-3.5 rounded-full border border-bronze/40 text-[13px] text-bronze">#{x}</span>' for x in facts)
    return f"""<div class="{'' if i == 0 else 'hidden '}text-center animate-swap" data-eqd="{i}" id="{key}">
        <p class="font-mark text-[12px] tracking-[.18em] text-bronze">{brand_}</p>
        <h2 class="mt-3 text-[clamp(26px,2.6vw,38px)] font-semibold tracking-[-.03em]">{name}</h2>
        <p class="mt-4 text-[16px] text-sub leading-[1.8] max-w-[34em] mx-auto">{one}</p>
        <div class="mt-6 flex flex-wrap justify-center gap-2">{tags}</div>
        <p class="mt-6 inline-flex gap-2 text-[15px]">{CHECK}<span>이런 분께 · {who}</span></p>
      </div>"""


ARR_BTN = 'w-12 h-12 rounded-full bg-white grid place-items-center text-ink shadow-[0_4px_16px_rgba(52,41,32,.12)] transition-colors hover:bg-ink hover:text-ivory'
eq = f"""<section id="top" class="relative isolate flex items-center justify-center text-center min-h-[min(70svh,620px)] overflow-hidden bg-ink text-white before:content-[''] before:absolute before:inset-0 before:-z-[1] before:bg-[rgba(46,38,33,.45)]">
  <div class="absolute inset-0 -z-[2]" aria-hidden="true" data-par><img class="w-full h-full object-cover will-change-transform" src="assets/interior-hero.webp" alt="" style="object-position:50% 40%"></div>
  <div class="{WRAP} pt-hh">
    <p class="{DISP} text-[clamp(44px,6vw,88px)]">Technology We Use</p>
    <h1 class="mt-3 text-[clamp(18px,1.4vw+10px,24px)] font-semibold tracking-[-.02em]">손기술 위에, 정품 장비</h1>
    <p class="mt-3 text-[clamp(14px,.6vw+11px,17px)] text-white/80">엄선한 프리미엄 장비로 관리의 깊이를 더합니다.</p>
  </div>
  <div class="absolute left-1/2 bottom-6 -translate-x-1/2 flex flex-col items-center gap-2 text-white/70" aria-hidden="true"><span class="font-display text-[14px] tracking-[.08em]">Scroll down</span><span class="block w-px h-8 bg-white/50"></span></div>
</section>
<section id="eqCarousel" class="{SEC} bg-mist overflow-hidden" aria-roledescription="carousel" aria-label="장비 소개">
  <div class="{WRAP}">
    <div class="flex justify-center gap-2 mb-12" role="tablist" aria-label="장비 선택">""" + ''.join(
    f'<button class="inline-flex items-center h-10 px-5 rounded-full text-[14px] border border-line bg-ivory text-sub transition-colors duration-200 hover:text-text aria-selected:bg-ink aria-selected:text-ivory aria-selected:border-ink" type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}" data-eqt="{i}">{DEVICES[k][2]}</button>'
    for i, (k, _) in enumerate(EQ_ORDER)) + f"""</div>
    <div class="relative">
      <ul class="relative h-[clamp(300px,42vw,520px)] touch-pan-y select-none" id="eqTrack">
      """ + ''.join(eq_slide(i, k) for i, (k, _) in enumerate(EQ_ORDER)) + f"""
      </ul>
      <button class="absolute left-0 lg:left-[8%] top-1/2 -translate-y-1/2 z-10 {ARR_BTN}" type="button" data-eqnav="-1" aria-label="이전 장비"><svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M11 3 L5 9 L11 15"/></svg></button>
      <button class="absolute right-0 lg:right-[8%] top-1/2 -translate-y-1/2 z-10 {ARR_BTN}" type="button" data-eqnav="1" aria-label="다음 장비"><svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M7 3 L13 9 L7 15"/></svg></button>
    </div>
    <div class="mt-12" aria-live="polite">
      """ + ''.join(eq_detail(i, k, w) for i, (k, w) in enumerate(EQ_ORDER)) + f"""
    </div>
  </div>
</section>
""" + ctaband('어떤 장비가 맞을지, 상담으로 정해 드립니다.', '피부와 체형 상태에 따라 손기술과 장비를 함께 설계합니다.')
page('equipment.html', '장비 소개 | 아르쎄에스테틱', '프랑스 LPG® 알리안스, 써마웨이브™, 스페인 Termosalud 자이오닉. 아르쎄에스테틱의 프리미엄 장비.', 'equipment', eq, 'assets/eq-lpg.webp')

review = phero('lounge-masks.webp', 'REVIEW', '고객후기', '네이버 플레이스에 고객님들이 직접 남겨주신 방문자 리뷰입니다.', [('고객후기', None)], '50% 60%') + f'''
<section id="reviews" class="{SEC}" aria-labelledby="rvT">
  <div class="{WRAP}">
    <div class="text-center mb-[clamp(40px,5vw,64px)]">
      <h2 id="rvT" class="text-[clamp(28px,2.8vw,40px)] font-semibold tracking-[-.03em]">방문자 리뷰</h2>
      <p class="mt-3 text-[clamp(15px,.6vw+12px,18px)] text-sub">네이버 플레이스에 고객님들이 직접 남겨주신 후기입니다.</p>
    </div>
    <div class="flex justify-between items-end gap-4 mb-5 text-[14px] text-sub"><p>Total <b class="text-bronze tabular-nums" data-count>133</b>건</p><a class="inline-flex items-center gap-1.5 hover:text-text" href="{NAVER}" target="_blank" rel="noopener">네이버에서 보기 {ARROW}</a></div>
    <div class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
{chr(10).join(review_card(r) for r in REVIEWS)}
    </div>
  </div>
</section>
<section class="{SEC} bg-beige">
  <div class="{WRAP}">
    {sh('BEFORE &amp; AFTER', '관리 전후 비교')}
    {ba_solo()}
  </div>
</section>
{ctaband('다음 후기의 주인공이 되어 보세요.', '1:1 상담으로 지금 상태에 맞는 관리를 안내해 드립니다.')}
'''
page('review.html', '고객후기 | 아르쎄에스테틱', '네이버 플레이스 방문자 리뷰 133건. 아르쎄에스테틱 고객후기.', 'review', review, 'assets/lounge-masks.webp')

F_LABEL = 'block text-[14px] font-medium mb-2'
F_INPUT = f'w-full h-16 border-0 border-b-[1.5px] border-line p-0 text-[22px] bg-transparent rounded-none transition-colors duration-200 {EASE} placeholder:text-mute focus:outline-none focus:border-bronze group-[.err]:border-error'
F_MSG = 'hidden mt-2 text-[13px] text-error group-[.err]:block'

contact = phero('entrance.webp', 'CONTACT &amp; LOCATION', '상담·오시는 길', '상담은 대표원장이 직접 진행합니다. 편하신 방법으로 문의해 주세요.', [('상담·오시는 길', None)], '50% 45%') + f'''
<section id="reserve" class="py-[clamp(120px,14vw,200px)]" aria-labelledby="resvT">
  <div class="group/resv {WRAP} grid gap-14 lg:grid-cols-[6fr_5fr] lg:gap-24" id="resvBox">
    <div>
      <h2 id="resvT" class="{SERIF} text-[clamp(26px,2.6vw,38px)]">상담 문의</h2>
      <p class="mt-4 text-[clamp(16px,1vw+11px,20px)] text-sub">상담 후 결정하셔도 괜찮습니다.</p>
      <div class="flex flex-wrap gap-x-8 gap-y-2 mt-8">
        <a class="{MORE} js-kakao" href="#">카카오톡 상담 {ARROW}</a>
        <a class="{MORE} js-tel" href="#">전화 <span class="js-tel-text"></span> {ARROW}</a>
      </div>
      <figure class="mt-10 max-w-[420px] aspect-[4/5] overflow-hidden rounded-[4px] bg-beige" data-ph data-par><img class="w-full h-full object-cover" src="assets/consult.webp" width="1080" height="1186" alt="대표원장이 상담실에서 고객과 마주 앉아 상담하는 모습" loading="lazy" style="object-position:60% 50%"></figure>
    </div>
    <div>
      <form class="grid gap-6 content-start group-[.sent]/resv:hidden" id="form" novalidate>
        <div class="group" id="fName"><label class="{F_LABEL}" for="name">이름</label><input class="{F_INPUT}" type="text" id="name" autocomplete="name" placeholder="홍길동"><p class="{F_MSG}">이름을 입력해 주세요.</p></div>
        <div class="group" id="fPhone"><label class="{F_LABEL}" for="phone">연락처</label><input class="{F_INPUT}" type="tel" id="phone" autocomplete="tel" inputmode="numeric" maxlength="13" placeholder="010-0000-0000"><p class="{F_MSG}">휴대폰 번호를 정확히 입력해 주세요.</p></div>
        <div class="group" id="fArea"><label class="{F_LABEL}" for="area">관리받고 싶은 부위</label><input class="{F_INPUT}" type="text" id="area" autocomplete="off" placeholder="예) 턱선, 얼굴 붓기, 어깨 뭉침"></div>
        <div class="group" id="fAgree"><label class="grid grid-cols-[22px_minmax(0,1fr)] gap-x-3 items-start text-[14px] leading-[1.6] text-sub cursor-pointer"><input class="appearance-none w-[22px] h-[22px] m-0 border-[1.5px] border-mute rounded-md bg-ivory grid place-items-center cursor-pointer transition-colors duration-150 {EASE} after:content-[''] after:w-1.5 after:h-[11px] after:border-solid after:border-white after:border-t-0 after:border-l-0 after:border-r-2 after:border-b-2 after:-translate-y-px after:rotate-45 after:opacity-0 checked:bg-ink checked:border-ink checked:after:opacity-100 focus-visible:outline-2 focus-visible:outline-offset-2 group-[.err]:border-error" type="checkbox" id="agree"><span class="pt-px">[필수] 상담 예약을 위한 개인정보(이름, 연락처) 수집·이용에 동의합니다. 상담 완료 후 6개월간 보관 후 파기됩니다.</span></label><p class="{F_MSG}">개인정보 수집·이용에 동의해 주세요.</p></div>
        <button class="{btn_cls('ink', extra='w-full')}" type="submit">상담 예약 신청</button>
      </form>
      <div class="hidden content-center gap-3 py-12 group-[.sent]/resv:grid group-[.sent]/resv:animate-swap" role="status"><b class="text-[32px] tracking-[-.03em]">신청이 접수되었습니다.</b><p class="text-sub">영업시간 내에 연락드려 예약 시간을 확정해 드릴게요.</p></div>
    </div>
  </div>
</section>
{location_sec()}
'''
page('contact.html', '상담·오시는 길 | 아르쎄에스테틱', '경남 김해시 율하숲길 21 303호. 월–토 10:00–21:00, 일요일 정기휴무. 아르쎄에스테틱 상담 문의.', 'contact', contact, 'assets/entrance.webp')
