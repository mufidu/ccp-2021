kata = input()
for character in '`~1234567890!@#$%^&*()-=[]\\;\',./\{\}|:\"<>?_+ ':
    kata = kata.replace(character, '')

kata = kata.lower()

j = len(kata)

try: 
    for i in range(j//2 if j%2==0 else j//2+1):
        if kata[0] != kata[-1]:
            kata = kata[1:-1]
        for i in range(len(kata)//2 if len(kata)%2==0 else len(kata)//2+1):
            if kata[i] != kata[0-i-1]:
                kata = kata[i:-i]
except:
    pass

print(len(kata))
