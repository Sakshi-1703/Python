while True:
    line = input('enter: ')
    if line[0] == '#': #doesnt print anything
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
