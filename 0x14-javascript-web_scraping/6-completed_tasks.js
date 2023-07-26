#!/usr/bin/node
/* script that computes the number of tasks completed by user id */

const args = process.argv;
const url = args[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const data = JSON.parse(body);
  const complete = {};
  for (let i = 0; i < data.length; i++) {
    if (data[i].completed === true) {
      if (complete[data[i].userId]) {
        complete[data[i].userId] = complete[data[i].userId] + 1;
      } else {
        complete[data[i].userId] = 1;
      }
    }
  }
  console.log(complete);
});
