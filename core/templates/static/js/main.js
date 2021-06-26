jQuery(document).ready(function ($) {
  //FIXED HEADER
  window.onscroll = function () {
    if (window.pageYOffset > 140) {
      $("#header-wrap").addClass("active");
    } else {
      $("#header-wrap").removeClass("active");
    }
  };

  //ISOTOPE
  let btns = $("#servicos .button-group button");

  btns.click(function (e) {
    $("#servicos .button-group button").removeClass("active");
    e.target.classList.add("active");

    let selector = $(e.target).attr("data-filter");
    $("#servicos .grid").isotope({
      filter: selector,
    });
  });

  $(window).on("load", function () {
    $("#servicos .grid").isotope({
      filter: "*",
    });
  });

  //MAGNIFY
  $(".grid .popup-link").magnificPopup({
    type: "image",
    gallery: {
      enabled: true,
      tPrev: "Anterioir",
      tNext: "Próxima",
      LCounter: "%curr% de %total%",
    },
  });

  //OWL
  $(".owl-carousel").owlCarousel({
    loop: true,
    margin: 30,
    autoplay: true,
    autoplayTimeout: 2000,
    dots: true,
    lazyload: true,
    nav: false,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 1,
      },
      1000: {
        items: 2,
      },
    },
  });
});
