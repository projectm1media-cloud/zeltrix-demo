/* ZELTRIX home — interacciones de portada y móvil. Sin dependencias. */
(() => {
  "use strict";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const mobile = matchMedia("(max-width: 820px)");
  const buzz = (ms = 10) => { try { navigator.vibrate && navigator.vibrate(ms); } catch (e) {} };

  /* Barra de progreso de scroll */
  const prog = $("#zprog");
  if (prog) {
    const on = () => {
      const h = document.documentElement.scrollHeight - innerHeight;
      prog.style.transform = "scaleX(" + (h > 0 ? Math.min(1, scrollY / h) : 0) + ")";
    };
    addEventListener("scroll", on, { passive: true }); on();
  }

  /* Brasas de luz roja en la portada */
  const em = $("#embers");
  if (em && !reduce) {
    const n = mobile.matches ? 12 : 20;
    for (let i = 0; i < n; i++) {
      const el = document.createElement("i");
      const st = el.style;
      st.setProperty("--x", (Math.random() * 100).toFixed(1) + "%");
      st.setProperty("--s", (2 + Math.random() * 4).toFixed(1) + "px");
      st.setProperty("--d", (7 + Math.random() * 8).toFixed(1) + "s");
      st.setProperty("--dl", (-Math.random() * 12).toFixed(1) + "s");
      st.setProperty("--dx", (Math.random() * 80 - 40).toFixed(0) + "px");
      em.appendChild(el);
    }
  }

  /* Burbujas de la portada: tocar para ver el detalle (auto-ciclo en móvil) */
  const chips = $$(".chip[data-cap]"), cap = $("#stage-cap");
  let ci = -1, manual = false, timer;
  const showChip = (i) => {
    ci = i;
    chips.forEach((c, k) => c.classList.toggle("on", k === i));
    if (!cap) return;
    cap.classList.add("swap");
    setTimeout(() => { cap.innerHTML = chips[i].dataset.cap; cap.classList.remove("swap"); }, 160);
  };
  chips.forEach((c, i) => c.addEventListener("click", () => { manual = true; clearInterval(timer); buzz(); showChip(i); }));
  if (chips.length && !reduce) {
    setTimeout(() => { if (mobile.matches && !manual) showChip(0); }, 1800);
    timer = setInterval(() => { if (mobile.matches && !manual) showChip((ci + 1) % chips.length); }, 3600);
  }

  /* Demo del ritual: la sesión de 10 min a velocidad x60 */
  const ring = $("#ring"), rt = $("#ring-t"), rs = $("#ring-s"), rh = $("#ring-h");
  const pg = ring && $(".pg", ring);
  if (ring && pg) {
    const FULL = 754, REST = 75, TOTAL = 600, SPEED = 60;
    let running = false;
    const fmt = (sec) => { sec = Math.max(0, Math.ceil(sec)); return String(Math.floor(sec / 60)).padStart(2, "0") + ":" + String(sec % 60).padStart(2, "0"); };
    const reset = () => {
      running = false; ring.classList.remove("demo", "done");
      pg.style.strokeDashoffset = ""; rt.textContent = "10:00"; rs.textContent = "una sesión"; rh.style.display = "";
    };
    const start = () => {
      if (running) return;
      running = true; buzz(15);
      ring.classList.remove("done"); ring.classList.add("in", "demo");
      rh.style.display = "none"; rs.textContent = "luz encendida";
      const t0 = performance.now(), dur = (TOTAL / SPEED) * 1000;
      const tick = (t) => {
        const k = Math.min(1, (t - t0) / dur);
        rt.textContent = fmt(TOTAL * (1 - k));
        pg.style.strokeDashoffset = REST + (FULL - REST) * k;
        if (k < 1) requestAnimationFrame(tick);
        else {
          ring.classList.add("done"); rs.textContent = "se apaga sola ✓"; buzz([20, 40, 20]);
          setTimeout(reset, 3200);
        }
      };
      requestAnimationFrame(tick);
    };
    ring.addEventListener("click", start);
    ring.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); start(); } });
  }

  /* Carrusel de tecnologías con puntos (móvil por CSS) */
  const tl = $(".tech-list");
  if (tl) {
    const cards = [...tl.children];
    const dots = document.createElement("div"); dots.className = "dots";
    cards.forEach(() => dots.appendChild(document.createElement("span")));
    tl.after(dots);
    let prev = -1;
    const set = () => {
      const left = tl.getBoundingClientRect().left + 16;
      let best = 0, bd = 1e9;
      cards.forEach((c, i) => { const d = Math.abs(c.getBoundingClientRect().left - left); if (d < bd) { bd = d; best = i; } });
      [...dots.children].forEach((d, i) => d.classList.toggle("on", i === best));
      if (best !== prev && prev !== -1) buzz(6);
      prev = best;
    };
    tl.addEventListener("scroll", set, { passive: true }); set();
    [...dots.children].forEach((d, i) => d.addEventListener("click", () => cards[i].scrollIntoView({ behavior: "smooth", inline: "start", block: "nearest" })));
  }

  /* Barra de compra pegajosa (móvil): tras la portada, oculta ante la zona de compra */
  const bar = $("#hm-bar"), hero = $(".hero-cta"), buy = $("#comprar"), band = $(".band");
  if (bar && hero && "IntersectionObserver" in window) {
    document.body.classList.add("has-hm");
    const v = { hero: true, buy: false, band: false };
    const upd = () => bar.classList.toggle("show", !v.hero && !v.buy && !v.band);
    const io = new IntersectionObserver((es) => es.forEach((e) => { v[e.target === hero ? "hero" : e.target === buy ? "buy" : "band"] = e.isIntersecting; upd(); }), { threshold: 0.15 });
    io.observe(hero); if (buy) io.observe(buy); if (band) io.observe(band);
  }
})();
