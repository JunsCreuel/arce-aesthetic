import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
REVIEWS = json.loads((ROOT / 'src' / 'reviews.json').read_text(encoding='utf-8'))

WRAP = 'w-full max-w-site mx-auto px-gutter'
SERIF = 'font-serif font-medium tracking-[-.025em] leading-[1.38]'
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
    ('ARCÉ', 'brand.html', 'brand', [('브랜드 소개', 'brand.html#about', 'ABOUT'), ('대표원장', 'brand.html#director', 'DIRECTOR'), ('공간', 'brand.html#space', 'SPACE'), ('관리 현장', 'brand.html#care', 'IN CARE')]),
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
  <div class="mt-8 grid gap-2">
    {kakao_btn(icon=False)}
    <a class="{btn_cls('line')} js-tel" href="#"><span class="js-tel-text"></span></a>
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
<div id="mcta" class="fixed inset-x-0 bottom-0 z-40 grid lg:hidden grid-cols-[7fr_3fr] gap-2 pt-3 px-[max(16px,env(safe-area-inset-left,0px))] pb-[calc(12px+env(safe-area-inset-bottom,0px))] bg-ivory shadow-[0_-1px_0_#E2D6C4] translate-y-[110%] transition-transform duration-300 {EASE} [&.show]:translate-y-0">
  {kakao_btn(size='bar')}
  <a class="{btn_cls('line', 'bar')} js-tel" href="#" aria-label="전화 문의">전화</a>
</div>'''


def page(fn, title, desc, cur, body, og='assets/corridor.webp'):
    html = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og}">
<meta name="theme-color" content="#1E3A4C">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Noto+Serif+KR:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="icon" href="assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
{header(cur)}
<main>
{body}
</main>
{FOOTER}
<script src="assets/js/site.js"></script>
</body>
</html>
'''
    (ROOT / fn).write_text(html, encoding='utf-8')


def sh(en, title, desc=''):
    p = f'<p class="mt-4 {SUB_TEXT} max-w-[36em] leading-[1.75]">{desc}</p>' if desc else ''
    return f'<div class="mb-[clamp(32px,4vw,56px)]"><p class="mt-4 font-mark tracking-[.36em] {SUB_TEXT} max-w-[36em] leading-[1.75]">{en}</p><h2 class="{SERIF} text-[clamp(28px,3vw,44px)]">{title}</h2>{p}</div>'


