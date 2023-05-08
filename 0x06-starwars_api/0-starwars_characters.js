#!/usr/bin/node

// this script prints all characters of a Star Wars movie

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], async function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const actors = JSON.parse(body).characters;
  for (const character of actors) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        }
        console.log(JSON.parse(body).name);
        .catch(alert);
      });
    });
  }
});
