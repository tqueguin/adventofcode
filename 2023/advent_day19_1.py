f = open("input.txt", mode="r")

lines = f.read().split('\n\n')

fp, sp = lines[0].split('\n'), lines[1].split('\n')
rules = dict()
for rule in fp:
    name = rule.split("{")[0]
    steps = rule.split("{")[1].strip("}").split(",")
    rules[name] = steps
parts = list()
for part in sp:
    comps = part.strip("{").strip("}").split(",")
    p = dict()
    for c in comps:
        p[c.split("=")[0]] = int(c.split("=")[1])
    parts.append(p)

total = 0
for part in parts:
    current_rule = "in"
    finished = False
    while not finished:
        steps_to_follow = rules[current_rule]
        for step in steps_to_follow:
            if step == "A":
                total += part["x"] + part["m"] + part["a"] + part["s"]
                finished = True
                break
            elif step == "R":
                finished = True
                break
            elif "<" not in step and ">" not in step:
                current_rule = step
                break
            else:
                condition = step.split(":")[0]
                if (condition[1] == "<" and part[condition[0]] < int(condition[2:])
                        or condition[1] == ">" and part[condition[0]] > int(condition[2:])):
                    current_rule = step.split(":")[1]
                    if current_rule == "A":
                        total += part["x"] + part["m"] + part["a"] + part["s"]
                        finished = True
                    elif current_rule == "R":
                        finished = True
                    break

print(total)
