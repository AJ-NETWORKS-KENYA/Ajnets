/**
 * AJNETWORKS — Modern Vanilla ES6+ UI Controller (Zero-jQuery)
 * Handles: Sticky Header, Mobile Navigation, Accordions, Tabs,
 * IntersectionObserver Counters & Progress Bars, Portfolio Filtering,
 * and Responsive Testimonial Carousels.
 */
(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    initStickyHeader();
    initMobileMenu();
    initAccordions();
    initTabs();
    initCountersAndProgress();
    initPortfolioFilter();
    initCarousels();
    initDismissibleMessages();
  });

  /* 1. Sticky Header */
  function initStickyHeader() {
    const siteHeader = document.getElementById("site-header");
    if (!siteHeader || !siteHeader.classList.contains("sticky-header")) return;

    const mainHeader = siteHeader.querySelector(".octf-main-header");
    const mobileHeader = siteHeader.querySelector(".header_mobile");
    let ticking = false;

    function updateHeader() {
      const threshold = siteHeader.offsetHeight + 30;
      const isStuck = window.scrollY >= threshold;
      if (mainHeader) mainHeader.classList.toggle("is-stuck", isStuck);
      if (mobileHeader) mobileHeader.classList.toggle("is-stuck", isStuck);
      ticking = false;
    }

    window.addEventListener(
      "scroll",
      function () {
        if (!ticking) {
          window.requestAnimationFrame(updateHeader);
          ticking = true;
        }
      },
      { passive: true }
    );
  }

  /* 2. Mobile Navigation Menu */
  function initMobileMenu() {
    const toggleWrap = document.getElementById("mmenu_toggle");
    const toggleBtn = toggleWrap ? toggleWrap.querySelector("button") : null;
    const mobileNav = document.querySelector(".mobile_nav");

    document
      .querySelectorAll(".mobile_mainmenu li.menu-item-has-children")
      .forEach(function (li) {
        if (!li.querySelector(".arrow")) {
          const arrow = document.createElement("span");
          arrow.className = "arrow";
          arrow.innerHTML = '<i class="flaticon-right-arrow"></i>';
          li.insertBefore(arrow, li.firstChild);
        }
      });

    if (toggleWrap && mobileNav) {
      toggleWrap.addEventListener("click", function () {
        const isActive = toggleWrap.classList.toggle("active");
        if (toggleBtn) {
          toggleBtn.setAttribute("aria-expanded", isActive ? "true" : "false");
        }
        mobileNav.style.display = isActive ? "block" : "none";
      });
    }

    document
      .querySelectorAll(".mobile_mainmenu > li > span.arrow")
      .forEach(function (arrow) {
        arrow.addEventListener("click", function () {
          const parentLi = arrow.parentElement;
          const subMenu = parentLi ? parentLi.querySelector(":scope > ul") : null;
          if (!subMenu) return;
          const isOpen = arrow.classList.toggle("active");
          subMenu.style.display = isOpen ? "block" : "none";
        });
      });
  }

  /* 3. Accordions (.ot-accordions) */
  function initAccordions() {
    document.querySelectorAll(".ot-accordions").forEach(function (container) {
      const items = Array.from(container.querySelectorAll(".acc-item"));
      items.forEach(function (item, idx) {
        const toggle = item.querySelector(".acc-toggle");
        const content = item.querySelector(".acc-content");
        if (!toggle || !content) return;

        if (idx === 0) {
          item.classList.add("current");
          content.classList.add("active");
          content.style.display = "block";
        }

        toggle.addEventListener("click", function (e) {
          e.preventDefault();
          const isActive = content.classList.contains("active");
          items.forEach(function (other) {
            other.classList.remove("current");
            const otherContent = other.querySelector(".acc-content");
            if (otherContent) {
              otherContent.classList.remove("active");
              otherContent.style.display = "none";
            }
          });
          if (!isActive) {
            item.classList.add("current");
            content.classList.add("active");
            content.style.display = "block";
          }
        });
      });
    });
  }

  /* 4. Tabs (.ot-tabs) */
  function initTabs() {
    document.querySelectorAll(".ot-tabs").forEach(function (tabGroup) {
      const headings = Array.from(tabGroup.querySelectorAll(".tabs-heading li"));
      const contents = Array.from(tabGroup.querySelectorAll(".tab-content"));

      if (headings.length > 0 && contents.length > 0) {
        headings[0].classList.add("current");
        contents[0].classList.add("current");
      }

      headings.forEach(function (li) {
        li.addEventListener("click", function () {
          const tabId = li.getAttribute("data-tab");
          headings.forEach((h) => h.classList.remove("current"));
          contents.forEach((c) => c.classList.remove("current"));
          li.classList.add("current");
          const target = tabId ? document.getElementById(tabId) : null;
          if (target) target.classList.add("current");
        });
      });
    });
  }

  /* 5. IntersectionObserver Counters & Progress Bars */
  function initCountersAndProgress() {
    if (!("IntersectionObserver" in window)) return;

    const counterObserver = new IntersectionObserver(
      function (entries, observer) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          observer.unobserve(el);

          const numSpan = el.querySelector("span.num");
          if (!numSpan) return;
          const target = parseInt(numSpan.getAttribute("data-to") || "0", 10);
          const duration = parseInt(numSpan.getAttribute("data-time") || "1500", 10);
          const startTime = performance.now();

          function tick(now) {
            const progress = Math.min((now - startTime) / duration, 1);
            numSpan.textContent = String(Math.floor(progress * target));
            if (progress < 1) {
              window.requestAnimationFrame(tick);
            } else {
              numSpan.textContent = String(target);
            }
          }
          window.requestAnimationFrame(tick);
        });
      },
      { threshold: 0.2 }
    );

    document
      .querySelectorAll(".ot-counter, .ot-counter2")
      .forEach((el) => counterObserver.observe(el));

    const progressObserver = new IntersectionObserver(
      function (entries, observer) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          observer.unobserve(el);
          const bar = el.querySelector(".progress-bar");
          if (bar) {
            const pct = bar.getAttribute("data-percent");
            if (pct) bar.style.width = pct;
          }
        });
      },
      { threshold: 0.2 }
    );

    document
      .querySelectorAll(".ot-progress")
      .forEach((el) => progressObserver.observe(el));
  }

  /* 6. Portfolio Filter (.projects-grid & .project_filters) */
  function initPortfolioFilter() {
    const filterSets = document.querySelectorAll(".project_filters");
    filterSets.forEach(function (filterSet) {
      const links = Array.from(filterSet.querySelectorAll("a"));
      const grid = document.querySelector(".projects-grid, #projects_grid");
      if (!grid) return;
      const items = Array.from(grid.querySelectorAll(".project-item"));

      links.forEach(function (link) {
        link.addEventListener("click", function (e) {
          e.preventDefault();
          links.forEach((l) => l.classList.remove("selected"));
          link.classList.add("selected");
          const selector = link.getAttribute("data-filter") || "*";
          items.forEach(function (item) {
            if (selector === "*" || item.matches(selector)) {
              item.style.display = "";
            } else {
              item.style.display = "none";
            }
          });
        });
      });
    });
  }

  /* 7. Lightweight Vanilla Carousel Replacement for .owl-carousel */
  function initCarousels() {
    document.querySelectorAll(".owl-carousel").forEach(function (carousel) {
      carousel.style.display = "grid";
      carousel.style.gap = "24px";
      const isTestimonial = carousel.classList.contains("ot-testimonials-slider");
      const updateGridColumns = function () {
        if (window.innerWidth >= 992) {
          carousel.style.gridTemplateColumns = isTestimonial
            ? "repeat(3, minmax(0, 1fr))"
            : "repeat(auto-fit, minmax(240px, 1fr))";
        } else if (window.innerWidth >= 768) {
          carousel.style.gridTemplateColumns = "repeat(2, minmax(0, 1fr))";
        } else {
          carousel.style.gridTemplateColumns = "1fr";
        }
      };
      updateGridColumns();
      window.addEventListener("resize", updateGridColumns, { passive: true });
    });
  }

  /* 8. Dismissible Message Boxes */
  function initDismissibleMessages() {
    document.querySelectorAll(".message-box > i").forEach(function (icon) {
      icon.addEventListener("click", function () {
        if (icon.parentElement) {
          icon.parentElement.style.display = "none";
        }
      });
    });
  }
})();
