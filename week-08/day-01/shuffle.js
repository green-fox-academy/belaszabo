let Shuffler = {
  cash: 10000,
  temp: 1,
  pick: function() {
    this.cash -= 1000;
    if (this.temp % 2 === 0) {
      Panama.deposit(1000);
    } else {
      Cyprus.deposit(1000);
    }
    this.temp++;
  }
};

const Panama = {
  cash: 0,
  name: 'Panama',
  tax: '1%',
  deposit: function(amt) {
    this.cash += amt;
  }
}

const Cyprus = {
  cash: 0,
  name: 'Panama',
  tax: '5%',
  deposit: function(amt) {
    this.cash += amt;
  }
}

Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000
Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000

console.log( Panama.cash ) // 2000 
console.log( Cyprus.cash ) // 2000 