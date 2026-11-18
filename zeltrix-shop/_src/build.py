#!/usr/bin/env python3
"""Genera las páginas HTML estáticas de zeltrix.shop.
Uso (desde la carpeta zeltrix-shop):  python _src/build.py
Edita el contenido aquí y vuelve a generar; los HTML resultantes son el entregable."""
import json, os, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://zeltrix.shop"
MAIL = "losvasquitos33@gmail.com"  # correo público que ya figura en la política de reembolso actual
DATE = "2026-11-18"

I = {  # iconos inline (stroke)
 "truck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7h11v9H3zM14 10h4l3 3v3h-7"/><circle cx="7.5" cy="17.5" r="1.6"/><circle cx="17.5" cy="17.5" r="1.6"/></svg>',
 "return": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 14 4 9l5-5"/><path d="M4 9h10a6 6 0 0 1 0 12h-3"/></svg>',
 "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="10" width="16" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>',
 "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/></svg>',
 "bag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 8h14l-1 12H6L5 8Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M4 8h16M4 16h16"/></svg>',
 "x": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
 "chev-l": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 5-7 7 7 7"/></svg>',
 "chev-r": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 5 7 7-7 7"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5 9-10"/></svg>',
 "hands": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 11V5a1.5 1.5 0 0 1 3 0v5m0 0V4a1.5 1.5 0 0 1 3 0v6m0 0V6a1.5 1.5 0 0 1 3 0v8a6 6 0 0 1-6 6h-1a6 6 0 0 1-5-3l-2-4a1.5 1.5 0 0 1 2.5-1.5L8 14"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 3 5 14h6l-1 7 8-11h-6z"/></svg>',
 "usb": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="7" y="3" width="10" height="7" rx="1"/><path d="M12 10v11M9 21h6"/></svg>',
}

def eur(v):
    return f"{v:.2f}".replace(".", ",") + " €"

PROD = {
 "gafas": dict(
   id="gafas", slug="gafas-luz-roja-anti-ojeras", name="Gafas de Luz Roja para el Contorno de Ojos", short="Gafas de Luz Roja",
   price=25.0, compare=35.5, sku="ZLX-GLR-01",
   imgs=[("gafas-1", "Gafas de luz roja Zeltrix con los paneles LED encendidos"),
         ("gafas-2", "Persona con las gafas de luz roja puestas"),
         ("gafas-3", "Detalles del diseño: carga USB-C, luz LED roja y sesión de 10 minutos"),
         ("gafas-4", "Vista del diseño ergonómico y los paneles de luz")],
   desc="Gafas de luz roja LED (630 nm) con microcorrientes y vibración sónica suave. Manos libres, sesiones de 10 minutos y carga USB. Envío en 24/48 h y 30 días para devoluciones.",
   title="Gafas de Luz Roja para el Contorno de Ojos | Zeltrix",
   card="Manos libres, 10 minutos al día. Luz LED roja, microcorrientes y vibración sónica suave para tu rutina de autocuidado.",
   tag="Black Friday"),
 "cargador": dict(
   id="cargador", slug="mini-banco-de-energia-ultra-compacto-5000mah-negro-con-cable-integrado", name="Mini Cargador Portátil 5000 mAh", short="Mini Cargador 5000 mAh",
   price=15.0, compare=0, sku="ZLX-MC-5K",
   imgs=[("cargador-1", "Mini cargador portátil negro de 5000 mAh con cable integrado")],
   desc="Mini cargador portátil ultra compacto de 5000 mAh con cable integrado, en negro. Energía de reserva para tu móvil. Envío en 24/48 h y 30 días para devoluciones.",
   title="Mini Cargador Portátil 5000 mAh con Cable Integrado | Zeltrix",
   card="Ultra compacto, 5000 mAh y cable integrado. Energía de reserva que cabe en el bolsillo.",
   tag="Esencial"),
}

def url(p): return f"/products/{p['slug']}"

