'use strict';

let main = document.querySelector('main');
console.log(main);

function makeHttpRequest(option, url, callback) {
  let httpRequest = new XMLHttpRequest();
  httpRequest.open(option, url, true);
  httpRequest.setRequestHeader('Accept', 'application/json');
  httpRequest.send();
  httpRequest.onreadystatechange = console.log;
  httpRequest.onload = function() {
    if (httpRequest.status >= 200 && httpRequest.status < 400){
      let data = JSON.parse(httpRequest.responseText).posts;
      callback(data);
    } else {
      console.log('Reached the API, but it returned an error');
  }
  };
}

function addArticleToHtml(score, url, title, ellapsedDays, user) {
  let article = document.createElement('article');
  main.appendChild(article);
  article.innerHTML = `<div class="counter"><img src="images/upvote.png" alt="upvote"><p>${score}</p><img src="images/downvote.png" alt="downvote"></div><div class="article-info"><a href="${url}">${title}</a><p>submitted ${ellapsedDays} day ago by ${user}</p><p><a href="#">Modify</a><a href="#">Remove</a></p></div>`
}

// function getEllapsedDays() {
//   let days = new Date (post.timestamp * 1000);
//   console.log(days);
// }

function checkUser(post) {
  let user = post.name;
  return (user == null ? user = 'Anonymous' : user);
}

function handleJsonData(data) {
  data.forEach(function(post) {
    addArticleToHtml(post.score, post.url, post.title, post.timestamp, checkUser(post));
  });
}

function addVoteing() {
  let arrow = document.querySelectorAll('.counter img');

}

function getAllPosts() {
  makeHttpRequest('GET', 'http://secure-reddit.herokuapp.com/simple/posts', handleJsonData);
}

getAllPosts();