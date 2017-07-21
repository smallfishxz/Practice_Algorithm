def anagrams(words):
    d = {}
    # each key in "d" is a sorted word, and each bucket is stored as a dict, to check for dupes
    for word in words:
        sorted_word = "".join(sorted(word))  # clumsy way to sort a word
        if sorted_word not in d:
          d[sorted_word]=[]
        d[sorted_word].append(word)
    print(d)

    result = []
    for key in d:
        bucket = []
        for word in d[key]:
            bucket.append(word)
            print(bucket)
        result.append(bucket)
        print(result)

    return result
print(anagrams(["star", "rats", "car", "arc", "arts", "stars"]))
