#!/usr/bin/node
const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  const arr = [];
  let i;
  for (i = 2; i < args.length; i++) {
    arr[i - 2] = parseInt(args[i]);
  }
  const max = Math.max.apply(null, arr);
  arr.splice(arr.indexOf(max), 1);
  const secondmax = Math.max.apply(null, arr);
  console.log(secondmax);
}
