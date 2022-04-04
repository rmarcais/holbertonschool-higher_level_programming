#!/usr/bin/node
const args = process.argv;
function factorial (a) {
  if (a === 1) {
    return (1);
  }
  return (a * factorial(a - 1));
}
let nb;
if (isNaN(args[2]) === true) {
  nb = 1;
} else {
  nb = parseInt(args[2]);
}
const result = factorial(nb);
console.log(result);
