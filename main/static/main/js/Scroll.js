$(window).scroll(function() {
    if ($(window).scrollTop() > 650) {
        $('.header_travel nav').addClass("scroll");
        $('.top_scroll').css("display", "block");
    } else {
        $('.header_travel nav').removeClass("scroll");
        $('.top_scroll').css("display", "none");
    }
});

$(function(){
	$('#top_scroll_button').click(function(){
		$('html, body').animate({scrollTop: 0}, 600);
		return false;
	});
});

$(document).ready(function() {
   var margin = 100; // переменная для контроля докрутки
   $("a").click(function() { // тут пишите условия, для всех ссылок или для конкретных
      $("html, body").animate({
         scrollTop: $($(this).attr("href")).offset().top+margin+ "px" // .top+margin - ставьте минус, если хотите увеличить отступ
      }, {
         duration: 1300, // тут можно контролировать скорость
         easing: "swing"
      });
      return false;
   });
});