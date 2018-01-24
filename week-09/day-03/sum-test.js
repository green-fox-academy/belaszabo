'use strict';

const test = require('tape');
const summer = require('./sum.js');

test('sum a list of integers', function(t) {
  let numbers = [1, 2, 3, 4, 5];

  let actual = summer.sum(numbers);
  let expected = 15;

  t.equal(actual, expected);
  t.end();
});

test('sum an empty list', function(t) {
  let numbers = [];

  let actual = summer.sum(numbers);
  let expected = 0;


  t.equal(actual, expected);
  t.end();
});
