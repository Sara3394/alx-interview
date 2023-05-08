#!/usr/bin/node

// this script prints all characters of a Star Wars movie

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], async function (error, response, body) {
  const data = JSON.parse(body).characters;
  for (const character of data) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        console.log(JSON.parse(body).name);
      });
    });
  }.catch(alert);
});
