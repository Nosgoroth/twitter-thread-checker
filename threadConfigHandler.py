import json, pathlib
from os.path import join as pathjoin

class ThreadConfigHandler:

    filename = 'threads.json'
    threads = None

    def __init__(self):
        self._read()

    def getAbspath(self):
        return pathjoin(pathlib.Path(__file__).parent.absolute(), self.filename)

    def _read(self):
        try:    
            with open(self.getAbspath(), 'r') as f:
                self.threads = json.load(f)
        except:
            self.threads = {}
            raise
    
    def _write(self):
        try:
            with open(self.getAbspath(), 'w') as f:
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
    
    def enableThread(self, threadId):
        self.threads[threadId]["enabled"] = True
        self._write()

    def disableThread(self, threadId):
        self.threads[threadId]["enabled"] = False
        self._write()