def phero(img, en, title, desc, crumbs, pos='50% 50%'):
    trail = '<a class="underline underline-offset-[3px] decoration-white/35" href="index.html">홈</a>'
    for label, href in crumbs:
        trail += ' <span aria-hidden="true">/</span> '
        trail += f'<a class="underline underline-offset-[3px] decoration-white/35" href="{href}">{label}</a>' if href else f'<span>{label}</span>'
    return f'''<section id="top" class="relative isolate flex items-end min-h-[min(62svh,560px)] overflow-hidden bg-ink text-white before:content-[''] before:absolute before:inset-0 before:-z-[1] before:bg-[linear-gradient(180deg,rgba(52,41,32,.45)_0%,rgba(52,41,32,.35)_40%,rgba(52,41,32,.88)_100%)]">
  <div class="absolute inset-0 -z-[2]" aria-hidden="true" data-par><img class="w-full h-full object-cover will-change-transform" src="assets/{img}" alt="" style="object-position:{pos}"></div>
  <div class="{WRAP} pt-[calc(var(--hh)+48px)] pb-[clamp(40px,6vw,72px)]">
    <nav class="flex gap-2 text-[13px] text-white/75 mb-5" aria-label="현재 위치">{trail}</nav>
    <p class="{EN} text-champagne mb-3">{en}</p>
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
      {kakao_btn()}
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
        f'<div class="group absolute inset-0 -z-[2] opacity-0 transition-opacity duration-[1200ms] {EASE} [&.on]:opacity-100{" on" if i == 0 else ""}" aria-hidden="true" data-hs="slide">'
        f'<img class="w-full h-full object-cover scale-[1.08] transition-transform duration-[7000ms] ease-linear group-[.on]:scale-100" src="assets/{img}" alt="" style="object-position:{pos}"{" fetchpriority=high" if i == 0 else " loading=lazy"}></div>'
        for i, (img, pos, *_r) in enumerate(HS))
    txts = ''.join(
        f'<div class="hidden [&.on]:block [&.on]:animate-swap-slow{" on" if i == 0 else ""}" data-hs="txt">'
        f'<p class="{EN} text-champagne mb-4">{en}</p>'
        f'<p class="{SERIF} text-[clamp(32px,4.2vw,62px)]">{t}</p>'
        f'<p class="mt-5 text-[clamp(15px,1vw+10px,20px)] font-light text-white/85 max-w-[30em] leading-[1.7]">{d}</p></div>'
        for i, (_img, _pos, en, t, d) in enumerate(HS))
    dots = ''.join(
        f'<button class="group w-12 h-8 flex items-center{" on" if i == 0 else ""}" type="button" aria-label="{i + 1}번째 슬라이드" data-hs="dot">'
        f'<i class="relative block w-full h-0.5 bg-white/30 overflow-hidden after:content-[\'\'] after:absolute after:inset-0 after:bg-white after:scale-x-0 after:origin-left group-[.on]:after:animate-fill-6 group-[.is-done]:after:scale-x-100"></i></button>'
        for i in range(len(HS)))
    return f'''<section id="hs" class="relative isolate flex items-end lg:items-center min-h-[100svh] overflow-hidden bg-ink text-white before:content-[''] before:absolute before:inset-0 before:-z-[1] before:bg-[linear-gradient(180deg,rgba(52,41,32,.35)_0%,rgba(52,41,32,.2)_35%,rgba(52,41,32,.6)_65%,rgba(52,41,32,.92)_100%)] lg:before:bg-[linear-gradient(90deg,rgba(52,41,32,.85)_0%,rgba(52,41,32,.5)_45%,rgba(52,41,32,.1)_80%)]">
  <h1 class="sr-only">아르쎄에스테틱 김해 장유 윤곽관리 · 조막얼굴메소드®</h1>
  {slides}
  <div class="{WRAP} pt-hh pb-[calc(40px+env(safe-area-inset-bottom,0px))] lg:pb-0">
    <div id="top" class="absolute inset-0 pointer-events-none"></div>
    {txts}
    <div class="flex flex-wrap gap-2 mt-8">
      {kakao_btn(light=True, extra='flex-[1_1_180px] lg:flex-none')}
      <a class="{btn_cls('line', extra='flex-[1_1_180px] lg:flex-none text-white')}" href="contact.html#reserve">상담 예약</a>
    </div>
    <div class="flex items-center gap-4 mt-10"><div class="flex gap-2">{dots}</div><span class="text-[13px] tabular-nums text-white/75" id="hsNum">01 / 03</span></div>
  </div>
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
    <figure class="relative w-full max-w-[480px] justify-self-center aspect-[4/5] overflow-hidden rounded-[4px] bg-ink" id="face">{imgs}</figure>
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
      <div class="relative aspect-square max-h-[640px] w-full grid place-items-center overflow-hidden bg-[radial-gradient(closest-side,#EEE3D2_0%,#EEE3D2_62%,rgba(210,237,233,0)_100%)]"><img class="max-w-[72%] max-h-[84%] w-auto h-auto object-contain drop-shadow-[0_24px_32px_rgba(52,41,32,.16)] animate-rise" id="eqImg" src="assets/eq-lpg.webp" alt="LPG 알리안스 장비" width="530" height="852" loading="lazy"></div>
      <div class="animate-swap" id="eqText">
        <p class="my-3 font-mark text-[12px] tracking-[.24em] text-bronze" id="eqBrand">LPG® · 프랑스</p>
        <h3 class="mt-2 {SERIF} text-[clamp(30px,3vw,44px)] !leading-[1.2]" id="eqName">LPG® 알리안스</h3>
        <p class="mt-4 text-[clamp(17px,.8vw+13px,22px)] leading-[1.6] max-w-[24em]" id="eqOne">롤러와 음압으로 피부를 부드럽게 집어 올리고 굴려, 뭉친 조직을 풀고 순환을 돕는 엔더몰로지 장비입니다.</p>
        <dl class="{EQ_FACTS}" id="eqFacts"></dl>
      </div>
    </div>
  </div>
