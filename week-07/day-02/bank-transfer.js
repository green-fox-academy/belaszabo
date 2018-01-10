'use strict';

var accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

// Create function that returns the name and balance of cash on an account

// Create function that transfers an amount of cash from one account to another
// it should have three parameters:
//  - from account_number
//  - to account_number
//  - amount of cash to transfer
//
// Log "404 - account not found" if any of the account numbers don't exist to the console.

function currentBalance(account) {
  accounts.forEach(function (e) {
    if (e['account_number'] === account) {
      console.log('Hello ' + e['client_name'] + ', your balance is ' + e['balance']);
    };
  });
}

// currentBalance(11234543);

function checkAccountNumber(account) {
  let validAccount = false;
  account.forEach(function (e) {
    if (e['account_number'] === account) {
      validaAccount = true;
    };
  });
}

function transferMoney(from, to, amount) {
  
}
