import random
import string

traffic_lights = ["Red", "Yellow", "Green"]
timing = [30, 2, 15]
# print(random.choices(traffic_lights, timing, k=10))

#==============================================#

random_letters = random.sample(string.ascii_lowercase, 10)
# print(random_letters)

players = ["Joan", "Jane", "Jenny", "Jenifer", "Joceline"]
# random.shuffle(players)
# print(players)

#=======================BINGO=============================#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers = ["1", "2", "3", "4", "5"]
# winning_combination = [3, 2, 4, 5, 7, 8, 6, 1, 10, 9]

Joan = [8, 1, 10, 4, 6, 5, 2, 3, 9, 7]
Jane = [5, 6, 1, 7, 8, 4, 9, 2, 3, 10]
Jenny = [8, 6, 7, 3, 1, 2, 10, 4, 9, 5]
Jenifer = [1, 8, 7, 4, 5, 10, 2, 9, 6, 3]
Joceline = [2, 7, 5, 8, 9, 1, 3, 4, 10, 6]

# TODO: shuffle numbers and if shuffled result is equal to numbers of 
# Joan, Jane, Jenny, Jenifer or Joceline, print BINGO! Otherwise print: "Try Again!"
# 