
// for scroll indicator

window.onscroll = function () { myFunction() };

function myFunction() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  document.getElementById("myBar").style.width = scrolled + "%";
}

// $('#myModal').on('shown.bs.modal', function () {
//   $('#myInput').trigger('focus')
// })

//   $('#myModal').modal('toggle');
// $('#myModal').modal('show');
// $('#myModal').modal('hide');
$(document).on("scroll", function () {

  if ($(document).scrollTop() > 70) {
    $(".primary-nav").addClass("shrink");
  } else {
    $(".primary-nav").removeClass("shrink");
  }

});