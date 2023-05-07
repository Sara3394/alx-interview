#!/usr/bin/node

const request = require('request');
const movies = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + id, async function (error, res, body) {
  
  const actors = JSON.parse(body).characters;
  for (const character of actors) {
    await new Promise((resolve, reject) => {
      request(character, (error, res, body) => {
        if (error) {
          console.log(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
