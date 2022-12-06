(function($) {
  
  "use strict";

  // Preloader
  function stylePreloader() {
    $('body').addClass('preloader-deactive');
  }

  // Background Image
  $('[data-bg-img]').each(function() {
    $(this).css('background-image', 'url(' + $(this).data("bg-img") + ')');
  });

  // Off Canvas JS
  var canvasWrapper = $(".off-canvas-wrapper");
  $(".btn-menu").on('click', function() {
    canvasWrapper.addClass('active');
    $("body").addClass('fix');
  });

  $(".close-action > .btn-close, .off-canvas-overlay").on('click', function() {
    canvasWrapper.removeClass('active');
    $(this).removeClass('fix');
  });


  
    /*---------------------------- 
        Sidebar Search Active
    -----------------------------*/
    function sidebarSearch() {
      var searchTrigger = $('.header-search-toggle'),
          endTriggersearch = $('button.search-close'),
          container = $('.main-search-active');

      searchTrigger.on('click', function() {
          container.addClass('inside');
      });

      endTriggersearch.on('click', function() {
          container.removeClass('inside');
      });

  };
  sidebarSearch();


  /*--------------------------------
        Swiper Slider Activation JS 
    ----------------------------------*/

    // Home 1 Slider
    var introSlider = new Swiper('.intro-slider', {
      loop: true,
      speed: 750,
      spaceBetween: 30,
      slidesPerView: 1,
      effect: 'fade',
      pagination: {
        el: '.home1-slider-pagination',
        clickable: true,
    }
  });


    var gallerySlider = new Swiper('.post-gallery', {
      slidesPerView : 1,
      speed: 1000,
      loop: true,
      spaceBetween : 10,
      autoplay: {
          delay: 2500,
          disableOnInteraction: true,
      },      
      pagination: {
        el: '.swiper-pagination',
        clickable: true
      },
      effect: 'fade',
      fadeEffect: { crossFade: true }
    });

    var brandLogoSlider = new Swiper('.brand-logo-slider-container', {
      slidesPerView : 5,
      loop: true,
      speed: 1000,
      spaceBetween : 30,
      autoplay: false,
      breakpoints: {
        1200:{
            slidesPerView : 5,
            spaceBetween : 100
        },

        992:{
            slidesPerView : 4,
            spaceBetween : 90
        },

        768:{
            slidesPerView : 3,
            spaceBetween : 110

        },

        576:{
            slidesPerView : 3,
            spaceBetween : 60
        },

        380:{
            slidesPerView : 3,
            spaceBetween : 30
        },

        0:{
            slidesPerView : 2,
            spaceBetween : 30
        }
      }
    });

  


    /* ----------------------------
        Portfolio Masonry Activation
    -------------------------------*/
    $(window).load(function () {
      $('.portfolio-default-area').imagesLoaded(function () {

          // filter items on button click
          $('.messonry-button, .blog-filter-menu').on('click', 'button', function () {
              var filterValue = $(this).attr('data-filter');
              $(this).siblings('.is-checked').removeClass('is-checked');
              $(this).addClass('is-checked');
              $grid.isotope({
                  filter: filterValue
              });
          });

          // init Isotope
          var $grid = $('.portfolio-list, .masonryGrid').isotope({
              percentPosition: true,
              transitionDuration: '0.7s',
              layoutMode: 'masonry',
              masonry: {
                  columnWidth: '.resizer',
              }
          });
      });
  })


  

  // Scroll Top Hide Show
  $(window).on('scroll', function(){
    if ($(this).scrollTop() > 250) {
      $('.scroll-to-top').fadeIn();
    } else {
      $('.scroll-to-top').fadeOut();
    }

    // Sticky Header
    if($('.sticky-header').length){
      var windowpos = $(this).scrollTop();
      if (windowpos >= 80) {
        $('.sticky-header').addClass('sticky');
      } else {
        $('.sticky-header').removeClass('sticky');
      }
    }

  });

  jQuery(document).ready(function($) {

    // Ajax Contact Form JS
    var form = $('#contact-form');
    var formMessages = $('.form-message');

    $(form).submit(function(e) {
        e.preventDefault();
        var formData = form.serialize();
        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: formData
        }).done(function(response) {
            // Make sure that the formMessages div has the 'success' class.
            $(formMessages).removeClass('alert alert-danger');
            $(formMessages).addClass('alert alert-success fade show');

            // Set the message text.
            formMessages.html("<button type='button' class='btn-close' data-bs-dismiss='alert'>&times;</button>");
            formMessages.append(response);

            // Clear the form.
            $('#contact-form input,#contact-form textarea').val('');
        }).fail(function(data) {
            // Make sure that the formMessages div has the 'error' class.
            $(formMessages).removeClass('alert alert-success');
            $(formMessages).addClass('alert alert-danger fade show');

            // Set the message text.
            if (data.responseText !== '') {
                formMessages.html("<button type='button' class='btn-close' data-bs-dismiss='alert'>&times;</button>");
                formMessages.append(data.responseText);
            } else {
                $(formMessages).text('Oops! An error occurred and your message could not be sent.');
            }
        });
    });
  
  });

  //Scroll To Top
  $('.scroll-to-top').on('click', function(){
    $('html, body').animate({scrollTop : 0},800);
    return false;
  });

  // Reveal Footer JS
  let revealId = $(".reveal-footer"),
    footerHeight = revealId.outerHeight(),
    windowWidth = $(window).width(),
    windowHeight = $(window).outerHeight();

  if (windowWidth > 991 && windowHeight > footerHeight) {
    $(".site-wrapper-reveal").css({
      'margin-bottom': footerHeight + 'px'
    });
  }

/*--
    Magnific Popup
-----------------------------------*/
  $('.gallery-popup').magnificPopup({
    type: 'image',
    gallery: {
        enabled: true,
    },
  });

  //Video Popup
  $('.play-video-popup').magnificPopup({
      type: 'iframe',
  });
  
  
/* ==========================================================================
   When document is loading, do
   ========================================================================== */
  
  $(window).on('load', function() {
    stylePreloader();
  });

  /* ----------------------------
      AOS Scroll Animation 
  -------------------------------*/
  $(window).on('scroll', function(){
    AOS.init({
            offset: 80,
            duration: 1000,
            once: true,
            easing: 'ease',
        });
    });
    
    AOS.init({
        offset: 80,
        duration: 1000,
        once: true,
        easing: 'ease',
    });

  
  

/* ==========================================================================
   When Window is resizing, do
   ========================================================================== */
  
  $(window).on('resize', function() {
  });
  

})(window.jQuery);