# ---------- plantillas comunes ----------
def head(title, desc, path, img="/assets/img/og.jpg", extra="", noindex=False, preload=""):
    canon = SITE + path
    return f"""<!doctype html>
<html lang="es-ES">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{H.escape(title)}</title>
<meta name="description" content="{H.escape(desc)}">
<link rel="canonical" href="{canon}">
{'<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'}
<meta name="theme-color" content="#0b0b0d">
<meta property="og:type" content="{'product' if '/products/' in path else 'website'}">
<meta property="og:site_name" content="Zeltrix">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="{H.escape(title)}">
<meta property="og:description" content="{H.escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}{img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" href="/assets/img/favicon-64.png" sizes="64x64">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Sora:wght@500;600;700&display=swap">
{preload}<link rel="stylesheet" href="/assets/styles.css">
{extra}</head>
"""

def header(cur=""):
    def a(href, label, key):
        return f'<a href="{href}"{" aria-current=\"page\"" if cur == key else ""}>{label}</a>'
    return f"""<body>
<a class="skip" href="#main">Saltar al contenido</a>
<div class="ann">Black Friday · Gafas de luz roja a <strong>25,00 €</strong> · Envío en 24/48 h</div>
<header class="hdr"><div class="wrap">
  <a class="logo" href="/" aria-label="Zeltrix, inicio"><img src="/assets/img/logo-white.png" alt="ZELTRIX" width="420" height="35"></a>
  <nav class="nav" id="nav" aria-label="Principal">
    {a("/#productos", "Productos", "p")}{a(url(PROD["gafas"]), "Gafas de luz roja", "g")}{a(url(PROD["cargador"]), "Mini cargador", "c")}{a("/pages/contact", "Contacto", "k")}
  </nav>
  <div class="hdr-r">
    <button class="icon-btn" data-open-cart aria-label="Abrir carrito">{I["bag"]}<span class="badge" data-cart-count hidden>0</span></button>
    <button class="icon-btn menu-btn" id="menu-btn" aria-label="Menú" aria-expanded="false" aria-controls="nav">{I["menu"]}</button>
  </div>
</div></header>
<main id="main">
"""

def footer():
    return f"""</main>
<footer class="ftr"><div class="wrap">
  <div class="cols">
    <div><img src="/assets/img/logo-white.png" alt="ZELTRIX" width="420" height="35" loading="lazy">
      <p style="max-width:34ch">Pequeños dispositivos de cuidado personal y tecnología diaria. Envío en 24/48 h y 30 días para devoluciones.</p></div>
    <div><h4>Tienda</h4><ul>
      <li><a href="{url(PROD['gafas'])}">Gafas de luz roja</a></li>
      <li><a href="{url(PROD['cargador'])}">Mini cargador 5000 mAh</a></li>
      <li><a href="/cart">Carrito</a></li></ul></div>
    <div><h4>Ayuda</h4><ul>
      <li><a href="/pages/contact">Contacto</a></li>
      <li><a href="/policies/refund-policy">Envíos y devoluciones</a></li>
      <li><a href="/policies/privacy-policy">Política de privacidad</a></li>
      <li><a href="/policies/terms-of-service">Términos del servicio</a></li></ul></div>
  </div>
  <div class="bot"><span>© 2026 zeltrix.shop</span><span>Los dispositivos de cuidado personal no son productos sanitarios.</span></div>
</div></footer>

<div class="scrim" id="scrim"></div>
<aside class="drawer" id="drawer" role="dialog" aria-modal="true" aria-labelledby="dr-title" aria-hidden="true">
  <div class="dr-h"><h2 id="dr-title">Tu carrito</h2><button class="icon-btn" id="drawer-close" aria-label="Cerrar carrito" style="color:var(--text)">{I["x"]}</button></div>
  <div class="dr-b"><ul id="drawer-lines"></ul></div>
  <div class="dr-f" id="drawer-foot" hidden>
    <div class="sum t"><span>Subtotal</span><span id="drawer-total">0,00 €</span></div>
    <p class="note">Impuestos incluidos. Envío y descuentos en el siguiente paso.</p>
    <a class="btn btn-glow btn-block" href="/cart">Finalizar compra</a>
  </div>
</aside>
<script src="/assets/main.js" defer></script>
</body>
</html>
"""

