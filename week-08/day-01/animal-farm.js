class Animal {
  
  constructor() {
    this.hunger = 5;
    this.thirst = 5;
  }

  eat() {
    this.hunger--;
  }

  drink() {
    this.thirst--;
  }

  play() {
    this.hunger++;
    this.thirst++;
  }

}


class Farm {

  constructor (slots) {
    this.slots = slots;
    this.animals = [];
  }

  breed() {
    if (this.animals.length < this.slots) {
      let animal = new Animal();
      this.animals.push(animal);
    }
  }

  slaughter() {
    let animalToKill = this.animals[0];
    for (let i = 1; i <= this.animals.length; i++) {
      if (animalToKill.hunger < this.animals[i]) {
        animalToKill = this.animals[i];
      }
    }
    let index = this.animals.indexOf(animalToKill);
    this.animals.splice(index, 1);
  }

  printReport() {
    let status;
    if (this.animals.length === this.slots) {
      status = 'full';
    } else if (this.animals.length === 0) {
      status = 'bankrupt';
    } else {
      status = 'okay';
    }
    console.log('The farm has ' + this.animals.length + ' living animals, we are ' + status);
  }

  progress() {
    console.log(this);
    for (let i = 0; i < this.animals.length; i++) {
      let temp = Math.floor(Math.random() * (3 - 1 + 1)) + 1;
      if (temp === 1) {
        this.animals[i].eat();
      } else if (temp === 2) {
        this.animals[i].drink();
      } else if (temp === 3) {
        this.animals[i].play();
      }
    }
    this.breed();
    this.slaughter();
    this.printReport();
    console.log(this);
}

}

const SheepFarm = new Farm(20);
SheepFarm.breed();
SheepFarm.breed();
SheepFarm.breed();
SheepFarm.breed();
SheepFarm.breed();
SheepFarm.breed();
SheepFarm.breed();
SheepFarm.breed();
SheepFarm.breed();
SheepFarm.breed();


SheepFarm.progress();