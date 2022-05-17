#!/usr/bin/node
const args = process.argv;
const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films/' + args[2])
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function (error) {
    console.log(error);
  });
