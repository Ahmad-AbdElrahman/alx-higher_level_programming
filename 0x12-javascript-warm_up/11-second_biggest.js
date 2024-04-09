#!/usr/bin/node
if (process.argv.length > 3) {
  let k = process.argv.slice(2);
  k.sort();
  let j = 0;
  for(let i = 0; i < process.argv.length; i++)  {
    if (process.argv[i] > j)  {
        j = process.argv[i]
    }
  }
  for(let i = k.length - 2; k[i] < j; i--)  {
    if (k[i] < j)  {
        j = k[i];
        break;
        }
  }
  console.log(j);
} else {
  console.log(0)
}