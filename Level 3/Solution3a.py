l = [4,8,4,16]
# l = [1,3]

cache = [0] * len(l)
print(cache)
count = 0
for i in range(0,len(l)):
    for j in range(0, i):
        if l[i] % l[j] == 0:
            cache[i] = cache[i] + 1
            count = count + cache[j]
            print("count", count)
        print(j)

print (cache)
print (count)