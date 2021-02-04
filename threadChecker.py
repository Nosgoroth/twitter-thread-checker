#!/usr/local/bin/python3

#Standard library
from pprint import pprint

# Program files
from pushover import pushover
from twitterThreadMining import getAllTweetsInThreadAfterThis
from threadConfigHandler import ThreadConfigHandler


if __name__ == '__main__':
    threadconfig = ThreadConfigHandler()

    for thread in threadconfig.iterate():
        print("\n\n--------------\n--- Thread %s ---\n--------------\n" % thread["id"])
        if not thread["enabled"]:
            print("Thread is disabled")
            continue
        newTweets = getAllTweetsInThreadAfterThis(thread["latestId"], includeThisTweet=False)
        if len(newTweets) > 0:
            print("%s new tweets" % len(newTweets))
            for tweet in newTweets:
                print("\n\n")
                print(tweet.full_text)
                pushover(tweet.full_text)
            lastTweet = newTweets[len(newTweets)-1]
            threadconfig.setThreadLatestId(thread["id"], lastTweet.id_str)
        else:
            print("No new tweets")
