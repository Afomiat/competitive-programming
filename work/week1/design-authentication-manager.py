class AuthenticationManager:
# Space complexity: O(k) where k is the number of unique tokens generated
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.token = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime + self.timeToLive
        # Time complexity: O(1)
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token and self.token[tokenId] > currentTime:
            self.token[tokenId] = currentTime + self.timeToLive
        
        # Time complexity: O(1)
    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = sum(1 for token_exp in self.token.values() if token_exp > currentTime ) 
        return count
        # Time complexity: O(n)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)