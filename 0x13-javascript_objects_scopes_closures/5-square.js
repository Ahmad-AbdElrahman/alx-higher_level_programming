#!/usr/bin/node

const Rectangle = require("./4-rectangle");

class Square extends Rectangle {
    constructor(size) {
        super(size, size);
        this.size = size;
    }

    double () {
        super.double();
    }
}

module.exports = Square;