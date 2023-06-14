#!/usr/bin/node
const args = process.argv;
const newArgs = args.slice(2).sort(function (a, b) { return a - b; });
if (args.length <= 3) {
  console.log(0);
} else {
  console.log(newArgs[newArgs.length - 2]);
}
