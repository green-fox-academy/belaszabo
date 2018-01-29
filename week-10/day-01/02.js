'use strict';

function Rectangle(a, b) {
  this.getArea = function() {
    return a * b;
  }

  this.getCircumference = function() {
    return 2 * (a + b);
  }
}

let square = new Rectangle(10, 10);

console.log(square.getArea());
console.log(square.getCircumference());
