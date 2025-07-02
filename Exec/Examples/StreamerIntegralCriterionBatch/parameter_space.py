#!/usr/bin/env python

import json
import numpy as np

# Set up the parameter space dictionary as you see fit.

# Either run this script to generate the default json file, or import this
# script directly through the --parameter-space-file option in the job script.

pspace = {
        "pressure" : {
            "target" : "chemistry",
            "uri" : ["gas", "law", "my_ideal_gas", "pressure"],
            "values" : list(np.arange(1e5, 11e5, 1e5))
            },
        "geometry_radius" : {
            "target" : "input",
            "uri" : "Vessel.rod_radius",
            "values" : [ [0.0, 25e-3] ]
            },
        }

if __name__ == '__main__':
    with open('parameter_space.json', 'w') as f:
        json.dump(pspace, f, indent=4)

