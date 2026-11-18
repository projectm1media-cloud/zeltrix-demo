/* ZELTRIX storefront — cart, drawer, gallery, checkout demo. No dependencies. */
(() => {
  "use strict";
  document.documentElement.classList.add("js");

  const ROOT = document.documentElement.dataset.root || "";
  const PRODUCTS = {
    gafas: { id: "gafas", name: "Gafas de Luz Roja para el Contorno de Ojos", short: "Gafas de Luz Roja", price: 25, compare: 35.5, img: ROOT + "assets/img/gafas-1-sm.webp", url: ROOT + "products/gafas-luz-roja-anti-ojeras.html", variant: "Blanco" },
    cargador: { id: "cargador", name: "Mini Cargador Portátil 5000 mAh", short: "Mini Cargador 5000 mAh", price: 15, compare: 0, img: ROOT + "assets/img/cargador-1-sm.webp", url: ROOT + "products/mini-banco-de-energia-ultra-compacto-5000mah-negro-con-cable-integrado.html", variant: "Negro · cable integrado" },
  };
  const KEY = "zeltrix_cart_v1", MAX = 10;
  const eur = new Intl.NumberFormat("es-ES", { style: "currency", currency: "EUR" });
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* ---------- Cart store ---------- */
  const store = {
    read() {
      try {
        const v = JSON.parse(localStorage.getItem(KEY) || "[]");
        return Array.isArray(v) ? v.filter((i) => PRODUCTS[i.id] && i.qty > 0).map((i) => ({ id: i.id, qty: Math.min(MAX, i.qty | 0) })) : [];
      } catch { return []; }
    },
    write(items) { try { localStorage.setItem(KEY, JSON.stringify(items)); } catch {} },
  };
  let items = store.read();
  const count = () => items.reduce((n, i) => n + i.qty, 0);
  const total = () => items.reduce((n, i) => n + i.qty * PRODUCTS[i.id].price, 0);
  const commit = () => { store.write(items); paint(); };
  const add = (id, qty = 1) => {
    const f = items.find((i) => i.id === id);
    if (f) f.qty = Math.min(MAX, f.qty + qty); else items.push({ id, qty: Math.min(MAX, qty) });
    commit();
  };
  const setQty = (id, q) => {
    if (q <= 0) items = items.filter((i) => i.id !== id);
    else { const f = items.find((i) => i.id === id); if (f) f.qty = Math.min(MAX, q); }
    commit();
  };
  window.addEventListener("storage", (e) => { if (e.key === KEY) { items = store.read(); paint(); } });

  /* ---------- Rendering ---------- */
  const lineHTML = (i) => {
    const p = PRODUCTS[i.id];
    return `<li class="line" data-id="${p.id}">
      <a href="${p.url}"><img src="${p.img}" alt="${p.short}" width="84" height="84" loading="lazy"></a>
      <div><h3><a href="${p.url}">${p.name}</a></h3><p class="u">${p.variant} · ${eur.format(p.price)}</p>
        <div style="display:flex;align-items:center">
          <div class="qty" role="group" aria-label="Cantidad de ${p.short}">
            <button type="button" data-dec aria-label="Reducir cantidad">−</button><output aria-live="polite">${i.qty}</output><button type="button" data-inc aria-label="Aumentar cantidad">+</button>
          </div><button type="button" class="rm" data-rm>Quitar</button></div></div>
      <div class="lt">${eur.format(p.price * i.qty)}</div></li>`;
  };
  const emptyHTML = () => `<div class="empty"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M6 7h12l-1 12H7L6 7Zm3 0a3 3 0 1 1 6 0"/></svg><h3>Tu carrito está vacío</h3><p>Añade un producto para empezar.</p><a class="btn btn-ink" href="${ROOT}index.html#productos">Ver productos</a></div>`;

  function paint() {
    const n = count();
    $$("[data-cart-count]").forEach((b) => { b.textContent = n; b.hidden = n === 0; });
    const list = $("#drawer-lines");
    if (list) {
      list.innerHTML = items.length ? items.map(lineHTML).join("") : emptyHTML();
      $("#drawer-foot").hidden = !items.length;
      $("#drawer-total").textContent = eur.format(total());
    }
    const page = $("#cart-lines");
    if (page) {
      page.innerHTML = items.length ? items.map(lineHTML).join("") : emptyHTML();
      const empty = !items.length;
      const co = $("#co-form"); if (co) co.hidden = empty;
      $$("[data-sum-sub],[data-sum-total]").forEach((e) => (e.textContent = eur.format(total())));
    }
  }
  const onLineClick = (e) => {
    const li = e.target.closest(".line"); if (!li) return;
    const id = li.dataset.id, cur = (items.find((i) => i.id === id) || {}).qty || 0;
    if (e.target.closest("[data-inc]")) setQty(id, cur + 1);
    else if (e.target.closest("[data-dec]")) setQty(id, cur - 1);
    else if (e.target.closest("[data-rm]")) setQty(id, 0);
  };

  /* ---------- Drawer (focus trap, Esc, scrim) ---------- */
  const drawer = $("#drawer"), scrim = $("#scrim");
  let lastFocus = null;
  const openDrawer = () => {
    if (!drawer) { location.href = ROOT + "cart.html"; return; }
    lastFocus = document.activeElement;
    drawer.classList.add("open"); scrim.classList.add("show");
    drawer.setAttribute("aria-hidden", "false"); document.body.style.overflow = "hidden";
    setTimeout(() => $("#drawer-close").focus(), 50);
  };
  const closeDrawer = () => {
    if (!drawer) return;
    drawer.classList.remove("open"); scrim.classList.remove("show");
    drawer.setAttribute("aria-hidden", "true"); document.body.style.overflow = "";
    if (lastFocus) lastFocus.focus();
  };
  if (drawer) {
    $("#drawer-close").addEventListener("click", closeDrawer);
    scrim.addEventListener("click", closeDrawer);
    drawer.addEventListener("click", onLineClick);
    document.addEventListener("keydown", (e) => {
      if (!drawer.classList.contains("open")) return;
      if (e.key === "Escape") return closeDrawer();
      if (e.key !== "Tab") return;
      const f = $$("a[href],button:not([disabled])", drawer).filter((x) => x.offsetParent !== null);
      if (!f.length) return;
      const a = f[0], z = f[f.length - 1];
      if (e.shiftKey && document.activeElement === a) { e.preventDefault(); z.focus(); }
      else if (!e.shiftKey && document.activeElement === z) { e.preventDefault(); a.focus(); }
    });
  }
  $$("[data-open-cart]").forEach((b) => b.addEventListener("click", (e) => { if (drawer) { e.preventDefault(); openDrawer(); } }));
  const page = $("#cart-lines"); if (page) page.addEventListener("click", onLineClick);

  /* ---------- Add to cart + qty selectors ---------- */
  const toast = (msg) => {
    let t = $(".toast"); if (!t) { t = document.createElement("div"); t.className = "toast"; t.setAttribute("role", "status"); document.body.append(t); }
    t.textContent = msg; t.classList.add("show"); clearTimeout(t._t); t._t = setTimeout(() => t.classList.remove("show"), 2200);
  };
  $$("[data-qty]").forEach((box) => {
    const out = $("output", box);
    box.addEventListener("click", (e) => {
      const v = +out.textContent;
      if (e.target.closest("[data-dec]")) out.textContent = Math.max(1, v - 1);
      if (e.target.closest("[data-inc]")) out.textContent = Math.min(MAX, v + 1);
    });
  });
  $$("[data-add]").forEach((b) => b.addEventListener("click", () => {
    const q = $("[data-qty] output"); const n = b.hasAttribute("data-use-qty") && q ? +q.textContent : 1;
    add(b.dataset.add, n);
    if (b.hasAttribute("data-quick")) toast("Añadido al carrito"); else openDrawer();
  }));

  /* ---------- Nav ---------- */
  const menu = $("#menu-btn"), nav = $("#nav");
  if (menu) menu.addEventListener("click", () => {
    const o = nav.classList.toggle("open"); menu.setAttribute("aria-expanded", o);
    document.body.style.overflow = o ? "hidden" : "";
  });
  $$("#nav a").forEach((a) => a.addEventListener("click", () => { nav.classList.remove("open"); document.body.style.overflow = ""; menu && menu.setAttribute("aria-expanded", "false"); }));

  /* ---------- Gallery ---------- */
  const gal = $("[data-gallery]");
  if (gal) {
    const main = $("[data-gal-main]", gal), btns = $$("[data-thumb]", gal);
    let idx = 0;
    const go = (i) => {
      idx = (i + btns.length) % btns.length;
      const b = btns[idx]; main.src = b.dataset.full; main.alt = b.dataset.alt;
      btns.forEach((x, k) => x.setAttribute("aria-current", k === idx));
    };
    btns.forEach((b, i) => b.addEventListener("click", () => go(i)));
    const pv = $("[data-prev]", gal), nx = $("[data-next]", gal);
    if (pv) pv.addEventListener("click", () => go(idx - 1));
    if (nx) nx.addEventListener("click", () => go(idx + 1));
    gal.addEventListener("keydown", (e) => { if (e.key === "ArrowLeft") go(idx - 1); if (e.key === "ArrowRight") go(idx + 1); });
    let sx = 0;
    $(".gal-main", gal).addEventListener("touchstart", (e) => (sx = e.touches[0].clientX), { passive: true });
    $(".gal-main", gal).addEventListener("touchend", (e) => { const d = e.changedTouches[0].clientX - sx; if (Math.abs(d) > 40) go(idx + (d < 0 ? 1 : -1)); }, { passive: true });
  }

  /* ---------- Sticky buy bar ---------- */
  const sticky = $("#sticky-buy"), anchor = $("#buy-anchor");
  if (sticky && anchor && "IntersectionObserver" in window) {
    document.body.classList.add("has-sticky");
    new IntersectionObserver(([en]) => sticky.classList.toggle("show", !en.isIntersecting && en.boundingClientRect.top < 0), { threshold: 0 }).observe(anchor);
  }

  /* ---------- Reveal on scroll (transform only, content never hidden) ---------- */
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { rootMargin: "0px 0px -8% 0px" });
    $$(".rv").forEach((el) => io.observe(el));
  } else $$(".rv").forEach((el) => el.classList.add("in"));

  /* ---------- Checkout (demo, nothing is charged or sent) ---------- */
  const form = $("#co-form");
  if (form) form.addEventListener("submit", (e) => {
    e.preventDefault();
    if (!items.length) return;
    const fd = new FormData(form);
    const order = "ZX-" + Math.random().toString(36).slice(2, 8).toUpperCase();
    $("#co-view").hidden = true; $("#done-view").hidden = false;
    $("#done-order").textContent = order; $("#done-email").textContent = fd.get("email");
    $("#done-total").textContent = eur.format(total());
    items = []; commit(); window.scrollTo({ top: 0, behavior: "smooth" });
  });

  /* ---------- Contact (opens the visitor's mail client) ---------- */
  const cf = $("#contact-form");
  if (cf) cf.addEventListener("submit", (e) => {
    e.preventDefault();
    const fd = new FormData(cf);
    const body = `${fd.get("msg")}\n\n— ${fd.get("name")}${fd.get("tel") ? " · " + fd.get("tel") : ""} · ${fd.get("email")}`;
    location.href = `mailto:${cf.dataset.to}?subject=${encodeURIComponent("Consulta desde zeltrix.shop")}&body=${encodeURIComponent(body)}`;
  });

  /* ---------- Count-up, ring, hero parallax ---------- */
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const ioC = "IntersectionObserver" in window ? new IntersectionObserver((es) => es.forEach((e) => {
    if (!e.isIntersecting) return; ioC.unobserve(e.target);
    const el = e.target;
    if (el.id === "ring") { el.classList.add("in"); return; }
    const node = [...el.childNodes].find((n) => n.nodeType === 3); if (!node || reduce) return;
    const to = +el.dataset.count, t0 = performance.now();
    const tick = (t) => { const k = Math.min(1, (t - t0) / 1400); node.nodeValue = Math.round(to * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(tick); };
    requestAnimationFrame(tick);
  }), { threshold: 0.4 }) : null;
  if (ioC) { $$("[data-count]").forEach((el) => ioC.observe(el)); const r = $("#ring"); if (r) ioC.observe(r); }
  else { const r = $("#ring"); if (r) r.classList.add("in"); }
  const stage = $("#stage");
  if (stage && !reduce && matchMedia("(hover:hover)").matches) {
    const img = $("img", stage);
    window.addEventListener("mousemove", (e) => {
      const x = (e.clientX / innerWidth - 0.5) * 2, y = (e.clientY / innerHeight - 0.5) * 2;
      img.style.transform = "translate(" + (x * -14) + "px," + (y * -10) + "px) rotate(" + (x * 2) + "deg)";
    }, { passive: true });
  }

  paint();
})();
