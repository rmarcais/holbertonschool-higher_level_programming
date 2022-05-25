$(document).ready(function () {
  $('#btn_translate').click(function () {
    const inp = $('#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + inp, function (data, status) {
      $('#hello').html(data.hello);
    });
  });
});
