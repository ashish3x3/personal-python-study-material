

'''

# A binary tree node
class Node:

    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# This function returns pointer to LCA of two given
# values n1 and n2
# This function assumes that n1 and n2 are present in
# Binary Tree
def findLCA(root, n1, n2):

    # Base Case
    if root is None:
        return None

    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if root.key == n1 or root.key == n2:
        return root

    # Look for keys in left and right subtrees
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca


# Driver program to test above function

# Let us create a binary tree given in the above example
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
# print "LCA(4,5) = ", findLCA(root, 4, 5).key
# print "LCA(4,6) = ", findLCA(root, 4, 6).key
# print "LCA(3,4) = ", findLCA(root, 3, 4).key
# print "LCA(2,4) = ", findLCA(root, 2, 4).key

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)
a7 = Node(7)

a1.left = a2
a1.right  = a3

a2.left = a4
a2.right = a5

a3.left = a6
a3.right = a7

print "LCA(2,4) = ", findLCA(a1, 2, 4).key


# lca = LCA(a1)
# lca.findLCAUtil(a2,a3)
# lca.findLCAUtil(a4,a5)
# lca.findLCAUtil(a4,a6)
# lca.findLCAUtil(a3,a4)
# lca.findLCAUtil(a2,a4)

'''

'''
Find in left sub tree and right sub tree for a node
if lst is true and rst is true, current node is LCA
if lst return a node and rst is false, then the current returnd node fro lst is the root of both nodes else rst would have returned a node too

'''


class Node(object):
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

class LCA(object):
	def __init__(self, node=None):
		self.root = node

	def findLCAUtil(self,n1, n2):
		# print 'finding LCA for ',n1,n2
		return self.findLCA(self.root,n1,n2)

	def findLCA(self, root,n1, n2):
		# print n1,n2,n1.val,n2.val, root

		if root == None:
			return None

		if root.val == n1.val or root.val == n2.val:
			return root

		lst = self.findLCA(root.left,n1, n2)
		rst = self.findLCA(root.right,n1, n2)

		# print lst, rst

		if lst and rst:
			# print 'LCA of ', n1.val,n2.val, root.val
			return root

		return lst if lst is not None else rst


a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)
a7 = Node(7)

a1.left = a2
a1.right  = a3

a2.left = a4
a2.right = a5

a3.left = a6
a3.right = a7

lca = LCA(a1)
print 'LCA of ', a2.val,a3.val, lca.findLCAUtil(a2,a3).val
print 'LCA of ', a4.val,a5.val, lca.findLCAUtil(a4,a5).val
print 'LCA of ', a4.val,a6.val, lca.findLCAUtil(a4,a6).val
print 'LCA of ', a3.val,a4.val, lca.findLCAUtil(a3,a4).val
print 'LCA of ', a2.val,a4.val, lca.findLCAUtil(a2,a4).val

Time Complexity: Time complexity of the above solution is O(n) as the method does a simple tree traversal in bottom up fashion.
Note that the above method assumes that keys are present in Binary Tree. If one key is present and other is absent, then it returns the present key as LCA (Ideally should have returned NULL).
We can extend this method to handle all cases by passing two boolean variables v1 and v2. v1 is set as true when n1 is present in tree and v2 is set as true if n2 is present in tree.


def findLCAUtil(root, n1, n2, v):

    # Base Case
    if root is None:
        return None

    # IF either n1 or n2 matches ith root's key, report
    # the presence by setting v1 or v2 as true and return
    # root (Note that if a key is ancestor of other, then
    # the ancestor key becomes LCA)
    if root.key == n1 :
        v[0] = True
        return root

    if root.key == n2:
        v[1] = True
        return root

    # Look for keys in left and right subtree
    left_lca = findLCAUtil(root.left, n1, n2, v)
    right_lca = findLCAUtil(root.right, n1, n2, v)

    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca


def find(root, k):

    # Base Case
    if root is None:
        return False

    # If key is present at root, or if left subtree or right
    # subtree , return true
    if (root.key == k or find(root.left, k) or
        find(root.right, k)):
        return True

    # Else return false
    return False

# This function returns LCA of n1 and n2 onlue if both
# n1 and n2 are present in tree, otherwise returns None
def findLCA(root, n1, n2):

    # Initialize n1 and n2 as not visited
    v = [False, False]

    # Find lac of n1 and n2 using the technique discussed above
    lca = findLCAUtil(root, n1, n2, v)

    # Returns LCA only if both n1 and n2 are present in tree
    if (v[0] and v[1] or v[0] and find(lca, n2) or v[1] and
        find(lca, n1)):
        return lca

    # Else return None
    return None

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

lca = findLCA(root, 4, 5)

if lca is not None:
    print "LCA(4, 5) = ", lca.key
else :
    print "Keys are not present"

lca = findLCA(root, 4, 10)
if lca is not None:
    print "LCA(4,10) = ", lca.key
else:
    print "Keys are not present"















