'use strict';

let summer = {
  sum: function(numbers) {
    let sum = 0;
    numbers.forEach(elem => sum += elem);
    return sum;
  }
}

// let list = [];
// console.log(summer.sum(list));

module.exports = summer;
