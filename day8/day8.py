import os
import re

posmap = {
    0:[0,1,2,3,4,5],
    1:[2,3],
    2:[1,2,3,4,5,6],
    3:[1,2,3,4,6],
    4:[0,2,3,6],
    5:[0,1,3,4,6],
    6:[0,1,3,4,5,6],
    7:[1,2,3],
    8:[0,1,2,3,4,5,6],
    8:[0,1,2,3,4,6]
}

posmap_str = {
    0:"abcefg",
    1:"cf",
    2:"acdeg",
    3:"acdfg",
    4:"bcdf",
    5:"abdfg",
    6:"abdefg",
    7:"acf",
    8:"abcdefg",
    9:"abcdfg"
}
# key = number of segments, value = number
countmap = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

def get_input(file):
    f = open(f"{os.path.dirname(__file__)}\\{file}", "r").read()
    splits = [line.split("|") for line in f.split("\n")]
    final = []
    for line in splits:
        newline = []
        for half in line:
            tokens = half.split(" ")
            newline.append([token for token in tokens if token != ""])
        final.append(newline)
    return final

def get_known(lines):
    line_objs = []
    for line in lines:
        signals = (get_knowns(line[0]))
        line_objs.append(Line(signals, line[1]))
    return line_objs

def get_knowns(set):
    knownmap = {}
    for token in set:
        if len(token) in countmap.keys():
            candidate = countmap[len(token)]
            knownmap[token] = candidate
        else:
            knownmap[token] = "unknown"

    return knownmap

class Line:
    def __init__(self, signals, outputs):
        self.signals = signals
        self.outputs = outputs
        self.knowns =  Line.get_local_knowns(signals)

        self.knowns[9] = Line.get_nine(self.knowns, self.signals)
        zeroandsix = Line.get_six_and_zero(self.knowns[9], self.knowns, self.signals)
        self.knowns[0] = zeroandsix[0]
        self.knowns[6] = zeroandsix[1]
        Line.get_five(self.knowns, self.signals)
        Line.get_three(self.knowns, self.signals)
        Line.get_two(self.knowns, self.signals)
        
        self.output_value = Line.get_output_value(self.knowns, self.outputs)

    @staticmethod
    def get_output_value(knowns, outputs):
        output_value = ""
        for output in outputs:
            found = False
            for num in knowns.keys():
                if set(output) == set(knowns[num]):
                    appendage = str(num)
                    found = True
                    if appendage == "2":
                        if len(get_common(output + knowns[1])) == 1:
                            appendage = "2"
                        else: 
                            appendage = "3"
                    output_value = output_value + appendage
            if found == False:
                if len(get_common(output + knowns[1])) == 1:
                    output_value = output_value + "2"
                else: 
                    output_value = output_value + "3"
        return output_value

    @staticmethod
    def get_five(knowns, signals):
        pos3 = ""
        pos4 = ""
        nineandzero = get_unique(knowns[9] + knowns[0])
        for char in nineandzero:
            if char in knowns[9]:
                pos3 = char
            elif char in knowns[0]:
                pos4 = char
        
        oneandsix = get_unique(knowns[1] + knowns[6])
        pos2 = "".join([char for char in oneandsix if char in knowns[1]])
        
        five = re.sub(pos4,"",knowns[6])

        for string in signals.keys():
            if set(five) == set(string):
                five = string

        knowns[5] = five

        return
    
    @staticmethod
    def get_three(knowns, signals):
        #if knowns[9] == "cafbge":
        #    print("hi")
        pos1 = ""
        pos2 = ""
        oneandfive = get_unique(knowns[1] + knowns[5])
        for char in oneandfive:
            if char in knowns[5]:
                pos1 = char
            if char in knowns[1]:
                pos2 = char
        cand = re.sub(pos1,"",knowns[5])
        cand = cand + pos2

        for string in signals.keys():
            if set(cand) == set(string):
                cand = cand


        knowns[3] = cand
        return

    @staticmethod
    def get_two(knowns, signals):

        pos4 = get_unique(knowns[9] + knowns[8])

        pos5 = get_common(knowns[1] + knowns[5])
        for char in knowns[1]:
            if char != pos5:
                pos2 = char
       
        two = re.sub(pos2,"",knowns[3])
        cand = two + pos4
       
        final = ""
        for string in signals.keys():
            if set(cand) == set(string):
                final = cand
        if final == "":
            signal_sets = {}
            knowns_sets = {}

            for signal in signals.keys():
                signal_sets[signal] = set(signal)
            for val in knowns.values():
                knowns_sets[val] = set(val)

            for signal in signals.keys():
                for key in knowns:
                    if not signal_sets[signal] in knowns_sets.values():
                        final = signal

        knowns[2] = final

        return


        #for signal in signals.keys():
        #    if not signal in knowns.values():
        #        knowns[2] = signal

    @staticmethod
    def get_local_knowns(signals):
        knowns = {key:value for (key,value) in signals.items() if value != "unknown"}
        return {v: k for k, v in knowns.items()}
                    
    @staticmethod
    def get_nine(knowns, signals):
        candidate = ""

        candidate = knowns[4] + knowns[7] + knowns[1] + knowns[8]
        candidate = get_common(candidate)
        
        finalcand = ""
        for key in signals:
            if len(key) == 6 and num_of_diffs(key, candidate) == 1:
                finalcand = key

        return finalcand

    @staticmethod
    def get_six_and_zero(nine, knowns, signals):
        zero = ""
        six = ""

        for string in signals:
            if not string in knowns and string != nine and len(string) == 6:
                #0 or 6
                if len(get_common(knowns[1] + string)) == 2:
                    zero = string
                elif len(get_common(knowns[1] + string)) == 1:
                    six = string
                
        return zero, six


#def get_final(knowns):
#
#    for line in knowns:
def get_common(string):
    commons = [char for char in string if string.count(char) > 1]
    final = ""
    for char in commons:
        if not char in final:
            final = final + char
    return "".join(final)

def get_unique(string):
    final = ""
    for char in string:
        if string.count(char) == 1:
            final = final + char
    return final

def num_of_diffs(string1, string2):
    return len(get_unique(string1 + string2))

input = get_input("day8.txt")
final_knowns = get_known(input)
final = 0
for known in final_knowns:
    final = final + int(known.output_value)
print(final)

