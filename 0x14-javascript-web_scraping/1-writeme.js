#!/usr/bin/node
const args = process.argv;
const fs = require('fs');

fs.writeFile(args[2], args[3], err => {
  if (err) {
    console.log(err);
  }
});
