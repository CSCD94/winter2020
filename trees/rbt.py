'''Exercise 4: Implementing Red Black Trees.'''

from btree import BTNode
from bst import BST, NoSuchValueException

BLACK = 0
RED = 1


class RedBlackTree(BST):
    '''A Red Black Tree.'''

    def insert(self, value):
        '''Insert a new RBTNode with value value into this RedBlackTree. Do
        not insert duplicates.

        '''
        if self._root is None:
            self._root = RBTNode(value, BLACK)
            return self
        # when not inserting at a root
        new_node = RBTNode(value, RED)
        _insert_leaf(self._root, new_node)
        _rebalance(new_node)
        return self


    # how is find and depth different from parent?
    """
    def find(self, value):
        '''Return a RBTNode from this RedBlackTree that contains the value
        value. If there is no such RBTNode in the tree, raise a
        NoSuchValueException.

        '''
        super().find(value)
        

    def depth(self, value):
        '''Return the depth (the number of RBTNodes on the root-to-node path)
        of a RBTNode that contains the value value, in this
        RedBlackTree. If there is no such node in this RedBlackTree,
        raise a NoSuchValueException.

        '''
        super().depth(value)
    """

    # Only if you feel like it! :)
    def delete(self, value):
        '''Delete a RBTNode that contains value value from this
       RedBlackTree. If there is no such RBTNode, raise a
       NoSuchValueException.

        '''

        pass


def _insert_leaf(node, new_node):
    '''Insert new_node at leaf level in the tree rooted at node.
    
    (?) prerequisite: node is not None
    '''
    if new_node < node:
        if node.left is None:
            node.left = new_node
            new_node.parent = node
        else:
            _insert_leaf(node.left, new_node)
    if new_node > node:
        if node.right is None:
            node.right = new_node
            new_node.parent = node
        else:
            _insert_leaf(node.right, new_node)
    return BST(node)

"""
# newly-defined helper function
def _recolouring(root, node):
    '''Recolour the node to fix a newly coloured RBT'''
    if not node == root:
        node.parent.colour = BLACK
        node.get_aunt().colour = BLACK
        node.get_grandparent().colour = RED
    _recolouring(node.get_grandparent())
"""
def _swap_colour(node1, node2):
    '''Swap the colour of node1 and node2'''
    node1_colour = node1.colour
    node1.colour = node2.colour
    node2.colour = node1_colour


def _rebalance(node):
    '''Fix the RedBlackTree root at newly inserted RBTNode node.'''
    # when parent is BLACK, we are done;
    # otherwise, need to fix the tree
    if node == self._root:
        self._root.colour = BLACK
    else:
        aunt = new_node.get_aunt()
        grandparent = new_node.get_grandparent()
        parent = new_node.parent
        if parent.colour == RED:
            # Case 1: the aunt of the new_node is RED
            # use recolouring to fix the tree            
            if aunt.colour == RED:
                parent.colour = BLACK
                aunt.colour = BLACK
                grandparent.colour = RED            
                _rebalance(grandparent)
            # Case 2: the aunt of the new_node is BLACK
            # use rotation to fix the tree
            if aunt.colour == BLACK:
                # left left case:
                if grandparent.left == parent and parent.left == new_node:
                    _rotate_right(grandparent)
                    _swap_colour(parent, grandparent)
                # left right case:
                if grandparent.left == parent and parent.right == new_node:
                    _rotate_left(parent)
                    _rotate_right(grandparent)
                    _swap_colour(parent, grandparent)                   
                # right right case:
                if grandparent.right == parent and parent.right == new_node:
                    _rotate_left(grandparent)
                    _swap_colour(parent, grandparent)
                # right left case:
                if grandparent.right == parent and parent.left == new_node:
                    _rotate_right(parent)
                    _rotate_left(grandparent)
                    _swap_colour(parent, grandparent)
    return self


