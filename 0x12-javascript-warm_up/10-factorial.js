#!/usr/bin/node
/* computes and prints a factorial */

const args = process.argv;
const inta = parseInt(args[2]);

function factory (a) {
  if (a === 0) {
    return (1);
  } else {
    return (a * factory(a - 1));
  }
}

if (isNaN(inta)) {
  console.log(1);
} else {
  console.log(factory(inta));
}
