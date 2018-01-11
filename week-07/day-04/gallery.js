'use strict';

let leftArrow = document.querySelector('.cls-1');
let rightArrow = document.querySelector('.cls-2');
let pictures = document.querySelectorAll('img');
let mainPicture = document.querySelector('.main-image');
let picPaths = [];

for (let i = 0; i < pictures.length; i++) {
  pictures[i].addEventListener('click', function(event) {
    let source = pictures[i].getAttribute('src');
    mainPicture.setAttribute('style', 'background-image: url(' + source +')');
  });
}


