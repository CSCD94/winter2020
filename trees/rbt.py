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
        # when not inserting at a root
        new_node = RBTNode(value, RED)
        _insert_leaf(self._root, new_node)
        # print (self)
        _rebalance(new_node)


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
    '''Insert new_node at leaf level in the tree rooted at node; return root
    '''

    if node is None:
        return new_node
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
    return node


def _swap_colour(node1, node2):
    '''Swap the colour of node1 and node2'''
    node1_colour = node1.colour
    node1.colour = node2.colour
    node2.colour = node1_colour


def _rebalance(node):
    '''Fix the RedBlackTree root at newly inserted RBTNode node.'''
    # when parent is BLACK, we are done;
    # otherwise, need to fix the tree
    if node.parent is None:
        node.colour = BLACK
    else:
        aunt = node.get_aunt()
        grandparent = node.get_grandparent()
        parent = node.parent
        if grandparent is not None:
            if parent.colour == RED:
                # Case 1: aunt is None or aunt of the new_node is BLACK
                # use rotation to fix the tree
                if aunt is None or aunt.colour == BLACK:
                    # left left case:
                    if node < parent < grandparent:
                        _rotate_right(grandparent)
                        # reports syntax error?
                        # ((parent.colour, grandparent.colour)
                        # = (grandparent.colour, parent.colour))
                        node.parent.colour = BLACK
                        node.get_sibling().colour = RED
                    # left right case:
                    if grandparent > parent and parent < node:
                        _rotate_left(parent)
                        _rebalance(node.left)
                    # right right case:
                    if grandparent < parent < node:
                        _rotate_left(grandparent)
                        node.parent.colour = BLACK
                        node.get_sibling().colour = RED
                    # right left case:
                    if grandparent < parent and parent > node:
                        _rotate_right(parent)
                        _rebalance(node.right)
                # Case 2: the aunt of the new_node is RED
                # use recolouring to fix the tree
                else:
                    parent.colour = BLACK
                    aunt.colour = BLACK
                    grandparent.colour = RED
                    _rebalance(grandparent)


def _rotate_left(node):
    '''Rotate the tree rooted at RBTNode node left.

    Precondition: node.right is not None

    '''
    sibling = node.right.left
    new_node = node.right.right
    aunt = node.left
    value = node.value
    node.value = node.right.value
    node.right = new_node
    if new_node is not None:
        new_node.parent = node
    node.left = RBTNode(value, left=aunt, right=sibling)
    if sibling is not None:
        sibling.parent = node.left
    if aunt is not None:
        aunt.parent = node.left


def _rotate_right(node):
    '''Rotate the tree rooted at RBTNode node right.

    Precondition: node.left is not None

    '''
    sibling = node.left.right
    new_node = node.left.left
    aunt = node.right
    value = node.value
    node.value = node.left.value
    node.left = new_node
    if new_node is not None:
        new_node.parent = node
    node.right = RBTNode(value, left=sibling, right=aunt)
    if sibling is not None:
        sibling.parent = node.right
    if aunt is not None:
        aunt.parent = node.right


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
        '''
        if x == 0:
            print(five)
            print(five.right)
            print(five.right.right)
            print(five.right.right.right) #11
            print(five.right.right.left) #7
            print(five.left)
            print(five.left.right)
            print(five.left.left)
            print(five.left.left.right)
            print(five.left.left.left)
        '''
        print(BT)

    print(20*'=')

    '''
    for x in (0, 4.5, 10, 11, 12, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7):
        print('Found {}.'.format(BT.find(x)))

    '''

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
