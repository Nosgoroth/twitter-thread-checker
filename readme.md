# Twitter Thread Checker

Checks and notifies of updates to twitter threads. Run `./threadChecker.py` to see all available actions.

## Following threads

* First, identify a Twitter thread you want to follow and obtain the id of its latest tweet (grab the number from the address bar in your browser).
* Run `./threadChecker.py --add 1356694358947471367` to start following the thread.
* You can then run `./threadChecker.py --notify` to run through all your followed threads and send notifications. You may want to cron this.
* You can disable checking the thread at any time with `./threadChecker.py --disable 1356694358947471367`, and then enable it again with `./threadChecker.py --enable 1356694358947471367`.
* List your followed threads with `./threadChecker.py --list`.

## Dependencies and acknoledgments

Uses Python 3 and the Tweepy library. Tested on Python 3.9. Uses the Pushover service for notifications.

Uses code from [lihkinVerma](https://github.com/lihkinVerma/Twitter-thread-mining).