def faq_ld(qas):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]}

def ld(*objs):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": list(objs)}, ensure_ascii=False) + "</script>\n"

ORG = {"@type": "Organization", "@id": SITE + "/#org", "name": "Zeltrix", "url": SITE, "logo": SITE + "/assets/img/icon-512.png"}
SITE_LD = {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE, "name": "Zeltrix", "inLanguage": "es-ES", "publisher": {"@id": SITE + "/#org"}}

import re as _re
def _rel(content, depth):
    R = "../" * depth
    def fix_url(u):
        if not u.startswith("/") or u.startswith("//"): return u
        if "#" in u:
            path, hashp = u.split("#", 1); h = "#" + hashp
        else:
            path, h = u, ""
        if path == "/": return R + "index.html" + h
        last = path.rsplit("/", 1)[-1]
        if "." not in last: path += ".html"
        return R + path.lstrip("/") + h
    content = _re.sub(r'(href|src|data-full)="(/[^"]*)"', lambda m: m.group(1) + '="' + fix_url(m.group(2)) + '"', content)
    content = _re.sub(r'srcset="([^"]*)"', lambda m: 'srcset="' + _re.sub(r'(^|, )(/[^ ,]+)', lambda k: k.group(1) + fix_url(k.group(2)), m.group(1)) + '"', content)
    content = content.replace('<html lang="es-ES">', '<html lang="es-ES" data-root="' + R + '">')
    return content

def write(path, content):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    if path.endswith(".html"):
        content = _rel(content, path.lstrip("/").count("/"))
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("OK", path)

def card(p, first=False):
    im = p["imgs"][0][0]
    pr = f'{eur(p["price"])}' + (f'<s>{eur(p["compare"])}</s>' if p["compare"] else "")
    return f"""<article class="card rv">
  <a class="card-img" href="{url(p)}" aria-label="{H.escape(p['name'])}"><span class="tag{' glow' if p['compare'] else ''}">{p['tag']}</span>
    <img src="/assets/img/{im}-sm.webp" srcset="/assets/img/{im}-sm.webp 480w, /assets/img/{im}.webp 1000w" sizes="(max-width:640px) 92vw, 560px" alt="{H.escape(p['imgs'][0][1])}" width="480" height="480" loading="lazy"></a>
  <div class="card-body"><h3><a href="{url(p)}">{p['name']}</a></h3><p>{p['card']}</p>
    <div class="card-foot"><span class="price">{pr}</span>
      <button class="btn btn-ink" style="min-height:46px;padding:0 22px" data-add="{p['id']}" data-quick>Añadir</button></div></div>
</article>"""

def acc(title, body, open_=False):
    return f'<details{" open" if open_ else ""}><summary>{title}</summary><div class="ans">{body}</div></details>'

# =============== HOME ===============
g = PROD["gafas"]; c = PROD["cargador"]
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "home_block.py"), encoding="utf-8").read())

