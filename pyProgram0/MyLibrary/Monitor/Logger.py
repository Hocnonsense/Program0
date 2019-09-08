"""
    version 1.0.0
"""

import sys, time

class Logger(object):
    """
    sys.stdout = Logger( _yourlogfilename_ )

    then everything in python will save in your log file.
"""
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

def savelog(filename = "programLog.txt"):
    sys.stdout = Logger(filename)
    print(time.strftime("new LOG at %Y-%m-%d %H:%M:%S :", time.localtime()))
