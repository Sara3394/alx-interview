#!/usr/bin/node
// this is a script that prints all characters of a Star Wars movie

const request = require('request');
const id = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + id, async function (err, res, body) {
  if (err) throw err;
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        if (err) {
          console.log(err);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
