// Create a prison function, that has your name as a private fugutive variable
// The function should return an object that has two methods:
//  - visit() // logs "[yourname] is visited [x] time(s)" to the console.
//    - the [x] times displayes the numbers the function is called
//    - If the fugitive variable is empty, then display "Nobody is here anymore"
//  - escape() // logs "BREAKING NEWS, [yourname] escaped the prison" to the console.
//    - it should empties the fugitive variable

function prison(name) {
  let fugitive = name;
  function Prisoner() {
    this.visitsNumber = 0;
    this.visit = function () {
      if (fugitive !== '') {
        this.visitsNumber++;
        console.log(fugitive + ' is visited ' + this.visitsNumber + ' time(s)');
      } else {
        console.log('Nobody is here anymore');
      }
    }
    this.escape = function () {
      console.log('BREAKING NEWS, ' + fugitive + ' escaped the prison');
      fugitive = '';
    }
  };
  return new Prisoner;
}

const alcatraz = prison('Sad Panda');

alcatraz.visit() // Sad Panda is visited 1 time(s)
alcatraz.visit() // Sad Panda is visited 2 time(s)
alcatraz.escape() // BREAKING NEWS, Sad Panda escaped the prison
alcatraz.visit() // Nobody is here anymore
