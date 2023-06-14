#!/usr/bin/node
const args = process.argv;
const parsed = parseInt(args[2]);
if (isNaN(parsed)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parsed; i++) {
    console.log('X'.repeat(parsed));
  }
}