</section>'''


def review_card(r, grid=False):
    kw = ''.join(f'<span class="text-[12px] py-1 px-2.5 rounded-[2px] border border-line text-ink">{k}</span>' for k in r['kw'])
    flex = '' if grid else 'flex-[0_0_min(84vw,360px)] snap-start'
    return f'''<article class="group {flex} flex flex-col gap-3 border-t border-[rgba(58,48,41,.28)] pt-6 px-1 pb-2" data-rv>
        <div class="flex justify-between items-baseline gap-3 text-[13px] text-sub"><b class="text-[15px] text-text">{r['who']}</b><span>{r['when']}</span></div>
        <p class="text-[15px] leading-[1.7] line-clamp-6 group-[.open]:line-clamp-none" data-rv-body>{r['body']}</p>
        <button class="self-start text-[13px] font-medium tracking-[.04em] text-bronze min-h-8" type="button" hidden data-rv-more>더보기</button>
        <div class="mt-auto flex flex-wrap gap-1.5">{kw}</div>
      </article>'''


KW = [('관리 효과가 좋아요', 115), ('맞춤 케어를 잘해줘요', 106), ('친절해요', 93), ('시술이 꼼꼼해요', 91)]


def rv_head():
    rows = ''.join(
        f'<li class="grid grid-cols-[132px_minmax(0,1fr)_36px] items-center gap-3 text-[13px] text-sub"><span>{n}</span>'
        f'<span class="h-px bg-[rgba(58,48,41,.16)]"><i class="block h-px bg-ink origin-left scale-x-[.02] transition-transform duration-1000 {EASE} group-[.in]:scale-x-[var(--w)]" style="--w:{c / KW[0][1]:.3f}"></i></span>'
        f'<span class="text-right font-display text-[16px] tabular-nums">{c}</span></li>'
        for n, c in KW)
    return f'''<div class="{WRAP} grid gap-8 mb-10 lg:grid-cols-[minmax(0,1fr)_minmax(0,480px)] lg:items-end">
    <div>
      <h2 id="rvT" class="{SERIF} text-[clamp(26px,2.6vw,38px)]">방문자 리뷰 <span class="font-display font-medium text-[1.25em] text-bronze tabular-nums" data-count>133</span></h2>
      <p class="mt-3 text-sub text-[15px]">네이버 플레이스에 고객님들이 직접 남겨주신 후기입니다.</p>
    </div>
    <ul class="group grid gap-3 max-w-[520px] w-full" id="kw" aria-label="리뷰 키워드 통계">{rows}</ul>
  </div>'''


NAVER = 'https://m.place.naver.com/place/2088530746/review/visitor'


def clinic_sec():
    dd = 'text-[17px] font-medium tabular-nums'
    dt = 'text-[13px] text-champagne'
    return f'''<section id="clinic" class="relative isolate flex items-end min-h-[100svh] overflow-hidden bg-ink text-white before:content-[''] before:absolute before:inset-0 before:-z-[1] before:bg-[linear-gradient(180deg,rgba(52,41,32,0)_30%,rgba(52,41,32,.6)_55%,rgba(52,41,32,.94)_100%)] lg:before:bg-[linear-gradient(180deg,rgba(52,41,32,0)_35%,rgba(52,41,32,.55)_60%,rgba(52,41,32,.92)_100%)]" aria-labelledby="clinicT">
  <div class="absolute inset-0 -z-[2]" aria-hidden="true"><img id="clinicImg" class="w-full h-[118%] object-cover object-[50%_45%] will-change-transform motion-reduce:!transform-none" src="assets/entrance.webp" alt="" loading="lazy" width="1500" height="2000"></div>
  <div class="{WRAP} pt-[120px] pb-[clamp(56px,7vw,96px)]">
    <h2 id="clinicT" class="leading-[0]"><img class="block w-auto h-[clamp(150px,17vw,250px)]" src="assets/logo-light.webp" width="260" height="267" alt="아르쎄에스테틱 오시는 길" loading="lazy"></h2>
    <dl class="mt-12 grid grid-cols-2 gap-x-4 gap-y-6 border-t border-white/30 pt-6 lg:grid-cols-4">
      <div class="grid gap-1"><dt class="{dt}">영업시간</dt><dd class="{dd}">월–토 10:00 – 21:00</dd></div>
      <div class="grid gap-1"><dt class="{dt}">휴무</dt><dd class="{dd}">일요일 정기휴무</dd></div>
      <div class="grid gap-1"><dt class="{dt}">주차</dt><dd class="{dd}">지하주차장</dd></div>
      <div class="grid gap-1"><dt class="{dt}">전화</dt><dd class="{dd}"><a class="js-tel js-tel-text underline underline-offset-4 decoration-white/40" href="#"></a></dd></div>
      <div class="grid gap-1 lg:col-span-2"><dt class="{dt}">주소</dt><dd class="{dd} js-addr"></dd></div>
    </dl>
    <a class="{MORE.replace('gap-2', 'gap-2.5')} mt-8 js-map" href="#" target="_blank" rel="noopener">네이버 지도에서 보기 {ARROW}</a>
  </div>
