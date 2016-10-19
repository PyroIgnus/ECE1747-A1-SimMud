#!/usr/bin/env python

import sys
import subprocess

def main(args):
    # Usage instructions
    if len(args) < 6 or len(args) > 7:
        print("Usage: {} <server> <client> <config> <port> <logfile> [<client_N>]".format(args[0]))
        return

    # Give meaningful names to arguments
    server, client = args[1], args[2]
    config, port   = args[3], args[4]
    logfile        = args[5]

    # Make sure argument has some default value
    client_n = int(args[6]) if len(args) == 7 else 100

    # Create a server process
    subprocess.Popen([server, config, port, logfile])

    # Create N client processes
    for i in range(client_n):
        subprocess.Popen([client, "localhost:" + port])

if __name__ == "__main__":
    main(sys.argv)
