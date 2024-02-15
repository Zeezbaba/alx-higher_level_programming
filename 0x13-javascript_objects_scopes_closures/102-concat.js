#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: node concatFiles.js <FileA> <FileB> <FileC>');
  process.exit(1);
}

const FileA = process.argv[2];
const FileB = process.argv[3];
const FileC = process.argv[4];

try {
  const content1 = fs.readFileSync(FileA, 'utf-8');
  const content2 = fs.readFileSync(FileB, 'utf-8');
  const concatenatedContent = content1 + content2;

  fs.writeFileSync(FileC, concatenatedContent);

  console.log(`Files "${FileA}" and "${FileB}" successfully concatenated to "${FileC}".`)
} catch (error) {
  console.error('An error occurred:', error.message);
  process.exit(1);
}
