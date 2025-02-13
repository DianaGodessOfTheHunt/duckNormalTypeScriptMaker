
___author___ = "diana;"

"""
the method to determine the range for the delay in duckNormalType
"""

def main():
    typeing_speed = input("plese input your typeing speed WPM: ")# gets the typeing speed (words per min)

    range_min = 0# the min recomended delay for your typeing speed
    range_max = 0# the max recomended delay for your typeing speed
    typeing_delay_median = 0# the median delay for your typeing speed
    letters_per_second = 0#the number of letters typed per second
    letter_range = 50# number of miliseconds from each extream of the range to the median
    letters_per_word = 5 # probable average of how many letters per word on average
    milisec_per_sec = 1000 # the number of milisecs per sec

    # calculate the number of letters per second (letters per second)
    letters_per_second = float(typeing_speed) * letters_per_word # now letters per min the
    letters_per_second = letters_per_second / 60 # now acualy letters per sec


    # calculate the number of milisecs between letters (delay median)
    typeing_delay_median = milisec_per_sec / letters_per_second

    print (typeing_delay_median)

    # set the range min and max 
    range_min = typeing_delay_median - letter_range
    range_max = typeing_delay_median + letter_range

    print ("min = " + str(range_min) + "\nmax = " + str(range_max))


main()
