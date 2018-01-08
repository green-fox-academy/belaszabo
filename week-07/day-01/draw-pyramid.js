'use strict';

var lineCount = 4;
let star = '*'

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

let a = lineCount - 1;

for (let i = lineCount; i > 0; i--) {
  console.log(' '.repeat(i) + star)
  star += '**'
}
