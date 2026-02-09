// static/js/divergence.js

class DivergenceMeter {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        if (!this.container) return;
        this.digits = this.container.querySelectorAll('.nixie-digit');
        this.isAnimating = false;
    }

    setValue(value) {
        const cleanValue = value.replace(/[^0-9]/g, '');
        this.digits.forEach((el, i) => {
            if (cleanValue[i]) el.innerText = cleanValue[i];
        });
    }

    animate(targetValue, duration = 800, callback = null) {
        if (this.isAnimating) return;
        this.isAnimating = true;

        const startTime = Date.now();
        const cleanTarget = targetValue.replace(/[^0-9]/g, '');

        const interval = setInterval(() => {
            const now = Date.now();

            this.digits.forEach(el => {
                el.innerText = Math.floor(Math.random() * 10);
                if (Math.random() > 0.8) el.classList.add('flicker');
                else el.classList.remove('flicker');
            });

            if (now - startTime >= duration) {
                clearInterval(interval);
                this.setValue(targetValue);
                this.digits.forEach(el => el.classList.remove('flicker'));
                this.isAnimating = false;
                if (callback) callback();
            }
        }, 40);
    }
}
