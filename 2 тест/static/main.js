// ============ Мобильное меню ============
const burger = document.getElementById('burger');
const nav = document.getElementById('nav');
if (burger && nav) {
    burger.addEventListener('click', () => {
        burger.classList.toggle('active');
        nav.classList.toggle('open');
    });
    nav.querySelectorAll('.nav__link').forEach(link => {
        link.addEventListener('click', () => {
            burger.classList.remove('active');
            nav.classList.remove('open');
        });
    });
}

// ============ Слайдер главного экрана ============
const heroSlides = document.querySelectorAll('[data-slide]');
const heroButtons = document.querySelectorAll('[data-slide-button]');
if (heroSlides.length > 1) {
    let activeSlide = 0;

    const showSlide = (index) => {
        activeSlide = index;
        heroSlides.forEach((slide, slideIndex) => {
            slide.classList.toggle('hero__slide--active', slideIndex === activeSlide);
        });
        heroButtons.forEach((button, buttonIndex) => {
            button.classList.toggle('hero__dot--active', buttonIndex === activeSlide);
        });
    };

    heroButtons.forEach((button, index) => {
        button.addEventListener('click', () => showSlide(index));
    });

    setInterval(() => showSlide((activeSlide + 1) % heroSlides.length), 6000);
}

// ============ Анимация появления при скролле ============
const reveals = document.querySelectorAll('[data-reveal]');
if (reveals.length) {
    const io = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in');
                io.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12 });
    reveals.forEach(el => io.observe(el));
}

// ============ Фильтр каталога ============
const chips = document.querySelectorAll('.chip');
const grid = document.getElementById('catalog-grid');
const empty = document.getElementById('empty');
if (chips.length && grid) {
    const cards = [...grid.querySelectorAll('.card')];
    chips.forEach(chip => {
        chip.addEventListener('click', () => {
            chips.forEach(c => c.classList.remove('chip--active'));
            chip.classList.add('chip--active');
            const filter = chip.dataset.filter;
            let visible = 0;
            cards.forEach(card => {
                const show = filter === 'all' || card.dataset.category === filter;
                card.style.display = show ? '' : 'none';
                if (show) visible++;
            });
            if (empty) empty.hidden = visible !== 0;
        });
    });
}

// ============ Кнопка "Оставить заявку" в карточке -> подставить авто в форму ============
const carSelect = document.getElementById('car-select');
document.querySelectorAll('.js-pick').forEach(btn => {
    btn.addEventListener('click', () => {
        if (carSelect && btn.dataset.car) {
            carSelect.value = btn.dataset.car;
        }
    });
});

// ============ Валидация и отправка формы ============
const form = document.getElementById('order-form');
if (form) {
    const success = document.getElementById('form-success');

    const setInvalid = (field, invalid) => field.classList.toggle('is-invalid', invalid);
    const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phoneRe = /[0-9]{6,}/; // минимум 6 цифр

    const validate = () => {
        let ok = true;

        const nameField = form.name.closest('.field');
        const nameOk = form.name.value.trim().length >= 2;
        setInvalid(nameField, !nameOk);
        if (!nameOk) ok = false;

        const phoneField = form.phone.closest('.field');
        const phoneOk = phoneRe.test(form.phone.value.replace(/\D/g, ''));
        setInvalid(phoneField, !phoneOk);
        if (!phoneOk) ok = false;

        const emailField = form.email.closest('.field');
        const emailVal = form.email.value.trim();
        const emailOk = emailVal === '' || emailRe.test(emailVal);
        setInvalid(emailField, !emailOk);
        if (!emailOk) ok = false;

        const agreeField = form.agree.closest('.checkbox');
        const agreeOk = form.agree.checked;
        setInvalid(agreeField, !agreeOk);
        if (!agreeOk) ok = false;

        return ok;
    };

    // снимаем ошибку при вводе
    form.querySelectorAll('input, select, textarea').forEach(el => {
        el.addEventListener('input', () => {
            const wrap = el.closest('.field, .checkbox');
            if (wrap) wrap.classList.remove('is-invalid');
            if (success) success.hidden = true;
        });
    });

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        if (!validate()) {
            const firstError = form.querySelector('.is-invalid');
            if (firstError) firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
            return;
        }
        // здесь можно отправить данные на сервер (fetch/AJAX)
        if (success) {
            success.hidden = false;
            success.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        form.reset();
    });
}

// ============ Год в подвале (если нужно динамически) ============
// document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
