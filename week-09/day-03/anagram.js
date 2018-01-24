'use strict';

function isAnagram (string1, string2) {
  if (typeof string1 !== 'string' || typeof string2 !== 'string') {
    throw new Error('The arguments entered are not strings')
  }
  let array1 = string1.toLowerCase().split('').sort();
  let array2 = string2.toLowerCase().split('').sort();

  array1.forEach(function(letter, index) {
    if (letter === ' ') {
      array1.splice(index, 1);
    }
  });
  array2.forEach(function(letter, index) {
    if (letter === ' ') {
      array2.splice(index, 1);
    }
  });
  return array1.every((element, i) => element === array2[i]);
}

console.log(isAnagram('anna', 'nana'));

module.exports = isAnagram;
