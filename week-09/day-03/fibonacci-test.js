'use strict';

const test = require('tape');
const getFibonacciNumber = require('./fibonacci.js');

test('get 0. element', function(t) {
  let actual = getFibonacciNumber(0);
  let expected = 0;

  t.equal(actual, expected);
  t.end();
});

test('get 10. element', function(t) {
  let actual = getFibonacciNumber(10);
  let expected = 55;

  t.equal(actual, expected);
  t.end();
});

test('not valid index', function(t) {
  t.throws(getFibonacciNumber.bind(null, 'hoho'), Error);
  t.end();
});
