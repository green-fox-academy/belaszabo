'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

let size = 4;
let myMatrix = [];

for (let i = 0; i < size; i++) {
  myMatrix.push('0 '.repeat(size - 1) + '1 ' + '0 '.repeat(i));
}

console.log(myMatrix);
