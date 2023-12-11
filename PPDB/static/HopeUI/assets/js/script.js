// 1) Format Nomor Telepon
$(document).ready(function () {
  $(".phone").inputmask("(+62) 999-9999-9999", {
    onincomplete: function () {
      swal("Opps !", "Incomplete phone. Please review !", "info");
      $(".phone").val("");
      return false;
    },
  });
});
