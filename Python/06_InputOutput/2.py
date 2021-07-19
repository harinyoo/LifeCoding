in_str = input("아이디를 입력해주세요.\n")

# print(type(in_str))
# >> <class 'str'>
# 즉, in_str은 string 이므로 11을 입력해도 숫자 11이 아닌, 문자열 "11"로 인식한다.
# 따라서 출력 결과도 "Hello! brooklyn"이 아닌, "Who are you?"가 된다.
# real_brooklyn = "11"이면 "Hello! brooklyn" 출력 가능.

real_brooklyn = "11"
real_sydney = "ab"
if real_brooklyn == in_str:
    print("Hello! brooklyn")
elif real_sydney == in_str:
    print("Hello! sydney")
else:
    print("Who are you?")
