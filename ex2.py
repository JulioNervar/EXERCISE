name = raw_input("Enter your name : ")
print "Good Morning " + name + "! Your name has " + str(len(name)) + " characters and the last characters of your name are " + name[len(name)-3:]

#BIODATA
print "******PLEASE FILL UP YOUR INFORMATION*******\n\n"
print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
name = raw_input("Name     : ") 
name1 = raw_input("Lastname : ") 
address = raw_input("Address  : ")
age= raw_input("Age      : ")
while age.isalpha():
    age= raw_input("Age      : ")
mobile= raw_input("Contact# : ")
while mobile.isalpha():
    mobile= raw_input("Contact# : ")
hobby=  raw_input("Hobbies  : ")
print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
school=raw_input("School Name : ")
year = raw_input("Year        : ")
course= raw_input("Course      : ")
print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
print "             PERSONAL INFORMATION            "
print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
print "     Good day! my name is " + name + " " + name1  + ". " + "I live at " + address + "."
print "     I am " + age + " years old. My contact number is " + mobile + " . " + "My hobby is "+ hobby + "."
print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
print "                    SCHOOL                   "
print "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
print "     Currently a " + year + " student taking up " + course + " in " + school