
// função para girar o slide

function changeSlide(radios) {
    let currentIndex = 2; // Começa no item 3 (índice 2)

    return () => {
        radios[currentIndex].checked = true;
        currentIndex = (currentIndex + 1) % radios.length;
    };
}

// encapsulando os slides
const radiosParceiros = document.querySelectorAll('input[name="slider"]');
const radiosCarouselTcexp = document.querySelectorAll('input[name="slider-carousel-tcexp"]');

// encapsulando cada função, para ficar mais organizado
const changeSlideParceiros = changeSlide(radiosParceiros);
const changeSlideCarouselTcexp = changeSlide(radiosCarouselTcexp);


function startCarousel(interval, changeSlideFunction) {
    return setInterval(changeSlideFunction, interval * 1000);
}

// intervalo em segundos
const intervalParceirosInSeconds = 3;
const intervalCarouselTcexpInSeconds = 5;

let intervalParceiros = startCarousel(intervalParceirosInSeconds, changeSlideParceiros);
let intervalCarouselTcexp = startCarousel(intervalCarouselTcexpInSeconds, changeSlideCarouselTcexp);

const containerParceiros = document.querySelector('.container-parceiros');
containerParceiros.addEventListener('mouseenter', () => {
    clearInterval(intervalParceiros);
});

containerParceiros.addEventListener('mouseleave', () => {
    intervalParceiros = startCarousel(intervalParceirosInSeconds, changeSlideParceiros);
});

const containerCarouselTcexp = document.querySelector('.container-carousel-tcexp');
containerCarouselTcexp.addEventListener('mouseenter', () => {
    clearInterval(intervalCarouselTcexp);
});

containerCarouselTcexp.addEventListener('mouseleave', () => {
    intervalCarouselTcexp = startCarousel(intervalCarouselTcexpInSeconds, changeSlideCarouselTcexp);
});
