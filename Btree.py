class Tree(object):

    def __init__(self,value,mother=None):
        self.value = value
        self.left = None
        self.right = None
        self.frequency = 1
        self.mother = mother

    def find(tree,value,prtPath=False):
        if tree.value == value:
            if prtPath == True:
                print ("Found the val at this tree : " + str(tree))
            return tree
        elif value < tree.value:
            if tree.left is not None:
                if tree.left.value is not None:
                    if prtPath == True:
                        print ("Val not here, diving left to : " + str(tree.left.value))
                return tree.left.find(value,prtPath)
        else:
            if tree.right is not None :
                if tree.right.value is not None:
                    if prtPath == True:
                        print ("Val not here, diving right to : " + str(tree.right.value))
                return tree.right.find(value,prtPath)
        return False

    def remove(tree,value):
        searched = tree.find(value)
        if (searched != False):
            childrenCount = searched.countChildrenNodes()
            if childrenCount == 0:
                mother = searched.mother
                if (mother.left == searched):
                    mother.left = None
                else:
                    mother.right = None
            elif childrenCount == 1:
                mother = searched.mother
                if mother.right == searched:
                    if searched.left is not None:
                        mother.right = searched.left
                    else:mother.right = searched.right
                else:
                    if searched.left is not None:
                        mother.left = searched.left
                    else:mother.left = searched.right
            else:
                if searched.left.value > searched.right.value:
                    max = searched.left
                    min = searched.right
                else:
                    max = searched.right
                    min = searched.left
                tmp_minval = min

                if searched == searched.mother.left:
                    searched.mother.left = tmp_minval
                else:
                    searched.mother.right = tmp_minval
                searched.mother.right.right = max
        else:return "Not Exist"

    def insert(tree,value):
        searched = tree.find(value)
        if(searched != False):
            searched.frequency += 1
            return 0
        if tree == None:
            tree = Tree(value)
        elif tree.value > value:
            if tree.left == None:
                tree.left = Tree(value,tree)
            else:tree.left.insert(value)
        elif tree.right == None:
            tree.right = Tree(value,tree)
        else:tree.right.insert(value)

    def printTreeOrder(tree):
        if tree.left:
            tree.left.printTreeOrder()
        if tree is not None:
            print(str(tree.value))
        if tree.right:
            tree.right.printTreeOrder()

    def printTreePreOrder(tree):
        print(str(tree.value))
        if tree.left:
            tree.left.printTreePreOrder()
        if tree.right:
            tree.right.printTreePreOrder()


    #Help_Function
    def countNodesT(tree,counter):
        if tree.right:
            counter += 1
            counter = tree.right.countNodesT(counter)
        if tree.left:
            counter += 1
            counter = tree.left.countNodesT(counter)
        return counter
    def countNodesTree(tree):
        return (tree.countNodesT(0) + 1)

    def countChildrenNodes(tree):
        c = 0
        if tree.left is not None:
            c += 1
        if tree.right is not None:
            c += 1
        return c




root = Tree(1)
root.insert(1)
root.insert(2)
root.insert(22)
root.insert(5)
root.insert(62)
root.printTreeOrder()


if root.find(5) is not None:
    Bol = True
print("Is 5 here? : " + str(Bol))
print ("The Mother of 5 is : " + str(str(root.find(5).mother.mother.mother.value)))

print(""
      "")

print(root.value)
print(root.right.value)
print(root.right.right.value)
print(root.right.right.left.value)
print(root.right.right.right.value)

print("")

print("Count : " + str(root.countNodesTree()))


print ("")
root.remove(2)
root.printTreeOrder()


print (""
       "")

#print root.value
#print root.right.value
#print root.right.right.value
#root.right.right.left = None
#print root.right.right.left
#print root.right.right.right.value

wordRoot = None

para_words = open("text.txt",'r').read().split(" ")
for word in para_words:
    word = word.replace(",","").replace(".","").replace("'","")
    if wordRoot == None: wordRoot = Tree(word)
    else:wordRoot.insert(word)



wordRoot.printTreePreOrder()


print ("")

chkword = wordRoot.find("career",True)
