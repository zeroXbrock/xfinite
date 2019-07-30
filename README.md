# xfinite

This thing does a speed test and tweets the result @Comcast. To use it, you'll need to make a Twitter app and get your own access keys. See [Twitter Developers](https://developer.twitter.com/en/docs/basics/apps/overview.html).

## Get Started

1. Make a .env file.
```sh
cp src/.env.example src/.env
```

2. Create a Twitter App and replace variables in `.env` with your own keys from Twitter.

## Run script once
Install dependencies and run...
```sh
cd src/
./start.sh
./run.sh
```

## Or... Run xfinite Daemon
To run a daemonized version that reports every half hour, [install docker](https://www.google.com/search?q=install+docker&rlz=1C5CHFA_enUS754US754&oq=install+docker), and run:
(you still need to create the .env file but you can skip everything else)
```sh
# assuming docker is installed and you're in the project root

# required: build daemon image
./build-daemon.sh

# option 1: run in background
./run-daemon.sh

# to stop daemon (background only):
./stop-daemon.sh

# OR...

# option 2: run in foreground (good for debugging; automatically stops on CTRL-C)
./run-daemon.sh -f
```

## Edit crontab
The crontab file (which dictates the schedule for xfinite to run) is here: `cron/xfinite-cron`. Feel free to change it as you see fit. I use [crontab.guru](https://crontab.guru/) to check my cron expressions. 

Remember to re-run `./build-daemon.sh` after changing the crontab file.

## Closing remarks
If you're actually going to run this, don't be a dick. Run it from a computer with a dedicated line to your router/modem because WiFi *does* slow it down.

## Upcoming Changes

* ✅ Daemonize (post every hour|day|week|...)
* Thresholds (don't tweet if within X% of advertised speed)
* Choose arguments (up & down only, etc.)
* Determine YOUR provider and tweet @ appropriately
* ✅ Post speedtest image w/ tweet
* Provide server-side reporting on clients' behalf (so n00bs can use it)

🖕@Comcast
