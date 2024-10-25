from os import walk
from os.path import join
from collections import Counter
import re
from sys import argv

counts = {}
for root, dir, files in walk(argv[1]):
    for file in files:
        if file.endswith('.py'):
            with open(join(root, file), "r") as auto:
                text = auto.read()
                subcounts = Counter(re.findall('[A-Za-z_]{4,}', text)) 
                for word, cnt in subcounts.items():
                    counts[word] = counts.get(word,0) + cnt

for w,i in counts.items():
    if i>3: print(w) 