const nowAgain = require('now-again')

console.log("using token:", process.env.AUTH_TOKEN)
// just run the scheduler for now
nowAgain.scheduler()
