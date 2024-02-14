#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && typeof w === 'number' && h > 0 && typeof h === 'number') {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width === 0 || this.height === 0) {
      console.log('');
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
