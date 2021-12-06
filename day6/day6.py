import os

class Incrementer:
    def __init__(self, text, days):
        self.state = Incrementer.get_state(text)
        self.total = Incrementer.get_total(self.state, days)
    
    @staticmethod
    def get_total(state, days):
        for i in range(days):
            state = Incrementer.increment(state)      
        return sum(state.values())

    @staticmethod
    def increment(state):
        counter = state
        for num in state.keys():
            if not counter[num] == 0 and not num == -1:
                counter[num - 1] += counter[num]
                counter[num] -= counter[num]

        if -1 in counter.keys():
            counter[6] += counter[-1]
            counter[8] += counter[-1]
            counter[-1] = 0
        return counter

    @staticmethod
    def get_state(text):
        nums = [int(num) for num in text.split(",")]
        counter = {}
        for i in range(-1, 9):
            counter[i] = 0
            if i in nums:
                counter[i] = nums.count(i)
        return counter

text = open(f"{os.path.dirname(__file__)}\\day6.txt", "r").read()
print(f"Number of fish after 80 days = {Incrementer(text, 80).total}")
print(f"Number of fish after 80 days = {Incrementer(text, 256).total}")