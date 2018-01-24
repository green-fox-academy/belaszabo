'use strict';

function getFibonacciNumber (index) {
  if (index < 2 && index >= 0) {
    return index;
  } else {
    return (getFibonacciNumber(index - 1) + getFibonacciNumber(index - 2));
  }
}

module.exports = getFibonacciNumber;
