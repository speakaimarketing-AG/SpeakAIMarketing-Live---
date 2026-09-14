// =========================================
// Speaking.Marketing — App JavaScript
// Theme Toggle | Navigation | Scroll Reveal
// =========================================

(function() {
    'use strict';

    // --- Theme Toggle ---
    const themeToggle = document.getElementById('themeToggle');
    const html = document.documentElement;

    const savedTheme = localStorage.getItem('sm-theme');
    if (savedTheme) {
        html.setAttribute('data-theme', savedTheme);
    } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        html.setAttribute('data-theme', 'dark');
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            var current = html.getAttribute('data-theme') || 'light';
            var next = current === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', next);
            localStorage.setItem('sm-theme', next);
        });
    }

    // --- Navigation ---
    var nav = document.querySelector('.nav');
    var hamburger = document.getElementById('navHamburger');
    var navLinks = document.getElementById('navLinks');

    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 50) {
            nav && nav.classList.add('nav--scrolled');
        } else {
            nav && nav.classList.remove('nav--scrolled');
        }
    }, { passive: true });

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navLinks.classList.toggle('active');
        });

        navLinks.querySelectorAll('.nav__link').forEach(function(link) {
            link.addEventListener('click', function() {
                hamburger.classList.remove('active');
                navLinks.classList.remove('active');
            });
        });
    }

    // --- Scroll Reveal ---
    var reveals = document.querySelectorAll('.reveal');
    if (reveals.length > 0 && 'IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

        reveals.forEach(function(el) { observer.observe(el); });
    }

    // --- Accordion ---
    document.querySelectorAll('.accordion__trigger').forEach(function(trigger) {
        trigger.addEventListener('click', function() {
            var item = trigger.parentElement;
            var content = item.querySelector('.accordion__content');
            var isActive = item.classList.contains('active');

            // Close all items in this accordion
            var accordion = item.closest('.accordion');
            if (accordion) {
                accordion.querySelectorAll('.accordion__item').forEach(function(i) {
                    i.classList.remove('active');
                    var c = i.querySelector('.accordion__content');
                    if (c) c.style.maxHeight = null;
                });
            }

            if (!isActive && content) {
                item.classList.add('active');
                content.style.maxHeight = content.scrollHeight + 'px';
            }
        });
    });

    // --- Currency Toggle (INR/USD) ---
    var currencyCheckbox = document.getElementById('currencyToggle');
    var pricingDiv = document.querySelector('.toggle:not(label)');

    function updatePrices(isUsd) {
        var prices = document.querySelectorAll('[data-inr]');
        prices.forEach(function(p) {
            p.textContent = isUsd ? p.getAttribute('data-usd') : p.getAttribute('data-inr');
        });
        
        var inrLabel = document.getElementById('inrLabel');
        var usdLabel = document.getElementById('usdLabel');
        if (inrLabel) {
            inrLabel.classList.toggle('active', !isUsd);
            inrLabel.classList.toggle('toggle-label--active', !isUsd);
        }
        if (usdLabel) {
            usdLabel.classList.toggle('active', isUsd);
            usdLabel.classList.toggle('toggle-label--active', isUsd);
        }
    }

    if (currencyCheckbox) {
        currencyCheckbox.addEventListener('change', function() {
            updatePrices(currencyCheckbox.checked);
        });
    }
    if (pricingDiv) {
        pricingDiv.addEventListener('click', function() {
            pricingDiv.classList.toggle('active');
            updatePrices(pricingDiv.classList.contains('active'));
        });
    }

})();
