#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, async (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const characters = JSON.parse(res.body).characters;

  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        if (err) {
          console.log(err);
          reject(err);
          return;
        }

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
