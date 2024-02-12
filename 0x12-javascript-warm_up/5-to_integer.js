#!/usr/bin/node
const integers = parseInt(process.argv[2]);

if (!isNaN(integers)) {
  console.log(`My number: ${integers}`);
} else {
  console.log('Not a number');
}
