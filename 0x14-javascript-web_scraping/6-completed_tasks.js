#!/usr/bin/node
const args = process.argv;
const axios = require('axios').default;
let i;
let tmp;
let count = 0;
const dico = {};

axios.get(args[2])
  .then(function (response) {
    for (i = 0; i < response.data.length; i++) {
      if (tmp !== response.data[i].userId) {
        count = 0;
      }
      if (response.data[i].completed === true) {
        count += 1;
        dico[response.data[i].userId] = count;
      }
      tmp = response.data[i].userId;
    }
    console.log(dico);
  })
  .catch(function (error) {
    console.log(error);
  });
