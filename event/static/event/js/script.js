$(document).ready(function() {
    function setHeight() {
      windowHeight = $(window).innerHeight() -56;
      $('.carousel-inner,.img-full').css('height', windowHeight);
      $('.carousel-inner,.img-full').width(window.innerWidth);
    };
    setHeight();
  
    $(window).resize(function() {
      setHeight();
    });
  });
  //  ***   set slider size equal to viewport   ***
  