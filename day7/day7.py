import os
import statistics

def get_base_cost(average):
    base_costs = []
    for num in nums:
        base_costs.append(abs(average - num))
    return base_costs

def get_complex_cost(target):
    base_costs = get_base_cost(target)
    complex_costs = []

    for num in base_costs:
        fuel_cost = 0
        increment = 1
        for i in range(int(num)):
            fuel_cost = fuel_cost + increment
            increment += 1
        complex_costs.append(fuel_cost)

    return sum(complex_costs)

def find_lowest(avg, cycles): 
    cost_dict = {}
    cost_dict[avg] = get_complex_cost(avg)
    steps = round(cycles / 2)
    for step in range(steps):       
        cost_dict[avg - step] = get_complex_cost(avg - step)
        cost_dict[avg + step] = get_complex_cost(avg + step)
    
    return cost_dict[min(cost_dict, key=cost_dict.get)]

text = open(f"{os.path.dirname(__file__)}\\day7.txt", "r").read()
nums = [int(num) for num in text.split(",")]
median = statistics.median(nums)
avg = round(sum(nums) / len(nums))

print(f"solution to part 1 = {sum(get_base_cost(median))}")
print(f"solution to part 2 = {find_lowest(avg, 5)}")