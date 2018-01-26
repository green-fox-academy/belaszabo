'use strict';

class MysqlModel {
  getAllPosts() {
    let dataToSend;
    connection.query('SELECT * FROM posts', (err, rows) => {
      if (err) throw err;
  
      console.log('Data received from reddit database!');
      dataToSend = {
        "posts": 
          rows
      }
    });
  return dataToSend;
  }
}

module.exports = new MysqlModel();