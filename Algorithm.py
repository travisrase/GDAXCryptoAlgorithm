import Purchase
import WebsocketClient
import AuthenticatedClient

class Algorithm:
    "Running algoritm class to be used by purchase objects"
    def __init__(self, arg):
        super(Algorithm, self).__init__()
        self.arg = arg
