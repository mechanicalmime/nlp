# coding: utf-8
from __future__ import division
from __future__ import print_function
import nltk, re, pprint, logging

logger = logging.getLogger(__name__)

log_file_handler = logging.FileHandler("%s.log" % __name__)
log_file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_file_handler.setFormatter(formatter)

logger.addHandler(log_file_handler)

#USE CODECS TO OPEN THE FILE, SINCE IS UNICODE ENCODED
#f = open(r"C:\Users\Guillermo\Code\nlp\document.txt", 'r')
#raw = f.read()
#output_file = open(r"C:\Users\Guillermo\Code\nlp\output.txt", 'w') #Letter Count
#letter_count = 0
#alpha_only_words = [re.sub(r"[^\w]", r"", w) for w in words]
#for alpha_only_word in alpha_only_words:
#letter_count += len(alpha_only_word)

#Word Count
def escape_regex_characters(character_list):
	result_list = []
	for character in character_list:
		if character in ['(',')','[',']', '.', '\\', '"']:
			result_list.append("\\" + character)
		else:
			result_list.append(character)

	logger.debug("%s %s %s %s %s", "escape_regex_characters", 
				 "character_list", character_list, 
				 "result_list", result_list)

	return result_list

def tokenize_by_whitespace(text):
	return nltk.tokenize.WhitespaceTokenizer().tokenize(text)

def remove_characters_from_token(characters_to_remove, token):
	characters_to_remove = escape_regex_characters(characters_to_remove)
	regex_pattern= re.compile(r"[%s]" % "".join(characters_to_remove))

	logger.debug("%s %s %s", "remove_characters_from_token", "regex", regex_pattern.pattern)

	return re.sub(regex_pattern, r"", token) 

def remove_characters_from_beginning(token, characters_to_remove):
	characters_to_remove = escape_regex_characters(characters_to_remove)
	regex_pattern= re.compile(r"^[%s]+" % "".join(characters_to_remove))

	logger.debug("%s %s %s", "remove_characters_from_beginning", "regex", regex_pattern.pattern)

	return re.sub(regex_pattern, r"", token) 

def remove_characters_from_end(token, characters_to_remove):
	characters_to_remove = escape_regex_characters(characters_to_remove)
	regex_pattern= re.compile(r"[%s]+$" % "".join(characters_to_remove))

	logger.debug("%s %s %s", "remove_characters_from_end", "regex", regex_pattern.pattern)
	
	return re.sub(regex_pattern, r"", token) 

def select_pure_alphanumeric_tokens(tokens):
	return [alpha for alpha in tokens if re.match(r"^\w+$", alpha)]

def select_non_pure_alphanumeric_tokens(tokens):
	return [non_alpha for non_alpha in tokens if not re.match(r"^\w+$", non_alpha)]

def select_contraction_tokens(tokens):
	return [contraction for contraction in tokens if re.match(r"^\w+'\w+$", contraction)]

def select_non_contraction_tokens(tokens):
	return [non_contraction for non_contraction in tokens if not re.match(r"^\w+'\w+$", non_contraction)]

def select_compound_tokens(tokens):
	return [compound for compound in tokens if re.match(r"^\w+-+\w+$", compound)]

def select_non_compound_tokens(tokens):
	return [non_compound for non_compound in tokens if not re.match(r"^\w+-+\w+$", non_compound)]

def split_compound_tokens(tokens):
	result_list = []
	for token in tokens:
		if re.match(r"^\w+-+\w+$", token):
			result_list += re.split(r"-+", token)

			logger.debug("%s %s %s", "split_compound_tokens", "compound match", token)
		else:
			result_list.append(token)

			logger.debug("%s %s %s", "split_compound_tokens", "non-compound match", token)
	return result_list
	
#Sentence Count

#Paragraph Count

#Chapter Count

#Book Count
