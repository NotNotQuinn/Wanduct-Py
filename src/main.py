from parser import parsemsg

class WanductBot():
    def __init__(self, options):
        """Takes
        param options:
            A dict with the following defalt items that can be overwritten:
                {
                    "login": None
                    "password: None
                }
        """
        self.options = options