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

function getPostTime(timestamp) {
  let time = Date.now();
  let date = new Date(timestamp);
  let since = time - date;
  since = new Date(since);
  let hour = since.getHours() - 1;
  let minute = since.getMinutes();
  return `${hour} hour(s) and ${minute} minute(s)`
}

//
//
//
// EZT A FUNCTIONT MEG RENDBE KENE TENNI MERT NAGYON GANY
//
//
//
function addArticleToHtml(score, url, title, ellapsedTime, user, id) {
  
  let postTime = getPostTime(ellapsedTime);
  // let domain = getDomain(url);
  
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
  articleInfo.innerHTML = `<a target="_blank" href="${url}">${title}</a><p>submitted ${postTime} ago by ${user}</p>` // <span class="domain">(${domain})</span>
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

// function getDomain(url) {
//   if (url == undefined) {
//     return '#';
//   } else {
//     let hostname;

//     if (url.indexOf("://") > -1) {
//         hostname = url.split('/')[2];
//     }
//     else {
//         hostname = url.split('/')[0];
//     }

//     hostname = hostname.split(':')[0];
//     hostname = hostname.split('?')[0];

//     return hostname;
//   }
// }

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
    makeHttpRequest('PUT', `http:/localhost:3000/posts/${id}/upvote`, console.log);
    changeArrowImage(arrow);
    score++;
    countNumber.innerText = score;
  }, {once: true});
}

function addDownVote(arrow, id, score, countNumber) {
  arrow.addEventListener('click', function() {
    makeHttpRequest('PUT', `http://localhost:3000/posts/${id}/downvote`, console.log);
    changeArrowImage(arrow);
    score--;
    countNumber.innerText = score;
  }, {once: true});
}

function getAllPosts() {
  makeHttpRequest('GET', 'http://localhost:3000/posts', handleJsonData);
}

function goToAddPostPage(button) {
  button.addEventListener('click', function() {
    window.location = 'add-post.html';
  });
}

function removePost(removeElement, id, parent, child) {
  removeElement.addEventListener('click', function() {
    makeHttpRequest('DELETE', `http://localhost:3000/posts/${id}`, console.log);
    console.log('Post deleted succesfully');
    parent.removeChild(child)
  });
}

goToAddPostPage(submit);

getAllPosts();
