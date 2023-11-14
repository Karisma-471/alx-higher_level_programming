#!/usr/bin/node

const argv1 = process.argv[2];

const numb = parseInt(argv1);

if (isNaN(numb)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + numb);
}
