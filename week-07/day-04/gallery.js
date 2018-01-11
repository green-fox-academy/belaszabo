'use strict';

let leftArrow = document.querySelector('.cls-1');
let rightArrow = document.querySelector('.cls-2');
let pictures = document.querySelectorAll('img');
let mainPicture = document.querySelector('.main-image');

//mukodo verzio, background beallitassal:
// for (let i = 0; i < pictures.length; i++) {
//   pictures[i].addEventListener('click', function(event) {
//     let source = pictures[i].getAttribute('src');
//     mainPicture.setAttribute('style', 'background-image: url(' + source +')');
//   });
// }

let currentPicture = mainPicture.getElementsByTagName('img')[0];

for (let i = 0; i < pictures.length; i++) {
  pictures[i].addEventListener('click', function(event) {
    let source = pictures[i].getAttribute('src');
    currentPicture.setAttribute('src', source);
  });
}

// function nextPic(index) {
//   mainPicture.removeChild();
//   mainPicture.appendChild(pictures[index + 1 ]);
//   currentPicture = pictures[index + 1];
// }

// showFirstPic();