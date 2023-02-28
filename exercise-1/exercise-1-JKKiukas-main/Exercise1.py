ice_cream_rating = 9
sleeping_rating = 10

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
my_name = first_name + " " + last_name
happiness_rating = (ice_cream_rating + sleeping_rating) / 2

print("\nMy name is", first_name, "and I give eating ice cream a score of", ice_cream_rating, "out of 10!")
print("I am", my_name, "and my sleeping enjoyment rating is", sleeping_rating, "/ 10!")
print("Based on the factors above, my happiness rating is", happiness_rating, "out of 10, or", happiness_rating * 10,
      "%!\n")

# All the data types below makes sense.
print(type(ice_cream_rating))
print(type(first_name))
print(type(happiness_rating))
