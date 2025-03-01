

(function($) {


	// add spinner when submit a form 
	document.getElementById("contact").addEventListener("submit", function(event) {
		var submitBtn = document.getElementById("submitBtn");
		var btnText = document.getElementById("btnText");
		var spinner = document.getElementById("spinner");
	
		// Hide text and show spinner
		btnText.classList.add("d-none");
		spinner.classList.remove("d-none");
	
		// Disable button to prevent multiple submissions
		submitBtn.disabled = true;
	
	
	});
	// Mean Menu
	$('.mean-menu').meanmenu({
		meanScreenWidth: "992"
	});
	
	// Sticky, Go To Top JS
	$(window).on('scroll', function() {
		// Header Sticky JS
		if ($(this).scrollTop() >150){  
			$('.navbar-area').addClass("is-sticky");
		}
		else{
			$('.navbar-area').removeClass("is-sticky");
		};
	});

	// aos 
	AOS.init({
		disable: function() {
			var maxWidth = 992;
			return window.innerWidth < maxWidth;
		}
	});

	// FAQ Accordion JS
	$('.accordion').find('.accordion-title').on('click', function(){
		// Adds Active Class
		$(this).toggleClass('active');
		// Expand or Collapse This Panel
		$(this).next().slideToggle('fast');
		// Hide The Other Panels
		$('.accordion-content').not($(this).next()).slideUp('fast');
		// Removes Active Class form Other Titles
		$('.accordion-title').not($(this)).removeClass('active');		
	});

	// popup youtube 
	$('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({ 
		disableOn: 100,
		type: 'iframe',
		mainClass: 'mfp-fade',
		removalDelay: 160,
		preloader: false,

		fixedContentPos: false
	}); 

	// Partners Logo Slider
	$('.partners-logo-slider').owlCarousel({
		loop:true,
		margin:30, 
		nav:false,
		dots:false,
		smartSpeed: 1000,
		autoplay: true,
		autoplayHoverPause: true,  
		responsive: {
			0:{
				items:2
			},
			600:{
				items:4
			}, 
			1000:{
				items:6
			} 
		} 
    }); 
	// Banner Two Slider
	$('.banner-two-slider').owlCarousel({
		loop:true,
		margin:30, 
		nav:false,
		dots:true,
		smartSpeed: 1000,
		autoplay: true,
		autoplayHoverPause: true,  
		responsive: {
			0:{
				items:1
			},
			600:{
				items:1
			}, 
			1000:{
				items:1
			} 
		} 
    }); 
	// Testimonials Two Slider
	$('.testimonials-two-slider').owlCarousel({
		loop:true,
		margin:30, 
		nav:true,
		dots:false,
		smartSpeed: 1000,
		autoplay: true,
		autoplayHoverPause: true,  
		navText: [
            '<i class="flaticon-left"></i>',  
            '<i class="flaticon-next"></i>',  
        ],   
		responsive: {
			0:{
				items:1
			},
			600:{
				items:1
			}, 
			992:{
				items:2
			},
			1000:{
				items:2
			} 
		} 
    }); 
	// Corporate-website-slider
	$('.corporate-website-slider').owlCarousel({
		loop:true,
		margin:30, 
		nav:true,
		dots:false,
		smartSpeed: 1000,
		autoplay: true,
		autoplayHoverPause: true,  
		navText: [
            '<i class="flaticon-left"></i>',  
            '<i class="flaticon-next"></i>',  
        ],   
		responsive: {
			0:{
				items:1
			},
			600:{
				items:1
			}, 
			750:{
				items:2
			},
			992:{
				items:3
			},
			1000:{
				items:3
			} 
		} 
    }); 

	//partners-logo-slider 
	$('.partners-logo-slider').owlCarousel({
		loop:true,
		margin:30, 
		nav:false,
		dots:false,
		smartSpeed: 1000,
		autoplay: true,
		autoplayHoverPause: true,  
		responsive:{
			0:{
				items:2
			},
			570:{
				items:3
			}, 
			600:{
				items:3
			}, 
			1000:{
				items:6
			} 
		} 
	});  
	// Portfolios Three Slider
	$('.portfolios-three-slider').owlCarousel({
		loop:true,
		margin:30, 
		nav:true,
		dots:false,
		smartSpeed: 1000,
		autoplay: true,
		autoplayHoverPause: true,  
		navText: [
            '<i class="flaticon-left"></i>',  
            '<i class="flaticon-next"></i>',  
        ],
		responsive:{
			0:{
				items:1
			},
			570:{
				items:1
			}, 
			600:{
				items:2
			}, 
			1000:{
				items:3
			} 
		} 
	});  

	//services slider
	$('.services-slider').owlCarousel({
		loop:true,
		margin:20, 
		nav:true,
		dots:false,
		smartSpeed: 1000,
		autoplay: true,
		autoplayHoverPause: true,  
		navText: [
            '<i class="flaticon-left"></i>',  
            '<i class="flaticon-next"></i>',  
        ],   
		responsive:{
			0:{
				items:1
			},
			500:{
				items:1
			}, 
			768:{
				items:2
			},
			992:{
				items:3
			},
			1024:{
				items:3 
			},
			1200:{
				items:4
			}, 
		} 
    });  

	// Portfolios Slider
	$('.portfolios-slider').owlCarousel({
		loop:true,
		margin:20, 
		nav:true,
		dots:false,
		smartSpeed: 1000,
		autoplay: true,
		autoplayHoverPause: true,  
		navText: [
            '<i class="flaticon-left"></i>',  
            '<i class="flaticon-next"></i>',  
        ],   
		responsive:{
			0:{
				items:1
			},
			500:{
				items:1
			}, 
			768:{
				items:2
			},
			992:{
				items:3
			},
			1024:{
				items:3 
			},
			1200:{
				items:4
			}, 
		} 
    });  
	// Our Best Services Slider
	$('.our-best-services-slider').owlCarousel({
		loop:true,
		margin:20, 
		nav:true,
		dots:false,
		smartSpeed: 1000,
		autoplay: true,
		autoplayHoverPause: true,  
		navText: [
            '<i class="flaticon-left"></i>',  
            '<i class="flaticon-next"></i>',  
        ],   
		responsive:{
			0:{
				items:1
			},
			500:{
				items:1
			}, 
			768:{
				items:2
			},
			992:{
				items:3
			},
			1024:{
				items:3 
			},
			1200:{
				items:3
			}, 
		} 
    });  

	// Testimoalis Slider
	$('.testimonials-slider').owlCarousel({
		loop:true,
		margin:20, 
		nav:true,
		dots:false,
		smartSpeed: 1000,
		autoplay: true,
		autoplayHoverPause: true,  
		navText: [
            '<i class="flaticon-left"></i>',  
            '<i class="flaticon-next"></i>',  
        ],   
		responsive:{
			0:{
				items:1
			},
			500:{
				items:1
			}, 
			768:{
				items:1
			},
			992:{
				items:1
			},
			1024:{
				items:1 
			},
			1200:{
				items:1
			}, 
		} 
    });  

	// Go to Top
	$(function(){
		// Scroll Event
		$(window).on('scroll', function(){
			var scrolled = $(window).scrollTop();
			if (scrolled > 600) $('.go-top').addClass('active');
			if (scrolled < 600) $('.go-top').removeClass('active');
		});  
		// Click Event
		$('.go-top').on('click', function() {
			$("html, body").animate({ scrollTop: "0" },  500);
		});
	}); 

	// Go to Top JS
	// Scroll Event
	$(window).on('scroll', function(){
		var scrolled = $(window).scrollTop();
		if (scrolled > 300) $('.go-top').addClass('active');
		if (scrolled < 300) $('.go-top').removeClass('active');
	});  

	// Click Event JS
	$('.go-top').on('click', function() {
		$("html, body").animate({ scrollTop: "0" },  500);
	}); 

	// Odometer JS 
	$('.odometer').appear(function(e) {
		var odo = $(".odometer");
		odo.each(function() {
			var countNumber = $(this).attr("data-count");
			$(this).html(countNumber);
		});
	});   

	// Count Time JS
	function makeTimer() {
		var endTime = new Date("november  30, 2022 17:00:00 PDT");			
		var endTime = (Date.parse(endTime)) / 1000;
		var now = new Date();
		var now = (Date.parse(now) / 1000);
		var timeLeft = endTime - now;
		var days = Math.floor(timeLeft / 86400); 
		var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
		var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600 )) / 60);
		var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));
		if (hours < "10") { hours = "0" + hours; }
		if (minutes < "10") { minutes = "0" + minutes; }
		if (seconds < "10") { seconds = "0" + seconds; }
		$("#days").html(days + "<span>Days</span>");
		$("#hours").html(hours + "<span>Hours</span>");
		$("#minutes").html(minutes + "<span>Minutes</span>");
		$("#seconds").html(seconds + "<span>Seconds</span>");
	}
	setInterval(function() { makeTimer(); }, 300);

	// Subscribe form JS
	$(".newsletter-form").validator().on("submit", function (event) {
		if (event.isDefaultPrevented()) {
		// handle the invalid form...
			formErrorSub();
			submitMSGSub(false, "Please enter your email correctly.");
		} else {
			// everything looks good!
			event.preventDefault();
		}
	});
	function callbackFunction (resp) {
		if (resp.result === "success") {
			formSuccessSub();
		}
		else {
			formErrorSub();
		}
	}
	function formSuccessSub(){
		$(".newsletter-form")[0].reset();
		submitMSGSub(true, "Thank you for subscribing!");
		setTimeout(function() {
			$("#validator-newsletter, #validator-newsletter-2").addClass('hide');
		}, 4000)
	}
	function formErrorSub(){
		$(".newsletter-form").addClass("animated shake");
		setTimeout(function() {
			$(".newsletter-form").removeClass("animated shake");
		}, 1000)
	}
	function submitMSGSub(valid, msg){
		if(valid){
			var msgClasses = "validation-success";
		} else {
			var msgClasses = "validation-danger";
		}
		$("#validator-newsletter, #validator-newsletter-2").removeClass().addClass(msgClasses).text(msg);
	}

	// AJAX MailChimp JS
	$(".newsletter-form").ajaxChimp({
		url: "https://Envy Theme.us20.list-manage.com/subscribe/post?u=60e1ffe2e8a68ce1204cd39a5&amp;id=42d6d188d9",
		callback: callbackFunction
	});

	// Language Switcher
	$(".language-option").each(function() {
		var each = $(this)
		each.find(".lang-name").html(each.find(".language-dropdown-menu a:nth-child(1)").text());
		var allOptions = $(".language-dropdown-menu").children('a');
		each.find(".language-dropdown-menu").on("click", "a", function() {
			allOptions.removeClass('selected');
			$(this).addClass('selected');
			$(this).closest(".language-option").find(".lang-name").html($(this).text());
		});
	})

    // Others Option For Responsive JS
	$(".others-option-for-responsive .dot-menu").on("click", function(){
		$(".others-option-for-responsive .container .container").toggleClass("active");
	});

	// Preloader JS
	jQuery(window).on('load',function(){
		jQuery(".preloader").fadeOut(500);
	});

	// Switch Btn
	$('body').append("<div class='switch-box'><label id='switch' class='switch'><input type='checkbox' onchange='toggleTheme()' id='slider'><span class='slider round'></span></label></div>");

})(jQuery);


// function to set a given theme/color-scheme
function setTheme(themeName) {
    localStorage.setItem('pixab_theme', themeName);
    document.documentElement.className = themeName;
}

