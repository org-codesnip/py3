from typing import List


class Node:
    def __init__(self):
        self.children = {}
        self.epsilon = False

    def push(self, word: List[int]):
        if not word:
            self.epsilon = True
            return
        c = word.pop()

        self_next = self.children.pop(c, Node())
        self_next.push(word)

        self.children[c] = self_next
