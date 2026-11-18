# Home / landing premium. Se ejecuta desde build.py (comparte sus funciones y variables).
home_faq = [
 ("¿Cuánto dura cada sesión?", "Unos 10 minutos. Las gafas de luz roja se apagan solas cuando termina el temporizador."),
 ("¿Cómo se cargan?", "Por USB con el cable incluido. Por seguridad, no se pueden encender mientras están conectadas a la carga."),
 ("¿Es un producto sanitario?", "No. Es un producto de cuidado personal. Si estás embarazada, llevas marcapasos u otro dispositivo implantado o tienes alguna condición médica, consulta con tu médico antes de usarlo."),
 ("¿Cuánto tarda el envío?", "Enviamos en 24/48 horas."),
 ("¿Y si no me convence?", "Dispones de 30 días desde que lo recibes para solicitar la devolución, según nuestra política de devoluciones."),
]
mq = "".join(f"<span>{t}</span>" for t in ["Luz LED roja 630 nm", "Microcorrientes EMS", "Vibración sónica suave", "Manos libres", "10 minutos", "Carga USB", "Black Friday"])
bag = I['bag'].replace('<svg', '<svg width="18" height="18"')

home = head("Zeltrix | Gafas de luz roja para el contorno de ojos y mini cargador", "Zeltrix: gafas de luz roja con microcorrientes y vibración sónica (25,00 €) y mini cargador portátil de 5000 mAh (15,00 €). Envío en 24/48 h y 30 días para devoluciones.", "/",
  extra='<link rel="stylesheet" href="/assets/landing.css">\n' + ld(ORG, SITE_LD, faq_ld(home_faq)),
  preload='<link rel="preload" as="image" href="/assets/img/gafas-1.webp" fetchpriority="high">\n') + header("") + f"""
<section class="hero lp dark"><div class="wrap">
  <div>
    <span class="pill"><i></i>Black Friday · -30 %</span>
    <h1><span>Luz roja.</span><span class="o">Diez minutos.</span><span class="glowtxt">Tu mirada.</span></h1>
    <p class="lead">Gafas de luz roja con microcorrientes y vibración sónica suave. Formato manos libres para tu ritual de autocuidado: lee, teletrabaja o simplemente descansa.</p>
    <div class="hero-cta">
      <a class="btn btn-glow" href="#comprar">Comprar ahora · {eur(g['price'])}</a>
      <a class="btn btn-line" href="#tecnologia">Ver cómo funcionan</a>
    </div>
    <ul class="hero-meta"><li>{I['truck']}Envío en 24/48 h</li><li>{I['return']}30 días para devoluciones</li><li>{I['lock']}Pago seguro</li></ul>
  </div>
  <div class="stage" id="stage">
    <img src="/assets/img/gafas-1.webp" alt="Gafas de luz roja Zeltrix con los paneles LED encendidos" width="1000" height="1000" fetchpriority="high">
    <div class="chip c1"><b>630 nm</b><small>Luz LED roja</small></div>
    <div class="chip c2"><b>10 min</b><small>Por sesión</small></div>
    <div class="chip c3"><b>45 g</b><small>Ultraligeras</small></div>
    <div class="chip c4"><b>{eur(g['price'])}</b><small>antes {eur(g['compare'])}</small></div>
  </div>
</div></section>

<div class="marq" aria-hidden="true"><div>{mq}{mq}{mq}{mq}</div></div>

<section class="sec dark-2" id="tecnologia"><div class="wrap">
  <div class="sec-head rv" style="max-width:720px"><p class="eyebrow">Tecnología</p><h2 class="h2">Tres tecnologías. <span class="glowtxt">Un solo ritual.</span></h2><p class="lead">Todo en un diseño ergonómico que apenas notarás que llevas puesto.</p></div>
  <div class="tech">
    <div class="tech-vis"><div class="fr"><img src="/assets/img/gafas-3.webp" alt="Detalles del diseño: carga USB-C, luz LED roja y sesión de 10 minutos" width="1000" height="1000" loading="lazy"></div></div>
    <div class="tech-list">
      <div class="tech-i rv"><div class="big">630<small style="font-size:.3em;letter-spacing:0"> nm</small></div><p class="n">01 · LUZ LED ROJA</p><h3>Luz roja de 630 nm</h3><p>Paneles LED rojos sobre el contorno de ojos, en un formato pensado para integrarse en tu rutina de cuidado personal en casa.</p></div>
      <div class="tech-i rv"><div class="big">EMS</div><p class="n">02 · MICROCORRIENTES</p><h3>Microcorrientes</h3><p>Almohadillas conductoras suaves con la piel que acompañan la luz con microcorrientes (EMS) durante toda la sesión.</p></div>
      <div class="tech-i rv"><div class="big">~</div><p class="n">03 · VIBRACIÓN SÓNICA</p><h3>Vibración sónica suave</h3><p>Una vibración delicada que convierte los 10 minutos en un momento de calma. Al terminar el temporizador, las gafas se apagan solas.</p></div>
    </div>
  </div>
</div></section>

<section class="sec-tight"><div class="wrap"><div class="stats rv">
  <div><b data-count="630">630</b><em style="display:none"></em><span>nm de luz LED roja</span></div>
  <div><b data-count="10">10</b><span>minutos por sesión, apagado automático</span></div>
  <div><b data-count="45">45<em>g</em></b><span>de peso: las olvidas al ponértelas</span></div>
  <div><b data-count="90">90<em>mAh</em></b><span>batería de litio integrada, carga USB</span></div>
</div></div></section>

<section class="sec" style="padding-top:clamp(24px,4vw,60px)"><div class="wrap life">
  <div class="ph rv"><img src="/assets/img/gafas-2.webp" alt="Persona con las gafas de luz roja puestas" width="745" height="745" loading="lazy"></div>
  <div class="rv">
    <p class="eyebrow">Manos libres</p>
    <h2 class="h2" style="margin:14px 0 16px">Póntelas. <br>Sigue con tu día.</h2>
    <p class="lead">Un momento de calma en solo 10 minutos al día. Diseño ergonómico que se adapta a tu rostro, sin cables mientras las usas ni nada que sostener.</p>
    <ul class="moments"><li>{I['hands']}Leyendo</li><li>{I['bolt']}Teletrabajando</li><li>{I['clock']}Descansando en el sillón</li></ul>
    <a class="btn btn-ink" href="#comprar">Quiero las mías</a>
  </div>
</div></section>

<section class="sec dark"><div class="wrap ritual">
  <div class="ring rv" id="ring">
    <svg viewBox="0 0 280 280" aria-hidden="true"><defs><linearGradient id="rg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff7a6b"/><stop offset="1" stop-color="#e5483f"/></linearGradient></defs><circle class="tr" cx="140" cy="140" r="120"/><circle class="pg" cx="140" cy="140" r="120"/></svg>
    <div class="tm"><b>10:00</b><span>una sesión</span></div>
  </div>
  <div class="rv">
    <p class="eyebrow">El ritual</p>
    <h2 class="h2" style="margin:14px 0 14px">Diez minutos y listo</h2>
    <p class="lead">Sin ajustes, sin apps, sin complicaciones.</p>
    <ol class="steps" style="list-style:none;padding:0">
      <li><div><b>Cárgalas por USB</b><span>Cable incluido, compatible con cualquier puerto o adaptador estándar.</span></div></li>
      <li><div><b>Póntelas y enciéndelas</b><span>Se adaptan a tu rostro. Por seguridad, no encienden mientras están conectadas a la carga.</span></div></li>
      <li><div><b>Relájate: se apagan solas</b><span>Al terminar el temporizador de 10 minutos, el dispositivo se apaga.</span></div></li>
    </ol>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head center rv"><p class="eyebrow">En la caja</p><h2 class="h2">Todo lo que necesitas</h2></div>
  <div class="bento">
    <div class="bt img b1 rv"><img src="/assets/img/gafas-lifestyle.webp" alt="Gafas masajeadoras Eye Massager junto a su caja" loading="lazy"><div class="cap"><h3>Gafas de luz roja</h3><p>Diseño ergonómico, paneles LED y almohadillas suaves con la piel.</p></div></div>
    <div class="bt dk rv">{I['usb'].replace('<svg','<svg class="ic"')}<h3>Cable de carga USB</h3><p>Compatible con cualquier puerto USB o adaptador estándar.</p></div>
    <div class="bt rv">{I['check'].replace('<svg','<svg class="ic"')}<h3>Manual de instrucciones</h3><p>Guía paso a paso para empezar.</p></div>
    <div class="bt img b4 rv" style="min-height:240px"><img src="/assets/img/gafas-4.webp" alt="Vista del diseño ergonómico y los paneles de luz" loading="lazy" style="object-position:50% 40%"><div class="cap"><h3>Ligeras y portátiles</h3><p>Unos 45 g. Para casa, la oficina o los viajes.</p></div></div>
  </div>
</div></section>

<section class="sec buy-sec dark" id="comprar"><div class="wrap buy-card">
  <div class="im rv"><img src="/assets/img/gafas-3.webp" alt="{g['name']}" width="1000" height="1000" loading="lazy"></div>
  <div class="rv">
    <span class="pill"><i></i>Oferta Black Friday</span>
    <h2 class="h2" style="margin-top:18px">{g['name']}</h2>
    <div class="big-p"><b>{eur(g['price'])}</b><s>{eur(g['compare'])}</s><span class="save">Ahorras {eur(g['compare']-g['price'])}</span></div>
    <p class="vat">Impuestos incluidos. Envío en 24/48 h.</p>
    <div class="buy-row"><div class="qty" data-qty role="group" aria-label="Cantidad"><button type="button" data-dec aria-label="Reducir cantidad">−</button><output aria-live="polite">1</output><button type="button" data-inc aria-label="Aumentar cantidad">+</button></div>
      <button class="btn btn-glow" data-add="gafas" data-use-qty>Añadir al carrito</button></div>
    <div class="trust"><div>{I['truck']}Envío en 24/48 h</div><div>{I['return']}30 días para devolver</div><div>{I['lock']}Pago seguro</div></div>
    <p><a href="{url(g)}" style="text-decoration:underline;color:var(--muted-d)">Ver todos los detalles del producto →</a></p>
  </div>
</div></section>

<section class="sec" id="productos"><div class="wrap">
  <div class="sec-head rv"><p class="eyebrow">También en Zeltrix</p><h2 class="h2">Energía para el resto del día</h2></div>
  <div class="pw rv">
    <div class="im"><img src="/assets/img/cargador-1.webp" alt="{c['imgs'][0][1]}" width="1000" height="1000" loading="lazy"></div>
    <div class="tx"><span class="tag" style="position:static">Esencial</span><h3 style="font-size:clamp(1.6rem,3vw,2.3rem)">{c['name']}</h3>
      <p class="lead">Ultra compacto, 5000 mAh y cable integrado. Energía de reserva que cabe en el bolsillo.</p>
      <p class="price">{eur(c['price'])}</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap"><button class="btn btn-ink" data-add="cargador" data-quick>Añadir al carrito</button><a class="btn btn-line" href="{url(c)}">Ver producto</a></div></div>
  </div>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap" style="max-width:860px">
  <div class="sec-head rv"><p class="eyebrow">Preguntas frecuentes</p><h2 class="h2">Todo claro antes de comprar</h2></div>
  <div class="acc rv">{''.join(acc(q, a) for q, a in home_faq)}</div>
</div></section>

<section class="band dark"><div class="wrap rv">
  <p class="eyebrow">Black Friday</p><h2 class="h2">Un regalo que <span class="glowtxt">sorprende</span></h2>
  <a class="btn btn-glow" href="#comprar">Comprar las gafas · {eur(g['price'])}</a>
</div></section>
""" + footer()
write("index.html", home)
