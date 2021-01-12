word = 'blind'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

import re
datas = []
word2 = word.lower()
for txt in pages:
    tmp = []    # url, href, score, links, link_score, matching_score
    head = re.findall("<meta(.+)\n", txt)
    for a in head:
        if 'content' in a:
            url = re.findall("content=\"(.+)\"/>$", a)
            tmp.append(url)
    body = txt[txt.find('<body>')+6:txt.find('</body>')]
    body_list = list(filter(lambda x: x != '', body.split('\n')))
    score = links = 0
    href = []
    for b in body_list:
        if b.startswith('<a'):
            links += 1
            href.append(re.findall("href=\"(.+)\">", b))
        else:
            word_list = re.sub('[^a-zA-Z]', '.', b).split('.')
            score += len([w for w in word_list if w.lower() == word2])
    else:
        tmp.append(href)
        tmp.append(score)
        tmp.append(links)
        tmp.append(0)
    datas.append(tmp)

for i in range(len(datas)):
    for href in datas[i][1]:
        for k in range(len(datas)):
            if href == datas[k][0]:
                datas[k][4] += (datas[i][2] / datas[i][3])

print(datas)

max = index = 0
for e, data in enumerate(datas):
    matching_score = data[2] + data[4]
    if max < matching_score:
        max = matching_score
        index = e
print(index)