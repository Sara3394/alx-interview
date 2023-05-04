#!/usr/bin/node

const request = require('request');
const mov = process.argv[2];

request.get(`https://swapi-api.hbtn.io/api/films/${mov}/`, async (err, res, body) => {
  for (const character of JSON.parse(body).characters) {
    const ppl = await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
    console.log(ppl);
  }
});
