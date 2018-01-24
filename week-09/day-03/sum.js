'use strict';

let summer = {
  sum: function(numbers) {
    let sum = 0;
    numbers.forEach(function (elem) {
      if (typeof elem !== 'number') {
        throw new Error('The list contains non number element(s)')
      }
      sum += elem;
    });
    return sum;
  }
}

// let list = [1, 2, 3];
// console.log(summer.sum(list));

module.exports = summer;
