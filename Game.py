from Base import screen

#Global Values
player = {"lvl": 1,
          "lives": 1}

side_mod = " "*6 + "][" + " " *36 + "][" # Space is equal to 52 - 2 * ( x + 2 )
display = [side_mod] * 8
text = ["line 1", "line 2"]

print("\n" * 5)
screen(display, text, player)
input()
