# let the user know what's going on
print ("Welcome to the assignment world!")
print ("Answer the questions below to weave a story.")
print ("-----------------------------------")

# variables containing all of your story info
yourGender = raw_input("Are you a Boy or a Girl? : ")
yourName = raw_input("What is your name?: ")
yourAge = raw_input("Your age?: ")
ageGap = raw_input("Age gap in years between u and ur closest sibling?: ")
activity1 = raw_input("Enter your favourite activity as a kid: ")
idol = raw_input("Enter the name of your childhood idol ")
profession = raw_input("Your current profession: ")
salutation = raw_input("What's your good bye line ?: ")

# this is the story. it is made up of strings and variables.
story = "Once upon a time there was a " + yourGender + " named " + yourName + " aged " + yourAge + " years old and his/her " \
" sister was " + ageGap + " years elder. They loved to " + activity1 + ". " + yourName + "s ambition was to become a " + idol + ", " \
" But destiny had other plans." + yourName + " ended up becoming a " + profession + ". Now " + yourName + " is happily married " \
"  with 3 kids. " + salutation +"!!!"

# finally we print the story
print (story)