#!/usr/bin/node
const args = process.argv;
const axios = require('axios');

axios.get('https://swapi-api.hbtn.io/api/films/' + args[2])
  .then(function (response) {
    console.log(response.data.title);
  });
