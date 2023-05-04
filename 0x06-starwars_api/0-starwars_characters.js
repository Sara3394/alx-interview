#!/usr/bin/node

//this is a script which prints all characters of a Star Wars movie

const request = require('request');

const movies = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movies}`;

request(url, async (err, res, body) => {
  err && console.log(err);

  const arrayofcharacters = (JSON.parse(res.body).characters);
  for (const character of arrayofcharacters) {
    await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        err && console.log(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
