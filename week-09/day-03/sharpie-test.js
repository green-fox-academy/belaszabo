'use strict';

const test = require('tape');
const Sharpie = require('./sharpie.js');

test ('blank color input throws error', function(t) {
  let testSharpie = new Sharpie('', 10);

  t.equal(testSharpie.color, 'Invalid input, please add a color string');
  t.end();
});
