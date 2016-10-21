#!/usr/bin/env python

import sys

import numpy as np
import matplotlib.pyplot as plt

def graph(fig, thread_ids, data, xticks, xticklabels):
    # Create a 4-plot graph of each property
    for i in range(1, 5):
        ax = fig.add_subplot(2, 2, i)
        for thread_id in thread_ids:
            ax.plot(data[thread_id][:, 0], data[thread_id][:, i])
        ax.set_xlabel("Minutes")
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

    plt.tight_layout()

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
    xticks = np.arange(0, max_time - min_time, 60000)
    xticklabels = ["{:.0f}".format(xtick / 60000.) for xtick in xticks]

    # Seperate data for each unique thread id
    data = dict()
    for thread_id in thread_ids:
        data[thread_id] = data_csv[np.where(data_csv[:, 0] == thread_id)[0], 1:]
        data[thread_id][:, 0] -= min_time

    # Compute moving average
    running_average_window = 5 * 1000
    time_splits = np.arange(0, max_time - min_time, running_average_window)
    time_windows = [(time_splits[i], time_splits[i + 1]) for i in range(time_splits.shape[0] - 1)]
    data_ma = dict()
    for thread_id in thread_ids:
        data_ma[thread_id] = np.zeros((len(time_windows), data[thread_id].shape[1]), np.uint32)
        for i in range(len(time_windows)):
            time_window = time_windows[i]
            idx = np.where(np.logical_and(time_window[0] <= data[thread_id][:, 0], data[thread_id][:, 0] <= time_window[1]))[0]
            data_ma[thread_id][i, 1:] = np.average(data[thread_id][idx, 1:], axis=0)
            data_ma[thread_id][i, 0] = (time_window[0] + time_window[1]) / 2.

    # Create graph
    graph(plt.figure(), thread_ids, data_ma, xticks, xticklabels)

    # Create a tight layout and display
    plt.show()

if __name__ == "__main__":
    main(sys.argv)
