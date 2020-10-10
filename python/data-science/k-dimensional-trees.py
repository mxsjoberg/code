# https://en.wikipedia.org/wiki/K-d_tree

from scipy.spatial import KDTree

# define set of points
points = [(1, 2), (3, 2), (5, 5), (2, 1), (4, 3), (1, 5)]

# create tree
kd_tree = KDTree(points)
kd_tree.data
# [[1 2]
#  [3 2]
#  [5 5]
#  [2 1]
#  [4 3]
#  [1 5]]

# index and distance to nearest point
dist, idx = kd_tree.query([(4.5, 1.25)])
dist                    # [ 1.67705098]
idx                     # [1]

# nearest point
kd_tree.data[idx]       # [[3 2]]

'''
Michael Sjoeberg
2018-11-05
https://github.com/michaelsjoeberg/python-playground/blob/master/data-science/k-dimensional-trees.py
'''