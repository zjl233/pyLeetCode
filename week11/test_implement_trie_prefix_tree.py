from unittest import TestCase

from week11.implement_trie_prefix_tree import Trie


class TestTrie(TestCase):
    def setUp(self) -> None:
        self.trie = Trie()

    def test_insert(self):
        ...

    def test_search(self):
        self.trie.insert('apple')
        self.assertEqual(1, self.trie.search('apple'))
        self.assertEqual(0, self.trie.search('bbb'))

    def test_starts_with(self):
        self.trie.insert('apple')
        self.assertTrue(self.trie.startsWith('app'))
        self.assertFalse(self.trie.startsWith('bbb'))

    def test_delete(self):
        self.trie.insert('apple')
        self.assertEqual(1, self.trie.search('apple'))
        self.trie.delete('apple')
        self.assertEqual(0, self.trie.search('apple'))


