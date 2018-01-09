'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(stopAt) {
  let total = 0;
  for (let i = 1; i < stopAt; i++) {
    total += i;
  }
  return total;
}

console.log(sum(3));
