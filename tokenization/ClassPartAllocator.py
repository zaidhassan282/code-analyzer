from tokenization.Classes import Classes as Cls

def ClassPartAllocator(param):
    ClassesAlpha,ClassesSymba = Cls()
    if param=="":
        return -1
    for key,value in ClassesAlpha.items():
        if param in value:
            return key
    for key,value in ClassesSymba.items():
        if param in value:
            return key
    return -1