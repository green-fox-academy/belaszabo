'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.
let eOccurance = fruits.map(function(word) {
  let e = 0;
  for (let i = 0; i < word.length; i++) {
    if (word[i] === 'e') {
      e++;
    }
  }
  return e;
});

console.log(eOccurance);
