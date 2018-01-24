'use strict';

const test = require('tape');
const countLetters = require('./count-letters.js');

test('count letters of empty string', function(t) {
  let actual = countLetters('')
  let expected = {}

  t.deepEqual(actual, expected);
  t.end();
});

test('count letters of string', function(t) {
  let actual = countLetters('aaaaaaaaaa')
  let expected = {
    a: 10
  }
  t.deepEqual(actual, expected);
  t.end();
});

test('count letters of string', function(t) {
  let actual = countLetters('apple')
  let expected = {
    a: 1,
    p: 2,
    l: 1,
    e: 1
  }
  t.deepEqual(actual, expected);
  t.end();
});

test('count letters of non string', function(t) {
  t.throws(countLetters.bind(null, 4556), Error);
  t.end();
});
