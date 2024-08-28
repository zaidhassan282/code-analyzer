class SemanticAnalyzer:
    def __init__(self):
        self.functionTableEntries = []
        self.mainTableEntries=[]
        self.bodyTable = []
        self.bodyTableEntries = []
        self.scope=0
        self.link=0
        self.funcStack=[]

    def insertMainTable(self,name,accMod,category,parent):
        if len(self.mainTableEntries):
            # redeclaration
            for obj in self.mainTableEntries:
                if obj["name"] == name:
                    return [False,f"re-declaration of class: {name}"]
            # undeclared parent check
            for obj in self.mainTableEntries:
                if parent=="None":
                    self.link+=1
                    self.mainTableEntries.append({"name":name,"accMod":accMod,"category":category,"parent":parent,"link":self.link})                
                    return [True,"success"]
                
                if obj["name"] == parent:
                    self.link+=1
                    self.mainTableEntries.append({"name":name,"accMod":accMod,"category":category,"parent":parent,"link":self.link})                
                    return [True,"success"]

            return [False,"un-declared identifier:"]

        else:
            if parent=="None":
                self.link+=1
                self.mainTableEntries.append({"name":name,"accMod":accMod,"category":category,"parent":parent,"link":self.link})                
                return [True,""]
            else: 
                return [False,f"Undeclared identifier: {parent}"]

    def insertFunctionTable(self,name,idType,scope):
        # Business logic
        for obj in self.functionTableEntries:
            if obj.name== name and obj.scope == scope:
                return [False,f"re-declaration of identifier: {name}"]
        self.functionTableEntries.append({"name":name,"type":idType,"scope":scope})
        return [True,""]

    def lookupIdScope(self,idVal):
        for obj in self.functionTableEntries:
            if obj.name == idVal and obj.scope == self.scope:
                return [True,""]
        return [False,f"Un-declared identifier: {idVal}"]


    def insertBodyTable(self,name,idType,accMod,typeModifier):
        for obj in self.bodyTableEntries:
            if obj.name== name:
                return [False,f"re-declaration of identifier: {name}"] 
        self.bodyTableEntries.append({"name":name,"idType":idType,"accMod":accMod,"typeModifier":typeModifier})
        return [True,""]


    def createScope(self):
        self.scope+=1
        self.funcStack.append(self.scope)      
        

    def destroyScope(self):
        self.bodyTable.append(self.bodyTableEntries)
        self.bodyTableEntries = []
        self.funcStack.pop()
        # --

