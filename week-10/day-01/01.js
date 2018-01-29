'use strict';

function Animals(says) {

  this.say = function () {
    console.log(says);
  }
}

let dog = new Animals('woof');

dog.say();
