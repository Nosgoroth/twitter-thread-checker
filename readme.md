# Twitter Thread Checker

Checks and notifies of updates to twitter threads.

CLI management of threads in watch not implemented, for now edit `threads.json` directly. The format is:

```js
{
    // Each thread in this format:
    "1356694358947471367": {
        "id": "1356694358947471367", // Same as dictionary key
        "latestId": "1356694358947471367", // To start, same as id.
        "enabled": true // You can disable checking threads with this
    }
}
```
