#!/usr/bin/node
const process = require('process');
const a = Number(process.argv[2])
function factorial(a) {
  if (a) {
        return a * factorial(a-1)
  } else {
    return 1
    }
}
console.log(factorial(a));