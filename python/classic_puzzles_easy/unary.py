# https://www.codingame.com/ide/puzzle/unary

message = input()

binary_message = ''.join(format(ord(x), 'b').zfill(7) for x in message)

previous_byte = '2'
answer = ""
for i in binary_message:
    if i != previous_byte:
        if i == '1': answer += ' 0 '
        else: answer += ' 00 '
    answer += '0'
    previous_byte = i

print(answer[1:])
