import unittest
from ..nlp import poc 

class NLPTestSuite(unittest.TestCase):

	def test_tokenize_using_whitespace(self):
		text = "It's possible, to.; create\n\ta\r\fmeaningful test case"

		expected_result = ["It's", "possible,", "to.;", "create", 
						   "a", "meaningful", "test", "case"]

		self.assertEqual(expected_result, poc.tokenize_by_whitespace(text))

	def test_remove_characters_from_token(self):
		token = ",,!?.;a;.s!?[d]()_\"''\\f"

		characters_to_remove = ['!', '?', ';', ',', '[', '\\', '.', 
								']', '(', ')', '_', '\'', '"']

		expected_result = "asdf"

		self.assertEqual(expected_result, poc.remove_characters_from_token(characters_to_remove, token))

	def test_remove_characters_from_beginning_of_token(self):
		token = "---[]...'''domo-[]\\mrroboto"

		characters_to_remove = ['-', '[', ']', '.', '\'']

		expected_result = "domo-[]\\mrroboto"

		self.assertEqual(expected_result, poc.remove_characters_from_beginning(token, characters_to_remove))

	def test_remove_characters_from_end_of_token(self):
		token = "mrroboto--[]'''domo---[]...'''"

		characters_to_remove = ['-', '[', ']', '.', '\'']

		expected_result = "mrroboto--[]'''domo"

		self.assertEqual(expected_result, poc.remove_characters_from_end(token, characters_to_remove))

	def test_escape_regex_characters(self):
		string_with_regex_characters = ['[',']','(',')','\\','.','"']

		expected_result = ['\\[','\\]','\\(','\\)','\\\\','\\.','\\"']

		self.assertEqual(expected_result, poc.escape_regex_characters(string_with_regex_characters))

	def test_select_pure_alphanumeric_tokens(self):
		tokens = ["4lph4num3r1c", "contrac'tion", "comp--ound", "we$$''..@ird"]

		expected_result = ["4lph4num3r1c"]

		self.assertEqual(expected_result, poc.select_pure_alphanumeric_tokens(tokens))

	def test_select_non_pure_alphanumeric_tokens(self):
		tokens = ["4lph4num3r1c", "contrac'tion", "comp--ound", "we$$''..@ird"]

		expected_result = ["contrac'tion", "comp--ound", "we$$''..@ird"]

		self.assertEqual(expected_result, poc.select_non_pure_alphanumeric_tokens(tokens))

	def test_select_contraction_tokens(self):
		tokens = ["4lph4num3r1c", "contrac'tion", "comp--ound", 
				  "we$$''..@ird", "'invalid'contraction''", "other''invalid"]

		expected_result = ["contrac'tion"]

		self.assertEqual(expected_result, poc.select_contraction_tokens(tokens))


	def test_select_non_contraction_tokens(self):
		tokens = ["4lph4num3r1c", "contrac'tion", "comp--ound", 
				  "we$$''..@ird", "'invalid'contraction''"]

		expected_result = ["4lph4num3r1c", "comp--ound", 
				  		   "we$$''..@ird", "'invalid'contraction''"]

		self.assertEqual(expected_result, poc.select_non_contraction_tokens(tokens))

	def test_select_compound_tokens(self):
		tokens = ["simplecompound-token", "complex----compound",
				  "simple", "---garbage---"]
		
		expected_result = ["simplecompound-token", "complex----compound"]

		self.assertEqual(expected_result, poc.select_compound_tokens(tokens))

	def test_select_non_compound_tokens(self):
		tokens = ["simplecompound-token", "complex----compound",
				  "simple", "---garbage---"]
		
		expected_result = ["simple", "---garbage---"]

		self.assertEqual(expected_result, poc.select_non_compound_tokens(tokens))

	def test_split_compound_tokens(self):
		tokens = ["simplecompound-token", "complex----compound",
				  "simple", "---garbage---"]	

		expected_result = ["simplecompound", "token", "complex", "compound",
						   "simple", "---garbage---"]

		self.assertEqual(expected_result, poc.split_compound_tokens(tokens))