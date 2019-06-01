# -*- coding:utf-8 -*-

class Node(object):
    '''节点'''

    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prior = None


class DoubleLinkList(object):
    '''双链表'''

    def __init__(self, node=None):
        self.__head = node # 头结点

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head is None

    def length(self):
        '''长度'''
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next  # 移动到下一个节点
        return count

    def travel(self):
        '''遍历链表'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('')

    def add(self, item):
        '''在链表头部添加元素'''
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prior = node

    def append(self, item):
        '''链表尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prior = cur

    def insert(self, pos, item):
        '''指定位置添加元素'''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            node.next = cur
            node.prior = cur.prior
            cur.prior.next = node
            cur.prior = node

    def delete(self, item):
        '''删除节点'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:  # 如果是头结点
                    self.__head = cur.next
                    if cur.next:  # 判断链表是否只有一个节点
                        cur.next.prior = None
                else:
                    cur.prior.next = cur.next
                    if cur.next:  # 如果不是最后一个节点
                        cur.next.prior = cur.prior
                break
            else:
                cur = cur.next

    def search(self, item):
        '''查找节点是否存在'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    dll = DoubleLinkList()
    dll.append(1)
    dll.append(12)
    dll.insert(2, 312)
    dll.insert(1, 222)
    dll.delete(12)
    dll.delete(312)
    dll.travel()
