'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array

function selectLastEvenNumber(numbers, callback) {
  for (let i = 0; i <= numbers.length; i++) {
    if (numbers[numbers.length - i] % 2 === 0) {
      return callback(numbers[numbers.length - i]);
    }
  }
}

function printNumber(num) {
  console.log(num);
}

selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8
