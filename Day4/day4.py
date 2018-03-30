from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve
import timeit

# tuple
user = ('bob', 'coder')
print("{0} is a {1}".format(user[0], user[1]))

# named tuple
User = namedtuple('User', 'name role')
user = User(name='bob', role='coder')
print(user.name)
print(user.role)

print("{0} is a {1}".format(user.name, user.role))

print("<------------------->")
# default dict
users = {'bob': 'coder'}
print(users['bob'])
# print(users['julian'])

print(users.get('bob'))
print(users.get('julian'))


challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6)]
print(challenges_done)

# challenges = {}
# for name, challenge in challenges_done:
#     challenges[name].append(challenge)

challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)

print("<------------------->")
# Counter
words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()

print(words[:5])


common_words = {}

for word in words:
    if word not in common_words:
        common_words[word] = 0
    common_words[word] += 1

start = timeit.default_timer()
# sort dict by values descending and slice first 5 to get most common
for k, v in sorted(common_words.items(),
                   key=lambda x: x[1],
                   reverse=True)[:5]:
    print(k, v)
print('manuel for stmt took {0} to complete'.format(timeit.default_timer() - start))

print("<------------------->")
start = timeit.default_timer()
print(Counter(words).most_common(5))
print('Counter command took {0} to complete'.format(timeit.default_timer() - start))

print("<------------------->")
# deque

lst = list(range(10000000))
deq = deque(range(10000000))


def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)


start = timeit.default_timer()
insert_and_delete(lst)
print('lst took {0} to complete'.format(timeit.default_timer() - start))

start = timeit.default_timer()
insert_and_delete(deq)
print('while deq took {0} to complete'.format(timeit.default_timer() - start))
