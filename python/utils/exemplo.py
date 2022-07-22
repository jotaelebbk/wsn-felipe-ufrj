from pymote import *
from pymote.conf import global_settings
from toplogies import Topology
from pymote.utils.filing import get_path, \TOPOLOGY_DIR
from numpy.random import seed
from networkx import *

seed(100) # to get same sequence for each run
# Network/Environment setup (100 m x 100 m)
global_settings.ENVIRONMENT2D_SHAPE = (100, 100)
global_settings.COMM_RANGE = 10 # comm. radius
net = Network()
h, w = net.environment.im.shape
n = 90 # total no of nodes (desired)
x_radius = 0.9*global_settings.COMM_RANGE
y_radius = 0.9*global_settings.COMM_RANGE
# Topology setup
# Generate a randomized grid network with
# 10% anchors (default)
net_gen = Topology(n_count=n, connected=True)
net = net_gen.generate_grid_network(name="Grid",
randomness=0.5)
# Get actual of number of nodes and Avg. degree
avg_deg = net.avg_degree()
na = net.__len__()
print "No. of Nodes: %s" % na
print "Avg. Degree: %s" % round(avg_deg, 3)
filename = "Simple Grid - %s nodes" %na
net.name = filename
# saving topology as PNG image
net.savefig(fname=get_path(TOPOLOGY_DIR, filename),
    title=net.name,
    xlabel="X-coordinate (m)",
    ylabel="Y-coordinate (m)",
    show_labels=True, format="png")

# display info about the network
print networkx.info(net)
# Save the network as json
net.save_json(get_path(TOPOLOGY_DIR,
filename+".json"), scale=(6, 5))
net.reset()
