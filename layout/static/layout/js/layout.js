$.noConflict();

jQuery(document).ready(function ($) {

  "use strict";

  [].slice.call(document.querySelectorAll('select.cs-select')).forEach(function (el) {
    new SelectFx(el);
  });

  jQuery('.selectpicker').selectpicker;


  $('.search-trigger').on('click', function (event) {
    event.preventDefault();
    event.stopPropagation();
    $('.search-trigger').parent('.header-left').addClass('open');
    $('#global-search').focus();
  });

  $('.search-close').on('click', function (event) {
    event.preventDefault();
    event.stopPropagation();
    $('.search-trigger').parent('.header-left').removeClass('open');
    $('#global-search').val('');
  });

  $('.equal-height').matchHeight({
    property: 'max-height'
  });


  // Counter Number
  $('.count').each(function () {
    $(this).prop('Counter', 0).animate({
      Counter: $(this).text()
    }, {
      duration: 3000,
      easing: 'swing',
      step: function (now) {
        $(this).text(Math.ceil(now));
      }
    });
  });


  // Menu Trigger
  $('#menuToggle').on('click', function (event) {
    var windowWidth = $(window).width();
    if (windowWidth < 1010) {
      $('body').removeClass('open');
      if (windowWidth < 760) {
        $('#left-panel').slideToggle(200, 'swing', function () {
          if ($('#left-panel').css('display') === 'none') {
            $('#left-panel').css('display', '')
          }
        });
      } else {
        $('#left-panel').toggleClass('open-menu');
      }
    } else {
      $('body').toggleClass('open');
      $('#left-panel').removeClass('open-menu');
    }
  });


  $(".menu-item-has-children.dropdown").each(function () {
    $(this).on('click', function () {
      var $temp_text = $(this).children('.dropdown-toggle').html();
      $(this).children('.sub-menu').prepend('<li class="subtitle">' + $temp_text + '</li>');
    });
  });


  // Logo Image
  $.ajax({
    url: '/api/layout/setting/1',
    success: function (data) {
      $("#logoImg").html('<img src="' + data['logo_img'] + '" alt="Logo">');
    }
  })


  // Load Resize
  $(window).on("load resize", function (event) {
    var windowWidth = $(window).width();
    if (windowWidth < 1010) {
      $('body').addClass('small-device');
    } else {
      $('body').removeClass('small-device');
    }

  });


});