def _rotate_left(node):
    '''Rotate the tree rooted at RBTNode node left.

    Precondition: node.right is not None

    '''
    #g = node
    #p = node.left
    node.left.parent = node.parent
    T3 = node.left.right
    node.left.right = node
    node.parent = node.left
    node.left = T3
    T3.parent = node


def _rotate_right(node):
    '''Rotate the tree rooted at RBTNode node right.

    Precondition: node.right is not None

    '''
    #g = node
    #p = node.right
    node.right.parent = node.parent
    T3 = node.right.left
    node.right.left = node
    node.parent = node.right.left
    node.right = T3
    T3.parent = node


class RBTNode(BTNode):
    '''A node in a RedBlackTree.'''

    def __init__(self, value, colour=BLACK, left=None, right=None,
                 parent=None):
        '''Init a RBTNode with value value, colour colour, parent parent, left
        child left, and right child right.

        '''

        BTNode.__init__(self, value, left, right)
        self.colour = colour
        self.parent = parent

    def get_grandparent(self):
        '''Return the grandparent of this RBTNode, or None if the parent is None.'''
        if self.parent is None:
            return None
        return self.parent.parent

    def get_sibling(self):
        '''Return the sibling of this RBTNode. Return None if this RBTNode is root.'''
        if self.parent is None:
            return None
        if self < self.parent:
            return self.parent.right
        # put if self > self.parent seems more readable?
        return self.parent.left

    def get_aunt(self):
        '''Return a sibling of this RBTNode's parent. Return None if this
        RBTNode is root or if this RBTNode's parent is root.

        '''
        return self.parent.get_sibling()

    def __str__(self):
        '''Return a str representation of this RedBlackTree.'''

        return '{}: {}'.format(BTNode.__str__(self), 'Red' if self.colour == RED else 'Black')


if __name__ == '__main__':
    five = RBTNode(5, BLACK)
    three = RBTNode(3, RED)
    six = RBTNode(6, RED)
    five.left, five.right = three, six
    three.parent = six.parent = five
    two = RBTNode(2, BLACK)
    four = RBTNode(4, BLACK)
    three.left, three.right = two, four
    two.parent = four.parent = three
    seven = RBTNode(7, BLACK)
    six.right = seven
    seven.parent = six
    one = RBTNode(1, RED)
    two.left = one
    one.parent = two

    BT = RedBlackTree(five)

    print(BT)
    print(BT.preorder())
    print(BT.inorder())
    print(BT.postorder())
    print(BT.is_bst())
    print(BT.size())
    print(BT.fringe())
    print(BT.height())

    print(20*'=')

    for x in (0, 4.5, 10, 11, 12, 15, 16, 17, 18, 19, 20):
        print('inserting ' + str(x))
        BT.insert(x)
        print(BT)

    print(20*'=')

    for x in (0, 5, 7, 10, 15, 20):
        print('Found {}.'.format(BT.find(x)))

    for x in (-1, 8):
        try:
            BT.find(x)
        except NoSuchValueException:
            print('find({}) raised a NoSuchValueException.'.format(x))

    print(20*'=')

    for x in (5, 3, 6, 2, 4, 7, 1, 4.5, 10, 0):
        print('Depth of {} is {}.'.format(x, BT.depth(x)))

    try:
        BT.depth(8)
    except NoSuchValueException:
        print('depth(8) raised a NoSuchValueException.')
    print(20*'=')

    # Only if you feel like it! :)
    # try:
    #     BT.delete(8)
    # except NoSuchValueException:
    #     print('delete(8) raised a NoSuchValueException.')

    # for x in (0, 4.5, 10, 5, 2, 3, 7, 4, 6, 1):
    #     print('Removing {}...'.format(x))
    #     BT.delete(x)
    #     print(BT)

    # try:
    #     BT.delete(8)
    # except NoSuchValueException:
    #     print('delete(8) raised a NoSuchValueException.')
