#!/usr/bin/env python
"""
__init__.py - Phenny Init Module
Copyright 2008, Sean B. Palmer, inamidst.com
Copyright 2014, Tiit Pikma
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/

"""
import bot
import sys
import time

def run(config):
    delay = 20
    if hasattr(config, "delay"):
        if isinstance(config.delay, int):
            delay = config.delay
        else:
            print >> sys.stderr, "warning: config has invalid delay, "\
                    "defaulting to %i seconds" % delay

    while True:
        try:
            bot.Phenny(config).run(config.host, config.port)
        except KeyboardInterrupt:
            sys.exit()

        print >> sys.stderr, "warning: disconnected, "\
                "reconnecting in %i seconds..." % delay
        time.sleep(delay)

if __name__ == '__main__':
    print __doc__
