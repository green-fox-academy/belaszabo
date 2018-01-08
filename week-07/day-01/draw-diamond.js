'use strict';

var lineCount = 7;



// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is

let star = '*';

for (let i = Math.floor(lineCount / 2); i > 0; i--) {
  console.log(' '.repeat(i) + star);
  star += '**';
}

for (let i = 0; i <= Math.floor(lineCount / 2); i++) {
  console.log(' '.repeat(i) + star.substr(i * 2 , star.length));
}
