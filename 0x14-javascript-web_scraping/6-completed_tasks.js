#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const doneTasks = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!doneTasks[todo.userId]) {
        doneTasks[todo.userId] = 1;
      } else {
        doneTasks[todo.userId] += 1;
      }
    }
  });
  console.log(doneTasks);
});
