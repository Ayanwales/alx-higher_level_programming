#!/usr/bin/node
/*  script that prints all characters of a Star Wars movie.
    with a given movie ID, this code presents callback hell issues
    fixed by use of promise and wait.
 */

const args = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];
const request = require('request');

function listAll (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (res.statusCode === 200 && !error) {
        resolve(body);
        const data = JSON.parse(body);
        const dataChar = data.characters;
        return dataChar;
      } else {
        console.log(error);
      }
    });
  });
}
function dataChar (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (res.statusCode === 200 && !error) {
        resolve(body);
        const data = JSON.parse(body);
        console.log(data.name);
      } else {
        reject(error);
      }
    });
  });
}
async function iter () {
  const fistRequest = await listAll(url);
  const numChar = JSON.parse(fistRequest).characters.length;
  for (let i = 0; i < numChar; i++) {
    const urlCh = JSON.parse(fistRequest).characters[i];
    await dataChar(urlCh);
  }
}
iter();
