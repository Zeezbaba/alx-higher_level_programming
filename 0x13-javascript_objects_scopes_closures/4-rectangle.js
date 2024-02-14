#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      this.width = 0;
      this.height = 0;
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

  rotate () {
    let swp = 0;
    swp = this.width;
    this.width = this.height;
    this.height = swp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
