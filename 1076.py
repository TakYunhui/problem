color_val = dict()
color_mul = dict()
color = ['black', 'brown', 'red', 'orange',
         'yellow', 'green', 'blue', 'violet',
         'grey', 'white']
for i in range(10):
    color_val[color[i]] = i
    color_mul[color[i]] = 10 ** i

first = input()
second = input()
third = input()
print(int(str(color_val[first]) + str(color_val[second])) * color_mul[third])