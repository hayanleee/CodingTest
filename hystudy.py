### 콤보박스 index로 value 값 찾기
self.comboBox.addItem("완제품", "CCN11671")
self.comboBox.currentIndexChanged.connect(self.currentIndexChanged1)
def currentIndexChanged1(self, index):
    self.cb1_idx = index
    print(self.comboBox.itemData(self.cb1_idx))


### FTP 파일 업로드
import ftplib
Output_Directory = ""
full_filePath = "S:\\Python\\csprogram\\ftptest\\_download_File\\Part 05.CATPart"
ftp = ftplib.FTP('192.168.1.35', 'ftpdraw', 'qwer1234!')
ftp.cwd(Output_Directory)
ftp.encoding='utf-8' # 한글도 가능하게!
with open(full_filePath, 'rb') as ftpup:
    ftp.storbinary('STOR ' + "Part 05.CATPart", ftpup)
ftp.rename("Part 05.CATPart", "0000abcde.CATPart")
ftp.quit()
ftpup.close()

#### 1번이랑 2번이랑 같은거, 포트차이
ftp = ftplib.FTP('127.0.0.1', 'ftpdraw', 'qwer1234!')    # 1번

ftp = ftplib.FTP()      # 2번
ftp.connect("127.0.0.1", "21")
ftp.login("ftpdraw", "qwer1234!")


### FTP 파일 다운로드
import ftplib
input_Directory = "S:\\Python\\csprogram\\ftptest\\Part 05.CATPart"
output_Directory = "\\"
ftp = ftplib.FTP('192.168.1.35', 'ftpdraw', 'qwer1234!')
fd = open(input_Directory, "wb")
ftp.cwd(output_Directory)
ftp.encoding='utf-8'
ftp.retrbinary("RETR " + "0000abcde.CATPart", fd.write)
ftp.quit()
fd.close()


### SHA256 변환, base64
import hashlib, base64
for realFiles in files:
    realFiles.replace('.', self.nowDate + '.')
    hashSHA = hashlib.sha256()
    hashSHA.update(realFiles.encode())
    sha = hashSHA.digest()
    bs = base64.b64encode(sha)
    ftype = realFiles[realFiles.rfind("."):]
    file = bs.decode('utf-8') + ftype
    self.shaFiles.append(file)


### SHA256 16진수 변환
import hashlib
shaFiles = []
files = ['abcdefg.txt', 'qwer123어니.txt']
for realFiles in files:
    hashSHA = realFiles.encode()
    hexdigest = hashlib.sha256(hashSHA).hexdigest()
    ftype = realFiles[realFiles.rfind("."):]
    file = hexdigest + ftype
    shaFiles.append(file)
print(shaFiles)


### hash + 16진수 파일확장명 유지(특문없음)
import hashlib
import datetime
now = datetime.datetime.now()
nowTime = now.strftime('%m%d%H%M%S')
realFiles = "Part 05.CATPart"
tmpfile =  realFiles + nowTime
hashSHA = tmpfile.encode()
hexdigest = hashlib.sha256(hashSHA).hexdigest()
ftype = realFiles[realFiles.rfind("."):]
file = hexdigest + ftype
print(file)



### QTreeWidget add child item
import sys
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget

if __name__ == '__main__':
    app = 0
    if QApplication.instance():
        app = QApplication.instance()
    else:
        app = QApplication(sys.argv)

    l1 = QTreeWidgetItem(["String A", "String B", "String C"])
    l2 = QTreeWidgetItem(["String AA", "String BB", "String CC"])

    for i in range(3):
        l1_child = QTreeWidgetItem(["Child A" + str(i), "Child B" + str(i), "Child C" + str(i)])
        l1.addChild(l1_child)

    for j in range(2):
        l2_child = QTreeWidgetItem(["Child AA" + str(j), "Child BB" + str(j), "Child CC" + str(j)])
        l2.addChild(l2_child)

    w = QWidget()
    w.resize(510, 210)

    tw = QTreeWidget(w)
    tw.resize(500, 200)
    tw.setColumnCount(3)
    tw.setHeaderLabels(["Column 1", "Column 2", "Column 3"])
    tw.addTopLevelItem(l1)
    tw.addTopLevelItem(l2)

    w.show()
    sys.exit(app.exec_())


### 딕셔너리 추가
#le = {123:'aaa'}
le = {}
le[456] = 'bbb' or le.update(456='bbb')

### url 열기
import webbrowser
webbrowser.open("http://172.21.0.129:8080/yPLM")

### ini 파일 읽기
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
downpath = config.get('PATH_INFO', 'downpath')

### ini 파일 쓰기
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
config.set('PATH_INFO', 'downpath', 'S:\\Python\\venv\\Lib\\site-packages\\pyqt5_tools')
with open('config.ini', 'w') as configfile:
    config.write(configfile)

### zfill 멋진거
In [1]: '{:<08d}'.format(190)
Out[1]: '19000000'

In [2]: '{:>08d}'.format(190)
Out[2]: '00000190'

### enumerate
t = [1, 5, 7, 33, 39, 52]
for p in enumerate(t):
    print(p)

