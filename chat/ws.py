import ws
import json

class WSThread(ws.WSThread):
    URL = "/chat/"
    ACCOUNT = {
            "User": "ctare",
            "Secret": "TEST",
            }

    def run(self):
        while self.loop:
            data = json.loads(self.ws.recv(), "utf-8")
            print("{user}: {msg}".format(
                user=data.get("username"),
                msg=data.get("message"),
                ))
