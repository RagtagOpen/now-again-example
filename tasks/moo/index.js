require('dotenv').config()
const cowsay = require('cowsay')
console.log(`EOF: ${cowsay.say({ text: process.env.INPUT })}`)