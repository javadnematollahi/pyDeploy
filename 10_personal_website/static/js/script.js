(function($) {
	
	"use strict";
	
	//Hide Loading Box (Preloader)
	function handlePreloader() {
		if($('.preloader').length){
			$('.preloader').delay(500).fadeOut(500);
		}
	}
	
	//Update Header Style and Scroll to Top
	function headerStyle() {
		if($('.main-header').length){
			var windowpos = $(window).scrollTop();
			var siteHeader = $('.main-header');
			//var scrollLink = $('.scroll-to-top');
			if (windowpos >= 60) {
				siteHeader.addClass('fixed-header');
				//scrollLink.fadeIn(300);
			} else {
				siteHeader.removeClass('fixed-header');
				//scrollLink.fadeOut(300);
			}
		}
	}
	
	headerStyle();
	
	//Open Main Menu
	if($('.main-header-bar .nav-toggler .toggler-btn').length){
		$('.main-header-bar .nav-toggler .toggler-btn').on('click', function(e) {
			e.preventDefault();
			$(this).toggleClass('active');
			$('.main-nav-outer').toggleClass('now-visible');
		});
	}
	
	//Main Menu Dropdown Toggle
	if($('.main-nav-box .navigation > li.dropdown > ul').length){
		
		//Show Submenu
		$('.main-nav-box .navigation > li.dropdown > a').on('click', function(e) {
			e.preventDefault();
			$(this).parent('li').addClass('open');
			$(this).parents('.navigation').addClass('subnav-visible');
		});
		
		//Hide Submenu
		$('.main-nav-box .navigation li > a[href="#menu-back"]').on('click', function(e) {
			e.preventDefault();
			$(this).parents('.navigation').removeClass('subnav-visible');
			$(this).parents('li').removeClass('open');
		});
		
	}
	
	//Submenu Dropdown Toggle
	if($('.header-style-two li.dropdown ul').length){
		$('.header-style-two li.dropdown').append('<div class="dropdown-btn"><span class="fa fa-angle-down"></span></div>');
		
		//Dropdown Button
		$('.header-style-two li.dropdown .dropdown-btn').on('click', function() {
			$(this).prev('ul').slideToggle(500);
		});
		
		//Disable dropdown parent link
		$('.header-style-two .navigation li.dropdown > a,.hidden-bar .side-menu li.dropdown > a').on('click', function(e) {
			e.preventDefault();
		});
	}
	
	//Hidden Bar Menu Config
	function hiddenBarMenuConfig() {
		var menuWrap = $('.hidden-bar .side-menu');
		// hidding submenu 
		menuWrap.find('.dropdown').children('ul').hide();
		// toggling child ul
		menuWrap.find('li.dropdown > a').each(function () {
			$(this).on('click', function (e) {
				e.preventDefault();
				$(this).parent('li.dropdown').children('ul').slideToggle();
	
				// adding class to item container
				$(this).parent().toggleClass('open');
	
				return false;
	
			});
		});
	}
	
	hiddenBarMenuConfig();
	
	//Hidden Sidebar
	if ($('.hidden-bar').length) {
		var hiddenBar = $('.hidden-bar');
		var hiddenBarOpener = $('.hidden-bar-opener');
		var hiddenBarCloser = $('.hidden-bar-closer');
		$('.hidden-bar-wrapper').mCustomScrollbar();
		
		//Show Sidebar
		hiddenBarOpener.on('click', function () {
			hiddenBar.addClass('visible-sidebar');
		});
		
		//Hide Sidebar
		hiddenBarCloser.on('click', function () {
			hiddenBar.removeClass('visible-sidebar');
		});
		
	}
	
	//Add One Page nav
	if($('.scroll-nav').length) {
		$('.scroll-nav').onePageNav();
	}
	
	//Update Fixed Nav Position
	function fixedNavStyle() {
		if($('.fixed-top-bar').length){
			var windowHeight = $(window).height();
			var windowpos = $(window).scrollTop();
			var fixedBar = $('.fixed-top-bar');
			if (windowpos >= windowHeight) {
				$('body').addClass('banner-height-reached');
				fixedBar.addClass('now-fixed');
			} else {
				$('body').removeClass('banner-height-reached');
				fixedBar.removeClass('now-fixed');
			}
		}
	}
	
	fixedNavStyle();
	
	//Hide Bootstrap Menu On Click over Mobile View
	$('.scroll-nav li a').on('click', function(){
		var windowWidth = $(window).width();
		if (windowWidth <= 767) {
			$('.nav-outer .navbar-toggle').trigger( "click" );
		}
	});
	
	
	//Adjust Banner Height
	function adjustBanner() {
		if($('.fullscreen-banner').length){
			var bannerHeight = $('.fullscreen-banner').height();
			var contentHeight = $('.fullscreen-banner .content-inner').innerHeight();
			var windowHeight = $(window).height();
			
			if (bannerHeight < windowHeight) {
				$('.fullscreen-banner').css('height',windowHeight);
			}else{
				$('.fullscreen-banner').css('height',contentHeight);	
			}
		}
	}
	
	adjustBanner();
	
	//Adjust Banner Slider Height
	function adjustBannerSlider() {
		if($('.overlay-slider-box').length){
			var windowHeight = $(window).height();
			
			$('.overlay-slider-box').css('height',windowHeight);
			
			if (windowHeight < 400) {
				$('.overlay-slider-box').css('height',400);	
			}
		}
	}
	
	adjustBannerSlider();
	
	//Banner Overlay Slider
	if($('.home-banner .overlay-slider').length){
		$(".home-banner .overlay-slider").bxSlider({
			adaptiveHeight: true,
			infiniteLoop: true,
			auto:true,
			controls: true,
			pause: 5000,
			speed: 1000,
			mode:'fade',
			pager:false,
			nextText: '<span class="fa fa-angle-right"></span>',
			prevText: '<span class="fa fa-angle-left"></span>'
		});
	}
	
	
	//Fact Counter + Text Count
	if($('.count-box').length){
		$('.count-box').appear(function(){
	
			var $t = $(this),
				n = $t.find(".count-text").attr("data-stop"),
				r = parseInt($t.find(".count-text").attr("data-speed"), 10);
				
			if (!$t.hasClass("counted")) {
				$t.addClass("counted");
				$({
					countNum: $t.find(".count-text").text()
				}).animate({
					countNum: n
				}, {
					duration: r,
					easing: "linear",
					step: function() {
						$t.find(".count-text").text(Math.floor(this.countNum));
					},
					complete: function() {
						$t.find(".count-text").text(this.countNum);
					}
				});
			}
			
		},{accY: 0});
	}
	
	
	//Jquery Knob animation 
	if($('.dial').length){
		$('.dial').appear(function(){
          var elm = $(this);
          var color = elm.attr('data-fgColor');  
          var perc = elm.attr('value');  
 
          elm.knob({ 
               'value': 0, 
                'min':0,
                'max':100,
                'skin':'tron',
                'readOnly':true,
                'thickness':0.05,
				'dynamicDraw': true,
				'displayInput':false
          });

          $({value: 0}).animate({ value: perc }, {
			  duration: 2000,
              easing: 'swing',
              progress: function () { elm.val(Math.ceil(this.value)).trigger('change');
              }
          });

          //circular progress bar color
          $(this).append(function() {
             // elm.parent().parent().find('.circular-bar-content').css('color',color);
              //elm.parent().parent().find('.circular-bar-content .txt').text(perc);
          });

          },{accY: 20});
    }
	
	
	//Progress Bar
	if($('.progress-line').length){
		$('.progress-line').appear(function(){
			var el = $(this);
			var percent = el.data('width');
			$(el).css('width',percent+'%');
		},{accY: 0});
	}
	
	
	//Gallery With Filters
	if($('.filter-list').length){
		$('.filter-list').mixItUp({});
	}
	
	//Single Item Carousel
	if ($('.single-item-carousel').length) {
		$('.single-item-carousel').owlCarousel({
			loop:true,
			margin:10,
			nav:true,
			smartSpeed: 1000,
			autoplay: 5000,
			navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
			responsive:{
				0:{
					items:1
				},
				600:{
					items:1
				},
				1200:{
					items:1
				}
			}
		});    		
	}
	
	//Client Testimonial Carousel
	if ($('.client-testimonial-carousel').length && $('.client-thumbs-carousel').length) {

		var $sync3 = $(".client-testimonial-carousel"),
			$sync4 = $(".client-thumbs-carousel"),
			flag = false,
			duration = 500;

			$sync3
				.owlCarousel({
					loop:true,
					items: 1,
					margin: 0,
					nav: true,
					navText: [ '<span class="fa fa-long-arrow-left"></span>', '<span class="fa fa-long-arrow-right"></span>' ],
					dots: true,
					autoplay: true,
					autoplayTimeout: 5000
				})
				.on('changed.owl.carousel', function (e) {
					if (!flag) {
						flag = false;
						$sync4.trigger('to.owl.carousel', [e.item.index, duration, true]);
						flag = false;
					}
				});

			$sync4
				.owlCarousel({
					loop:true,
					margin:20,
					items: 1,
					nav: false,
					navText: [ '<span class="fa fa-long-arrow-left"></span>', '<span class="fa fa-long-arrow-right"></span>' ],
					dots: false,
					center: false,
					autoplay: true,
					autoplayTimeout: 5000,
					responsive: {
						0:{
				            items:1,
				            autoWidth: false
				        },
				        400:{
				            items:1,
				            autoWidth: false
				        },
				        600:{
				            items:1,
				            autoWidth: false
				        },
				        1000:{
				            items:1,
				            autoWidth: false
				        },
						1200:{
				            items:1,
				            autoWidth: false
				        }
				    },
				})
				
		.on('click', '.owl-item', function () {
			$sync3.trigger('to.owl.carousel', [$(this).index(), duration, true]);
		})
		.on('changed.owl.carousel', function (e) {
			if (!flag) {
				flag = true;		
				$sync3.trigger('to.owl.carousel', [e.item.index, duration, true]);
				flag = false;
			}
		});
	}
	
	
	// Sponsors Carousel
	if ($('.sponsors-carousel-one').length) {
		$('.sponsors-carousel-one').owlCarousel({
			loop:true,
			margin:30,
			nav:true,
			smartSpeed: 500,
			autoplay: 4000,
			navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
			responsive:{
				0:{
					items:1
				},
				480:{
					items:2
				},
				600:{
					items:3
				},
				1024:{
					items:3
				},
				1200:{
					items:4
				},
				1440:{
					items:5
				}
			}
		});    		
	}
	
	//Sortable Masonary with Filters
	function enableMasonry() {
		if($('.masonry-gallery .items-container').length){

			var winDow = $(window);
			// Needed variables
			var $container=$('.masonry-gallery .items-container');
			var $filter=$('.filter-btns');

			$container.isotope({
				filter:'*',
				 masonry: {
					columnWidth : '.masonry-item.small-item'
				 },
				animationOptions:{
					duration:500,
					easing:'linear'
				}
			});


			// Isotope Filter
			$filter.find('li').on('click', function(){
				var selector = $(this).attr('data-filter');

				try {
					$container.isotope({
						filter	: selector,
						animationOptions: {
							duration: 500,
							easing	: 'linear',
							queue	: false
						}
					});
				} catch(err) {

				}
				return false;
			});


			winDow.on('resize', function(){
				var selector = $filter.find('li.active').attr('data-filter');

				$container.isotope({
					filter	: selector,
					animationOptions: {
						duration: 500,
						easing	: 'linear',
						queue	: false
					}
				});
			});


			var filterItemA	= $('.filter-btns li');

			filterItemA.on('click', function(){
				var $this = $(this);
				if ( !$this.hasClass('active')) {
					filterItemA.removeClass('active');
					$this.addClass('active');
				}
			});
		}
	}

	enableMasonry();
	
	
	//Custom Seclect Box
	if($('.custom-select-box').length){
		$('.custom-select-box').selectmenu().selectmenu('menuWidget').addClass('overflow');
	}
	
	
	//LightBox / Fancybox
	if($('.lightbox-image').length) {
		$('.lightbox-image').fancybox({
			openEffect  : 'fade',
			closeEffect : 'fade',
			helpers : {
				media : {}
			}
		});
	}
	
	//Contact Form Validation
	if($('#contact-form').length){
		$('#contact-form').validate({
			rules: {
				username: {
					required: true
				},
				email: {
					required: true,
					email: true
				},
				subject: {
					required: true
				},
				message: {
					required: true
				}
			}
		});
	}
	
	// Scroll to a Specific Div
	if($('.scroll-to-target').length){
		$(".scroll-to-target").on('click', function() {
			var target = $(this).attr('data-target');
		   // animate
		   $('html, body').animate({
			   scrollTop: $(target).offset().top
			 }, 1000);
	
		});
	}
	
	// Elements Animation
	if($('.wow').length){
		var wow = new WOW(
		  {
			boxClass:     'wow',      // animated element css class (default is wow)
			animateClass: 'animated', // animation css class (default is animated)
			offset:       0,          // distance to the element when triggering the animation (default is 0)
			mobile:       false,       // trigger animations on mobile devices (default is true)
			live:         true       // act on asynchronously loaded content (default is true)
		  }
		);
		wow.init();
	}

/* ==========================================================================
   When document is Scrollig, do
   ========================================================================== */
	
	$(window).on('scroll', function() {
		headerStyle();
		fixedNavStyle();
	});
	
/* ==========================================================================
   When Window is Resized, do
   ========================================================================== */
	
	$(window).on('resize', function() {
		adjustBanner();
		adjustBannerSlider();
	});	
		
/* ==========================================================================
   When document is loaded, do
   ========================================================================== */
	
	$(window).on('load', function() {
		handlePreloader();
		fixedNavStyle();
		enableMasonry();
		adjustBanner();
		adjustBannerSlider();
	});	

})(window.jQuery);