'use strict';

// let button = document.querySelector('button');

// function makeHttpRequest(option, url, data) {
//   let httpRequest = new XMLHttpRequest();
//   httpRequest.open(option, url);
//   httpRequest.setRequestHeader('Accept', 'application/json');
//   httpRequest.setRequestHeader('Content-type', 'application/json');
//   httpRequest.setRequestHeader('Username', 'MrPeanutbutter');
//   httpRequest.onreadystatechange = console.log;
//   httpRequest.onload = function() {
//     if (httpRequest.status >= 200 && httpRequest.status < 400){
//       console.log('Posting succesful!');
//       window.location = 'index.html';
//       } else {
//         console.log('Reached the API, but it returned an error');
//       }
//     };
//   httpRequest.send(data);
// }

// button.addEventListener('click', function() {
//   let inputTitle = document.querySelector('#title').value;
//   let inputUrl = document.querySelector('#url').value;
  
//   let dataToSend = new Object();
//   dataToSend.title = String(inputTitle);
//   dataToSend.url = String(inputUrl);
//   dataToSend.owner = "MrPeanutbutter";
  
//   let jsonDataToSend = JSON.stringify(dataToSend);
//   console.log(jsonDataToSend);

//   makeHttpRequest('POST', 'https://time-radish.glitch.me/posts', jsonDataToSend);

// });



