import argparse
import json
import string
from random import randrange

parser = argparse.ArgumentParser(description='Turn an acronym into a random phrase')
parser.add_argument('acronym', nargs=1)
parser.add_argument('iters',nargs='?',default=2,type=int)
args = parser.parse_args()

acronym=args.acronym[0]
print('input: ' + acronym)

allwords=json.load(open('words.json',mode='r',buffering=1))

wordlist={c:[] for c in string.ascii_lowercase}
for word in allwords:
	wordlist[word[0].lower()].append(word)

for i in range(0,args.iters):
	print('output:', end=" ")
	for char in acronym:
		print(wordlist[char.lower()][randrange(0,len(wordlist[char.lower()]))], end=" ")
	print()
