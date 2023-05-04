#!/usr/bin/node

const request = require('request');
const movies = process.argv[2];

request.get(`https://swapi-api.hbtn.io/api/films/${movies}/`, async (_error, ServerResponse, body) => {
   _error && console.log(_error);

  const arrayofcharacters = (JSON.parse(ServerResponse.body).characters);
  for (const character of arrayofcharacters) {
    await new Promise((resolve, reject) => {
      request(character, (_error, ServerResponse, body) => {
        _error && console.log(_error);
  
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
   