# =============== PRODUCTOS ===============
def pdp(p, cur, bullets, specs, includes, how, extra_acc, faqs, related, notice):
    n = len(p["imgs"])
    thumbs = ""
    if n > 1:
        thumbs = '<div class="thumbs" role="group" aria-label="Miniaturas">' + "".join(
            f'<button type="button" data-thumb data-full="/assets/img/{k}.webp" data-alt="{H.escape(a)}" aria-current="{"true" if i == 0 else "false"}" aria-label="Ver imagen {i+1}"><img src="/assets/img/{k}-sm.webp" alt="" width="96" height="96" loading="lazy"></button>'
            for i, (k, a) in enumerate(p["imgs"])) + "</div>"
    navb = f'<button class="gal-nav prev" data-prev aria-label="Imagen anterior">{I["chev-l"]}</button><button class="gal-nav next" data-next aria-label="Imagen siguiente">{I["chev-r"]}</button>' if n > 1 else ""
    k0, a0 = p["imgs"][0]
    save = f'<span class="save">Ahorras {eur(p["compare"]-p["price"])}</span>' if p["compare"] else ""
    cmp_ = f'<s>{eur(p["compare"])}</s>' if p["compare"] else ""
    product_ld = {"@type": "Product", "@id": SITE + url(p) + "#product", "name": p["name"], "description": p["desc"], "sku": p["sku"],
        "image": [f"{SITE}/assets/img/{k}.webp" for k, _ in p["imgs"]], "brand": {"@type": "Brand", "name": "Zeltrix"},
        "offers": {"@type": "Offer", "url": SITE + url(p), "priceCurrency": "EUR", "price": f"{p['price']:.2f}", "availability": "https://schema.org/InStock", "itemCondition": "https://schema.org/NewCondition",
                   "hasMerchantReturnPolicy": {"@type": "MerchantReturnPolicy", "applicableCountry": "ES", "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow", "merchantReturnDays": 30, "returnMethod": "https://schema.org/ReturnByMail"}}}
    crumbs_ld = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": p["short"], "item": SITE + url(p)}]}
    page = head(p["title"], p["desc"], url(p), img=f"/assets/img/{k0}.webp", extra=ld(ORG, SITE_LD, product_ld, crumbs_ld, faq_ld(faqs)),
        preload=f'<link rel="preload" as="image" href="/assets/img/{k0}.webp" fetchpriority="high">\n') + header(cur)
    page += f"""
<div class="wrap">
<nav class="crumbs" aria-label="Migas de pan"><a href="/">Inicio</a><span>/</span>{p['short']}</nav>
<div class="pdp">
  <div class="gal" data-gallery>
    <div class="gal-main"><img data-gal-main src="/assets/img/{k0}.webp" alt="{H.escape(a0)}" width="1000" height="1000" fetchpriority="high">{navb}</div>
    {thumbs}
  </div>
  <div class="buy">
    <p class="eyebrow">{'Black Friday' if p['compare'] else 'Zeltrix'}</p>
    <h1>{p['name']}</h1>
    <p class="sub">{p['sub']}</p>
    <div class="price-l"><b>{eur(p['price'])}</b>{cmp_}{save}</div>
    <p class="vat">Impuestos incluidos. Envío en 24/48 h.</p>
    <div id="buy-anchor" class="buy-row">
      <div class="qty" data-qty role="group" aria-label="Cantidad"><button type="button" data-dec aria-label="Reducir cantidad">−</button><output aria-live="polite">1</output><button type="button" data-inc aria-label="Aumentar cantidad">+</button></div>
      <button class="btn btn-glow" data-add="{p['id']}" data-use-qty>Añadir al carrito</button>
    </div>
    <div class="trust"><div>{I['truck']}Envío en 24/48 h</div><div>{I['return']}30 días para devolver</div><div>{I['lock']}Pago seguro</div></div>
    <ul class="pts">{''.join(f'<li>{I[ic]}<span>{t}</span></li>' for ic, t in bullets)}</ul>
    <div class="acc">
      {acc('Especificaciones', '<table class="tbl">' + ''.join(f'<tr><th>{a}</th><td>{b}</td></tr>' for a, b in specs) + '</table>', True)}
      {acc('Qué incluye la caja', '<ul>' + ''.join(f'<li>{x}</li>' for x in includes) + '</ul>')}
      {how}{extra_acc}
      {acc('Envío y devoluciones', '<p>Enviamos en 24/48 horas. Dispones de 30 días desde que recibes el producto para solicitar la devolución. Consulta las condiciones en nuestra <a href="/policies/refund-policy" style="text-decoration:underline">política de devoluciones</a>.</p>')}
      {acc('Preguntas frecuentes', ''.join(f'<p style="margin-bottom:14px"><b style="color:var(--text)">{q}</b><br>{a}</p>' for q, a in faqs))}
    </div>
    {notice}
  </div>
</div>
</div>

<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="sec-head rv"><p class="eyebrow">También en Zeltrix</p><h2 class="h2">Completa tu pedido</h2></div>
  <div class="grid" style="max-width:580px">{card(related)}</div>
</div></section>

<div class="sticky-buy" id="sticky-buy"><div class="nm">{p['short']}<small>{eur(p['price'])}</small></div><button class="btn btn-glow" data-add="{p['id']}">Añadir al carrito</button></div>
""" + footer()
    write(f"products/{p['slug']}.html", page)

