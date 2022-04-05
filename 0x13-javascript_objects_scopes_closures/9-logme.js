#!/usr/bin/node
exports.logMe = (function () {
  let i = -1;
  return function (item) {
    i++;
    console.log(i + ': ' + item);
  };
})();
