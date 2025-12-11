const swiper = new Swiper('.myArticlesSwiper', {
  spaceBetween: 20,
  loop: true,
  grabCursor: true,

  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },

  breakpoints: {
    320: { slidesPerView: 1 },
    480: { slidesPerView: 2 },
    768: { slidesPerView: 3 },
    1024: { slidesPerView: 4 },
    1280: { slidesPerView: 6 },
  },
});


const swiper1 = new Swiper('.swiper1', {
  slidesPerView: 4,
  spaceBetween: 20,
  loop: true,

  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },

  breakpoints: {
    320: { slidesPerView: 1 },
    640: { slidesPerView: 2 },
    1024: { slidesPerView: 4 },
  },
});
