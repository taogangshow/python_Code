class Home:
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.resi_area = new_area#房屋总面积
        self.contain_items = []
    def __str__(self):
        if len(self.contain_items)>0:
            msg = "房屋总面积为:%d平米\n可用面积为:%d\n户型为:%s\n地理位置:%s\n"%(self.area,self.resi_area,self.info,self.addr)
            msg+="当前房屋里的家具有:%s"%(str(self.contain_items))
        else:
            msg = "房屋总面积为:%d平米\n可用面积为:%d\n户型为:%s\n地理位置:%s\n"%(self.area,self.area,self.info,self.addr)
        return msg
    def add_item(self,item):
        #self.resi_area-=item.area
        #self.contain_items.append(item.name)
        self.resi_area-=item.get_area()
        self.contain_items.append(item.get_name())
class Bed:
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area
    def __str__(self):
        return "%s的占用面积为:%d平米"%(self.name,self.area)
    def get_area(self):
        return self.area
    def get_name(self):
        return self.name

fangzi = Home(120,"三室一厅","北京市-朝阳区-长安街-888号")
print(fangzi)
print("*"*50)
bed1 = Bed("席梦思",4)
print(bed1)
print("*"*50)
fangzi.add_item(bed1)
print(fangzi)
print("*"*50)
bed2 = Bed("三人床",6)
print(bed2)
print("*"*50)
fangzi.add_item(bed2)
print(fangzi)
print("*"*50)
