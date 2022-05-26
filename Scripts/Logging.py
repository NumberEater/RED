class Mode:
    MODE_ERROR = 0
    MODE_WARNING = 1
    MODE_INFO = 2
    MODE_NONE = 3


class Logger:

    def __init__(self, initial_mode):
        self.mode = initial_mode

    def set_mode(self, mode):
        self.mode = mode

    def Error(self, message):
        if self.mode <= Mode.MODE_ERROR:
            print("ERROR: {0}".format(message))

    def Warning(self, message):
        if self.mode <= Mode.MODE_WARNING:
            print("WARNING: {0}".format(message))

    def Info(self, message):
        if self.mode <= Mode.MODE_INFO:
            print("INFO: {0}".format(message))
