import os
from smac.scenario.scenario import Scenario
from smac.runhistory.runhistory import RunHistory
import numpy
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import argparse


def main():
    parser = argparse.ArgumentParser(description='test', fromfile_prefix_chars="@")
    parser.add_argument('-s', '--scenario_file', dest='scenario', required=True)
    parser.add_argument('-rh', '--runhistory_file', dest='runhistory', required=True)
    parser.add_argument('-o', '--output_file', dest='output', required=True)
    args = parser.parse_args()

    scenario = Scenario(args.scenario)
    # We load the runhistory, ...
    rh_path = os.path.join(args.runhistory)
    runhistory = RunHistory(aggregate_func=None)
    runhistory.load_json(rh_path, scenario.cs)

    cost_default = 1
    cost_incumbent = []
    for entry, values in runhistory.data.items():  # iterate over data because it is an OrderedDict
        config_id = entry.config_id  # look up config id
        config = runhistory.ids_config[config_id]  # look up config
        z_ = values.cost  # get cost
        if config_id == 1: #default configuration
            cost_default = z_
        else:
            cost_incumbent.append(z_)
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    x = range(len(cost_incumbent))
    ax1.plot(x, cost_incumbent, linestyle='None', marker='o', color="black")
    ax1.plot([0, len(x)], [cost_default, cost_default], 'r-')
    plt.ylabel("Loss")
    plt.xlabel("SMAC")
    plt.title("Performance of Incumbent compared to Default Configuration")
    plt.savefig(args.output)


if "__main__" == __name__:
    main()

