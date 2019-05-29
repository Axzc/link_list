# -*- coding:utf-8 -*-

class Node(object):
    '''节点'''

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class LinkList(object):
    '''链表'''

    def __init__(self, node=None):
        self.__head = node # 头结点

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head == None

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

    def insert(self, pos, item):
        '''指定位置添加元素'''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            prior = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                prior = prior.next
            node.next = prior.next
            prior.next = node

    def remove(self, item):
        '''删除节点'''
        cur = self.__head
        prior = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:  # 如果是头结点
                    self.__head = cur.next
                else:
                    prior.next = cur.next
                break
            else:
                prior = cur
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
    ll = LinkList()
    print(sll.is_empty())
    print(sll.length())
    ll.append(12)
    ll.add(10)
    ll.travel()
    ll.insert(0, 333)
    ll.travel()
