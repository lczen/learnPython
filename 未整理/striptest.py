line = '''Hooray! It's , snowing! It's time to make a snowman.James runs out.'''

words = line.strip()
print(words)
words = words.strip(",")
print(words)
words = words.strip(".")
print(words)
words = words.split()
print(words)