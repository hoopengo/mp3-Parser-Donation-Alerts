import random
import requests
import os
print('Выберите в какую папку будут сохранятся .wav фалы (Авто-Создание):')
path = input()
try:
	os.mkdir(path)
except OSError:
	pass
def parse():
	while True:
		url = "http://static.donationalerts.ru/audiodonations/"
		a = random.randint(11111, 99999)
		b = random.randint(111,999)
		url = url + str(a) + '/'
		url = url + str(a) + str(b) + ".wav"
		r = requests.get(url, stream=True)
		if r.status_code == 200:
			with open(path + '/' + str(random.randint(1,1000000)) + '.wav', 'wb') as f:
				f.write(r.content)
			print(url)
print('Подождите... Это займёт около минуты!')
parse()