g["sub"] = "Diseño ergonómico y manos libres para incorporarlas a tu rutina de autocuidado en casa. Un momento de calma en solo 10 minutos al día."
c["sub"] = "Ultra compacto, 5000 mAh y cable integrado. Energía de reserva siempre a mano."

g_faqs = [
 ("¿Cuánto dura cada sesión?", "Unos 10 minutos. El dispositivo se apaga solo cuando termina el temporizador."),
 ("¿Cómo se carga?", "Por USB con el cable incluido. Por seguridad, no se puede encender mientras está conectado a la carga."),
 ("¿Es un producto sanitario?", "No, es un producto de cuidado personal. Si estás embarazada, llevas marcapasos u otro dispositivo implantado o tienes alguna condición médica, consulta con tu médico antes de usarlo."),
 ("¿Y si no me convence?", "Dispones de 30 días desde que lo recibes para solicitar la devolución, según nuestra política de devoluciones."),
]
pdp(g, "g",
 [("bolt", "Luz LED roja (630 nm) + microcorrientes (EMS) + vibración sónica suave."),
  ("hands", "Manos libres: póntelas mientras lees, teletrabajas o descansas en el sillón."),
  ("clock", "Temporizador de 10 minutos con apagado automático."),
  ("usb", "Batería de litio integrada: una carga completa permite varias sesiones.")],
 [("Tecnología", "Luz LED roja (630 nm) + microcorrientes (EMS) + vibración sónica suave"), ("Batería", "Polímero de litio integrada, 90 mAh, 3,7 V"),
  ("Material", "ABS de alta durabilidad y almohadillas conductoras suaves con la piel"), ("Peso", "Unos 45 g"), ("Sesión", "10 minutos con apagado automático"), ("Carga", "USB (cable incluido)")],
 ["1 × Gafas de luz roja", "1 × Cable de carga USB (compatible con cualquier puerto USB o adaptador de corriente estándar)", "1 × Manual de instrucciones"],
 acc("Cómo usarlas", "<ul><li>Carga las gafas con el cable USB incluido.</li><li>Colócalas sobre el contorno de ojos y enciéndelas.</li><li>Relájate durante unos 10 minutos: se apagan solas al terminar.</li></ul><p style='margin-top:10px'>Por seguridad, no se pueden encender mientras están conectadas al cable de carga.</p>"),
 "", g_faqs, c,
 '<p class="notice"><b>Importante.</b> Es un producto de cuidado personal, no un producto sanitario. Si estás embarazada, llevas marcapasos u otro dispositivo implantado, o tienes alguna condición médica, consulta con tu médico antes de usarlo.</p>')

c_faqs = [
 ("¿Necesito llevar un cable aparte?", "No, el cable viene integrado en el propio cargador."),
 ("¿Cuánto tarda el envío?", "Enviamos en 24/48 horas."),
 ("¿Y si no me convence?", "Dispones de 30 días desde que lo recibes para solicitar la devolución, según nuestra política de devoluciones."),
]
pdp(c, "c",
 [("bolt", "Ultra compacto: cabe en el bolsillo o en el bolso."), ("usb", "Cable integrado: no dependes de llevar otro cable."),
  ("clock", "5000 mAh de energía de reserva para tu día a día.")],
 [("Capacidad", "5000 mAh"), ("Color", "Negro"), ("Cable", "Integrado"), ("Puerto", "USB-C · PD 20 W")],
 ["1 × Mini cargador portátil con cable integrado"], "", "", c_faqs, g, "")

