'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

function calculateCuboid (a, b, c) {
  let surfaceArea = 2 * (a * b + a * c + b * c);
  let volume = a * b * c;
  console.log(surfaceArea);
  console.log(volume);
}

calculateCuboid (2, 3, 5);
