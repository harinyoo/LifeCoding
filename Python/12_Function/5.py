input_id = input("아이디를 입력해주세요.\n")

def login(id):
    members = ['brooklyn', 'sydney', 'victoria']
    for member in members:
        if member == id:
            return True
    return False

if login(input_id):
    print('Hello, ' + input_id)
else:
    print('Who are you?')
