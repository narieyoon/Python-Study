# 데이터 입력받기
N_num = int(input(""))
num = input("")
N_cal = input("")

num_list = ''.join(num.split())
N_cal_list = list(map(int, N_cal.split()))


cal_list_1 = list(map(lambda x: x[0]*x[1], list(zip(['+', '-', '*', '/'] , N_cal_list))))
cal_list_2 = ''.join(cal_list_1)

def chkDupNum(s):
    result = ''
    for i in range(len(s)):
        if str(i) in s:
            result += str(i)
    return len(result) == len(s)

cal_num_lst = []

for i in range(0, pow(10, N_num)):
    if len(str(i)) == N_num - 1 and chkDupNum(str(i)):
        cal_num_lst.append(str(i))
    elif len(str(i)) == N_num - 2 and chkDupNum('0'+ str(i)):
        cal_num_lst.append('0'+ str(i))

def Num_to_Chr(s):
    result = ''
    for i in s:
        result += cal_list_2[int(i)]
    return result

cal_list_3 = list(map(Num_to_Chr, cal_num_lst))


def Num_suffle(n,s):
    result = n[0]
    for i in range(N_num - 1):
        if '-' in result and s[i] == '/':
            result =  str(eval((result + ' * -1' + s[i].replace('/', '//')) + n[i+1]) * -1)
        else:
            result =  str(eval(result + s[i].replace('/', '//') + n[i+1]))
    return result

result = list(map(lambda x:eval(Num_suffle(num_list, x)), cal_list_3))

print(max(result))
print(min(result))
