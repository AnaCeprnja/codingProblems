

################################################################################
#Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!"
def hello_name(name):
  return "Hello " + name + "!"
print (hello_name('Bob'))


##########################
#Given a simple expression tree, consisting of basic binary operators i.e., + , – ,*
# and / and some integers, evaluate the expression tree.

 #   *
  # / \
 #+    +
# / \  / \
#3  2  4  5

#You should return 45, as it is (3 + 2) * (4 + 5).