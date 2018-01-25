'use strict';

const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use('/assets', express.static('assets'));

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function (req, res) {

  res.json();
});

app.listen(8080, function() {
  console.log('The server is running');
});
