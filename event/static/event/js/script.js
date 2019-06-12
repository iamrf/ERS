$(document).ready(function() {
    function setHeight() {
      windowHeight = $(window).innerHeight() -56;
      $('.carousel-inner,.img-fit').css('height', windowHeight);
      $('.carousel-inner,.img-fit').width(window.innerWidth);
    };
    setHeight();
  
    $(window).resize(function() {
      setHeight();
    });
  });
  //  ***   set slider size equal to viewport   ***
  