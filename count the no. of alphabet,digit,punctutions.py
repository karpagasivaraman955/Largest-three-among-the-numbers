n = "python37#"
count = 0
digit = 0
pun = 0
for i in range(0, len(n)):
    if("a" <= n[i] <= "z") or ("A" <= n[i] <= "Z"):
        count = count + 1
    elif 0 <= n[i] <= 9:
        digit = digit + 1
    else:
        pun = pun + 1
print(count,digit,pun)