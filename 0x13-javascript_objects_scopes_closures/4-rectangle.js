#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let string = '';
      for (let i = 0; i < this.width; i++) {
        string += 'X';
      }
      console.log(string);
    }
  }

  rotate () {
    const i = this.height;
    this.height = this.width;
    this.width = i;
  }

  double () {
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }
}

module.exports = Rectangle;
