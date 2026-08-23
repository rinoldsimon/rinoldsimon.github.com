(function () {
  var root = document.documentElement;
  var themeButton = document.querySelector(".theme-toggle");

  function theme() {
    return root.getAttribute("data-theme") === "light" ? "light" : "dark";
  }

  function syncLabel() {
    if (!themeButton) return;
    themeButton.setAttribute(
      "aria-label",
      theme() === "dark" ? "Switch to light theme" : "Switch to dark theme"
    );
  }

  function apply(next) {
    root.setAttribute("data-theme", next);
    try {
      localStorage.setItem("theme", next);
    } catch (e) {}
    syncLabel();
  }

  syncLabel();

  if (themeButton) {
    themeButton.addEventListener("click", function () {
      apply(theme() === "dark" ? "light" : "dark");
    });
  }

  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (!toggle || !nav) return;

  function setOpen(open) {
    document.body.classList.toggle("nav-open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  }

  toggle.addEventListener("click", function () {
    setOpen(!document.body.classList.contains("nav-open"));
  });

  nav.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function () {
      setOpen(false);
    });
  });
})();
