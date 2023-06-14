#!/usr/bin/node
/* function that returns the number of occurrences in a list */

exports.nbOccurences = function (list, searchElement) {
  const listSorted = list.sort();
  const isEqualTo = (element) => element === searchElement;
  const isInList = listSorted.findIndex(isEqualTo);
  let count = 0;
  if (isInList !== -1) {
    count = 1;
    for (let i = isInList + 1; i < list.length; i++) {
      if (listSorted[i] === searchElement) {
        count = count + 1;
      } else {
        break;
      }
    }
  }
  return (count);
};
