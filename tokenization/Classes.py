def Classes():
    ClassesAlpha = {
        "void": ['void'],
        'grid': ['grid'],
        "jabtak": ['jabtak'],
        "karo": ['karo'],
        "agar": ['agar'],
        'warna': ['warna'],
        'return': ['return'],
        'Main': ['Main'],
        'class': ['class'],
        'naya': ['naya'],
        'passive': ['passive'],
        'aur': ['aur'],
        'ya': ['ya'],
        "BrkCont": ['roko', 'jari'],  # Break Continue
        "DT": ["int", "float", "bool", "string", "char"],  # Data types
        "AM": ["ijtemai", "infiradi", "protected", "andruni"],  # Access Modifiers
        "VO": ['arzi', 'badlo'],  # Virtual Override
        "extends": ['extends'],          #for inheritance
    }

    classesSymba = {
        '!': ['!'],
        "PM": ['+', '-'],  # Plus Minus class
        "MDM": ['*', '/', '%'],  # Binary operator class

        "Comp_asgn": ["+=", "-=", "*=", "/=", "%="],         # Compound Assignment operator
        "RelOp": ['>','<','>=','<=','!=','=='],          #Relational Operators
        "=": ['='],  # Assignment operator class,
        "inc_dec": ['+o','-o'],   # increment and decrement
        ";": [';'],        #End of Statement
        ",":[','],
        ".":['.'],
        "{":['{'],
        "}":['}'],
        "(":['('],
        ")":[')'],
        "[":['['],
        ']':[']']
    }

    return [ClassesAlpha,classesSymba]
