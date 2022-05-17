#!/usr/bin/node
const args = process.argv;
const axios = require('axios').default;
let i;
const dico = {};

axios.get(args[2])
  .then(function (response) {
    for (i = 0; i < response.data.length; i++) {
      if (response.data[i].completed === true) {
        if (dico[response.data[i].userId] === undefined) {
          dico[response.data[i].userId] = 0;
        }
        dico[response.data[i].userId] += 1;
      }
    }
    console.log(dico);
  })
  .catch(function (error) {
    console.log(error);
  });
