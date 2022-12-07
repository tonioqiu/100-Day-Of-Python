#Already used functions wth outputs
#DocStrings are used to describe what a function does
#DocStrings are placed inside the function, right after the first line

def format_name(f_name, l_name):
    """Take a first and last name and format it 
    to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    else:
        formated_f_name = f_name.title()
        formated_l_name = l_name.title()
        return f"{formated_f_name} {formated_l_name}"


format_name("jim", "smith")

#comment with # is not a docstring
"""avoid commenting with docstrings, use # instead """
#You can use ctrl + / to comment out a line of code, 
#or highlight multiple lines and use ctrl + / to comment out all of them