#!/usr/bin/node
const string = 'C is fun';
let i;
const args = process.argv;
let nb;
if (isNaN(args[2]) === true) {
  console.log('Missing number of occurrences');
} else {
  nb = parseInt(args[2]);
  for (i = 0; i < nb; i++) {
    console.log(string);
  }
}
