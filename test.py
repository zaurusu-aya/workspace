s = []
while True:
    h = input('集計:')
    if h == '':
        break
    else:
        s.append(str(h))

s_list = s

result = {}
for name in s_list:
    name = name.strip()
    if not name in result:
        result[name] = 0
    result[name] += 1

for name, v in result.items():
    print(name + ' = ' + str(v))
