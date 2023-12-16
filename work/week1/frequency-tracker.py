class FrequencyTracker:
    def __init__(self):
       
        self.freq_dict = {}
        self.freq_count_dict = {}

    def add(self, number: int) -> None:
        old_freq = self.freq_dict.get(number, 0)
        new_freq = old_freq + 1
        self.freq_dict[number] = new_freq

      
        self.freq_count_dict[new_freq] = self.freq_count_dict.get(new_freq, 0) + 1

       
        if old_freq > 0:
            self.freq_count_dict[old_freq] -= 1
            if self.freq_count_dict[old_freq] == 0:
                del self.freq_count_dict[old_freq]

    def deleteOne(self, number: int) -> None:
   
        if number in self.freq_dict and self.freq_dict[number] > 0:
            old_freq = self.freq_dict[number]
            
            self.freq_count_dict[old_freq] -= 1

            if self.freq_count_dict[old_freq] == 0:
                del self.freq_count_dict[old_freq]

            self.freq_dict[number] -= 1

            if self.freq_dict[number] > 0:
                new_freq = self.freq_dict[number]
                self.freq_count_dict[new_freq] = self.freq_count_dict.get(new_freq, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        
        return frequency in self.freq_count_dict


# # Your FrequencyTracker object will be instantiated and called as such:
# # obj = FrequencyTracker()
# # obj.add(number)
# # obj.deleteOne(number)
# # param_3 = obj.hasFrequency(frequency)