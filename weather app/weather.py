import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 850

def test_function(entry):
	print("This is the entry of the :", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def format_response(weather):
	try:
		name = weather['name'].upper()
		desc = weather['weather'][0]['description'].upper()
		temp = weather['main']['temp']

		final_str = 'City : %s \nConditions : %s \nTemp(°C) : %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving\n that information'

	return final_str

def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='C:\\Users\\shikh\\Desktop\\Python VScode\\mini projects\\weather app\\newart.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#00BFFF', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=50)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="SEARCH", font=35, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#00BFFF', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font = 'Helvetica 25 bold')
label.place(relwidth=1, relheight=1)

root.mainloop()