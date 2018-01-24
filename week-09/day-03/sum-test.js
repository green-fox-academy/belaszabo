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

test('sum a list with one element', function(t) {
  let numbers = [1];

  let actual = summer.sum(numbers);
  let expected = 1;


  t.equal(actual, expected);
  t.end();
});

test('sum a list of null', function(t) {
  let numbers = [null];

  t.throws(summer.sum.bind(null, numbers), Error);
  t.end();
});

test('test with string', function(t) {
  let numbers = ['hello'];

  t.throws(summer.sum.bind(null, numbers), Error);
  t.end();
});
