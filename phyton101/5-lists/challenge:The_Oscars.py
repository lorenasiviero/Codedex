best_pictures = [
    '2019 - Parasite',
    '2018 - Green Book',
    '2017 - The Shape of Water',
    '2016 - Moonlight',
    '2015 - Spotlight',
    '2014 - Birdman',
    '2013 - 12 Years a Slave',
    '2012 - Argo',
    '2011 - The Artist'
]

recent_winners = [
    '2024 - Anora',
    '2023 - Oppenheimer',
    '2022 - Everything Everywhere All at Once',
    '2021 - CODA',
    '2020 - Nomadland'
]

# Insert each recent winner at the front (index 0)
for winner in reversed(recent_winners):   # reverse so 2020 is inserted first
    best_pictures.insert(0, winner)       # .insert() is the list method

print(best_pictures)

# The code above is a Python script that demonstrates how to manipulate lists.
# It starts with a list of best picture winners from the Oscars, and then it adds recent winners to the front of the list.
# The script uses a for loop to iterate through the recent winners in reverse order, inserting each one at the front of the best_pictures list.
# Finally, it prints the updated list of best picture winners.