(0, 1)
(1, 5)
(2, 7)
(3, 33)
(4, 39)
(5, 52)

for i, v in enumerate(t):
    print("index : {}, value: {}".format(i,v))

index : 0, value: 1
index : 1, value: 5
index : 2, value: 7
index : 3, value: 33
index : 4, value: 39
index : 5, value: 52

### 이중리스트 생성
>>> a = []
>>> a.append([])
>>> a[0].append(10)
>>> a[0].append(20)
>>> a.append([])
>>> a[1].append(500)
>>> a[1].append(600)
>>> a[1].append(700)
>>> a
[[10, 20], [500, 600, 700]]

###파일 자동 열기
import subprocess

p = subprocess.Popen(["notepad.exe", "S:\\Python\\csprogram\\ftptest\\test.txt"], stdout = subprocess.PIPE)
# Popen(["exe경로", "실행시킬파일경로"] ~~

### 날짜 datetime
import datetime

now = datetime.datetime.now()
nowTime = now.strftime('%Y-%m-%d %H:%M:%S')

### 자바 서버로 연동!
import requests
import sys
URL = "http://172.20.3.26:8080/yPLM/cad/draw/select/makeXML.do"
data = { 'root_file' : "D:\\util\\VIZDesign\\VIZCoreTrans_x64_20190402\\NT_VC14_64_DLL\\sample\\U_JOINT ASSY\\00.U_JOINT ASSY.CATProduct",
         'result_file' : "D:\\util\\VIZDesign\\VIZCoreTrans_x64_20190402\\NT_VC14_64_DLL\\sample\\U_JOINT ASSY\\result.xml",
         'id' : 'admin',
         'pwd' : 'ny123'
}
try:
    r = requests.post(url = URL, data = data)
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)

### 한국어 있으면 return > 0
import re
text = "한글 123abc d어이 상실"
text2 = "asdfjghwentcaw어"
text3 = "afnweukvhrk/2389@^@*#!_ adjkh"
text4 = "D:\\##S드라이브_통기레쓰\\#dw"
KoreanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', text))
print(KoreanCount)

### 클래스 변수 변경
class One(object):
    def example(self):
        self.what = 'aaaaaaaa'

a = One()
a.__class__.what = 'test'
print(a.what)

### 로컬 image 보이기
from PyQt5.QtGui import QPixmap
pixmap = QPixmap("S:\\Python\\csprogram\\ftptest\\U_JOINT ASSY.jpg")
pixmap = pixmap.scaled(230,220)
# pixmap = pixmap.scaledToHeight(240)  # 사이즈가 조정
self.label_20.setPixmap(pixmap)

### 웹 image 보이기
import urllib.request
from PyQt5.QtGui import QPixmap
url = "http://ytms.yura.co.kr/images/main/loginbt.jpg"
data = urllib.request.urlopen(url).read()
pixmap = QPixmap()
pixmap.loadFromData(data)
pixmap = pixmap.scaled(230,220)
# pixmap = pixmap.scaledToHeight(240)  # 사이즈가 조정
self.label_20.setPixmap(pixmap)

### 웹 urlopen(url, data)
import urllib.request
import urllib.parse
url = "http://172.20.3.26:8080/yPLM/cad/draw/insert/getThumbImage.do"
fname = '6f0d15e3322ddbda5504e5932554cb7dd3cd8f41e845a8227415c94de01c25ea.jpg'
data = urllib.parse.urlencode({'filename': fname}).encode()
try:
    image = urllib.request.urlopen(url, data).read()
except urllib.request.URLError as e:
    print(e.reason)
    return 0
except urllib.request.HTTPError as e:
    print('Reason: ', e.code)
    return 0

pixmap = QPixmap()
pixmap.loadFromData(image)
pixmap = pixmap.scaled(230,220)
self.label_20.setPixmap(pixmap)

### 클래스 변수 상속
class parent:
    def __init__(self):
        self.gogo()
    def gogo(self):
        self.id = 'admin'
class child(parent):
    def __init__(self):
        print(parent().id)
child()

### 변수 지정하지 않고 for 문
def run(self):
    for _ in range(10):
        ## 변수를 지정하지 않고 단순 반복을 하고 싶을 때는 _언더바를 사용한다.
        print(threading.currentThread().getName())

### progressbar 부드럽게
animation = QtCore.QPropertyAnimation(self.progressBar, b"value")
animation.setDuration(2000)
animation.setStartValue(0)
animation.setEndValue(100)
animation.start()

### 제너레이터
for name, age in mydict.items(): #mydict에 아이템을 하나씩 접근해서, key, value를 각각 name, age에 저장
    if age == search_age:
        print name

같은말 : [name for name, age in mydict.items() if age == search_age]

### 라벨 gif movie
movie = QtGui.QMovie("image/loading.gif")
self.label_gif.setMovie(movie)
movie.start()


### cmd command 실행
import os
os.popen("""D:\\final_test\\00.U_JOINT ASSY.CATProduct""")
# os.popen("Your command here")


