'use strict';

const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use('/assets', express.static('assets'));

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function (req, res) {
  if (req.query.input === undefined) {
    res.body = {
      "error": "Please provide an input!"
    }
  } else {
    res.body = {
      "received": req.query.input,
      "result":  req.query.input * 2
    }
  }
  res.json(res.body);
});

app.get('/greeter', function (req, res) {
  if (req.query.name === undefined) {
    res.body = {
      "error": "Please provide a name!"
    }
  } else if (req.query.title === undefined) {
    res.body = {
      "error": "Please provide a title!"
    }
  } else {
    res.body = {
      "welcome_message": "Oh, hi there " + req.query.name + ", my dear " + req.query.title + "!"
    }
  }
  res.json(res.body);
});

app.get('/appenda/:word', function (req, res) {
  if (req.params.word != 0) {
    res.body = {
      "appended": req.params.word + "a"
    }
    res.json(res.body);
  } else {
    res.send(404);
  }
});

app.listen(8080, function() {
  console.log('The server is running');
});
