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

//
//
//
// EZT A FUNCKTIOT MEG RENDBE KENE TENNI MERT NAGYON GANY
//
//
//
function addArticleToHtml(score, url, title, ellapsedTime, user, id) {
  
  function putRequest() {
    makeHttpRequest('PUT', `http://secure-reddit.herokuapp.com/simple/posts/${id}/upvote`, console.log);
  }
   
  let article = document.createElement('article');
  let counter = document.createElement('div');
  let upArrow = document.createElement('img');
  let countNumber = document.createElement('p');
  let downArrow = document.createElement('img');
  counter.classList.add('counter');
  upArrow.setAttribute('src', 'images/upvote.png');
  downArrow.setAttribute('src', 'images/downvote.png');
  addUpVote(upArrow, id, score, countNumber);
  addDownVote(downArrow, id, score, countNumber);
  countNumber.innerText = score;
  main.appendChild(article);
  article.appendChild(counter);
  counter.appendChild(upArrow);
  counter.appendChild(countNumber);
  counter.appendChild(downArrow);
  let articleInfo = document.createElement('div');
  articleInfo.classList.add('article-info');
  articleInfo.innerHTML = `<a href="${url}">${title}</a><p>submitted ${ellapsedTime} day ago by ${user}</p><p><a href="#">Modify</a><a href="#">Remove</a></p>`
  article.appendChild(articleInfo);
}

function checkUser(post) {
  let user = post.name;
  return (user == null ? user = 'Anonymous' : user);
}

function handleJsonData(data) {
  data.forEach(function(post) {
    addArticleToHtml(post.score, post.url, post.title, post.timestamp, checkUser(post), post.id);
  });
}

function changeArrowImage(arrow) {
  let originalSrc = arrow.getAttribute('src');
  originalSrc = originalSrc.split('.');
  let usedSrc = originalSrc[0] + 'd.' + originalSrc[1];
  arrow.setAttribute('src', usedSrc);
}

function addUpVote(arrow, id, score, countNumber) {
  arrow.addEventListener('click', function() {
    makeHttpRequest('PUT', `http://secure-reddit.herokuapp.com/simple/posts/${id}/upvote`, console.log);
    changeArrowImage(arrow);
    score++;
    countNumber.innerText = score;
  }, {once: true});
}

function addDownVote(arrow, id, score, countNumber) {
  arrow.addEventListener('click', function() {
    makeHttpRequest('PUT', `http://secure-reddit.herokuapp.com/simple/posts/${id}/downvote`, console.log);
    changeArrowImage(arrow);
    score--;
    countNumber.innerText = score;
  }, {once: true});
}

function getAllPosts() {
  makeHttpRequest('GET', 'http://secure-reddit.herokuapp.com/simple/posts', handleJsonData);
}

getAllPosts();
