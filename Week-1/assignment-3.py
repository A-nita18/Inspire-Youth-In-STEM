book_title = ["the","great","expectations"]
word_counter = {}

for word in book_title:
    word_counter[word] = word_counter.get(word,0) + 1
print(word_counter)    

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)