document.addEventListener('DOMContentLoaded', function () {
  $(document).ready(function () {
    $('#btn_translate').click(function () {
      const language = $('#language_code').val();
      const url = 'https://fourtonfish.com/hellosalut/?lang=' + language;
      $.get(url, function (data) {
        $('#hello').text(data.hello);
      });
    });
  });
});
