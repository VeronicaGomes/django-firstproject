$(window).scroll(function(){
    $('nav').toggleClass('scrolled', $(this).scrollTop() > 700);
    });

$(".slider").owlCarousel({
        loop: true,
        autoplay: true,
        autoplayTimeout: 2000, //2000ms = 2s;
        autoplayHoverPause: true,
      });


$('.date').datetimepicker({
	timepicker: false,
	datepicker: true,
	format:'Y-m-d',
	value:'2020-9-13',
	weeks:true
});


$('.has-dropdown').mouseenter(function(){

	var $this = $(this);
	$this
		.find('.dropdown')
		.css('display', 'block')
		.addClass('animated-fast fadeInUpMenu');

}).mouseleave(function(){
	var $this = $(this);

	$this
		.find('.dropdown')
		.css('display', 'none')
		.removeClass('animated-fast fadeInUpMenu');
});




/*$("#datepicker").datetimepicker({
	timepicker:false,
	datepicker:true,
	format: 'Y-m-d',
	value:'2020-9-12',
	weeks:true
});	*/

