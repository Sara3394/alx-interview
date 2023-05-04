#!/usr/bin/node

// this is a script which prints all characters of a Star Wars movie

const request = require('request');

const movie = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movie}`;

request(url, async (err, res, body) => {
  if (err) {
    console.log(err);
  }
  for (const character of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        if (err) {
          reject(err);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
