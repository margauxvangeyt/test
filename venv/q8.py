import re
# first we do a function that checks is the URL given is valid or not
def is_valid_url_basic(url):
    """
    :param url: The URL to be validates/checked
    :return:True if the URl is valid, False otherwise
    """
    url_pattern = re.compile(r'https?://\S+')
    return bool(url_pattern.match(url))

# user needs to enter a URL to check
url_to_check = input("Enter a URL to check: ")

# If the entered URL is not valid, print an error message and ask for a valid URL
while not is_valid_url_basic(url_to_check):
    print(f"{url_to_check} is not a valid URL.")
    url_to_check = input("Enter a valid URL: ")

# if its valid then the loop will end and let the person know its valid
print(f"{url_to_check} is a valid URL.")
