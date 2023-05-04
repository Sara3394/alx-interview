#!/usr/bin/node

// this is a script which prints all characters of a Star Wars movie

const request = require('request');
const mov = process.argv[2];

request.get(`https://swapi-api.hbtn.io/api/films/${mov}/`, async (err, res, body) => {
  for (const character of JSON.parse(body).characters) {
    const ppl = await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
    console.log(ppl);
  }
});
