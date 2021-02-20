S = list(input())
s_S = S[0::2]
b_S = S[1::2]

s_S = "".join(s_S)
b_S = "".join(b_S)

s_S = s_S.islower()
b_S = b_S.isupper()

if s_S == True and b_S == True:
  print("Yes")
elif s_S == True or b_S == False:
  print("Yes")
elif s_S == False or b_S == True:
  print("Yes")
else:
  print("No")