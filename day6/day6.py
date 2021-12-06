import os
import copy

def get_state(text):
    nums = [int(num) for num in text.split(",")]
    counter = {}
    for i in range(-1, 9):
        counter[i] = 0
        if i in nums:
            counter[i] = nums.count(i)
    return counter

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

def get_total(state, days):
    for i in range(days):
        state = increment(state)      
    return sum(state.values())

state = get_state(open(f"{os.path.dirname(__file__)}\\day6.txt", "r").read())
print(f"Number of fish after 80 days = {get_total(copy.deepcopy(state), 80)}")
print(f"Number of fish after 256 days = {get_total(state, 256)}")