"""
Read crossfit.com main page and get the WOD
"""

from bs4 import BeautifulSoup
import requests
import ssl


def getWOD():
    """
    Make url request to crossfit.com and get the workout of the day
    """
    url = "https://www.crossfit.com/"
    html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(html.text, 'html.parser')


    workout = []
    # locate the proper html location of daily wod
    for art in soup.find_all('article', {'class': "_2IQsj5-LQZkOE2YtIR0usu"}):
        for p in art.find_all('p'):
            workout.append(p.text.strip())
    # return (workout_type, workout_contents)
    return (workout[0], workout[1])




if __name__ == "__main__":
    wod = getWOD()
    for line in wod:
        print(line)
