'use strict';

class Sharpie {

  constructor(color, width) {
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

let green = new Sharpie('green', 10);

while (green.use()) {
  green.use();
}
