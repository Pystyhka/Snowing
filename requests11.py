import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q=Великий Новгород&appid=7b8e6cb3fc74f4b6482c0b886178404f'
response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Великий Новгород&appid=7b8e6cb3fc74f4b6482c0b886178404f')
data = response.json()
aried_snow = ['light snow','snow','heavy snow','sleet','light shower sleet','shower sleet','light rain and snow','rain and snow','light shower snow','shower snow','heavy shower snow']
def checking_for_snow():
    check_for_snow = data['weather'][0]['description']
    if check_for_snow in aried_snow:
        return 'yes'
    else:
        return 'no'
abc = checking_for_snow()
print(abc)


