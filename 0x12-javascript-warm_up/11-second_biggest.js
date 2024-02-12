#!/usr/bin/node
function secondMax (integers) {
  const arrangedInt = integers.sort((a, b) => b - a);
  return arrangedInt[1] || 0;
}

const argument = process.argv.slice(2).map(Number);

if (argument.length <= 1) {
  console.log(0);
} else {
  console.log(secondMax(argument));
}
