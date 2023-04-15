import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = 'https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the fruit and calorie information
table = soup.find('table')

# Extract the rows from the table
rows = table.find_all('tr')

# Extract the headers of the table
headers = [header.text.strip() for header in rows[0].find_all('th')]

# Extract the fruit and calorie data from each row
data = []
names = []
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)
    name_all = row.findAll("th")[0].text.strip().split('\n', 1)
    name1 = name_all[0]
    name1.replace('\xa0', '')
    name2 = name_all[1]
    n3 = name2.split("\t\t\t")
    if n3[1][0].isalpha(): 
        name3 = n3[1].replace('\n', '')
        name3 = name3.replace(',', '')
        # print(name3)
        name = name1 + " " + name3
    else:
        name = name1
    names.append(name.lower())
    # print(name)
    # print(n3)
    # print(row.findAll("th")[0].text.strip().split('\n'))
    # print(row.findAll("th")[0].text.strip().split('\n', 1))
    # name = row.findAll("th")[0].text.strip().split('\n')[0]
    # names.append(name)

# Create a dictionary with the fruits as keys and the calories as values
fruit_calories = {}
for i in range(len(data)):
# for row in data:
    fruit_calories[names[i]] = data[i][0]

# Print the dictionary
# print(fruit_calories)

user_input = input("Item: ").strip().lower()
if 'avocado' in user_input:
    user_input = 'avocado california'
    print("Calories: " + str(fruit_calories['avocado california']))
elif user_input in fruit_calories:
    print("Calories: " + str(fruit_calories[user_input]))
else:
    pass
