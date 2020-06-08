# from pip._vendor.distlib.compat import raw_input
# import os
#
# userInput = raw_input("Enter Option: \n(1) Convert URL to TinyUrl\n(2) Convert TinyUrl to URL \n(3) Quit\n\n: ")
# clear = lambda: os.system('clear')
#
# while(userInput != '3'):
#     clear()
#     userInput = raw_input("Enter Option: \n(1) Convert URL to TinyUrl\n(2) Convert TinyUrl to URL \n(3) Quit\n\n: ")
#

import random

from pip._vendor.distlib.compat import raw_input


class TinyUrlConverter:
    store = {}
    reverseStore = {}
    storeTrack = {}
    selectChar = "qwertyuiopasdfghjklzxcvbnm1234567890"
    domain = "http://localhost/"

    #Genrates a length long randomized key based on the characters in selectChar.
    def randomKey(self, length):
        result = ""
        for i in range(length):
            result = result + self.selectChar[random.randint(0, len(self.selectChar) - 1)]
        # print("Random: ", result)
        return result

    #Converts a long URL to tinyurl
    def generateUrl (self, longUrl):
        if(self.reverseStore.get(longUrl) == None):
            key = self.randomKey(5)
            self.store[key] = [longUrl, 0]
            self.reverseStore[longUrl] = key
        else:
            return self.domain + self.reverseStore[longUrl]
        return self.domain + key

    #Converts a short URL into a Long URL
    def getLongUrl (self, key):
        if(self.store.get(key) != None):
            self.store.get(key)[1] = self.store.get(key)[1] + 1
            return self.store.get(key)[0]
        return -1

    def getTracking(self, key):
        if (self.store.get(key) != None):
            return self.store.get(key)[1]
        else:
            -1

