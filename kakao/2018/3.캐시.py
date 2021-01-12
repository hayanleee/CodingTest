cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

time = 0
cache = []
if cacheSize == 0:
    print(len(cities) * 5)

for arr in cities:
    arr = arr.lower()
    if arr in cache:
        time += 1
        cache.pop(cache.index(arr))
        cache.append(arr)
    else:
        time += 5
        if len(cache) >= cacheSize:
            cache.pop(0)
        cache.append(arr)
print (time)