'use strict';

const test = require('tape');
const isAnagram = require('./anagram.js');

test('compare one letter words', function(t) {
  t.ok(isAnagram('a', 'a'))
  t.end();
});

test('compare blank strings', function(t) {
  t.ok(isAnagram('', ''))
  t.end();
});

test('compare non strings', function(t) {
  t.throws(isAnagram.bind(null, 2, 'an'), Error);
  t.end();
});

test('compare several letter words', function(t) {
  t.ok(isAnagram('anna', 'anna'))
  t.end();
});

test('compare several letter words with space', function(t) {
  t.ok(isAnagram('anna', 'an na'))
  t.end();
});

test('compare several letter words with space, uppercase', function(t) {
  t.ok(isAnagram('Anna', 'an na'))
  t.end();
});
