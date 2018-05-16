# Project: QuickReads
# This app takes the input of a textbook and breaks it down to analyze how long
# it takes to read. It will be doin this with each chapter and the book as a whole.
# The app will also feature data mining and provide a bargraph to compare each chapter's
# read time.
# Professor Min Soon Park, Infost 350-001, Spring 2018
# Created by Joshua Lynch and Wa Xiong, April 22 - May 8

import os
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def main():
    #data to plot
    chapter = []
    minutes = []

    totalWord = 0
    count = 1                                                   # count is a counter for the chapters
    time = 0
    again = "yes"                                               # again is the prompt var for the while loop

    while(again == "yes"):
        book = str(input("Enter name of book: "))

        directory =os.path.join("/home/waxiong/FinalProject/" + book)   # the initial directory string must be
                                                                        # set up to the users desired path

        if (os.path.isdir(book)):                               # check for existing book (directory)
            for subdir, dirs, files in os.walk(directory):      # navigate the book
                for file in files:                              # for loop
                    if file.endswith(".txt"):                   # searches for text files
                        f=open(os.path.join(subdir, file),'r')  # open text files

                    try:                                        # try and catch text files
                        with f as fObj:
                            contents = fObj.read()

                        words = contents.split()                # spits content to get the words
                        numWords = len(words)                   # counts the words in int value
                        totalWord += numWords                   # adds the words to a total counter

                        time = int(numWords/175.0)              # equation for the read time, 175 is the average word per minute
                                                                # int cast is to round the time

                        chapter.append(str(count))              # append count and time to the designated list
                        minutes.append(time)                    # used for creating bar graph

                        print("CH", count, "Words: ", numWords, "words \tRead Time: ", time, "minutes")
                        count += 1                              # increment count for the next chapter

                    except ValueError:
                        msg = "The file, " + file + ", is not a txt document.\n"
                        #print(msg)                             # There is no need to print an error message it was just for testing the case


            time = int(totalWord/175.0)                         # Reuse var time for the equation with totalWord
            time1 = time / 60 - int(time / 60)
            print("\nTotal Words: " , totalWord, "\tTotal Time: ", int(time / 60), "hours and ", int(time1 * 60), "minutes")

            #chapter.append('All')                              # this line of code is to
            #minutes.append(time)                               # view the total time in the graph


            #plot
            y_pos= np.arange(len(chapter))

            plt.bar (y_pos, minutes, label = 'Time', align='center', alpha=0.5)
            plt.xticks (y_pos, chapter)
            plt.ylabel ('Minutes')
            plt.xlabel ('Chapters')
            plt.title (book)

            plt.legend()
            plt.savefig('BookBarGraph')

        else:                                                   # counterpart to the if statement above
            print("Sorry, the book you enter may be misspelled or does not exist.")

        again = str(input("\nWould user like to get the data of another book? ('yes' or 'no'): "))
        print("\n")

main()
