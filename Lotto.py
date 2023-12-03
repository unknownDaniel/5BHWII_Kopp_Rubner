import random
import matplotlib.pyplot as plt
import numpy as np

dictionary = {}
for i in range(1, 46):
  dictionary[i] = 0

def draw(list, how_many):
  for i in range(how_many):
    num = random.randint(0, len(list) - 1)
    dictionary[list[num]] += 1
    list = list[:num] + list[num + 1:]

for i in range(10000):
  # liste von 1 bis 45 erstellen
  numbers = list(range(1, 46))
  draw(numbers, 6)

print(dictionary)
plt.bar(dictionary.keys(), dictionary.values())
plt.show()