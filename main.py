import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple

# Lots of colors used in testing. From the matplotlib website.
# https://matplotlib.org/api/colors_api.html#classes
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', 'tab:blue', 'tab:orange', 'tab:green',
          'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

Epsilon = .9
MinPoints = 15


# Not cached, I believe this makes DBSCAN O(n^2)
# Get all neighbors of a point
def list_neighbors(data: List[np.array], point: np.array, eps: float) -> List[np.array]:
    points = []
    # Distance. https://stackoverflow.com/questions/1401712/how-can-the-euclidean-distance-be-calculated-with-numpy
    for pt in data:
        if np.linalg.norm(pt - point) <= eps:
            points.append(pt)
    return points


class Point:
    def __init__(self, pos: np.array, cluster: int, coretype: str, neighbors: List[np.array]):
        self.pos = pos
        self.cluster = cluster
        self.coretype = coretype
        self.neighbors = neighbors
        self.marked = False


def dbscan(data, eps, minPts) -> Tuple[List[Point], int]:
    # First, construct knowledge of all points: is it a core point?
    # What about an edge point?
    points = []
    for datum in data:
        neighbors = list_neighbors(data, datum, eps)
        points.append(Point(datum, -1, "", neighbors))
    for point in points:
        if len(point.neighbors) >= minPts:
            point.coretype = "core"
        else:
            point.coretype = "noncore"
    # If the point is a non-core point but has a neighbor
    # that is a core point, it must be an edge point.
    for point in points:
        if point.coretype == "noncore":
            for pt in point.neighbors:
                for p in points:
                    if all(pt == p.pos) and p.coretype == "core":
                        point.coretype = "edge"
            if point.coretype != "edge":
                point.coretype = "noise"

    # Now begin defining clusters.
    count = 1
    for point in points:
        if point.coretype == "core":
            count = expandcluster(points, count, point)

    return points, count


def expandcluster(points, cluster, startpoint, isfirst=True):
    # Start jumping down the rabbit hole of neighbors.
    if startpoint.marked:
        return cluster
    for pt in startpoint.neighbors:
        for p in points:
            if all(pt == p.pos) and not p.marked:
                p.marked = True
                p.cluster = cluster
                if p.coretype == "core":
                    cluster = expandcluster(points, cluster, p, False)
    return cluster + 1 if isfirst else cluster


arr = np.genfromtxt("ClusterPlot.csv", skip_header=1, delimiter=',', usecols=(1, 2))
fig, ax = plt.subplots()

Points, clustercount = dbscan(arr, Epsilon, MinPoints)

for P in Points:
    if P.coretype == "core":
        color = 'r'
    elif P.coretype == "edge":
        color = 'y'
    elif P.coretype == "noise":
        color = 'b'
    else:
        color = 'g'
    ax.plot([P.pos[0]], [P.pos[1]], 'o', color=colors[P.cluster])

plt.xlabel(f"Number of Clusters: {clustercount}")
plt.show()
