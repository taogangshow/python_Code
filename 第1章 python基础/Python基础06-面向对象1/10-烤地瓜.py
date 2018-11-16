class SweetPotato:
    def __init__(self):
        self.cookedLevel = 0
        self.cookString = "生的"
        self.condiments = []
    def __str__(self):
        msg = "地瓜状态:"+self.cookString+"\n"+"烘烤等级:"+str(self.cookedLevel)+"\n"+"添加的佐料有:无"
        if len(self.condiments)>0:
            msg = "地瓜状态:"+self.cookString+"\n"+"烘烤等级:"+str(self.cookedLevel)+"\n"+"添加的佐料有:"+str(self.condiments)
        return msg

        #return "地瓜　状态:%s(%d) 添加的佐料有:%s"%(self.cookString,self.cookedLevel,str(self.condiments))
    def cook(self,cook_time):
        self.cookedLevel+=cook_time
        if self.cookedLevel>=0 and self.cookedLevel<3:
            self.cookString="生的"
        elif self.cookedLevel>=3 and self.cookedLevel<5:
            self.cookString="半生不熟"
        elif self.cookedLevel>=5 and self.cookedLevel<8:
            self.cookString="熟了"
        elif self.cookedLevel>=8:
            self.cookString="糊了"
    def addCondiments(self,condiments):
        self.condiments.append(condiments)

di_gua = SweetPotato()
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("番茄酱")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("沙拉酱")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("芝士")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("鱼子酱")
print(di_gua)
di_gua.cook(1)
print(di_gua)
