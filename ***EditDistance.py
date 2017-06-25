/*
Question

This is a pretty straight forward Ninja question suitable for any language.  Easy to understand, a few tricky cases, plenty of room for clever solutions and for a candidate to really goof up.  There are language-specific pitfalls too (C/C++ pointers, for instance).  It seems simple (and can be if they think of the nice tricks to exploit) but requires some detailed coding, attention to details, and forethought.

The question is, write a function to return if two words are exactly "one edit" away.

bool OneEditApart(string s1, string s2);
That returns true if two words are exactly one edit apart, where an edit is:

Insert one character anywhere in the word (including at the beginning and end)
Remove one character
Replace exactly one character
Examples:

OneEditApart("cat", "dog") = false
OneEditApart("cat", "cats") = true
OneEditApart("cat", "cut") = true
OneEditApart("cat", "cast") = true
OneEditApart("cat", "at") = true
OneEditApart("cat", "act") = false
*/

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
  
