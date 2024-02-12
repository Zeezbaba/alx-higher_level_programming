#!/usr/bin/node

const argCount = process.argv.length;

if (argCount > 2) {
	console.log('Argument found');
} else if (argCount > 3) {
	console.log('Arguments found');
} else {
	console.log('No argument');
}
