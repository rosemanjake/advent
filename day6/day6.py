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
    for num in state.keys():
        if not state[num] == 0 and not num == -1:
            state[num - 1] += state[num]
            state[num] -= state[num]

    if -1 in state.keys():
        state[6] += state[-1]
        state[8] += state[-1]
        state[-1] = 0
    return state

def get_total(state, days):
    for i in range(days):
        state = increment(state)      
    return sum(state.values())

state = get_state(open(f"{os.path.dirname(__file__)}\\day6.txt", "r").read())
print(f"Number of fish after 80 days = {get_total(copy.deepcopy(state), 80)}")
print(f"Number of fish after 256 days = {get_total(state, 256)}")