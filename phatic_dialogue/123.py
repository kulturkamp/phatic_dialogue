with open('sport.txt', 'r') as f:
    lines = f.readlines()

# remove spaces
lines = [line.replace('. ', '.').replace('\n', '') for line in lines]

# finally, write lines in the file
with open('sport.txt', 'w') as f:
    f.writelines(lines)