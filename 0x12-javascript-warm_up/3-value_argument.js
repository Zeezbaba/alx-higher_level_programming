#!/usr/bin/node
const [, argc] = process.argv;

if (argc) {
  console.log(argc);
} else {
  console.log('No argument');
}
