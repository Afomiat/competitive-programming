class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {c: i for i, c in enumerate(order)}

        def compare_words(word1, word2):
            for char1, char2 in zip(word1, word2):
                if order_dict[char1] < order_dict[char2]:
                    return True
                elif order_dict[char1] > order_dict[char2]:
                    return False

            return len(word1) <= len(word2)

        return all(compare_words(words[i], words[i + 1]) for i in range(len(words) - 1))