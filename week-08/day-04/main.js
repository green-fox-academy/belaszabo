'use strict';

let main = document.querySelector('main');
let submit = document.querySelector('.submit');

function makeHttpRequest(option, url, callback) {
  let httpRequest = new XMLHttpRequest();
  httpRequest.open(option, url);
  httpRequest.setRequestHeader('Accept', 'application/json');
  httpRequest.onreadystatechange = console.log;
  httpRequest.send();
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
// EZT A FUNCTIONT MEG RENDBE KENE TENNI MERT NAGYON GANY
//
//
//
function addArticleToHtml(score, url, title, ellapsedTime, user, id) {
  
  function putRequest() {
    makeHttpRequest('PUT', `https://time-radish.glitch.me/posts/${id}/upvote`, console.log);
  }
   
  let article = document.createElement('article');
  main.appendChild(article);
  
  let counter = document.createElement('div');
  counter.classList.add('counter');
  article.appendChild(counter);
  
  let upArrow = document.createElement('img');
  upArrow.setAttribute('src', 'images/upvote.png');
  counter.appendChild(upArrow);
  
  let countNumber = document.createElement('p');
  countNumber.innerText = score;
  counter.appendChild(countNumber);
  
  let downArrow = document.createElement('img');
  downArrow.setAttribute('src', 'images/downvote.png');
  counter.appendChild(downArrow);
  
  
  let articleInfo = document.createElement('div');
  articleInfo.classList.add('article-info');
  articleInfo.innerHTML = `<a href="${url}">${title}</a><p>submitted ${ellapsedTime} day ago by ${user}</p>`
  article.appendChild(articleInfo);
  
  let links = document.createElement('p');
  articleInfo.appendChild(links);
  
  let modify = document.createElement('a');
  modify.innerText = 'Modify';
  modify.setAttribute('href', `edit-post.html?title=${title}&url=${url}&id=${id}`);
  links.appendChild(modify);
  
  let remove = document.createElement('a');
  remove.innerText = 'Remove';
  remove.setAttribute('href', '#');
  links.appendChild(remove);
  
  addUpVote(upArrow, id, score, countNumber);
  addDownVote(downArrow, id, score, countNumber);
  removePost(remove, id, main, article);
}

function checkUser(post) {
  let user = post.owner;
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
    makeHttpRequest('PUT', `https://time-radish.glitch.me/posts/${id}/upvote`, console.log);
    changeArrowImage(arrow);
    score++;
    countNumber.innerText = score;
  }, {once: true});
}

function addDownVote(arrow, id, score, countNumber) {
  arrow.addEventListener('click', function() {
    makeHttpRequest('PUT', `https://time-radish.glitch.me/posts/${id}/downvote`, console.log);
    changeArrowImage(arrow);
    score--;
    countNumber.innerText = score;
  }, {once: true});
}

function getAllPosts() {
  makeHttpRequest('GET', 'https://time-radish.glitch.me/posts', handleJsonData);
}

function goToAddPostPage(button) {
  button.addEventListener('click', function() {
    window.location = 'add-post.html';
  });
}

function removePost(removeElement, id, parent, child) {
  removeElement.addEventListener('click', function() {
    makeHttpRequest('DELETE', `https://time-radish.glitch.me/posts/${id}`, console.log);
    console.log('Post deleted succesfully');
    parent.removeChild(child)
  });
}

goToAddPostPage(submit);

getAllPosts();
