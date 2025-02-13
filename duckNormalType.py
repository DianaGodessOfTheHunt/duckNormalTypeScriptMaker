import random

___author___ = "Diana;"
"""
duckNormalType beta v:1.0.0
this makes a rubber duck script for typeing stuff in a way that looks like it is being naturaly typed 
useable on a flipper 0
put what you want in wrighting.txt 
make shure duckScript.txt is empty becuase it will be overwriten

difrences from previous versions: 
alpha: did not work and was glitchy the to get time would cause it to not completely finish sometimes 
especialy with longer wrightings
beta v:1.0.0:present
"""

wrightingToCoppy = open ("/directory/of/wrighting.txt", "r")#make so it will open the correct folder
wrighting = str (wrightingToCoppy.read().splitlines())
#wrighting = wrighting[wrighting.find("'"):wrighting.find("'")-1]

lengthOfWrighting = len(wrighting)
wrighting = wrighting[2:lengthOfWrighting - 2]
lengthOfWrighting = len(wrighting)
charictorOn = 0

"""for testing difrent methods"""
def testing():
    print(getSleepTime(100))

"""
main the main method where everything heppens
"""
def main():
    duckCode = ""
    """unused XXX"""
    curentLetter = 0
    endPoint = 0#where the portion of typeing should end
    """unused end XXX"""
    temp = ""



    for x in range(0,lengthOfWrighting):
        duckCode += spliceWrighting(x)# the line to print

        duckCode += getSleepTime()# natural pause

    duckScript = open("/directory/of/duckScript.txt", "w")#opens txt file for duck script
    duckScript.write(duckCode)

"""
spliceWrighting takes int and gets that charicter
int letter = the curent letter number on
return str outstring the letter combined withstring to combine nicely
"""
def spliceWrighting(letter):

    currentCharictor = wrighting[letter]
    outString = ""
    if (currentCharictor == " "):
        outString = "SPACE"

    else:
        outString = "STRING " + str (currentCharictor)

    outString += "\n"#gets new line
    print(outString)#testing

    return outString

"""
getSleepTime gets a random amount of time to sleep for 
return str sleep_code is the code to make it sleep for a random amount
"""
def getSleepTime():

    randomPause = random.randint(1,40)
    sleep_time = random.randint(100,10000)#change to make difrent amount of time for pauses
    sleep_code = "DELAY "
    if (20>= randomPause):#for long delay eg: thinking
        sleep_time * random.randint(10,50)# change to change the amount of time that it can be 
        # paused for this changes sleep_time by multiplying it by the random int
        print ("testing")
        
    str_sleep_time = (str) (sleep_time)
    sleep_code += str_sleep_time
    sleep_code += "\n"
    return sleep_code

main()
#testing()

