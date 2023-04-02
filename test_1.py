####### 1000. 입출력 다루기 - 덧셈(https://www.acmicpc.net/problem/1000)
# A, B = input().split()
# print(int(A) + int(B))

####### 1001. 입출력 다루기 - 뺄셈(https://www.acmicpc.net/problem/1001)
# A, B = input().split()
# print(int(A) - int(B))

####### 1001. 입출력 다루기 - 나눗셈(https://www.acmicpc.net/submit/1008)
# A, B = input().split()
# print(int(A) / int(B))

####### 사칙연산 - (https://www.acmicpc.net/problem/10869)
# a, b = input().split()
# A = int(a)
# B = int(b)
# print(A + B)
# print(A - B)
# print(A * B)
# print(int(A / B))
# print(A % B)

####### ??! - https://www.acmicpc.net/problem/10926
# name = input()
# print(name + "??!")

####### 서기 불기 변환 - https://www.acmicpc.net/problem/18108
# year = int(input())
# print(year - 543)

####### https://www.acmicpc.net/problem/10430
# a,b,c = input().split()
# A,B,C = int(a), int(b), int(c)
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)


####### https://www.acmicpc.net/problem/2588
A = int(input())
B = int(input())
B_100 = int(B / 100) # 100의 자리 숫자이고 100의 배수
B_10 = int((B - B_100) / 10) # 10의 자리 숫자이고 10의 배수
B_1 = B - B_100 - B_10 # 1의 자리 숫자
print(B_100)
print(B_10)
print(B_1)
num1 = B_1 * A
num2 = B_10 * A
num3 = B_100 * A
print(num1)
print(num2)
print(num3)
print(num1 + num2 + num3)