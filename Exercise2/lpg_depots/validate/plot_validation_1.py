import os
from smac.scenario.scenario import Scenario
from smac.runhistory.runhistory import RunHistory
import numpy
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

"""
This file runs SMAC and then restores the run with an extended computation
budget. This will also work for SMAC runs that have crashed and are continued.
"""

def main():
    scenario = Scenario("scenario.txt")
    # We load the runhistory, ...
    rh_path = os.path.join("validated_runhistory.json")
    runhistory = RunHistory(aggregate_func=None)
    runhistory.load_json(rh_path, scenario.cs)
    
    cost_default = []
    cost_incumbent = []
    for entry,values in runhistory.data.items():  # iterate over data because it is an OrderedDict
        config_id = entry.config_id  # look up config id
        config = runhistory.ids_config[config_id]  # look up config
        z_ = values.cost  # get cost
        if config_id == 1:
            cost_default.append(z_)
        else:
            cost_incumbent.append(z_)
    plt.plot(cost_incumbent,cost_default,'ro', color="gray")

    x = numpy.linspace(0,max(max(cost_incumbent),max(cost_default)),0.1)
    #plt.plot(x,x,'k',color="red")
    plt.ylabel("Default Configuration")
    plt.xlabel("Incumbent of run 1")
    plt.title("Performance of Incumbents compared to Default Configuration")
    
    plt.savefig("perf_inc_vs_def.png")
if "__main__" == __name__:
    
    main()
