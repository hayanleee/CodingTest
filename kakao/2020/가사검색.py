words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
# result = [3, 2, 4, 1, 0]

result = []
for query in queries:
    if query[:1] == '?':
        result.append(len([word for word in words if word.endswith(query.replace('?',"")) and len(word) == len(query)]))
    else:
        result.append(len([word for word in words if word.startswith(query.replace('?',"")) and len(word) == len(query)]))
print(result)