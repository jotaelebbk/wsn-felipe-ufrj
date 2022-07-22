#config.py

import math

# Describe the scenarios that will be simulated
# scenarios should be described in the following format:
# scenario_name = (routing_topology, sleep_scheduling, aggregation_model)
# where routing_topology may be:
#   
#   'LEACH': LEACH
#   'S-LEACH ': Novo algoritmo
#   'CAMAW  ': Novo algoritmo
#   'H-CAMAW  ': Novo algoritmo
#   
# and sleep_scheduling may be:
#   None                 : No sleep scheduling (mind that None is not a string)
#   'Pso'                : Particle Swarm Optimization
#   'ModifiedPso'        : Modified PSO
#   'GeneticAlgorithm'   : Genetic Algorithm
# and aggregation_model may be:
#   'zero'  : Zero cost
#   'total' : 100% cost
#   'linear': TODO spec
#   'log'   : log cost
# the 4th argument is the nickname of that plot, if not specified (None),
# then the name is: routing_topology + sleep_scheduling

# for convenience, the scenarios list also accepts commands that are
# executed in run.py

scenario0 = ('LEACH',    None, 'zero', 'LEACH' )
scenario1 = ('SLEACH', None, 'zero',  'SLEACH')
#scenario11 = ('FCM', None, 'zero',  'FCM')
#scenario2 = ('CAMAW',   None, 'zero',  'CAMAW')
#scenario3 = ('HCAMAW',   None, 'zero',  'HCAMAW')
#scenario4 = ('HCAMAW',   None, 'zero',  'HCAMAW')
#scenario5 = ('LEACH',  'Pso',              'zero',  'Pso')
#scenario6 = ('LEACH',  'Ecca',             'zero',  'ECCA')
#scenario7 = ('LEACH',  'GeneticAlgorithm', 'zero',  'GeneticAlgorithm')
#scenario31 = ('LEACH',   None,              'zero',  'BS at (125,125)')
#scenario32 = ('LEACH',   None,              'zero',  'BS at (65,65)')
#scenario33 = ('LEACH',   None,              'zero',  'BS at (0,0)')
#scenario34 = ('LEACH',   None,              'zero',  'BS at (-65,-65)')
# list with all scenarios to simulate

# example of configuration to get first part of results
scenarios = [
              "cf.FITNESS_ALPHA=0.5",
              "cf.FITNESS_BETA=0.5",
              scenario0,
              scenario1,
	      #scenario11,
              #scenario2,
              #scenario3,
	      #scenario4,
              #scenario5,
	      "plot_clusters(network)",
              #"plot_time_of_death(network)",
              "plot_traces(traces)",
              "network.get_BS().pos_y=-75.0",
#              scenario3,
#              scenario0,
#              scenario1,
#              scenario2,
#              scenario5,
#              scenario4,
              "save2csv(traces)",
              
            ]

#scenarios = [*
              #"cf.FITNESS_ALPHA=0.7",*
              #"cf.FITNESS_BETA=0.3",*
             #"cf.FITNESS_ALPHA=0.34",
             #"cf.FITNESS_BETA=0.33",
             #"cf.FITNESS_GAMMA=0.33",
              #scenario0,       *     
              #scenario1,   *
              #scenario2,       
              #scenario3,
              #scenario4,
#              "cf.FITNESS_ALPHA=0.34",
#              "cf.FITNESS_BETA=0.33",
#              "cf.FITNESS_GAMMA=0.33",
              #scenario6,
              #scenario5,
              #scenario7,
#              scenario6,
#              #'cf.BS_POS_X=65.0',
#              #'cf.BS_POS_Y=65.0',
#              #scenario32,
#              #'cf.BS_POS_X=0.0',
#              #'cf.BS_POS_Y=0.0',
#              #scenario33,
#              #'cf.BS_POS_X=-65.0',
#              #'cf.BS_POS_Y=-65.0',
#              #scenario34,
#              "save2csv_raw(traces)", *
#              "plot_traces(traces)", *
#            ] *

#scenarios = [
#              "cf.FITNESS_ALPHA=0.5",
#              "cf.FITNESS_BETA=0.5",
#              scenario4,
#              scenario5,
#              scenario6,
#              "cf.FITNESS_ALPHA=0.75",
#              "cf.FITNESS_BETA=0.25",
#              scenario4,
#              scenario5,
#              scenario6,
#              "cf.FITNESS_ALPHA=0.25",
#              "cf.FITNESS_BETA=0.75",
#              scenario4,
#              scenario5,
#              scenario6,
#              "cf.FITNESS_ALPHA=1.0",
#              "cf.FITNESS_BETA=0.0",
#              scenario4,
#              scenario5,
#              scenario6,
#              "cf.FITNESS_ALPHA=0.0",
#              "cf.FITNESS_BETA=1.0",
#              scenario4,
#              scenario5,
#              scenario6,
#              "save2csv(traces)",
#            ]

## tracer options
TRACE_ENERGY         = 0
TRACE_ALIVE_NODES    = 1
TRACE_COVERAGE       = 1
TRACE_LEARNING_CURVE = 0

## Runtime configuration
#MAX_ROUNDS = 15000
MAX_ROUNDS = 5000
# number of transmissions of sensed information to cluster heads or to
# base station (per round)
MAX_TX_PER_ROUND = 1

NOTIFY_POSITION = 0

## Network configurations:
# number of nodes
NB_NODES = 100
#NB_NODES = 300
# node sensor range
COVERAGE_RADIUS = 15 # meters 
# node transmission range
TX_RANGE = 30 # meters
BSID = -1
# area definition
#AREA_WIDTH = 250.0
#AREA_LENGTH = 250.0
AREA_WIDTH = 100.0
AREA_LENGTH = 100.0
# base station position
#BS_POS_X = 125.0
#BS_POS_Y = 125.0
BS_POS_X = 50.0
BS_POS_Y = 50.0

# packet configs
MSG_LENGTH = 4000 # bits
HEADER_LENGTH = 150 # bits
# initial energy at every node's battery
INITIAL_ENERGY = 2 # Joules


## Energy Configurations
# energy dissipated at the transceiver electronic (/bit)
E_ELEC = 50e-9 # Joules
# energy dissipated at the data aggregation (/bit)
E_DA = 5e-9 # Joules
# energy dissipated at the power amplifier (supposing a multi-path
# fading channel) (/bin/m^4)
E_MP = 0.0013e-12 # Joules
# energy dissipated at the power amplifier (supposing a line-of-sight
# free-space channel (/bin/m^2)
E_FS = 10e-12 # Joules
THRESHOLD_DIST = math.sqrt(E_FS/E_MP) # meters


## Routing configurations:
NB_CLUSTERS = 5
# FCM fuzzyness coeficient
FUZZY_M = 2


## Sleep Scheduling configurations:
NB_INDIVIDUALS = 10
MAX_ITERATIONS = 50
# ALPHA and BETA are the fitness function' weights
# where ALPHA optimizes energy lifetime, BETA the coverage
FITNESS_ALPHA  = 0.34
FITNESS_BETA   = 0.33
FITNESS_GAMMA  = 0.33
WMAX = 0.6
WMIN = 0.1


## Other configurations:
# grid precision (the bigger the faster the simulation)
GRID_PRECISION = 1 # in meters
# useful constants (for readability)
INFINITY = float('inf')
MINUS_INFINITY = float('-inf')

RESULTS_PATH = './results/'
