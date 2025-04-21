import json

with open("creeper_head.json") as f:
    data: list = json.load(f)

print(data)

for y in range(len(data)):
    # print("Y:", y)
    print(y, data[y])
    for x in range(len(data[y])):
        # print("X:", x)
        print(x, y, data[y][x])

