#!/usr/bin/node
const args = process.argv;
const axios = require('axios').default;
let i;
const url = 'https://swapi-api.hbtn.io/api/people/18/';
let count = 0;

axios.get(args[2])
  .then(function (response) {
    for (i = 0; i < response.data.results.length; i++) {
      if (response.data.results[i].characters.includes(url) === true) {
        count += 1;
      }
    }
    console.log(count);
  });
