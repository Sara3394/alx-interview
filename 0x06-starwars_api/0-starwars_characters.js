#!/usr/bin/node

const request = require('request');
const movies = process.argv[2];

request.get(`https://swapi-api.hbtn.io/api/films/${movies}/`, async (_error, response, body) => {
   _error && console.log(_error);

  const arrayofcharacters = (JSON.parse(response.body).characters);
  for (const character of arrayofcharacters) {
    await new Promise((resolve, reject) => {
      request(character, (_error, response, body) => {
        _error && console.log(_error);
  
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
   
