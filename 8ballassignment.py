import time
import random

name=input ("please Put in your name, Nickname, It don't even matter!")
    

question=input ("whats your question")

values = ["No boi #rejected", "Yes! Congrats! Flex on em!", "yes sir!", "Nope! you thought!", "unforuntatnly, no", "Yea buddy!"]
print("Finna Find yo future! IG: @im.biggrittz")
time.sleep(4)
print(random.choice(values))
      

question=input ("Do you want to keep playing 8 ball game? Type lower case 'yes' to keep playing and don't space it ethier!")

while question == "yes":
    ask=input ("what is your question?")
    values = ["No boi #rejected", "Yes! Congrats! Flex on em!", "You know what ion even know"]
    print("Finna Find yo future! IG: @im.biggrittz")
    time.sleep(4)
    print(random.choice(values))
    question=input ("Do you want to keep playing 8 ball game? Aye remember to put lower case y in yes if you wana keep playing and no spaces!")


