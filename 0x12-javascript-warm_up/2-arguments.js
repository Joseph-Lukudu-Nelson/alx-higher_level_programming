#!/usr/bin/node
// a script that prints a message depending of the number of arguments passed:

const Argument = process.argv.length;
console.log(Argument === 2 ? ' No argument ' : Argument === 3 ? ' Argument found ' : ' Arguments found ');
