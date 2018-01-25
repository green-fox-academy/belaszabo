'use strict';

let button = document.querySelector('button');
let url = window.location;
let inputTitle = document.querySelector('#title');
let inputUrl = document.querySelector('#url');

function makeHttpRequest(option, url, data) {
  let httpRequest = new XMLHttpRequest();
  httpRequest.open(option, url);
  httpRequest.setRequestHeader('Accept', 'application/json');
  httpRequest.setRequestHeader('Content-type', 'application/json');
  httpRequest.setRequestHeader('Username', 'MrPeanutbutter');
  httpRequest.onreadystatechange = console.log;
  httpRequest.onload = function() {
    if (httpRequest.status >= 200 && httpRequest.status < 400){
      console.log('Editing the post was succesful!');
      window.location = 'index.html';
      } else {
        console.log('Reached the API, but it returned an error');
      }
    };
  httpRequest.send(data);
}

function getOriginalData() {
  makeHttpRequest('GET', 'https://time-radish.glitch.me/posts')
}

function getParameterByName(name, url) {
  if (!url) url = window.location.href;
  name = name.replace(/[\[\]]/g, "\\$&");
  let regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
      results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}

let title = getParameterByName('title', url);
let linkUrl = getParameterByName('url', url);
let id = getParameterByName('id', url);

inputTitle.setAttribute('value', title);
inputUrl.setAttribute('value', linkUrl);

button.addEventListener('click', function() {
  let dataToSend = new Object();
  dataToSend.title = String(inputTitle.value);
  dataToSend.url = String(inputUrl.value);
  dataToSend.owner = "MrPeanutbutter";
  
  let jsonDataToSend = JSON.stringify(dataToSend);
  console.log(jsonDataToSend);

  makeHttpRequest('PUT', `https://time-radish.glitch.me/posts/${id}`, jsonDataToSend);

});



