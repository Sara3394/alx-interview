#!/usr/bin/node

// this is a script that prints all characters of a Star Wars movie

const request = require('request');
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
