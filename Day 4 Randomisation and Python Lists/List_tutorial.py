
#the order in the list is important
#List start counting from 0

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", 
"Connecticut", "Massachusetts", "Maryland", "South Carolina","New Hampshire", 
"Virginia", "New York", "North Carolina","Rhode Island", "Vermont", "Kentucky",
"Tennessee", "Ohio","Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama",
"Maine", "Missouri", "Arkansas", "Michigan", "Florida","Texas", "Iowa", "Wisconsin",
"California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska",
"Colorado", "North Dakota", "South Dakota", "Montana","Washington", "Idaho", "Wyoming",
"Utah", "Oklahoma","New Mexico", "Arizona", "Alaska", "Hawaii"]

#change a specific item in a list
states_of_america[1] = "Pencilvania"

#add 1 item
states_of_america.append("Angeland")
#add list to a list
states_of_america.extend(["Antonioland","Jerland"])

#print result
print(states_of_america)