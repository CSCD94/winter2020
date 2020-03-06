'''Exercise 3. Complexity of tree operations -- Part 1.'''

import random
import statistics
import matplotlib.pyplot as plt

from bst import BST
from btree import BTNode, BTree


def get_random_btree(items: list):
    '''Return a BTree with elements from items inserted at random:
    all insertions at leaf level;
    at each level, go right with prob 50% and left with prob 50%.'''

    random.shuffle(items)
    node = None
    for item in items:
        node = random_insert(node, item)
    return BTree(node)


def random_insert(node, value):
    '''Return node with value insterted randomly into a subtree rooted at node;
    insertion at leaf level;
    at each level, go right with prob 50% and left with prob 50%.'''

    # use random.random() to decide left or right

    if node is None:
        return BTNode(value)
    # Insert to the left is > 0.5
    if random.random() > 0.5:
        if node.left is None:
            node.left = BTNode(value)
        else:
            random_insert(node.left, value)
    else:
        if node.right is None:
            node.right = BTNode(value)
        else:
            random_insert(node.right, value)
    return node


def get_bst(items):
    '''Return a BST with elements from items, inserted in order starting
    with an empty tree.

    '''
    bst = BST()
    for item in items:
        bst = bst.insert(item)
    return bst


def get_random_bst(num_nodes):
    '''Return a BST created by inserting elements from range(num_nodes) in
    random order.'''

    # use random.shuffle() to randomize a list
    items = list(range(num_nodes))
    random.shuffle(items)
    bst = BST()
    for item in items:
        bst = bst.insert(item)
    return bst


def plot_heights_bsts(num_nodes, num_trees):
    '''For each N in range(num_nodes), create num_trees random BSTs of size
    N, and calculate their average height. Return a list
    [avg_height_0, avg_height_1, ..., avg_height_N-1]
    '''

    # use statistics.mean() to calculate the averages

    avg_height = []
    for N in range(num_nodes):
        height = []
        for _ in range(num_trees):
            height.append(get_random_bst(N).height())
        avg_height.append(statistics.mean(height))
    return avg_height


def plot_heights_btrees(num_nodes, num_trees):
    '''For each N in range(num_nodes), create num_trees random BTrees of
    elements [0,..N), and calculate their average height. Return a list
    [avg_height_0, avg_height_1, ..., avg_height_N-1]
    '''

    # use statistics.mean() to calculate the averages

    avg_height = []
    for N in range(num_nodes):
        height = []
        for _ in range(num_trees):
            height.append(get_random_btree(list(range(N))).height())
        avg_height.append(statistics.mean(height))
    return avg_height


if __name__ == '__main__':

    #print(get_random_bst(5))
    #print(get_random_btree(list(range(5))))

    # Plot num_nodes vs average height of random BST with num_nodes nodes.
    # change to 50 & 1000 when confident
    NUM_TREES = 10
    MAX_NODES = 100

    XS = list(range(MAX_NODES))


    YS1 = plot_heights_btrees(MAX_NODES, NUM_TREES)
    YS2 = plot_heights_bsts(MAX_NODES, NUM_TREES)

    plt.xlabel('Number of nodes.')
    plt.ylabel('Average height.')
    plt.plot(XS, YS1, label='randomly built binary trees')
    plt.plot(XS, YS2, label='random bsts')
    plt.legend()

    plt.show()