</section>'''


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

home = f'''{hero_slider()}

<section class="{SEC}">
  <div class="{WRAP}">
    <div>
      <p class="{EN} text-bronze mb-4">ABOUT ARCÉ</p>
      <p class="{LEAD}"><b>아르쎄에스테틱</b>은 윤곽관리 26년 경력의 조외현 대표원장이 직접 진단하고 관리하는 김해 장유의 윤곽 전문 에스테틱입니다.</p>
      <p class="{LEAD}">유행하는 시술 대신, 얼굴과 몸이 가진 본래의 균형을 해부학적으로 읽어내고 정돈하는 것. 처음에는 느리지만 시간이 갈수록 가속도가 붙는 변화를 지향합니다.</p>
      <p class="mt-8 mb-4"><a class="{MORE}" href="brand.html">브랜드 스토리 {ARROW}</a></p>
    </div>
  </div>
</section>

<div class="py-[clamp(48px,6vw,96px)] overflow-hidden whitespace-nowrap select-none" aria-hidden="true">
  <p class="font-mark text-[clamp(56px,9vw,150px)] leading-[1.1] tracking-[.02em] text-transparent [-webkit-text-stroke:1px_#3A3029] will-change-transform" data-mq="-1"><span class="inline-block">FACE CONTOUR, REBALANCED &nbsp;·&nbsp; FACE CONTOUR, REBALANCED &nbsp;·&nbsp; FACE CONTOUR, REBALANCED &nbsp;·&nbsp;</span></p>
  <p class="font-mark text-[clamp(56px,9vw,150px)] leading-[1.1] tracking-[.02em] text-ink will-change-transform" data-mq="1"><span class="inline-block">ARCÉ AESTHETIC &nbsp;·&nbsp; ARCÉ AESTHETIC &nbsp;·&nbsp; ARCÉ AESTHETIC &nbsp;·&nbsp; ARCÉ AESTHETIC &nbsp;·&nbsp;</span></p>
</div>

{method_sec()}

{eq_sec()}

<section class="{SEC}">
  <div class="{WRAP}">
    {sh('CARE PROGRAM', '고민에 맞춘<br>네 가지 관리 프로그램')}
    <div class="grid gap-4 grid-cols-1 md:grid-cols-2 2xl:grid-cols-4">
''' + '\n'.join(
    f'''      <a class="group relative isolate flex flex-col justify-end min-h-[360px] 2xl:min-h-[480px] rounded-[4px] overflow-hidden text-white p-7 before:content-[''] before:absolute before:inset-0 before:-z-[1] before:bg-[linear-gradient(180deg,rgba(52,41,32,0)_30%,rgba(52,41,32,.85)_100%)]" href="{href}"><img class="absolute inset-0 w-full h-full object-cover -z-[2] transition-transform duration-[600ms] {EASE} group-hover:scale-[1.04]" src="assets/{img}" alt="" loading="lazy" style="object-position:{pos}"><span class="{EN} text-champagne">{en}</span><span class="mt-2 {SERIF} text-[clamp(20px,1vw+14px,26px)] !leading-[1.3]">{t}</span><span class="mt-2 text-[14px] text-white/85 leading-[1.6]">{d}</span><span class="mt-4 inline-flex items-center gap-1.5 text-[14px] font-medium tracking-[.04em]">자세히 보기 {ARROW}</span></a>'''
    for href, img, pos, en, t, d in PCARDS) + f'''
    </div>
  </div>
</section>

