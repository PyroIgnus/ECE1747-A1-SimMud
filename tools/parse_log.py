#!/usr/bin/env python

import sys

import numpy as np
import matplotlib.pyplot as plt

def main(args):
    # Usage instructions
    if len(args) != 2:
        print("Usage: {} <logfile>".format(args[0]))
        return

    # Load csv file
    logfile = args[1]
    data_csv = np.genfromtxt(logfile, dtype = None, delimiter = ',')

    # Get unique thread ids, min and max time
    thread_ids = np.unique(data_csv[:, 0])
    min_time = np.min(data_csv[:, 1])
    max_time = np.max(data_csv[:, 1])

    # Set plot ticks for displaying ticks spent
    xticks = np.linspace(0, max_time - min_time, 8)
    xticklabels = ["{:.0f}".format(xtick) for xtick in xticks]

    # Seperate data for each unique thread id
    data = dict()
    for thread_id in thread_ids:
        data[thread_id] = data_csv[np.where(data_csv[:, 0] == thread_id)[0], 1:]
        data[thread_id][:, 0] -= min_time


    # Create a 4-plot graph of each property
    fig = plt.figure()
    for i in range(1, 5):
        ax = fig.add_subplot(2, 2, i)
        for thread_id in thread_ids:
            ax.plot(data[thread_id][:, 0], data[thread_id][:, i])
        ax.set_xlabel("Ticks")
        ax.set_xticks(xticks)
        ax.set_xticklabels(xticklabels, rotation=45)

    # Label all y axes
    plt.subplot(2, 2, 1)
    plt.ylabel("Number of Client Requests")
    plt.subplot(2, 2, 2)
    plt.ylabel("Ticks spent for Requests")
    plt.subplot(2, 2, 3)
    plt.ylabel("Number of Client Updates")
    plt.subplot(2, 2, 4)
    plt.ylabel("Ticks spent for Updates")

    # Create a tight layout and display
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main(sys.argv)
