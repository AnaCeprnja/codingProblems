

################################################################################
#Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!"
def hello_name(name):
  return "Hello " + name + "!"
print (hello_name('Bob'))


##########################
#Given a simple expression tree, consisting of basic binary operators i.e., + , – ,*
# and / and some integers, evaluate the expression tree.

# or asked this way
# Suppose an arithmetic expression is given as a binary tree. 
#Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.
#Given the root to such a tree, write a function to evaluate it.



 #   *
  # / \
 #+    +
# / \  / \
#3  2  4  5

#You should return 45, as it is (3 + 2) * (4 + 5).