'use strict';

let TennisGame1 = function(player1Name, player2Name) {
  this.matchScore1 = 0;
  this.matchScore2 = 0;
  this.player1Name = player1Name;
  this.player2Name = player2Name;
};

TennisGame1.prototype.wonPoint = function(playerName) {
  playerName === "player1" ? this.matchScore1++ : this.matchScore2++;
};

TennisGame1.prototype.getScore = function() {
  let score = "";
  let tempScore = 0;
  if (this.matchScore1 === this.matchScore2) {
      let scores = {
        0: "Love-All",
        1: "Fifteen-All",
        2: "Thirty-All",
        'default': "Deuce"
      };
      return score = scores[this.matchScore1] || scores['default'];
  } else if (this.matchScore1 >= 4 || this.matchScore2 >= 4) {
    let minusResult = this.matchScore1 - this.matchScore2;
    if (minusResult === 1) {
      score = "Advantage player1";
    } else if (minusResult === -1) {
      score = "Advantage player2";
    } else if (minusResult >= 2) {
      score = "Win for player1";
    } else {
      score = "Win for player2";
      }
  } else {
    for (let i = 1; i < 3; i++) {
      if (i === 1) {
        tempScore = this.matchScore1;
      } else {
        score += "-";
        tempScore = this.matchScore2;
      }
      let newScore = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty"
      }
      score += newScore[tempScore];
    }
  }
  return score;
};

if (typeof window === "undefined") {
  module.exports = TennisGame1;
}
