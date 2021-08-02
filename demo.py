#!usr/bin/env python3
import random
icecream = ["flavors", "salty"]
tlgclass= ["Adrian","Bikash","Chas","Chathula","Chris","Hongyi","Jauric","Joe L.","Joe V.","Josh","Justin","Karlo","Kerri-Leigh","Jason","Nicholas","Peng","Philippe","Pierre","Stephen","Yun"]
icecream.append(int(99))
choice =int( input("Pick a number between 0 and 19 or a students name"))

print("{} {}, and {} chooses to be {}".format(icecream[-1],icecream[0],tlgclass[random.randrange(0,19)],icecream[1]))

