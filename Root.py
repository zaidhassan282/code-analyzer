# All imports
import pathlib
from tokenization.WordTokenizer import WordTokernizer
from LexicalErrs import LexicalErrorDetector
from syntaxAnalyzer.syntaxAnalyzer import SA

#                           Implemetation

# Reading text file as input of program.
file = open(str(pathlib.Path(__file__).parent.absolute())+"/Code.txt","r")
stringData =file.read()

# Word tokenizer will generate the token sets.
tokenSets = WordTokernizer(stringData)
print(f"==========>>Token Set\n{tokenSets}\n<<==========")

# Lexical error detector will detect the invalid tokens from tokens set.
LexicalErrorDetector(tokenSets)

# Syntax analyzer, analyzes token sets and will print the syntax error, if occur.
tokenSets.append(("$", "$", -1))

# Syntaxt analzer constructor calling.
saInst = SA()

# Passing taokensets as input in Syntax Analyzer.
saInst.SyntaxAnalyzer(tokenSets)