<section id="reviews" class="py-[clamp(96px,10vw,140px)] bg-beige" aria-labelledby="rvT">
  {rv_head()}
  <div class="flex gap-8 overflow-x-auto snap-x snap-mandatory [scrollbar-width:none] [&::-webkit-scrollbar]:hidden px-gutter pb-2 scroll-px-gutter cursor-grab overscroll-x-contain" id="rvTrack" tabindex="0" aria-label="방문자 리뷰">
      {''.join(review_card(r) for r in REVIEWS)}
  </div>
  <div class="{WRAP} flex flex-wrap gap-x-8 gap-y-2"><a class="{MORE} mt-8" href="review.html">후기 모두 보기 {ARROW}</a><a class="{MORE} mt-8" href="{NAVER}" target="_blank" rel="noopener">네이버에서 리뷰 전체 보기 {ARROW}</a></div>
</section>

{clinic_sec()}

{ctaband('관리 전, 지금 얼굴의 균형부터 확인해 보세요.', '1:1 상담은 대표원장이 직접 진행합니다. 상담 후 결정하셔도 괜찮습니다.')}
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

brand = phero('corridor.webp', 'ABOUT ARCÉ', '얼굴을 더하지 않습니다', '흩어진 균형을 제자리로 돌려놓는 것. 아르쎄가 26년간 지켜온 관리의 기준입니다.', [('ARCÉ', None)], '50% 40%') + f'''
<section id="about" class="py-[clamp(128px,16vw,240px)]" aria-label="아르쎄의 철학">
  <div class="{WRAP}">
    <p class="{SERIF} text-[clamp(28px,4.2vw,60px)] max-w-[13em] [&_.w]:text-mute [&_.w]:transition-colors [&_.w]:duration-[250ms] [&_.w]:{EASE} [&_.w.on]:text-text motion-reduce:[&_.w]:text-text" id="sayT">얼굴을 더하지 않습니다. 흩어진 균형을 제자리로 돌려놓습니다.</p>
    <p class="mt-10 text-[clamp(16px,1.2vw+10px,22px)] text-sub">처음에는 느리지만, 시간이 갈수록 가속도가 붙는 변화.</p>
  </div>
</section>
<section class="{SEC} bg-mist">
  <div class="{WRAP}">
    {sh('OUR STANDARD', '아르쎄가 지키는 세 가지 기준')}
    <ul class="grid border-t border-text lg:grid-cols-3 lg:gap-x-10 lg:border-t-0">
''' + ''.join(
    f'''      <li class="grid grid-cols-[56px_minmax(0,1fr)] gap-4 py-8 border-b border-line lg:grid-cols-1 lg:border-t lg:border-t-text lg:border-b-0"><span class="font-display text-[14px] text-bronze pt-1">0{i + 1}</span><div><b class="block text-[clamp(18px,1vw+12px,22px)] tracking-[-.02em]">{t}</b><p class="mt-2 text-sub text-[15px] leading-[1.7]">{d}</p></div></li>
''' for i, (t, d) in enumerate(VALS)) + f'''    </ul>
  </div>
</section>
<section id="director" class="py-[clamp(120px,14vw,200px)]" aria-labelledby="dirT">
  <div class="{WRAP} grid grid-cols-[minmax(0,1fr)_minmax(0,44%)] [grid-template-areas:'top_photo'_'rest_rest'] gap-x-5 gap-y-8 items-start sm:grid-cols-[minmax(0,1fr)_minmax(0,42%)] sm:[grid-template-areas:'top_photo'_'rest_photo'] sm:grid-rows-[auto_1fr] sm:gap-x-[clamp(32px,6vw,96px)] 2xl:grid-cols-[minmax(0,560px)_minmax(0,460px)] 2xl:justify-center 2xl:gap-x-20">
    <div class="[grid-area:top] min-w-0">
      <p class="flex items-end mb-5 sm:mb-8 font-display text-[88px] sm:text-[clamp(112px,13vw,200px)] font-extralight tracking-[-.07em] leading-[.8] text-bronze tabular-nums" aria-label="26년" data-count>26<small class="font-mark text-[clamp(13px,1vw,18px)] tracking-[.3em] text-text font-normal mb-[.5em] ml-4 leading-[1.6]">YEARS</small></p>
      <h2 class="{SERIF} text-[30px] sm:text-[clamp(30px,3vw,44px)] !leading-[1.2]" id="dirT">조외현<span class="block mt-2 sm:inline sm:mt-0 sm:ml-3 text-[.42em] font-medium text-sub tracking-normal">대표원장</span></h2>
      <p class="mt-6 text-[16px] sm:text-[clamp(18px,1vw+12px,24px)] leading-[1.6] max-w-[20em]">“시술 없이 자연스럽게,<br>건강하고 아름답게 나이 드는 관리.”</p>
    </div>
    <figure class="group [grid-area:photo] sm:self-center relative aspect-[4/5] max-w-[520px] w-full overflow-hidden rounded-[4px] bg-cream" id="dirPhoto" data-ph><img class="w-full h-full object-cover object-[50%_0] scale-[1.04] transition-transform duration-[1200ms] {EASE} group-[.in]:scale-100" src="assets/director-tall.webp" width="484" height="870" alt="조외현 대표원장" loading="lazy"><figcaption class="hidden sm:block absolute left-5 bottom-4 font-mark text-[13px] tracking-[.24em] text-text">JO OE HYUN</figcaption></figure>
    <div class="[grid-area:rest] min-w-0">
      <ul class="mt-8 grid gap-3 text-[16px] text-sub">
        <li><b class="text-text font-medium">누적 관리 고객 5만 명 이상</b></li>
        <li>국제 시데스코(CIDESCO) 자격</li>
        <li>대구한의대학교 대학원 한방피부미용학 석사</li>
        <li>마산대학교 뷰티케어학과 겸임교수</li>
        <li>2022–2025 경남기능경기대회 채점감독</li>
      </ul>
      <button class="{btn_cls('line', 'dir', 'mt-10')}" id="cvOpen" type="button">전체 이력 보기 <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M10 4 V16 M4 10 H16"/></svg></button>
    </div>
  </div>
</section>
<dialog class="border-0 p-0 w-[min(680px,calc(100%-32px))] max-h-[calc(100%-64px)] rounded-3xl bg-ivory text-text backdrop:bg-[rgba(52,41,32,.5)] open:animate-pop open:backdrop:animate-fade" id="cv" aria-labelledby="cvT">
  <div class="pt-10 px-8 pb-8 grid gap-8">
    <div class="flex justify-between items-start gap-4"><h3 id="cvT" class="text-[28px] font-bold tracking-[-.03em]">조외현 대표원장</h3><button class="w-12 h-12 rounded-full grid place-items-center bg-mist flex-none" id="cvClose" type="button" aria-label="닫기"><svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 3 L15 15 M15 3 L3 15"/></svg></button></div>
    <div><h4 class="{H4}">학력 · 직위</h4>{cv_list(CV_EDU)}</div>
    <div><h4 class="{H4}">경력</h4>{cv_list(CV_CAREER)}</div>
    <div><h4 class="{H4}">자격 · 연수</h4>{cv_list(CV_CERT)}</div>
  </div>
</dialog>
<section id="space" class="py-[clamp(96px,10vw,140px)]" aria-labelledby="spaceT">
  <div class="{WRAP} flex flex-wrap justify-between items-end gap-x-10 gap-y-4 mb-10">
    <h2 id="spaceT" class="{SERIF} text-[clamp(28px,3vw,44px)]">아르쎄의 공간</h2>
    <p class="{SUB_TEXT}">밝고 깨끗한 공간에서, 관리에만 집중하세요.</p>
  </div>
  <div class="flex gap-4 overflow-x-auto snap-x snap-mandatory [scrollbar-width:none] [&::-webkit-scrollbar]:hidden px-gutter scroll-px-gutter cursor-grab overscroll-x-contain" id="gal" tabindex="0" aria-label="매장 사진">
''' + ''.join(
    f'''    <figure class="group relative flex-none snap-start overflow-hidden rounded-[4px] bg-mist h-[clamp(420px,68vh,720px)] {"aspect-[4/3] max-sm:w-[90vw]" if wide else "aspect-[3/4] max-sm:w-[78vw]"} max-sm:h-auto"><img class="w-full h-full object-cover pointer-events-none transition-transform duration-[600ms] {EASE} group-hover:scale-[1.03]" src="assets/{src}" width="{w}" height="{h}" alt="{alt}" loading="lazy"><figcaption class="absolute left-4 bottom-3.5 text-white text-[14px] font-semibold [text-shadow:0_1px_8px_rgba(0,0,0,.35)]">{cap}</figcaption></figure>
''' for src, w, h, alt, cap, wide in GAL) + f'''  </div>
</section>
<section id="care" class="py-[clamp(96px,10vw,140px)]" aria-labelledby="careT">
  <div class="{WRAP} flex flex-wrap justify-between items-end gap-x-10 gap-y-3 mb-10">
    <h2 id="careT" class="{SERIF} text-[clamp(26px,2.6vw,38px)]">관리 현장</h2>
    <p class="{SUB_TEXT}">원장이 직접, 처음부터 끝까지 관리합니다.</p>
  </div>
  <div class="flex gap-4 overflow-x-auto snap-x snap-mandatory [scrollbar-width:none] [&::-webkit-scrollbar]:hidden px-gutter scroll-px-gutter lg:max-w-site lg:mx-auto lg:justify-center lg:overflow-visible" id="careRow">
''' + ''.join(
    f'''    <figure class="flex-[0_0_min(64vw,300px)] snap-start aspect-[9/16] rounded-[4px] overflow-hidden bg-beige lg:flex-[1_1_0] lg:max-w-[340px]"><video class="block w-full h-full object-cover" poster="assets/{n}.jpg" muted loop playsinline preload="none" aria-label="{a}"><source src="assets/{n}.mp4" type="video/mp4"><source src="assets/{n}.webm" type="video/webm"></video></figure>
''' for n, a in CARE) + f'''  </div>
</section>
{ctaband('대표원장이 직접, 처음부터 끝까지.', '상담부터 관리, 사후 홈케어 가이드까지 한 분이 책임집니다.')}
'''
page('brand.html', '브랜드 소개 | 아르쎄에스테틱', '얼굴을 더하지 않고 흩어진 균형을 바로잡는 김해 장유 윤곽 전문 에스테틱, 아르쎄. 대표원장 조외현 소개와 공간.', 'brand', brand)

