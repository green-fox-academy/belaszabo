class ElevatorController {

}

class ElevatorModel {

  constructor(maxFloor, maxPeople) {
    this.maxFloor = maxFloor;
    this.maxPeople = maxPeople;
    this.elevatorPosition = 0;
    this.elevatorDirection = 'up';
    this.people = 0;
  }

  addPeople() {
    if (this.people < this.maxPeople) {
      this.people++;
    }
  }

  removePeople() {
    if (this.people > 0) {
      this.people--;
    }
  }

  moveUp() {
    if (this.elevatorPosition < this.maxFloor) {
      this.elevatorDirection = 'up';
      this.elevatorPosition++;
    }
  }

  moveDown() {
    if (this.elevatorPosition > 0) {
      this.elevatorDirection = 'down';
      this.elevatorPosition--;
    }
  }

}

class ElevatorView {

}
