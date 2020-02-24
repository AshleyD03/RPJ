from discord.ext.commands import Bot 
import time 
import random

question_list = [
    "Which fictional city is the home of Batman?",
    "Who is the lead singer of Aerosmith",
    "What was the first animated feature length film",
    "Which Roman emperor supposedly fiddled while Rome burned?",
    "Which colour infinity stone controlls reality?",
    "Who played as Captain America in the MCU",
    "What movie does the Awesome Mix Originate from?",
    "Which band originaly wrote Brandy (You're a Fine Girl)",
    "Which pokemon is described as the Prototurtle pokemon?",
    "Who original wrote the song American Pie?"
    ]
answer_list = ["gotham city","steven tyler","snow white","Nero","red","chris evans","guardians of the galaxy","looking glass","tirtouga","don mclean"] 

BOT_PREFIX = ("!", "?")
TOKEN = "NTg2OTI0MTE5NzQ5Mjk2MTQ5.XP6zOw.g50xND2l9hQ2dyaZOT4Klcup9Z4"

client = Bot(command_prefix = BOT_PREFIX)

@client.command()
async def eight_ball():
    possible_responses = [
        "That is a resounds no",
        "It isn't realy that likely",
        "I wouldn't hope so",
        "Fairly Wrong",
        "50/50 Chance",
        "Sure"
    ]
    await client.say(random.choice(possible_responses))

client.run(TOKEN)

