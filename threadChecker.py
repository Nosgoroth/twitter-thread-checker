#!/usr/local/bin/python3

#Standard library
from optparse import OptionParser
from html import unescape

# Program files
from pushover import pushover
from twitterThreadMining import getAllTweetsInThreadAfterThis, init as initTwitterApi
from threadConfigHandler import ThreadConfigHandler

threadconfig = ThreadConfigHandler()

def listThreads():
    for thread in threadconfig.iterate():
        print("* %s %s" % ( thread["id"], "DISABLED" if not thread["enabled"] else "" ) )

def notifyThreads():
    initTwitterApi()
    for thread in threadconfig.iterate():
        print("\n\n--------------\n--- Thread %s ---\n--------------\n" %
              thread["id"])
        if not thread["enabled"]:
            print("Thread is disabled")
            continue
        newTweets = getAllTweetsInThreadAfterThis(
            thread["latestId"], includeThisTweet=False)
        if len(newTweets) > 0:
            print("%s new tweets" % len(newTweets))
            for tweet in newTweets:
                text = unescape(tweet.full_text)
                print("\n\n")
                print(text)
                pushover(text)
            lastTweet = newTweets[len(newTweets)-1]
            threadconfig.setThreadLatestId(thread["id"], lastTweet.id_str)
        else:
            print("No new tweets")

def main():
    parser = OptionParser(usage="Usage: %prog [options]")


    parser.add_option("--list", action="store_true", dest="list", help="List all threads")
    parser.add_option("--notify", action="store_true", dest="notify",
                        help="Process all active threads and send notifications")
    parser.add_option("--add", action="store", dest="add", help="Add a thread")
    parser.add_option("--enable", action="store", dest="enable", help="Enable a thread")
    parser.add_option("--disable", action="store", dest="disable", help="Disable a thread")
                    
    (options, args) = parser.parse_args()

    if options.list:
        listThreads()
    elif options.notify:
        notifyThreads()
    elif options.add:
        try:
            threadconfig.addNewThread(options.add)
            print("Thread %s added" % options.add)
        except:
            print("Couldn't add thread")
    elif options.enable:
        try:
            threadconfig.enableThread(options.enable)
            print("Thread %s enabled" % options.enable)
        except:
            print("Couldn't enable thread")
    elif options.disable:
        try:
            threadconfig.disableThread(options.disable)
            print("Thread %s disabled" % options.disable)
        except:
            print("Couldn't disable thread")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
