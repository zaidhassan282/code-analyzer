def LexicalErrorDetector(tokenSets):
    print("\n==============>Lexical Errors:")
    for index in range(len(tokenSets)):
        if tokenSets[index][0] =="Invalid":
            print(tokenSets[index][2])
    print("\n<<===========================\n")