# collections modules
# Counter
#count unique characters
from collections import Counter

my_list = [1,1,1,2,2,2,3,4,3,3,4,3]
print(Counter(my_list))

my_list = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a']
print(Counter(my_list))

my_str = 'aaaabbbbcccddd'
print(Counter(my_str))

sentence = 'this is a sentence that contains a group of word'
print(Counter(sentence))

# default dict
from collections import defaultdict
d = { 'a': 10 }
d = defaultdict(lambda: 0)


