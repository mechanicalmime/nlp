# coding: utf-8
from __future__ import division
from __future__ import print_function
import nltk, re, pprint

f = open('document.txt')
raw = f.read()

output_file = open('output.txt', 'w')

tokens = nltk.word_tokenize(raw)

words = [w.lower() for w in tokens]

vocab = sorted(set(words))

#Letter count
letter_count = 0

alpha_only_words = [re.sub(r"[^\w]", r"", w) for w in words]
for alpha_only_word in alpha_only_words:
	letter_count += len(alpha_only_word)

#Word count
word_count = 0 #len(set(words))

words_only = [w for w in words if re.match(r"[\w']+", w)]
contractions = [w for w in words if re.match(r"'", w) and not re.match(r"^'+$", w)]

whitespace_tokens = nltk.tokenize.WhitespaceTokenizer().tokenize(raw)
clean_wp_tokens = [re.sub(r"[,.!?:;\(\)\*_\"\[\]]+", r"", wp).lower() for wp in whitespace_tokens]

#remove BEGINNING single quotes
clean_wp_tokens = [re.sub(r"^'+", r"", wp) for wp in clean_wp_tokens]

#remove ENDING single quotes
clean_wp_tokens = [re.sub(r"'+$", r"", wp) for wp in clean_wp_tokens]

#remove BEGINNING -- sequence
clean_wp_tokens = [re.sub(r"^-+", r"", wp) for wp in clean_wp_tokens]

#remove ENDING -- sequence
clean_wp_tokens = [re.sub(r"-+$", r"", wp) for wp in clean_wp_tokens]

#remove empty tokens
clean_wp_tokens = [wp for wp in clean_wp_tokens if wp]

#Any token not made completely out of letters
remaining_dirty_tokens = [dt for dt in clean_wp_tokens if not re.match(r"^[a-z]+$", dt)]

#Valid pure letter words
only_letter_words = [ol for ol in clean_wp_tokens if re.match(r"^[a-z]+$", ol)]

#Exclude contractions
remaining_dirty_tokens = [dt for dt in remaining_dirty_tokens if not re.match(r"^[a-z]+'[a-z]+$", dt)]

#Valid words with contractions
contraction_words = [cw for cw in clean_wp_tokens if re.match(r"^[a-z]+'[a-z]+$", cw)]

#Tokens separated by - (compound words)
compound_words = [cw for cw in remaining_dirty_tokens if re.match(r"^[a-z]+(-[a-z]+)+$", cw)]

#Exclude valid compound words
remaining_dirty_tokens = [dt for dt in remaining_dirty_tokens if not re.match(r"^[a-z]+(-[a-z]+)+$", dt)]

for rdt in remaining_dirty_tokens:
	print(rdt, file=output_file)

#Sentence count

#Paragraph count

#Chapter count

#Book count? 

