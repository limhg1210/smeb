// $.noConflict();

$(document).ready(function () {

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


  // Load Resize
  $(window).on("load resize", function (event) {
    var windowWidth = $(window).width();
    if (windowWidth < 1010) {
      $('body').addClass('small-device');
    } else {
      $('body').removeClass('small-device');
    }
  });


  // Logo Image
  $.ajax({
    url: '/api/layout/setting/1',
    success: function (data) {
      $("#logoImg").html('<img src="' + data['logo_img'] + '" alt="Logo">');
    }
  })
});

// global usage function
function linebreaksbr(string) {
  return string.replace(/(?:\r\n|\r|\n)/g, '<br>');
}

function datetimeString(string) {
  const days = ['일', '월', '화', '수', '목', '금', '토'];
  const datetime = new Date(string);
  const year = String(datetime.getFullYear());
  const month = String(('0' + (datetime.getMonth() + 1)).slice(-2));
  const date = String(('0' + (datetime.getDate())).slice(-2));
  const day = days[datetime.getDay()];
  const hour = String(('0' + (datetime.getHours())).slice(-2));
  const minute = String(('0' + (datetime.getMinutes())).slice(-2));
  return `${year}. ${month}. ${date}. (${day}) ${hour}:${minute}`
}

function todayInputString() {
  const today = new Date();
  const year = String(today.getFullYear());
  const month = String(('0' + (today.getMonth() + 1)).slice(-2));
  const date = String(('0' + (today.getDate())).slice(-2));
  return `${year}-${month}-${date}`
}

function appendSelect(selectId, getUrl, value, text) {
  $.ajax({
    url: getUrl,
    method: 'GET',
    success: function (data) {
      $('#' + selectId).append(`<option value="">------</option>`)
      for (let i = 0; i < data.results.length; i++) {
        $('#' + selectId).append(
          `<option value='${data.results[i][value]}'>${data.results[i][text]}</option>`
        )
      }
    }
  })
}