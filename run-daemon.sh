#!/bin/bash
# run-daemon.sh
# Runs xfinite in a dockerized server that triggers the script periodically.
#
# Usage:
#   # run in background
#   ./run-daemon.sh
#   
#   # to stop daemon (background only):
#   ./stop-daemon.sh
#
#   # run in foreground (automatically stops on CTRL-C)
#   ./run-daemon.sh -f

if [ "$1" == "-f" ]; then
    docker run -it --name xfinite --net host xfinite-daemon
    docker stop xfinite
    docker rm xfinite
else
    docker run -d --name xfinite --net host xfinite-daemon
fi
