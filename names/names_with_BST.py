#This is a class
# 
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of node (self.value)    
        # compare to the new value we want to insert

        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            elif self.left is None:
                self.left = BSTNode(value)

        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            elif self.right is None:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
            if self.value == target:
                return True
            if self.value > target:
                if self.left is None:
                    return False
                found = self.left.contains(target)
            else:
                if self.right is None:
                    return False
                found = self.right.contains(target)
            return found

import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
bst2 = BSTNode('Names2')
for name_2 in names_2:
    bst2.insert(name_2)
f.close()

duplicates = []  # Return the list of duplicates in this data structure

for name_1 in names_1:
    if bst2.contains(name_1) == True:
        duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.