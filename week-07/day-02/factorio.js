'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(number) {
  let total = 1;
  for (let i = 1; i <= number; i++) {
    total *= i;
  }
  return total;
}

console.log(factorio(5));
