#!/usr/bin/node
const arr = require('./100-data').list;
console.log(arr);
const newlist = arr.map((num, idx) => {
  return num * idx;
});
console.log(newlist);
