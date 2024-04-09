#!/usr/bin/node

const Rectangle = require("./4-rectangle");

class Square extends Rectangle {
<<<<<<< HEAD
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  double () {
    super.double();
  }
=======
    constructor(size) {
        super(size, size);
    }

    double () {
        super.double();
    }
>>>>>>> ae25f2f7537e02a27544e49bcb41e789c8e00cf5
}

module.exports = Square;