#!/usr/bin/node
exports.esrever = function (list) {
  const listReve = [];
  for (let i = list.length - 1; i >= 0; i--) {
    listReve.push(list[i]);
  }
  return (listReve);
};
