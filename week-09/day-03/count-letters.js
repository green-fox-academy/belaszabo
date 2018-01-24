'use strict';

function countLetters (string) {
  if (typeof string !== 'string') {
    throw new Error('Argument is not a string!');
  }
  let letterCounts = {};
  string.split('').forEach(function (letter) {
    if (letterCounts[letter] > 0) {
      letterCounts[letter]++;
    } else {
      letterCounts[letter] = 1;
    }
  });
  return letterCounts;
}

module.exports = countLetters;
