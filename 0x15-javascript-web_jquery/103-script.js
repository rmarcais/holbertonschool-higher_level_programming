$(document).ready(function () {
  $('#language_code').keyup(function (event) {
    if (event.which === 13) {
      $('#btn_translate').click();
    }
  });

  $('#btn_translate').click(function () {
    const inp = $('#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + inp, function (data, status) {
      $('#hello').html(data.hello);
    });
  });
});
