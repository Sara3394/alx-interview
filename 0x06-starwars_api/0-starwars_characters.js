#!/usr/bin/node

const request = require('request');
const movies = process.argv[2];

request.get(`https://swapi-api.hbtn.io/api/films/${movies}/`, async (_error, response, body) => {

  const arrayofcharacters = (JSON.parse(res.body).characters);
  for (const character of arrayofcharacters) {
    const ppl = await new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
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