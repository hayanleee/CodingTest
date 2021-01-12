n = 4
folding = [0]
for i in range(n-1):
    folding = folding + [0] + [1-i for i in folding[::-1]]
print(folding)