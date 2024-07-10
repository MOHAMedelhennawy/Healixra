function hidePopup() {
    popup = document.querySelector('.flash').style.visibility="hidden";
}

setTimeout("hidePopup()", 3000)

$(document).ready(function(){
    $(".owl-carousel").owlCarousel({
      // your options here
      items: 4,
      loop: true,
      nav: true ,
      dots: true,
      autoplay: true,
      autoplayTimeout: 5000,
      smartSpeed: 4000,
    });
  });
  