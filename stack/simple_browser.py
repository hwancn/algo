# -*- coding: utf-8 -*-

"""
浏览器的前进后退的简易实现

我们使用两个栈，X 和 Y，我们把首次浏览的页面依次压入栈X，
当点击后退按钮时，依次从X中出栈，并且将出栈的数据压入栈Y，
当点击前进按钮时，依次从Y中出栈，并且将出栈的数据压入栈X，
若X中没有数据了，说明不可以后退了，
若Y中没有数据了，说明不可以前进了

需要注意一点的是，若浏览了新的页面，则需要清空Y

极客时间：https://time.geekbang.org/column/article/41222
"""

import sys
sys.path.append('../')
from stack.linked_stack import LinkedStack


class Browser:

    def __init__(self):
        self.forward_stack = LinkedStack()
        self.back_stack = LinkedStack()

    def can_forward(self):
        if self.back_stack.is_empty():
            return False
        return True

    def can_back(self):
        if self.forward_stack.is_empty():
            return False
        return True

    def open(self, url):
        print('open new url %s' % url, end='\n')
        self.forward_stack.push(url)
        # 打开新的页面的时候，需要清空Y栈
        self.back_stack.empty()

    def forward(self):
        if not self.can_forward():
            return
        top = self.back_stack.pop()
        self.forward_stack.push(top)
        print('forward to %s' % top, end='\n')

    def back(self):
        if not self.can_back():
            return
        top = self.forward_stack.pop()
        self.back_stack.push(top)
        print('back to %s' % self.forward_stack.top, end='\n')


if __name__ == '__main__':
    browser = Browser()
    browser.open('a')
    browser.open('b')
    browser.open('c')
    if browser.can_back():
        browser.back()

    if browser.can_forward():
        browser.forward()

    browser.back()
    # 打开新的页面d
    browser.open('d')
    browser.back()
    browser.back()

# a-->b-->c-->b-->c-->b-->d-->b-->a


