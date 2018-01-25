'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');

const app = express();

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'redditdb'
});
connection.connect((err) => {
  if (err) throw err;
  console.log('Connected!');
});

app.use('/images', express.static('images'));
app.use(express.static('public'));

app.use(bodyParser.json());

app.get('/', function (req, res) {
  res.status(200);
  res.sendFile(__dirname + '/index.html');
});

app.get('/index.html', function (req, res) {
  res.status(200);
  res.sendFile(__dirname + '/index.html');
});

app.get('/add-post.html', function (req, res) {
  res.status(200);
  res.sendFile(__dirname + '/add-post.html');
});

app.get('/posts', function (req, res) {
  connection.query('SELECT * FROM posts', (err, rows) => {
    if (err) throw err;

    console.log('Data received from reddit database!');
    let dataToSend = {
      "posts": 
        rows
    }
    res.status(200);
    res.json(dataToSend);
  });
});

app.post('/posts', function (req, res) {
  console.log(req.body);
  connection.query('INSERT INTO posts SET ?', req.body, (err, res) => {
    if(err) throw err;

    console.log('New post added to the database');
  });
  res.status(201);
  res.json(req.body);
});


app.listen(3000, function() {
  console.log('The server is running');
});