### 윈도우 외부 프로그램 실행 (stderr=subprocess.PIPE, stdin=subprocess.PIPE 해줘야 exe 에서도 돌아감...)
import subprocess
VIZDesign_path = "C:\\Program Files\\Softhills\\VIZDesign\\V3.34.4\\VIZDesign.exe"
openFile_path = "D:\\final_test\\00.U_JOINT ASSY.CATProduct"
try:
    p = subprocess.Popen([VIZDesign_path, openFile_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
except:
    print("error")


### 암호화복호화
py -m pip install pycryptodome 해야됨..ㅎㅎㅎ 2버전은 pycrypto 맞는데 3은 dome 붙여야함


### psycopg2 fetchall 튜플말고 딕셔너리로 받고싶을때
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

### cx_oracle connection 방법
1. Connection String을 이용하는 방법
'user/password@address:port/sid' 의 형태
conn = cx_Oracle.connect('scott/tiger@localhost:1521/orcl')
conn = cx_Oracle.connect('sys/orange@localhost:1521/orcl', mode = cx_Oracle.SYSDBA)

2. DSN 을 이용하는 방법
('user' , 'password' , dsn object) 를 인자로 전달합니다.
dsn object는 ('address', port, 'sid')를 인자로 생성하면 됩니다.
dsn = cx_Oracle.makedsn('localhost',1521,'orcl')
conn = cx_Oracle.connect('scott','tiger',dsn)
conn = cx_Oracle.connect('sys','orange',dsn, mode = cx_Oracle.SYSDBA)

conn = cx_Oracle.connect('scott','tiger',cx_Oracle.makedsn('localhost',1521,'orcl'))
conn = cx_Oracle.connect('sys','orange',cx_Oracle.makedsn('localhost',1521,'orcl'), mode = cx_Oracle.SYSOPER)


### cx_oracle 헤매던거 (string, dsn 형태에 따라 서비스이름, sid 붙여주는게 달라)
conn = cx_Oracle.connect("yplmuser/plmuser119@192.168.1.36:1521/yplm.nyi.co.kr")        # 맨뒤에 서비스 이름이야

dsn = cx_Oracle.makedsn("192.168.1.36", 1521, "yplm")                                   # 맨뒤에 SID 야
conn = cx_Oracle.connect("yplmuser", "plmuser119", dsn)

### 출력... separate...
print("하나","둘","셋",1,2,3,sep='-')  # result : 하나-둘-셋-1-2-3

### 딕셔너리를 이용한 switch 함수
a = 2
def switch(x):
    print({0:"영", 1:"일", 2:"이"}.get(x, "default"))      # 받아온 key 값이 존재하지않으면 두번째 인자("default")를 반환한다.
switch(a)

### 람다 함수 (람다: 이름이 없는 함수 → lambda 매개변수들: 식)
def inc(n):
    return lambda x:x+n
f = inc(2)
print(f(12))

### 람다 함수2 (lambda 매개변수들: 식)(인수들)
# 같은내용
def plus_ten(x):
    return x + 10
plus_ten(1)        # 11
# 다른표현
plus_ten = lambda x: x + 10
plus_ten(1)        # 11
# 다른표현2
(lambda x: x + 10)(1)       # 11

### 람다 함수3 (lambda 매개변수들: 식1 if 조건식 else 식2)   ← 식1 은 참일때, 식2 는 거짓일때
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x % 3 == 0 else x, a))     # [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]

### 람다 함수3 응용해서 내가만든거 ㅋㅋㅋ
fsum = 100
max = 20
max = (lambda fsum,max: fsum if fsum>=max else max)(fsum, max)
print(max)

### for 문 한줄로
tmp = [2,3,4,5]
new = []
for i in tmp:
    new.append(i*2)
# 같은 내용
new = list([i*2 for i in tmp])

### for 문 한줄로 + if 추가
tmp = [2,3,4,5]
new = []
for i in tmp:
    if i>3:
        new.append(i*2)
    else:
        new.append(i*3)
# 같은 내용
new = list([i*2 if i>3 else i*3 for i in tmp])
# 이때! else가 없는경우 if를 앞에 넣으면 안된다.
new = list([i*3 for i in tmp if i>3])

### 한줄코딩
words = ['abcd', 'dbed', 'abc', 'ewr']
for txt in words:
    if 'ab' in txt:
        print("있음")
# 같은 내용
if any('ab' in txt for txt in words):
    print("있음")

### 한줄코딩2
some_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
resultlist = []
for s in some_list:
    if "abc" in s:
        resultlist.append(s)
# 같은 내용
matching = [s for s in some_list if "abc" in s]


### boolean 이용한..
tmp = [1,2]
print(bool(tmp))
print(int(not bool(tmp)))

### 독스트링
def funcA():
    '''함수 A 입니다'''
    pass
print(funcA.__doc__)

### 비공개 클래스 속성 (속성앞에 __ 붙이면 클래스 바깥에선 접근불가)
class Cls:
    __hystr = "hide"

### str.join(iterable)
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(''.join(a))           # abcdefg
print(''.join(a[:4]))       # abcd

### str에 list() 씌워주면
a = "abcdefg"
print(list(a))              # a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']