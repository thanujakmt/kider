

const swiper = new Swiper(".swiper",{
    slidesPerView:2,
    loop:true,
    autoplay:{
      delay:5000,
    },
    navigation:{
      nextEl: ".next",
      prevEl: ".prev",
    },  
    
  })