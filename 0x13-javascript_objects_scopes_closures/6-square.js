#!/usr/bin/node
/**
 * Square class that inherits from previous square class
 */
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let j = 0;
      while (j < this.width) {
        myVar += myChar;
        y++;
      }

      console.log(myVar);
    }
  }
}

module.exports = Square;
