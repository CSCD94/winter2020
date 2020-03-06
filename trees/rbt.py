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

        

    def find(self, value):
        '''Return a RBTNode from this RedBlackTree that contains the value
        value. If there is no such RBTNode in the tree, raise a
        NoSuchValueException.

        '''

        pass

    def depth(self, value):
        '''Return the depth (the number of RBTNodes on the root-to-node path)
        of a RBTNode that contains the value value, in this
        RedBlackTree. If there is no such node in this RedBlackTree,
        raise a NoSuchValueException.

        '''

        pass

    # Only if you feel like it! :)
    def delete(self, value):
        '''Delete a RBTNode that contains value value from this
       RedBlackTree. If there is no such RBTNode, raise a
       NoSuchValueException.

        '''

        pass


def _insert_leaf(node, new_node):
    '''Insert new_node at leaf level in the tree rooted at node.'''

    pass


def _rebalance(node):
    '''Fix the RedBlackTree root at newly inserted RBTNode node.'''

    pass


def _rotate_left(node):
    '''Rotate the tree rooted at RBTNode node left.

    Precondition: node.right is not None

    '''

    pass


def _rotate_right(node):
    '''Rotate the tree rooted at RBTNode node right.

    Precondition: node.right is not None

    '''

    pass


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

        pass

    def get_sibling(self):
        '''Return the sibling of this RBTNode. Return None if this RBTNode is root.'''

        pass

    def get_aunt(self):
        '''Return a sibling of this RBTNode's parent. Return None if this
        RBTNode is root or if this RBTNode's parent is root.

        '''

        pass

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
