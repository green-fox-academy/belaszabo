'use strict';

// Check if the array contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

var numbers = [1,2,3,4,5,7,6,8];

function findNumber(numbers) {
  let temp = 0;
  numbers.forEach(function (e) {
    if (e === 7) {
      temp += 1;
    };
  });
  if (temp > 0) {
    console.log('Hoorray');
  } else {
    console.log('Nooooo');
  }
}

findNumber(numbers);