method = phero('interior-hero.webp', 'SIGNATURE METHOD', '조막얼굴메소드<sup>®</sup>', '해부학을 기반으로 대표원장이 직접 개발하고 상표로 등록한 아르쎄만의 윤곽관리 프로토콜입니다.', [('조막얼굴메소드®', None)], '50% 50%') + f'''
<section class="{SEC}">
  <div class="{WRAP} {SPLIT}">
    <div>
      {sh('WHY JOMAK METHOD', '얼굴 라인은<br>근육과 근막이 만듭니다')}
      <p class="{LEAD}">같은 골격이라도 씹는 습관, 자세, 순환 상태에 따라 얼굴의 윤곽은 달라집니다. 조막얼굴메소드®는 윤곽을 흐트러뜨리는 원인을 해부학적으로 찾아 근육과 근막의 균형을 바로잡는 데 집중합니다.</p>
      <ul class="{CHK} mt-8">
        <li>대표원장의 1:1 얼굴 진단으로 시작합니다</li>
        <li>저작근·광대 주변·목까지 이어지는 흐름을 함께 관리합니다</li>
        <li>필요한 경우 정품 장비를 더해 관리의 깊이를 설계합니다</li>
      </ul>
    </div>
    <figure class="{SPLIT_IMG}" data-ph data-par><img class="w-full h-full object-cover" src="assets/consult.webp" alt="대표원장이 상담실에서 고객과 마주 앉아 상담하는 모습" loading="lazy" style="object-position:60% 50%"></figure>
  </div>
</section>
{method_sec()}
<section class="{SEC}" id="result">
  <div class="{WRAP}">
    {sh('BEFORE &amp; AFTER', '관리 전후 비교', '가운데 손잡이를 좌우로 움직여 관리 전후의 얼굴 라인을 비교해 보세요.')}
    {ba_solo()}
  </div>
</section>
{ctaband('내 얼굴의 균형, 진단부터 받아보세요.', '조막얼굴메소드® 상담은 대표원장이 직접 진행합니다.', '조막얼굴 윤곽관리')}
'''
page('method.html', '조막얼굴메소드® | 아르쎄에스테틱', '해부학 기반으로 대표원장이 직접 개발하고 상표 등록한 아르쎄의 윤곽관리 프로토콜, 조막얼굴메소드®.', 'method', method, 'assets/interior-hero.webp')


