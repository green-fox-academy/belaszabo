'use strict';
let button = document.querySelector('button');

button.addEventListener('click', function() {
  let inputTitle = document.querySelector('#title').value;
  let inputUrl = document.querySelector('#url').value;
  
  let dataToSend = new Object();
  dataToSend.title = String(inputTitle);
  dataToSend.url = String(inputUrl);
  dataToSend.owner = "MrPeanutbutter";
  
  let jsonDataToSend = JSON.stringify(dataToSend);
  console.log(jsonDataToSend);

  makeHttpRequest('POST', 'http://secure-reddit.herokuapp.com/simple/posts', jsonDataToSend);

});

function makeHttpRequest(option, url, data) {
  let httpRequest = new XMLHttpRequest();
  httpRequest.open(option, url, true);
  httpRequest.setRequestHeader('Accept', 'application/json');
  httpRequest.setRequestHeader('Content-type', 'application/json');
  httpRequest.setRequestHeader('User', 'MrPeanutbutter');
  httpRequest.send(data);
  httpRequest.onreadystatechange = console.log;
  httpRequest.onload = function() {
    if (httpRequest.status >= 200 && httpRequest.status < 400){
      console.log('Posting succesful!');
      setTimeout(function() {
        window.location = 'index.html';
      }, 3000);
    } else {
      console.log('Reached the API, but it returned an error');
  }
  };
}

