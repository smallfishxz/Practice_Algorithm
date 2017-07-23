
# DS reference: http://www.geeksforgeeks.org/data-structure-dictionary-spell-checker/
# Implemenation reference: http://www.geeksforgeeks.org/trie-insert-and-search/

# Example:
# setup({"foo", "bar", "baz", NULL});
# isMember("foo");  //returns true
# isMember("garply");  //returns false
# isMember("f.o");  //returns true (it matches foo)
# isMember("..");  // returns false (there are no two-letter words) 

# Make it clear in this section that time spent in setup should be reasonable, 
# but time spent in isMember() is the most important thing.

# Official
def findMatch(trie, word):
    return findMatchHelper(trie, trie.getRoot(), word, 0)

def findMatchHelper(trie, node, word, index):
    if index == len(word)
        # if we're at the end of the word                                      
        return trie.isTerminalNode(node)

    let = word[index]
    if let == '*':
        # wildcard character: search each child of this node                                          
        for child in trie.getAllChildren(node):
            if findMatchHelper(trie, child, word, index + 1):
                return True

        return False

    child = trie.getChild(node, let)
    if child == None:
        # this node doesn't contain the child we're looking for, so the word is not here              
        return False

    return findMatchHelper(trie, child, word, index + 1)

# Full implementation
class TrieNode:
     
    # Trie node class
    def __init__(self):
        self.children = [None]*26
 
        # isLeaf is True if node represent the end of the word
        self.isLeaf = False
    
    # def isTerminalNode(self):
    #   if self.isLeaf == True:
    #     return True
    #   else:
    #     return False
 
class Trie:
     
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
 
    def getNode(self):
     
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
 
    def _charToIndex(self,ch):
         
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
         
        return ord(ch)-ord('a')
 
 
    def insert(self,key):
         
        # If not present, inserts key into trie
        # If the key is prefix of trie node, 
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
 
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
 
        # mark last node as leaf
        pCrawl.isLeaf = True

    def search(self, key):
         
        # Search key in the trie
        # Returns true if key presents 
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
 
        return pCrawl != None and pCrawl.isLeaf
 
    def getAllChildren(self, node):
      if node is not None:
        return node.children
      else:
        return None
    
    def getChild(self, node, c):
      index=self._charToIndex(c)
      if node is not None:
        return node.children[index]
      else:
        return None
      
def findMatchHelper(tier, node, word, index):
    if index == len(word):
        # if we're at the end of the word 
      if node is not None:
        return node.isLeaf
      else:
        return False

    let = word[index]
    print(let)
    print(node)
    if let == '*':
    # wildcard character: search each child of this node   
      if tier.getAllChildren(node) is not None:
        for child in tier.getAllChildren(node):
          print(child)
          if findMatchHelper(tier, child, word, index + 1):
            return True

      return False
  
    child = tier.getChild(node, let)
    if child == None:
    # this node doesn't contain the child we're looking for, so the word is not here              
      return False
    print('Child is not None')
    return findMatchHelper(tier, child, word, index + 1)
      
def findMatch(tier, word):
    print(tier.root)
    return findMatchHelper(tier, tier.root, word, 0)

# driver function
def main():
 
    # # Input keys (use only 'a' through 'z' and lower case)
    # keys = ["the","a","there","anaswe","any",
    #         "by","their"]
    # output = ["Not present in trie",
    #           "Present in tire"]
 
    # # Trie object
    # t = Trie()
 
    # # Construct trie
    # for key in keys:
    #     t.insert(key)
 
    # # Search for different keys
    # print("{} ---- {}".format("the",output[t.search("the")]))
    # print("{} ---- {}".format("these",output[t.search("these")]))
    # print("{} ---- {}".format("their",output[t.search("their")]))
    # print("{} ---- {}".format("thaw",output[t.search("thaw")]))
    
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["foo","bar","baz"]
    output = ["Not present in trie",
              "Present in tire"]
 
    # Trie object
    t = Trie()
 
    # Construct trie
    for key in keys:
        t.insert(key)
 
    # Search for different keys
    # print("{} ---- {}".format("foo",output[findMatch(t, "foo")]))
    # print("{} ---- {}".format("f*o",output[findMatch(t, "f*o")]))
    print("{} ---- {}".format("**",output[findMatch(t, "**")]))
    # print("{} ---- {}".format("thaw",output[t.search("thaw")]))
 
# if __name__ == '__main__':
#     main()

main()