def program(fn, img, pos, en, title, desc, intro, recs, steps, devices, note, care):
    rec = ''.join(f'<li>{r}</li>' for r in recs)
    st = ''.join(
        f'<li class="grid grid-cols-[64px_minmax(0,1fr)] gap-4 py-6 border-b border-line lg:grid-cols-1 lg:border-t lg:border-t-text lg:border-b-0 lg:pt-5"><span class="font-display text-[15px] text-bronze">0{i + 1}</span><div><b class="text-[clamp(17px,.6vw+14px,20px)]">{t}</b><p class="mt-1.5 text-sub text-[15px] leading-[1.7]">{d}</p></div></li>'
        for i, (t, d) in enumerate(steps))
    dev = ''.join(
        f'<a class="inline-flex items-center gap-2 min-h-12 px-5 rounded-[2px] border border-line bg-ivory text-[15px] font-medium tracking-[.02em] hover:border-ink" href="equipment.html#{h}">{n} {ARROW}</a>'
        for n, h in devices)
    devsec = f'''<section class="{SEC}">
  <div class="{WRAP}">
    {sh('DEVICE', '함께 사용하는 장비', '상태에 따라 손기술에 아래 장비를 더해 관리합니다.')}
    <div class="flex flex-wrap gap-2">{dev}</div>
  </div>
</section>''' if devices else ''
    notep = f'<p class="mt-6 text-[13px] text-sub leading-[1.7]">{note}</p>' if note else ''
    body = phero(img, en, title, desc, [('관리 프로그램', 'program-face.html'), (title, None)], pos) + f'''
<section class="{SEC}">
  <div class="{WRAP} {SPLIT}">
    <div>
      {sh('PROGRAM', '프로그램 소개')}
      {''.join(f'<p class="{LEAD}">{x}</p>' for x in intro)}
    </div>
    <div>
      <p class="{EN} text-bronze mb-5">RECOMMENDED FOR</p>
      <ul class="{CHK}">{rec}</ul>
      {notep}
    </div>
  </div>
</section>
<section class="{SEC} bg-beige">
  <div class="{WRAP}">
    {sh('PROCESS', '관리 과정')}
    <ol class="grid border-t border-text lg:grid-cols-4 lg:gap-x-8 lg:border-t-0">{st}</ol>
  </div>
</section>
{devsec}
{ctaband(f'{title}, 상담으로 시작하세요.', '현재 상태를 진단한 뒤 필요한 관리와 회차를 안내해 드립니다.', care)}
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

eq = phero('interior-hero.webp', 'PREMIUM DEVICE', '손기술 위에, 정품 장비', '엄선한 프리미엄 장비로 관리의 깊이를 더합니다.', [('장비', None)], '50% 40%') + '\n' + eq_sec(head=False) + '\n' + ctaband('어떤 장비가 맞을지, 상담으로 정해 드립니다.', '피부와 체형 상태에 따라 손기술과 장비를 함께 설계합니다.')
page('equipment.html', '장비 소개 | 아르쎄에스테틱', '프랑스 LPG® 알리안스, 써마웨이브™, 스페인 Termosalud 자이오닉. 아르쎄에스테틱의 프리미엄 장비.', 'equipment', eq, 'assets/eq-lpg.webp')

review = phero('lounge-masks.webp', 'REVIEW', '고객후기', '네이버 플레이스에 고객님들이 직접 남겨주신 방문자 리뷰입니다.', [('고객후기', None)], '50% 60%') + f'''
<section id="reviews" class="py-[clamp(96px,10vw,140px)] bg-ivory" aria-labelledby="rvT">
  {rv_head()}
  <div class="grid gap-x-10 gap-y-12 px-gutter max-w-site mx-auto md:grid-cols-2 2xl:grid-cols-3">
{chr(10).join(review_card(r, grid=True) for r in REVIEWS)}
  </div>
  <div class="{WRAP}"><a class="{MORE} mt-8" href="{NAVER}" target="_blank" rel="noopener">네이버에서 리뷰 전체 보기 {ARROW}</a></div>
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
      <div class="flex flex-wrap gap-2 mt-10">
        {kakao_btn()}
        <a class="{btn_cls('line')} js-tel" href="#"><span class="js-tel-text"></span></a>
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
{clinic_sec()}
'''
page('contact.html', '상담·오시는 길 | 아르쎄에스테틱', '경남 김해시 율하숲길 21 303호. 월–토 10:00–21:00, 일요일 정기휴무. 아르쎄에스테틱 상담 문의.', 'contact', contact, 'assets/entrance.webp')
