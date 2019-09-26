# -*- coding: utf-8 -*-
"""
trie树
"""


class TrieNode:
    def __init__(self, data: str):
        self._data = data
        self._children = [None] * 26
        self._is_ending_char = False


class Trie:

    def __init__(self):
        self._root = TrieNode('/')

    def insert(self, text: str) -> None:
        p = self._root
        for item_str in text:
            item_index = ord(item_str) - ord('a')
            if p._children[item_index] is None:
                p._children[item_index] = TrieNode(item_str)
            p = p._children[item_index]
        p._is_ending_char = True

    def find(self, pattern: str) -> bool:
        p = self._root
        for item_str in pattern:
            item_index = ord(item_str) - ord('a')
            if p._children[item_index] is None:
                return False
            p = p._children[item_index]
        if p._is_ending_char:
            # 找到
            return True
        else:
            # 不能完全匹配，只是前缀
            return False


if __name__ == "__main__":

    strs = ["how", "hi", "her", "hello", "so", "see"]
    trie = Trie()
    for s in strs:
        trie.insert(s)

    for s in strs:
        print(trie.find(s))

    print(trie.find("swift"))

"""
True
True
True
True
True
True
False
"""