#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === 'C' || c === 'c') {
      for (let i = 0; i < this.height; i++) {
        let string = '';
        for (let i = 0; i < this.width; i++) {
          string += c;
        }
        console.log(string);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
