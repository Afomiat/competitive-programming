class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        card = deque()

        for i in range(len(deck)):
            if card:
                card.appendleft(card.pop())
            card.appendleft(deck[i])
        return card