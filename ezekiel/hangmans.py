import random
words = ['mc.chicken', 'dawg', 'cat in hats', 'mouses', 'red coats']
def pick_a_word():
    return random.choice(words)

print(pick_a_word())