# =============== CARRITO / CHECKOUT (DEMO) ===============
cart = head("Carrito y finalizar compra | Zeltrix", "Revisa tu carrito y finaliza tu pedido en Zeltrix.", "/cart", noindex=True, extra=ld(ORG)) + header("") + f"""
<div class="wrap">
<div id="co-view">
  <div class="page-h"><h1>Tu carrito</h1></div>
  <div class="co">
    <div>
      <div class="panel"><ul id="cart-lines"></ul></div>
      <form id="co-form" hidden style="margin-top:18px">
        <div class="panel"><h2>Contacto</h2><div class="f">
          <div class="fld"><label for="email">Correo electrónico</label><input id="email" name="email" type="email" required autocomplete="email" placeholder="tu@correo.com"></div></div></div>
        <div class="panel"><h2>Entrega</h2><div class="f">
          <div class="f2"><div class="fld"><label for="fn">Nombre</label><input id="fn" name="fn" required autocomplete="given-name" placeholder=" "></div>
            <div class="fld"><label for="ln">Apellidos</label><input id="ln" name="ln" required autocomplete="family-name" placeholder=" "></div></div>
          <div class="fld"><label for="ad">Dirección</label><input id="ad" name="ad" required autocomplete="street-address" placeholder=" "></div>
          <div class="f2"><div class="fld"><label for="zp">Código postal</label><input id="zp" name="zp" required inputmode="numeric" pattern="[0-9]{{5}}" autocomplete="postal-code" placeholder=" "></div>
            <div class="fld"><label for="ct">Ciudad</label><input id="ct" name="ct" required autocomplete="address-level2" placeholder=" "></div></div>
          <div class="f2"><div class="fld"><label for="cn">País</label><select id="cn" name="cn" autocomplete="country"><option>España</option><option>Portugal</option><option>Francia</option><option>Italia</option><option>Alemania</option></select></div>
            <div class="fld"><label for="ph">Teléfono (opcional)</label><input id="ph" name="ph" type="tel" autocomplete="tel" placeholder=" "></div></div>
        </div></div>
        <div class="panel"><h2>Pago</h2>
          <div class="demo-note"><span>ⓘ</span><span><b>Modo demostración.</b> Esta tienda es una demo: no se procesa ningún pago ni se envía ningún pedido real.</span></div>
          <div class="pm"><label><input type="radio" name="pm" value="card" checked> Tarjeta de crédito o débito</label><label><input type="radio" name="pm" value="paypal"> PayPal</label></div>
        </div>
        <button class="btn btn-glow btn-block" style="margin-top:18px" type="submit">Completar pedido (demo)</button>
      </form>
    </div>
    <aside class="aside panel"><h2>Resumen</h2>
      <div class="sum" style="margin-bottom:10px"><span>Subtotal</span><span data-sum-sub>0,00 €</span></div>
      <div class="sum" style="margin-bottom:10px"><span>Envío</span><span>24/48 h</span></div>
      <hr style="border:0;border-top:1px solid var(--line);margin:16px 0">
      <div class="sum t"><span>Total</span><span data-sum-total>0,00 €</span></div>
      <p class="note" style="margin-top:12px">Impuestos incluidos. 30 días para devoluciones.</p>
    </aside>
  </div>
</div>
<div class="done" id="done-view" hidden>
  <div class="ok">{I['check']}</div>
  <h1>¡Pedido de demostración completado!</h1>
  <p>Número de pedido <b id="done-order"></b> · Total <b id="done-total"></b>.</p>
  <p>En una tienda real enviaríamos la confirmación a <b id="done-email"></b>. Aquí no se ha cobrado ni enviado nada.</p>
  <p style="margin-top:26px"><a class="btn btn-ink" href="/">Volver a la tienda</a></p>
</div>
</div>
""" + footer()
write("cart.html", cart)

