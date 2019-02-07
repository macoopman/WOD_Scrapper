"""
Read crossfit.com main page and get the WOD
"""

from bs4 import BeautifulSoup
import requests
import ssl


url = "https://www.crossfit.com/"

html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(html.text, 'html.parser')


workout = []
count = 0
for art in soup.find_all('article', {'class': "_2IQsj5-LQZkOE2YtIR0usu"}):
    for p in art.find_all('p'):
        workout.append(p.text.strip())


workout_type = workout[0]
workout_body = workout[1]
print(workout_type)
print(workout_body)
