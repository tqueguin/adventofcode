import timeit

f = open("input.txt", mode="r")

lines = f.read().split('\n\n')

fp, sp = lines[0].split('\n'), lines[1].split('\n')
rules = dict()
for rule in fp:
    name = rule.split("{")[0]
    steps = rule.split("{")[1].strip("}").split(",")
    rules[name] = steps

def test_part(part):
    current_rule = "in"
    finished = False
    while not finished:
        steps_to_follow = rules[current_rule]
        for step in steps_to_follow:
            if step == "A":
                return True
            elif step == "R":
                return False
            elif "<" not in step and ">" not in step:
                current_rule = step
                break
            else:
                condition = step.split(":")[0]
                if (condition[1] == "<" and part[condition[0]] < int(condition[2:])
                        or condition[1] == ">" and part[condition[0]] > int(condition[2:])):
                    current_rule = step.split(":")[1]
                    if current_rule == "A":
                        return True
                    elif current_rule == "R":
                        return False
                    break

x-> 0;4000
m-> 0;4000
a-> 0;4000
s-> 0;4000