from nose.tools import *
from ex49 import lexicon

def test_directions():
	assert_equal(lexicon.scan("north"),[('direction', 'north')])
	result = lexicon.scan("north south east")
	assert_equal(result, [('direction', 'north'),
						  ('direction', 'south'),
						  ('direction', 'east')])
						  
def test_verb():
	assert_equal(lexicon.scan("go"),[('verb', 'go')])
	result = lexicon.scan("go kill eat")
	assert_equal(result, [('verb', 'go'),
						  ('verb', 'kill'),
						  ('verb', 'eat')])
						  
def test_prep():
	assert_equal(lexicon.scan("the"), [('prep', 'the')])
	result = lexicon.scan("the in of")
	assert_equal(result, [('prep', 'the'),
										('prep', 'in'),
										('prep', 'of')])
										
def test_dig():
	assert_equal(lexicon.scan("1234"), [('dig', '1234')])
	result = lexicon.scan("3 45 987")
	assert_equal(result, [('dig', '3'),
						  ('dig', '45'),
						  ('dig', '987')])
						  
def test_noun():
	assert_equal(lexicon.scan("beer"), [('noun', 'beer')])
	result = lexicon.scan("beer princess")
	assert_equal(result, [('noun', 'beer'),
						  ('noun', 'princess')])
						  
def test_error():
	assert_equal(lexicon.scan("ASQSA"), [('error', 'ASQSA')])
	result = lexicon.scan("bear IAS fdsafeqfsd")
	assert_equal(result, [('error', 'bear'),
						  ('error', 'IAS'),
						  ('error', 'fdsafeqfsd')])										