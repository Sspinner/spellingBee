"""
Construct all words containing only those letters in a given set.
Use lexicon of english words of length 4 or greater downloaded from

https://elexicon.wustl.edu/query13/query13.html

and installed in the same directory as this script as four_and_greater.csv.
"""
import pandas as pd

lexicon = pd.read_csv("four_and_greater.csv.gz").dropna()
lexicon['letts'] = lexicon['Word'].apply(lambda x: set(x))

opt_letter_set = set(input('Enter 6 optional letters as single string in any order: '))
key_letter = input('Enter key letter: ')
letter_set = opt_letter_set.union(set(key_letter))
results = lexicon[(lexicon.letts <= letter_set)]
results = results[results.Word.apply(lambda x: key_letter in x)]

print(f"There are {len(results)} matching words")
print()
print(results)


