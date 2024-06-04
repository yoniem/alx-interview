#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        resolve(JSON.parse(body).name);
      });
    });
  };

  const fetchAllCharacters = async () => {
    for (const characterUrl of characters) {
      try {
        const characterName = await fetchCharacter(characterUrl);
        console.log(characterName);
      } catch (error) {
        console.error(error);
      }
    }
  };

  fetchAllCharacters();
});
