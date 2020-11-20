url = "http://youtube.com"
my_str = url.replace("http://", "") # 규칙1
# print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙2
# my_str[0:5] -> 0 ~ 5 직전까지. (0,1,2,3,4)
# print(my_str)
# 0~3 자리 = nav, 글자갯수 = 5, e의 갯수=1, 맨 끝에 !
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url,password ))