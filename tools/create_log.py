#!/usr/bin/env python

import os
import sys
import subprocess
import time

def main(args):
    # Usage instructions
    if len(args) < 6 or len(args) > 8:
        print("Usage: {} <server> <client> <config> <port> <logfile> [<client_N>] [<run_time>]".format(args[0]))
        return

    # Give meaningful names to arguments
    server, client = args[1], args[2]
    config, port   = args[3], args[4]
    logfile        = args[5]

    # Make sure argument has some default value
    client_n = int(args[6]) if len(args) >= 7 else 500
    run_time = int(args[7]) if len(args) == 8 else 1

    # Create a server process
    server = subprocess.Popen([server, config, port, logfile])

    # Create N client processes
    clients = [0] * client_n
    for i in range(client_n):
        clients[i] = subprocess.Popen([client, "localhost:" + port], stdout=open(os.devnull, 'wb'))

    # Wait for 5 minutes
    time.sleep(run_time * 60)

    # Kill server
    server.kill()

    # Kill the children
    for i in range(client_n):
        clients[i].kill()

if __name__ == "__main__":
    main(sys.argv)
