import requests
import bs4

res = requests.get('https://www.wunderground.com/weather/us/va/lynchburg')
res.raise_for_status()

textSoup = bs4.BeautifulSoup(res.text, features="html.parser")
elem = textSoup.select('.wu-value')
print('The temperature is ' + elem[0].getText() + 'F')
elem = textSoup.select('.feels-like > span')
print('It feels like ' + elem[0].getText() + 'F')
elem = textSoup.select('.condition-icon > p')
print('Condition: ' + elem[0].getText() + '!')

