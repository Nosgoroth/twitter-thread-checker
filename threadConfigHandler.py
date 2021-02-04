import json

class ThreadConfigHandler:

    filename = 'threads.json'
    threads = None

    def __init__(self):
        self._read()

    def _read(self):
        try:    
            with open(self.filename, 'r') as f:
                self.threads = json.load(f)
        except:
            self.threads = {}
            raise
    
    def _write(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.threads, f)
        except:
            pass

    def iterate(self):
        for thread in self.threads:
            yield self.threads[thread]

    def addNewThread(self, id):
        self.threads[id] = {
            "id": id,
            "enabled": True,
            "latestId": id
        }
        self._write()

    def setThreadLatestId(self, threadId, latestId):
        self.threads[threadId]["latestId"] = latestId
        self._write()
    
    def enableThread(self, id):
        self.threads[id]["enabled"] = True
        self._write()

    def disableThread(self,id):
        self.threads[id]["enabled"] = False
        self._write()

