const circulo = document.getElementById('revolving_circle');
    const botoes = document.querySelectorAll('.botao');

    botoes.forEach(botao => {
        botao.addEventListener('mouseenter', () => {
            const rcRect = circulo.getBoundingClientRect();
            const btRect = botao.getBoundingClientRect();

            const rcCentroX = rcRect.left + rcRect.width / 2;
            const rcCentroY = rcRect.top + rcRect.height / 2;

            const btCentroX = btRect.left + btRect.width / 2;
            const btCentroY = btRect.top + btRect.height / 2;

            const angulo = Math.atan2(
                btCentroY - rcCentroY,
                btCentroX - rcCentroX
            ) * (180 / Math.PI) + 90;

            circulo.style.transition = 'transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)';
            circulo.style.transform = `translateY(-50%) rotate(${angulo}deg)`;
        });
    });