class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # one child for each letter of the alphabet
        self.is_end_of_word = False  # flag to indicate end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            index = self._char_to_index(ch)
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            index = self._char_to_index(ch)
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            index = self._char_to_index(ch)
            if not node.children[index]:
                return False
            node = node.children[index]
        return True
