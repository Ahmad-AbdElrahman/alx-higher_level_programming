#!/usr/bin/node
const process = require('process');
if (Number(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    let string = '';
    for (let i = 0; i < process.argv[2]; i++) {
      string += 'X';
    }
    console.log(string);
  }
} else {
  console.log('Missing size');
}
