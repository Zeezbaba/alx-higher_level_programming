#!/usr/bin/node

const dict = require('./101-data.js').dict;

const idOccurences = (dictOccurence) => {
  const userIdOccurences = {};

  for (const id in dictOccurence) {
    const occurences = dictOccurence[id];

    if (!(occurences in userIdOccurences)) {
      userIdOccurences[occurences] = [];
    }
    userIdOccurences[occurences].push(id);
  }
  return userIdOccurences;
}

const newDict = idOccurences(dict);
console.log(newDict);
