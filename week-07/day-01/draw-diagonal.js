'use strict';

var lineCount = 6;
let sign = '%';
let space = ' ';

// Write a program that draws a
// square like this:
//
//
// %%%%%
// %%  %
// % % %
// %  %%
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

console.log(sign.repeat(lineCount));

for (let i = 0; i < lineCount - 2; i++) {
  console.log(sign + space.repeat(i) + sign + space.repeat(lineCount - i - 3) + sign);
}

console.log(sign.repeat(lineCount));