# =============== CONTACTO ===============
contact = head("Contacto | Zeltrix", "Escríbenos para cualquier duda sobre tu pedido, envíos o devoluciones en Zeltrix.", "/pages/contact", extra=ld(ORG, {"@type": "ContactPage", "url": SITE + "/pages/contact", "name": "Contacto"})) + header("k") + f"""
<div class="wrap" style="max-width:760px">
  <div class="page-h"><p class="eyebrow">Atención al cliente</p><h1 style="margin-top:12px">Contacto</h1><p class="lead" style="margin-top:14px">Cuéntanos qué necesitas y te respondemos por correo.</p></div>
  <form class="panel f" id="contact-form" data-to="{MAIL}" style="margin:28px 0 clamp(56px,8vw,110px)">
    <div class="f2"><div class="fld"><label for="name">Nombre</label><input id="name" name="name" required autocomplete="name"></div>
      <div class="fld"><label for="cemail">Correo electrónico</label><input id="cemail" name="email" type="email" required autocomplete="email"></div></div>
    <div class="fld"><label for="tel">Teléfono (opcional)</label><input id="tel" name="tel" type="tel" autocomplete="tel"></div>
    <div class="fld"><label for="msg">Mensaje</label><textarea id="msg" name="msg" required></textarea></div>
    <button class="btn btn-ink" type="submit">Enviar mensaje</button>
    <p class="note">Al enviar se abrirá tu aplicación de correo con el mensaje preparado para {MAIL}.</p>
  </form>
</div>
""" + footer()
write("pages/contact.html", contact)

# =============== LEGALES ===============
def legal(path, title, desc, body):
    pg = head(title + " | Zeltrix", desc, path, extra=ld(ORG)) + header("") + f'<div class="wrap"><div class="page-h"><h1>{title}</h1></div><div class="legal">{body}<p style="margin-top:32px;font-size:.85rem;color:var(--muted)">Última actualización: 18 de noviembre de 2026.</p></div></div>' + footer()
    write(path.lstrip("/") + ".html", pg)

