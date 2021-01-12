# 전화번호 목록   [효율성테스트 - 통과 (3.29ms, 15.3MB)]
# sort : 원본 리스트 변환 / sorted : 새로운 리스트 반환
# sort() 더 빠름
phone_book = ['119', '97674223', '1195524421']
phone_book.sort()
for i in range(len(phone_book)-1):
    if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
        print("False")
print("True")


# 베스트 풀이
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True


