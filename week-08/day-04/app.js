'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');

const app = express();

app.use('/images', express.static('images'));
app.use(express.static('public'));

app.use(bodyParser.json());

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});



app.listen(3000, function() {
  console.log('The server is running');
});
