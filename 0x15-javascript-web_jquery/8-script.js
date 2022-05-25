$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
  $.each(data.results, function (index, value) {
    $('#list_movies').append('<li>' + value.title + '</li>');
  });
});
