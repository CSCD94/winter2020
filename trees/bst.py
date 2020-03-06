'''Exercise 2: Implementing Binary Search Trees.'''

from btree import BTree, BTNode


# 1) Check the case of having an empty BST as input, for every function.
# 2) Consider the following helpers:


def _insert(node, new_node):
    '''Return the BST that results from inserting new_node into the BST
    rooted at node. Do not insert duplicates.

    '''

    if node is None:
        return BST(new_node)
    # when node is not None
    if new_node < node:
        if node.left is None:
            node.left = new_node
        else:
            _insert(node.left, new_node)
    if new_node > node:
        if node.right is None:
            node.right = new_node
        else:
            _insert(node.right, new_node)
    return BST(node)


def _delete(node, value, parent):
    '''Delete a BTNode that contains value value from the BST rooted at
    node. If there is no such BTNode, raise a NoSuchValueException.
    Pre: parent is the parent BTNode of node
    '''

    if node is None:
        raise NoSuchValueException
    if value < node.value:
        _delete(node.left, value, node)
    elif value > node.value:
        _delete(node.right, value, node)
    else:
        _delete_node(node, parent)


def _update_parent(node, parent, new_value):
    '''Update the value of
        -- parent.left to new_value if node is the left child of parent
        -- parent.right to new_value if node is the right child of parent
        TODO: (?) new_value should be a node (can be None)
    '''
    if parent > node:
        parent.left = new_value
    elif parent < node:
        parent.right = new_value


def _delete_node(node, parent):
    '''Remove the BTNode node from the tree rooted at BTNode.
    Pre: parent is the BTNode parent of node
         node is not None
    Hint: this is where you use get_min
    '''

    # leaf is included in this case; where node.left == None
    if node.right is None:
        _update_parent(node, parent, node.left)
    # Need to delete the min node and update parent
    else:
        min = _get_min(node.right)
        substitute = BTNode(min)
        _delete(node, min, parent)
        substitute.left = node.left
        substitute.right = node.right
        _update_parent(node, parent, substitute)


def _get_min(node):
    '''Return the minimum value of a subtree rooted at node.'''
    # Note that this returns the value stored in the node, not the node itself.
    """
     if node is None:
        # TODO: return ? for None
        return
    """
    if node.left is None:
        return node.value
    else:
        return _get_min(node.left)


class BST(BTree):
    '''A Binary Search Tree.'''

    def insert(self, value):
        '''Insert a new BTNode with value value into this BST. Do not insert
        duplicates.

        '''
        return _insert(self._root, BTNode(value))

    def find(self, value):
        '''Return a BTNode from this BST that contains the value value. If
        there is no such BTNode in the tree, raise a
        NoSuchValueException.

        '''
        return _find(self._root, value)

    def depth(self, value):
        '''Return the depth (the number of BTNodes on the root-to-node path)
        of a BTNode that contains the value value, in this BST. If
        there is no such node in this BST, raise a NoSuchValueException.

        '''
        return _depth(self._root, value)

    def delete(self, value):
        '''Delete a BTNode that contains value value from this BST. If there
        is no such BTNode, raise a NoSuchValueException.

        '''

        # this one will take a bit longer :)
        # special case: empty tree
        if self._root is None:
            raise NoSuchValueException
        # special case: deleting a root
        if self._root.value == value:
            # create a fake root (use min - 1 as value), then remove root
            fake_root = BTNode(_get_min(self._root) - 1)
            fake_root.right = self._root
            _delete(fake_root, self._root.value, None)
            self._root = fake_root.right
        else:
            _delete(self._root, value, None)

        # Still don't understand why case 1 doesn't work
        """
        node = self.find(value)
        if node.left is None and node.right is None:
            node = None
        # to delete has no right child
        elif node.right is None:
            node = node.left
        # to delete has right child
        else:
            successor = find_min(node.right)
            node.value = successor.value
            node.right = successor.right
            successor = None
        """


class NoSuchValueException(Exception):
    pass


def _find(node, value):
    '''Find a node with value value from a BST rooted at node. If there is no
    such BTNode, raise a NoSuchValueException.

    '''
    if node is not None:
        if node.value == value:
            return node
        elif node.left is not None and node.value > value:
            return _find(node.left, value)
        elif node.right is not None and node.value < value:
            return _find(node.right, value)

    raise NoSuchValueException


def _depth(node, value):
    '''Return the depth (the number of BTNodes on the root-to-node path)
    of a BTNode that contains the value value, in BST rooted at node. If
    there is no such node in this BST, raise a NoSuchValueException.
    '''
    if node is not None:
        if node.value == value:
            return 1
        elif node.left is not None and node.value > value:
            return 1 + _depth(node.left, value)
        elif node.right is not None and node.value < value:
            return 1 + _depth(node.right, value)

    raise NoSuchValueException


if __name__ == '__main__':
    BT = BST(BTNode(5,
                    BTNode(3,
                           BTNode(2, BTNode(1), None),
                           BTNode(4)),
                    BTNode(6, None, BTNode(7))))
    # the string shuld be '\n\t\t7\n\n\t6\n\n5\n\n\t\t4\n\n\t3\n\n\t\t2\n\n\t\t\t1\n'
    print(BT)
    print(BT.preorder())
    print(BT.inorder())
    print(BT.postorder())
    print(BT.is_bst())
    print(BT.size())
    print(BT.fringe())
    print(BT.height())

    print(20*'=')

    for x in (0, 4.5, 10):
        BT.insert(x)
        print(BT)

    print(20*'=')

    for x in (0, 5, 7, 10):
        print('Found {}.'.format(BT.find(x)))

    for x in (-1, 8):
        try:
            BT.find(x)
        except NoSuchValueException:
            print('find({}) raised a NoSuchValueException.'.format(x))

    print(20*'=')

    try:
        BT.find(8)
    except NoSuchValueException:
        print('find(8) raised a NoSuchValueException.')

    for x in (5, 3, 6, 2, 4, 7, 1, 4.5, 10, 0):
        print('Depth of {} is {}.'.format(x, BT.depth(x)))

    try:
        BT.depth(8)
    except NoSuchValueException:
        print('depth(8) raised a NoSuchValueException.')
    print(20*'=')

    try:
        BT.delete(8)
    except NoSuchValueException:
        print('delete(8) raised a NoSuchValueException.')

    for x in (0, 4.5, 10, 5, 2, 3, 7, 4, 6, 1):
        print('Removing {}...'.format(x))
        BT.delete(x)
        print(BT)

    try:
        BT.delete(8)
    except NoSuchValueException:
        print('delete(8) raised a NoSuchValueException.')