legal("/policies/refund-policy", "Envíos y devoluciones", "Política de envíos y devoluciones de Zeltrix: envío en 24/48 horas y 30 días para devoluciones.", f"""
<h2>Envíos</h2><p>Preparamos y enviamos los pedidos en 24/48 horas. Te avisaremos por correo cuando tu pedido salga.</p>
<h2>Devoluciones: 30 días</h2><p>Dispones de 30 días desde que recibes el artículo para solicitar una devolución. El artículo debe estar en el mismo estado en que lo recibiste, sin usar y en su embalaje original, y necesitarás el comprobante de compra.</p>
<p>Para iniciar una devolución, escríbenos a <a href="mailto:{MAIL}">{MAIL}</a>. Si se acepta, te indicaremos cómo y dónde enviar el paquete. No se aceptarán devoluciones sin haberlas solicitado previamente.</p>
<h2>Productos dañados o equivocados</h2><p>Revisa tu pedido en cuanto lo recibas y contacta con nosotros de inmediato si el artículo está defectuoso, dañado o es incorrecto, para que podamos solucionarlo.</p>
<h2>Periodo de desistimiento de 14 días (UE)</h2><p>Si el pedido se envía dentro de la Unión Europea, tienes derecho a desistir de la compra en un plazo de 14 días naturales sin necesidad de justificación, en las condiciones indicadas arriba.</p>
<h2>Reembolsos</h2><p>Te informaremos cuando recibamos e inspeccionemos tu devolución. Si se aprueba, el reembolso se realizará con el mismo método de pago utilizado en la compra.</p>
""")
legal("/policies/privacy-policy", "Política de privacidad", "Cómo trata Zeltrix tus datos personales conforme al RGPD.", f"""
<p>Esta política explica cómo tratamos tus datos personales cuando visitas zeltrix.shop o realizas un pedido.</p>
<h2>Responsable</h2><p>zeltrix.shop · Contacto: <a href="mailto:{MAIL}">{MAIL}</a>. <mark>[Completar antes de publicar: razón social, NIF y domicilio]</mark></p>
<h2>Datos que tratamos</h2><ul><li>Datos de contacto y entrega (nombre, correo, dirección, teléfono) para gestionar tu pedido.</li><li>Datos de pago, tratados por la pasarela de pago, no almacenados por nosotros.</li><li>El contenido de tu carrito se guarda únicamente en tu navegador (almacenamiento local).</li></ul>
<h2>Finalidad y base jurídica</h2><p>Gestionar y entregar tus pedidos y atender tus consultas (ejecución de contrato e interés legítimo). Solo enviaremos comunicaciones comerciales si das tu consentimiento.</p>
<h2>Conservación y destinatarios</h2><p>Conservaremos los datos el tiempo necesario para cumplir las obligaciones legales. Podemos compartirlos con transportistas y proveedores de pago estrictamente para prestar el servicio.</p>
<h2>Tus derechos</h2><p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a <a href="mailto:{MAIL}">{MAIL}</a>. También puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>
""")
legal("/policies/terms-of-service", "Términos del servicio", "Condiciones de uso y compra de zeltrix.shop.", f"""
<h2>Información general</h2><p>Este sitio web es operado por zeltrix.shop. <mark>[Completar antes de publicar: razón social, NIF y domicilio]</mark> Al usar la tienda aceptas estos términos.</p>
<h2>Productos y precios</h2><p>Mostramos los productos con la mayor precisión posible; los colores pueden variar ligeramente según la pantalla. Los precios están en euros e incluyen impuestos. Podemos modificar precios y disponibilidad sin previo aviso.</p>
<h2>Pedidos</h2><p>Un pedido se considera aceptado cuando lo confirmamos por correo. Podemos rechazar o cancelar pedidos por error de precio, falta de stock o sospecha de fraude, reembolsando cualquier importe cobrado.</p>
<h2>Productos de cuidado personal</h2><p>Los dispositivos de cuidado personal no son productos sanitarios y no sustituyen el consejo médico. Si tienes dudas sobre su uso, consulta con tu médico.</p>
<h2>Envíos y devoluciones</h2><p>Se rigen por nuestra <a href="/policies/refund-policy">política de envíos y devoluciones</a>.</p>
<h2>Ley aplicable</h2><p>Estos términos se rigen por la legislación española y la normativa europea de consumidores.</p>
<h2>Contacto</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p>
""")

# =============== 404, sitemap, robots, vercel.json ===============
nf = head("Página no encontrada | Zeltrix", "La página que buscas no existe.", "/404", noindex=True) + header("") + '<div class="wrap"><div class="done"><p class="eyebrow">Error 404</p><h1 style="margin:14px 0">Esta página no existe</h1><p>Puede que el enlace haya cambiado.</p><p style="margin-top:26px"><a class="btn btn-ink" href="/">Volver al inicio</a></p></div></div>' + footer()
write("404.html", nf)

pages = ["/", url(g), url(c), "/pages/contact", "/policies/refund-policy", "/policies/privacy-policy", "/policies/terms-of-service"]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE}{p}</loc><lastmod>{DATE}</lastmod></url>\n" for p in pages) + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /cart\n\nSitemap: {SITE}/sitemap.xml\n")
write("vercel.json", json.dumps({
  "cleanUrls": True, "trailingSlash": False,
  "redirects": [{"source": "/products/gafas-anti-ojeras", "destination": f"/products/{g['slug']}", "permanent": True},
                {"source": "/collections/all", "destination": "/#productos", "permanent": True}],
  "headers": [
    {"source": "/assets/img/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
    {"source": "/assets/(styles.css|main.js)", "headers": [{"key": "Cache-Control", "value": "public, max-age=3600, must-revalidate"}]},
    {"source": "/(.*)", "headers": [
      {"key": "X-Content-Type-Options", "value": "nosniff"}, {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
      {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"}, {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()"}]}]
}, indent=2) + "\n")
write(".vercelignore", "_src\n")
