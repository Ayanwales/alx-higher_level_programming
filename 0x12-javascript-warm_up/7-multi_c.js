#!/usr/bin/node
const args = process.argv;
const parsed = parseInt(args[2]);
if (!args[2]) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parsed; i++) {
    console.log('C is fun');
  }
}
