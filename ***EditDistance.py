# Question

# This is a pretty straight forward Ninja question suitable for any language.  Easy to understand, a few tricky cases, plenty of room for clever solutions and for a candidate to really goof up.  There are language-specific pitfalls too (C/C++ pointers, for instance).  It seems simple (and can be if they think of the nice tricks to exploit) but requires some detailed coding, attention to details, and forethought.

# The question is, write a function to return if two words are exactly "one edit" away.

# bool OneEditApart(string s1, string s2);
# That returns true if two words are exactly one edit apart, where an edit is:

# Insert one character anywhere in the word (including at the beginning and end)  
# Remove one character
# Replace exactly one character
# Examples:

# OneEditApart("cat", "dog") = false
# OneEditApart("cat", "cats") = true
# OneEditApart("cat", "cut") = true
# OneEditApart("cat", "cast") = true
# OneEditApart("cat", "at") = true
# OneEditApart("cat", "act") = false

# Solution

# There are a few variations.  The "best" approach seems to be to walk each string in unison, tracking if a difference has been encountered.  If a second difference is encountered, return false.  If one string is longer than the other, then the difference must mean it is an insertion, so skip a character in the longer string and continue.  There are symmetry and short circuit opportunities as well.  Below are examples of the pretty much optimal versions.

# Things to note:

# Did they ask what it might be used for? (a good sign)
# Does their solution stop as quickly as possible?
# Did they notice they can swap s1 and s2 to only handle one case of one being larger than the other (instead of having to handle both)?
# Do they return the correct value for the same string being passed in for both values?
# Do they walk through their solution with different test values?  Thorough tests include testing insertions/removals from the beginning and end, strings that are very different in length, prefixes of each other, etc etc.
# Sometimes the candidate might traverse both strings from the front *and* back, noting when a difference is encountered in both directions.  They then compare how close their "cursors" are in both strings to draw a conclusion.  This can work, too, but it basically doubles the chance for errors, bounds violations, and off-by-one errors!

Def OneEditApart(string s1, string s2):
  if len(s1) > len(s2): 
    s2, s1 = s1, s2
  size_delta = len(s2) - len(s1)
  
  if size_delta > 1:
    return False
  
  saw_difference = False
  i = j = 0
  while i < len(s1):
    if s1[i] != s2[j]:
      if saw_difference == True:
        return False
      saw_difference = True
      if size_delta > 0:
        j = j+1
        continue
    i = i+1
    j = j+1
  
  return saw_difference or size_delta > 0 
  # return saw_difference or size_delta = 1
  # Why should have the or logic?
  # 'cat' vs. 'cab': return saw_difference = True or size_delta > 0 = False
  # 'cat' vs. 'cate': return saw_difference = False or size_delta > 0 = True
  
# Where People Fail

# Sometimes they don't see an easy solution or try something very complex.  Often they don't filter out the very different length strings and try to keep track of how many differences there are, or try to backtrack when differences don't work out.  The more if statements and branches and temporary variables, the more likely the candidate is off in the woods.  Offering hints to keep them on target is fine (such as helping them break it down into 3 cases: insert char, remove char, change char, then maybe hinting that two of those are the same case).

# Off-by-one and accessing out of the array boundaries happens a lot, too.  Edge testing is important.  I've yet to see a working, simple recursive solution, but it's possible.  I've seen recursion go awry a lot, though, so be aware.

# [edit]Easier version

# If a candidate is really struggling, you can simplify and have them not worry about length differences.  Or you can talk about video games or cats or something to just fill the time and be pleasant, because chances are, if they struggle with the base version even when given hints, they are probably not destined to work at facebook.

# [edit]Bonus question

# Make it *fast*!  Especially important in the graph version below where it is the heart of an O(n**2) solution.

# Use the above function to create a graph where nodes are the words in the dictionary and edges indicate they are one edit apart.

# Is the graph connected?
# What might such a graph be used for?  (spell checking, other simple off-by-one error corrections, a fun word-play facebook game!)
# How fast is constructing the graph?
# A super bright candidate might see a nice O(n) way to make the graph.  In fact, this question orignated by first asking for a graph, but I found that the function above gave pretty good signal, so I reduced it to that.
