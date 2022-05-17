#!/usr/bin/node
const args = process.argv;
const axios = require('axios').default;
let i;

function getCharacter () {
  axios.get('https://swapi-api.hbtn.io/api/films/' + args[2])
    .then(async function (response) {
      for (i = 0; i < response.data.characters.length; i++) {
        await axios.get(response.data.characters[i])
          .then(function (response) {
            console.log(response.data.name);
          })
          .catch(function (error) {
            console.log(error);
          });
      }
    })
    .catch(function (error) {
      console.log(error);
    });
}
getCharacter();
