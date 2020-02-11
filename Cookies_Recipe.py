# Making cookies. A recipe says that it takes 1.5 cups of sugar, 1 cup of butter
#and 2.75 cups of flour to make 48 cookies.
# If you divide these out, that means to make one cookie, you need (1/32) cups
#of sugar, (1/48) cups of butter, and (11/192) cups of flour to make 1 cookie.

# Let's first set up these values as such:

sugar = (1/32)
butter = (1/48)
flour = (11/192)

# Now we need to get user input to determine how many cookies they want to get!

cookies = int(input('Enter number of cookies:'))

# So now we have the number of cookies we want, let's do multiplication

amtSugar = cookies * sugar
amtButter = cookies * butter
amtFlour = cookies * flour

# With this we now know how many cups of everything we need, and we just need
#a print function to sum it all up for the user!

print('You need', amtSugar, 'cups of sugar,', amtButter, 'cups of butter and', amtFlour, 'cups of flour.')
