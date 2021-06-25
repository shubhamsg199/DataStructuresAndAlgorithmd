# initialize a list
word_list = list(map(str,input().split()))
anagram_list = []
for word_1 in word_list:
    for word_2 in word_list:
        if word_1 != word_2 and (sorted(word_1)==sorted(word_2)):
            anagram_list.append(word_1)
list1 = []
for i in anagram_list:
    if i not in list1:
        list1.append(i)
print(*list1,sep=',')