/* ==========================================================================
   jQuery plugin settings and other scripts
   ========================================================================== */

$(document).ready(function(){
  // The page layout keeps the footer at the bottom through CSS flexbox.
  // FitVids init
  $("#main").fitVids();

  // init sticky sidebar
  $(".sticky").Stickyfill();

  var stickySideBar = function(){
    // Adjust if the follow button is shown based upon screen size
    var width = $(window).width();
    var $authorButton = $(".author__urls-wrapper button");
    var show = $authorButton.length === 0 ? width >= 925 : !$authorButton.is(":visible");

    // Don't show the follow button if there is no content for it
    var count = $('.author__urls.social-icons li').length - $('li[class="author__desktop"]').length;
    if (!show && count === 0) {
      $authorButton.hide();
      show = false;
    }

    if (show) {
      // fix
      Stickyfill.rebuild();
      Stickyfill.init();
      $(".author__urls").show();
      $authorButton.attr("aria-expanded", "true");
    } else {
      // unfix
      Stickyfill.stop();
      $(".author__urls").hide();
      $authorButton.removeClass("open").attr("aria-expanded", "false");
    }
  };

  stickySideBar();

  $(window).resize(function(){
    stickySideBar();
  });

  // Follow menu drop down
  $(".author__urls-wrapper button").on("click", function() {
    var isOpen = $(this).attr("aria-expanded") === "true";
    $(".author__urls").stop(true, true).fadeToggle("fast");
    $(this).toggleClass("open", !isOpen).attr("aria-expanded", String(!isOpen));
  });

  // Keep the navigation disclosure state available to keyboard and screen readers.
  var syncNavigationState = function() {
    var isOpen = !$("#site-nav .hidden-links").hasClass("hidden");
    $("#site-nav button").attr("aria-expanded", String(isOpen)).toggleClass("close", isOpen);
  };
  $("#site-nav button").on("click", syncNavigationState);
  $(window).on("resize", syncNavigationState);
  syncNavigationState();

  $(document).on("keydown", function(event) {
    if (event.key !== "Escape") return;
    if ($("#site-nav button").attr("aria-expanded") === "true") {
      $("#site-nav .hidden-links").addClass("hidden");
      syncNavigationState();
      $("#site-nav button").trigger("focus");
    }
    if ($(".author__urls-wrapper button").is(":visible") && $(".author__urls-wrapper button").attr("aria-expanded") === "true") {
      $(".author__urls").stop(true, true).hide();
      $(".author__urls-wrapper button").removeClass("open").attr("aria-expanded", "false").trigger("focus");
    }
  });

  // init smooth scroll, this needs to be slightly more than then fixed masthead height
  $("a").smoothScroll({offset: -65});

  // add lightbox class to all image links
  $("a[href$='.jpg'],a[href$='.jpeg'],a[href$='.JPG'],a[href$='.png'],a[href$='.gif']").addClass("image-popup");

  // Magnific-Popup options
  $(".image-popup").magnificPopup({
    type: 'image',
    tLoading: 'Loading image #%curr%...',
    gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0,1] // Will preload 0 - before current, and 1 after the current image
    },
    image: {
      tError: '<a href="%url%">Image #%curr%</a> could not be loaded.',
    },
    removalDelay: 500, // Delay in milliseconds before popup is removed
    // Class that is added to body when popup is open.
    // make it unique to apply your CSS animations just to this exact popup
    mainClass: 'mfp-zoom-in',
    callbacks: {
      beforeOpen: function() {
        // just a hack that adds mfp-anim class to markup
        this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
      }
    },
    closeOnContentClick: true,
    midClick: true // allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source.
  });

});
