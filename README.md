# xfinite

This thing does a speed test and tweets the result @Comcast. To use it, you'll need to make a Twitter app and get your own access keys. See [Twitter Developers](https://developer.twitter.com/en/docs/basics/apps/overview.html).

## Get Started

0. Make a .env file.
```sh
cp .env.example .env
```

1. Create a Twitter App and replace variables in `.env` with your own keys from Twitter.

2. Install dependencies and run...
```sh
./start.sh
./run.sh
```

If you're actually going to run this, don't be a dick. Run it from a computer with a dedicated line to your router/modem because WiFi *does* slow it down.

Upcoming Changes:

* Daemonize (post every hour|day|week|...)
* Thresholds (don't tweet if within X% of advertised speed)
* Choose arguments (up & down only, etc.)
* Determine YOUR provider and tweet @ appropriately
* ✅ Post speedtest image w/ tweet
* Provide server-side reporting on clients' behalf (so n00bs can use it)

🖕@Comcast
