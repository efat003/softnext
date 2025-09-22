
document.addEventListener('DOMContentLoaded', () => {

    /* ----------------- Mobile Menu ----------------- */
    const menuToggle        = document.getElementById('menu-toggle');
    const mobileMenu        = document.getElementById('mobile-menu');
    const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');

    function toggleMobileMenu() {
        if (!mobileMenu || !mobileMenuOverlay) return;
        mobileMenu.classList.toggle('active');
        mobileMenuOverlay.classList.toggle('active');
        document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
    }
    menuToggle?.addEventListener('click', toggleMobileMenu);
    mobileMenuOverlay?.addEventListener('click', toggleMobileMenu);
    document.querySelectorAll('.mobile-nav-links a')
        .forEach(link => link.addEventListener('click', toggleMobileMenu));

    /* ----------------- Testimonial Slider ----------------- */
    const testimonialTrack  = document.getElementById('testimonial-track');
    const testimonialSlides = document.querySelectorAll('.testimonial-slide');
    const prevBtn           = document.getElementById('testimonial-prev');
    const nextBtn           = document.getElementById('testimonial-next');
    const dots              = document.querySelectorAll('.slider-dot');

    let currentIndex = 0;
    function updateSlider() {
        if (!testimonialTrack) return;
        testimonialTrack.style.transform = `translateX(-${currentIndex * 100}%)`;
        dots.forEach((dot, i) => dot.classList.toggle('active', i === currentIndex));
    }
    function nextSlide() { currentIndex = (currentIndex + 1) % testimonialSlides.length; updateSlider(); }
    function prevSlide() { currentIndex = (currentIndex - 1 + testimonialSlides.length) % testimonialSlides.length; updateSlider(); }

    nextBtn?.addEventListener('click', nextSlide);
    prevBtn?.addEventListener('click', prevSlide);
    dots.forEach(dot => dot.addEventListener('click', () => {
        const i = parseInt(dot.dataset.index, 10);
        if (!isNaN(i)) { currentIndex = i; updateSlider(); }
    }));
    if (testimonialSlides.length) setInterval(nextSlide, 5000);

    /* ----------------- FAQ Accordion ----------------- */
    document.querySelectorAll('.faq-item').forEach(item => {
        const q = item.querySelector('.faq-question');
        q?.addEventListener('click', () => item.classList.toggle('active'));
    });

    /* ----------------- Back to Top ----------------- */
    const backToTopBtn = document.getElementById('backToTop');
    window.addEventListener('scroll', () => backToTopBtn?.classList.toggle('active', window.pageYOffset > 300));
    backToTopBtn?.addEventListener('click', e => { e.preventDefault(); window.scrollTo({top:0,behavior:'smooth'}); });

    /* ----------------- Counter Animation ----------------- */
    const statNumbers  = document.querySelectorAll('.stat-number');
    const aboutSection = document.querySelector('.about');
    let countersAnimated = false;
    function animateCounter(el, target) {
        let current = 0, step = target / 100, stepTime = 20;
        const timer = setInterval(() => {
            current += step;
            if (current >= target) { el.textContent = target; clearInterval(timer); }
            else { el.textContent = Math.floor(current); }
        }, stepTime);
    }
    function handleScroll() {
        if (!aboutSection) return;
        const r = aboutSection.getBoundingClientRect();
        if (!countersAnimated && r.top <= window.innerHeight && r.bottom >= 0) {
            statNumbers.forEach(stat => {
                const t = parseInt(stat.dataset.count, 10);
                if (!isNaN(t)) animateCounter(stat, t);
            });
            countersAnimated = true;
        }
    }
    window.addEventListener('scroll', handleScroll);
    handleScroll();

    /* ----------------- Contact Form ----------------- */
    const contactForm = document.getElementById('contactForm');
    contactForm?.addEventListener('submit', e => {
        e.preventDefault();
        alert('Thank you for your message! We will get back to you soon.');
        contactForm.reset();
    });

    /* ----------------- Navbar Scroll Effect ----------------- */
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (!navbar) return;
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(255,255,255,0.95)';
            navbar.style.backdropFilter = 'blur(10px)';
        } else {
            navbar.style.background = 'white';
            navbar.style.backdropFilter = 'none';
        }
    });

    /* ----------------- Google Map (Dhaka, Bangladesh) ----------------- */
    const mapContainer = document.getElementById('map');
    if (mapContainer && window.google && google.maps) {
        const dhaka = { lat: 23.8103, lng: 90.4125 };
        const map   = new google.maps.Map(mapContainer, { center: dhaka, zoom: 12 });
        new google.maps.Marker({ position: dhaka, map: map, title: 'Our Location' });
    }

    /* ----------------- Generic Slider ----------------- */
    const slides = document.querySelectorAll('.slide');
    const sliderDots = document.querySelectorAll('.slider-dot');
    let currentSlide = 0;
    function showSlide(n) {
        slides.forEach(s => s.classList.remove('active'));
        sliderDots.forEach(d => d.classList.remove('active'));
        currentSlide = (n + slides.length) % slides.length;
        slides[currentSlide].classList.add('active');
        sliderDots[currentSlide].classList.add('active');
    }
    if (slides.length) setInterval(() => showSlide(currentSlide + 1), 5000);
    sliderDots.forEach(dot => dot.addEventListener('click', () => {
        const i = parseInt(dot.dataset.slide, 10);
        if (!isNaN(i)) showSlide(i);
    }));

});

