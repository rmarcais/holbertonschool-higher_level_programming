#!/usr/bin/node
const args = process.argv;
const axios = require('axios').default;

axios.get(args[2])
  .then(function (response) {
    console.log('code: ' + response.status);
  })
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  });
