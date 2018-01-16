class ElevatorController {

  constructor() {
    this.up = document.querySelector('#up');
    this.down = document.querySelector('#down');
    this.add = document.querySelector('#add');
    this.remove = document.querySelector('#remove');
    this.elevator = new ElevatorModel(10, 10);
    this.view = new ElevatorView(this.elevator.people, this.elevator.maxFloor - 1);
    
    this.up.addEventListener('click', function() {
      controller.elevator.moveUp();
      controller.view.updatePeople();
    });
    this.down.addEventListener('click', function() {
      controller.elevator.moveDown();
      controller.view.updatePeopleDown();
    });
    this.add.addEventListener('click', function() {
      controller.elevator.addPeople();
      controller.view.updatePeople();
    });
    this.remove.addEventListener('click', function() {
      controller.elevator.removePeople();
      controller.view.updatePeople();
    });
  }
}

class ElevatorModel {

  constructor(maxFloor, maxPeople) {
    this.maxFloor = maxFloor;
    this.maxPeople = maxPeople;
    this.elevatorPosition = this.maxFloor - 1;
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
    if (this.elevatorPosition > 0) {
      this.elevatorDirection = 'up';
      this.elevatorPosition--;
    }
  }

  moveDown() {
    if (this.elevatorPosition < this.maxFloor - 1) {
      this.elevatorDirection = 'down';
      this.elevatorPosition++;
    }
  }

}

class ElevatorView {

  constructor(people, currentFloor) {
    this.lift = document.querySelector('ul');
    for (let i = 0; i < 10; i++) {
      this.lift.innerHTML += '<li></li>'
    }
    this.floor = document.getElementsByTagName('li');
    this.floor[currentFloor].innerText = 0;
    this.floor[currentFloor].style.backgroundColor = 'green';
  }

  updatePeople() {
    if (controller.elevator.elevatorPosition >= 0 && controller.elevator.elevatorPosition <= 9) {
      if (controller.elevator.elevatorPosition !== 9) {
        this.floor[controller.elevator.elevatorPosition + 1].innerText = '';
        this.floor[controller.elevator.elevatorPosition + 1].style.backgroundColor = 'white';
      }
      this.floor[controller.elevator.elevatorPosition].innerText = controller.elevator.people;
      this.floor[controller.elevator.elevatorPosition].style.backgroundColor = 'green';
    }
  }

  updatePeopleDown() {
    if (controller.elevator.elevatorPosition >= 0 && controller.elevator.elevatorPosition <= 9) {
      if (controller.elevator.elevatorPosition !== 0) {
        this.floor[controller.elevator.elevatorPosition - 1].innerText = '';
        this.floor[controller.elevator.elevatorPosition - 1].style.backgroundColor = 'white';
      }
      this.floor[controller.elevator.elevatorPosition].innerText = controller.elevator.people;
      this.floor[controller.elevator.elevatorPosition].style.backgroundColor = 'green';
    }
  }
}

let controller = new ElevatorController();
