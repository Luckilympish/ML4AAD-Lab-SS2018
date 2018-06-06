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
    parser.add_argument('-s', '--scenario_SMAC', dest='scenario_SMAC', required=True)
    parser.add_argument('-rh', '--runhistory_SMAC', dest='runhistory_SMAC', required=True)

    parser.add_argument('-sR', '--scenario_ROAR', dest='scenario_ROAR', required=True)
    parser.add_argument('-rhR', '--runhistory_ROAR', dest='runhistory_ROAR', required=True)
    parser.add_argument('-o', '--output', dest='output', required=True)
    args = parser.parse_args()

    scenario_SMAC = Scenario(args.scenario_SMAC)
    scenario_ROAR = Scenario(args.scenario_ROAR)
    # We load the runhistory, ...
    rh_path_SMAC = os.path.join(args.runhistory_SMAC)
    runhistory_SMAC = RunHistory(aggregate_func=None)
    runhistory_SMAC.load_json(rh_path_SMAC, scenario_SMAC.cs)

    rh_path_ROAR = os.path.join(args.runhistory_ROAR)
    runhistory_ROAR = RunHistory(aggregate_func=None)
    runhistory_ROAR.load_json(rh_path_ROAR, scenario_ROAR.cs)

    cost_SMAC = []
    cost_ROAR = []
    for entry, values in runhistory_SMAC.data.items():  # iterate over data because it is an OrderedDict
        if len(cost_SMAC) == 20:
            break;
        config_id = entry.config_id  # look up config id
        config = runhistory_SMAC.ids_config[config_id]  # look up config
        z_ = values.cost  # get cost
        cost_SMAC.append(z_)
    for entry, values in runhistory_ROAR.data.items():  # iterate over data because it is an OrderedDict
        config_id = entry.config_id  # look up config id
        config = runhistory_ROAR.ids_config[config_id]  # look up config
        z_ = values.cost  # get cost
        cost_ROAR.append(z_)

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    x = range(20) #comparison is done only for 20 runs
    #plot SMAC and ROAR performance
    ax1.plot(cost_SMAC, 'o', color='red',label='SMAC')
    ax1.plot(cost_ROAR, '+', color='blue',label='ROAR')

    plt.ylabel("Loss")
    plt.xlabel("#Evaluations")
    plt.title("Performance of SMAC compared to ROAR")
    plt.legend()
    plt.savefig(args.output)


if "__main__" == __name__:
    main()
