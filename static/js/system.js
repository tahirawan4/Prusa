

// =============
// =============



 jQuery(document).ready(function() {
   var mediasize = 767;
   if ($(window).width() <= mediasize) {
     jQuery("#myModal1").modal('show');
   }
   
     jQuery('.headSlider').slick({
         dots: true,
         arrows: false,
         infinite: true,
         speed: 2000,
         slidesToShow: 1,
         autoplay:false,
         autoplaySpeed: 2000
     });
     jQuery('.proSlider').slick({
         dots: false,
         arrows: false,
         infinite: true,
         speed: 2000,
         slidesToShow: 4,
         slidesToScroll:1,
         autoplay:false,
         autoplaySpeed: 2000,
             responsive: [
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1,
            
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
        ]
     });

      jQuery('.proDetailSlider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.proDetailSliderNav'
      });
      jQuery('.proDetailSliderNav').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.proDetailSlider',
        dots: false,
        centerMode: true,
        focusOnSelect: true
      });

   });