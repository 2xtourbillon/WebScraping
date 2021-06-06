
from bs4 import BeautifulSoup

with open('website.html', encoding='UTF-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)
# print(soup.title.string)

# print(soup.prettify()) #print entire html code with indents
# print(soup.li.string) #first li tag

# searching through websites for all of the components

# print(*soup.find_all(name='a'), sep='\n') #all enchor tags
all_anchor_tags = soup.find_all(name='a')

for tag in all_anchor_tags:
    # print(tag.getText()) #just the text
    # print(tag.get('href')) #just the link
    pass

heading = soup.find_all(name='h1', id='name') #find tag and by name
section_heading = soup.find(name='h3', class_='heading') #find by class but use class_ (with underscore to avoid res word)
# print(section_heading.getText())
# print(section_heading.name())
# print(section_heading.get('class')) # get the value of the attribute

# nesting your search by drilling down into an element using CSS selectors
# company_url = soup.select_one(selector='p a') #looking for an 'a' tag sitting inside a 'p' tag
# company_url = soup.select_one(selector='#name') # use the '#' to select an id tag
company_url = soup.select(selector='.heading') # use the class selector for 'heading'
print(company_url)

