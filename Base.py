# Display screen with :
# display, array with 8 id's),
# bottext, array with 2 id's)
# base, object with lives and lvl property
def screen(display, botText, base): 
    line = "!-"+"=-"*24 + "=!" 
    topText = "!  LVL: " + str(base["lvl"]) + " "*29 + "LIVES: " + str(base["lives"]) + " " * 5 + "!"
    print(line + "\n" + topText + "\n" + line)
    for i in range (8):
        print(display[i])
    print(line)
    for i in range (2):
        print("!  " + botText[i] + " " * (48 - len(botText[i])) + "!")
    print(line)

