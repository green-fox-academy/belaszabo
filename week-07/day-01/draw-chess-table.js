// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % % 
//  % % % %
//

for (let i = 1; i < 9; i++) {
  if (i % 2 === 0) {
    console.log(' %'.repeat(4))
  } else {
    console.log('% '.repeat(4))
  }
}
