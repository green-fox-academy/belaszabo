'use strict';

class Sharpie {

  constructor(color, width) {
    if (typeof color !== 'string' || color.length === 0) {
      throw 'Invalid input, please add a color string';
    }
    this.color = color;
    this.width = width;
    this.inkAmount = 100;
  }

  use() {
    if ((this.inkAmount -= this.width) >= 0) {
      this.inkAmount -= this.width;
      console.log('Ink used');
      return true;
    } else {
      console.log('Out of ink!');
      return false;
    }
  }
}

module.exports = Sharpie;
