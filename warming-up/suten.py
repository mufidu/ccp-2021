# The rule of suten is quite simple, the elephant beats the human (“elephant crushes human”), the human beats the ant (“human crushes ant”), and the ant beats the elephant (“the small ant defeats the elephant by means of attacking elephant's sensitive trunk and ears”). This simple rule makes suten popular among Indonesian children and it is often used as a fair choosing method between two people. See Figure 1 for illustration.

# Input Format

# The input consists of two lines where each line contains N characters and every two consecutive characters are separated by a space. A character is either e, h, or a, where e represents elephant, h represents human, and a represents ant. There is no information about N, you have to read it from the input. The first line represents the hand gestures of Eko, while the second line signify the hand signs of Ganesh.

# The output of the program is:

# The string "Eko wins" if Eko wins the game.
# The string "Ganesh wins" if Ganesh wins the game.
# The string "Draw" if neither Eko nor Ganesh wins the game.

eko = input().split()
ganesh = input().split()
eko_wins = 0
ganesh_wins = 0

for i in range(len(ganesh)):
    if ganesh[i] == eko[i]:
        continue
    if eko[i] == 'e' and ganesh[i] == 'h':
        eko_wins += 1
    elif eko[i] == 'h' and ganesh[i] == 'a':
        eko_wins += 1
    elif eko[i] == 'a' and ganesh[i] == 'e':
        eko_wins += 1
    elif ganesh[i] == 'e' and eko[i] == 'h':
        ganesh_wins += 1
    elif ganesh[i] == 'h' and eko[i] == 'a':
        ganesh_wins += 1
    elif ganesh[i] == 'a' and eko[i] == 'e':
        ganesh_wins += 1    

if eko_wins > ganesh_wins:
    print("Eko wins")
elif ganesh_wins > eko_wins:
    print("Ganesh wins")
else:
    print("Draw")

