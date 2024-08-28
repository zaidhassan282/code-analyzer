from bagOfWords.FilterStartingSpaces import FilterStartingSpaces
from bagOfWords.WordsGenerator import WordsGenerator
import pytest

def test_for_filter_starting_spaces_1():
    assert FilterStartingSpaces([' ','1','2','3','4']) == ['1','2','3','4']

def test_for_filter_starting_spaces_2():
    assert FilterStartingSpaces(['1','2','3','4']) == ['1','2','3','4']

def test_for_words_generator_1():
    assert WordsGenerator(['i','n','t',' ','n','a','m','e','=',' ','\'','a','\'',"\"",'o','k','\"'])==\
    ["int","name","=","'a'","\"ok\""]