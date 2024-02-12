#!/usr/bin/node
const square = parseInt(process.argv[2]);

if (!isNaN(square)) {
  for (let i = 0; i < square; i++) {
    let row = '';
    for (let j = 0; j < square; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
