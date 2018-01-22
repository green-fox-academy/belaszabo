'use strict';

let TennisGame1 = function(player1Name, player2Name) {
  this.matchScore1 = 0;
  this.matchScore2 = 0;
  this.player1Name = player1Name;
  this.player2Name = player2Name;
};

TennisGame1.prototype.wonPoint = function(playerName) {
  if (playerName === "player1") {
    this.matchScore1 ++;
  } else {
    this.matchScore2 ++;
  }
};

TennisGame1.prototype.getScore = function() {
  let score = "";
  let tempScore = 0;
  if (this.matchScore1 === this.matchScore2) {
    switch (this.matchScore1) {
      case 0:
        score = "Love-All";
        break;
      case 1:
        score = "Fifteen-All";
        break;
      case 2:
        score = "Thirty-All";
        break;
      default:
        score = "Deuce";
        break;
    }
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
      switch (tempScore) {
        case 0:
          score += "Love";
          break;
        case 1:
          score += "Fifteen";
          break;
        case 2:
          score += "Thirty";
          break;
        case 3:
          score += "Forty";
          break;
        }
    }
  }
  return score;
};

if (typeof window === "undefined") {
  module.exports = TennisGame1;
}
