# Now Again Example

## Installation

Clone this repo, then run `npm install`.

You'll also want to install the [now tools](https://zeit.co/download).

## Configuration

Run `npm run setup` to save your now token as a secret. This will allow your deployed server to deploy tasks.

## Run a single task locally

You can install the now-again command line tool globally with `npm i -g ragtagopen/now-again`.

With that installed, you can run a single job with a command like so

    now-again run moo --input yooooooo

## Deploy the server (with scheduler)

Run `npm run deploy` to deploy the example, mapping the token secret to an environment variable.

Don't forget to use the `now scale` command to fix the instance count to 1, or else the scheduler job will go to sleep:

1. Run `now ls` to see your deployments.
1. Copy the url that starts with "now-again-example"
1. Run `now scale [now-again-example-url] 1`

Now your deployment will be set to 1 instance, and it won't go to sleep.
