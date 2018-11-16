# -*- coding: utf-8 -*-
class Deque(object):
    def __init__(self):
        self.__list = []

    def add_front(self,item):
        """从队头加入一个item元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """从队尾加入一个item元素"""
        self.__list.append(item)

    def remove_front(self):
        """从队头删除一个item元素"""
        return self.__list.pop(0)

    def remove_rear(self):
        """从队尾删除一个item元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断双端队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == "__main__":
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_front(3)
    deque.add_front(4)
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_front())
    print("* "*20)
    deque.add_rear(5)
    deque.add_rear(6)
    deque.add_rear(7)
    deque.add_rear(8)
    print(deque.remove_rear())
    print(deque.remove_rear())
    print(deque.remove_rear())
    print(deque.remove_rear())