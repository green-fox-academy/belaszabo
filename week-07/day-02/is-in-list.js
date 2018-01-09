'use strict';
// Check if array contains all of the following elements: 4,8,12,16
// Create a 'numChecker' function that accepts 'listOfNumbers' as an input
// it should return "true" if it contains all, otherwise "false"

var listOfNumbers = [2, 4, 6, 8, 10, 14, 16]

function numChecker(listOfNumbers) {
  let temp = 0;
  listOfNumbers.forEach(function (e) {
    if (e === 4 || e === 8 || e === 12 || e === 16) {
      temp += 1;
    };
  });
  console.log(temp === 4);
}

numChecker(listOfNumbers);
