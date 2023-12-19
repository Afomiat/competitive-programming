class Bitset:
    def __init__(self, size):
        self.size = size
        self.bits = [0] * size
        self.count_ones = 0
        self.inverse = [1] * size

    def fix(self, idx):
        if 0 <= idx < self.size and self.bits[idx] == 0:
            self.bits[idx] = 1
            self.count_ones += 1
            self.inverse[idx] = 0

    def unfix(self, idx):
        if 0 <= idx < self.size and self.bits[idx] == 1:
            self.bits[idx] = 0
            self.count_ones -= 1
            self.inverse[idx] = 1

    def flip(self):
        self.bits, self.inverse = self.inverse, self.bits
        self.count_ones = self.size - self.count_ones

    def all(self):
        return self.count_ones == self.size

    def one(self):
        return self.count_ones > 0

    def count(self):
        return self.count_ones

    def toString(self):
        return ''.join(map(str, self.bits))

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()