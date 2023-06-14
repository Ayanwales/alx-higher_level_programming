#!/usr/bin/node
/*  script that imports an array and creates
    new list with each value equal to the value of the initial list,
    multipled by the index in the list
 */

const list = require('./100-data').list;
const listNew = list.map((value, index) => { return value * index; });
console.log(list);
console.log(listNew);
