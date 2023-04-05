#counting

zork = 0
print('Before: zork=', zork)
for num in [3, 12, 71, 19, 8, 32]:
    zork = zork + 1
    print (zork, num)
print('after: zork=', zork)
print('Done!')

#summing

zork = 0
print('Before: zork=', zork)
for num in [3, 12, 71, 19, 8, 32]:
    zork = zork + num
    print (zork)
print('after: zork=', zork)
print('Done!')

#average

count = 0
sum = 0
print('Before: count=', count)
for num in [3, 12, 71, 19, 8, 32]:
    count = count + 1
    sum = sum + num
    avg = sum / count
print('after: count=', count)
print('after: sum=', sum)
print('after: average=', avg)
print('Done!')

#filtering 

print('before')
for value in [3, 12, 71, 19, 8, 32]:
    if value > 20:
        print (value)
print('done')






