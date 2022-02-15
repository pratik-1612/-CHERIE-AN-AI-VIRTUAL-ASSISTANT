import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser
import random
import requests
import randfacts
from datetime import date, datetime




def hello():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        print("Good Morning sir")
        machine_speak(f"Good Morning sir")
    elif (hour >= 12) and (hour < 16):
        print("Good afternoon sir")
        machine_speak(f"Good afternoon sir")
    elif (hour >= 16) and (hour < 19):
        print("Good Evening sir")
        machine_speak(f"Good Evening sir")
    print("I am CHERIE. How may I assist you?")
    machine_speak(f"I am CHERIE. How may I assist you?")
machine=pyttsx3.init()
machine.setProperty("rate", 160)
voices = machine.getProperty("voices")
machine.setProperty('voice', voices [1].id)
recognizer=sr.Recognizer()

def machine_speak(text):
    machine.say(text)
    machine.runAndWait()
def quote():
	try:
		response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
		if response.status_code == 200:
			## extracting the core data
			json_data = response.json()
			data = json_data['data']
			print(data[0]['quoteText'])
			machine_speak(data[0]['quoteText'])
		else:
			print("Error while getting quote")
	except:
		print("Something went wrong! Try Again!")
def find_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def get_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
def cherie():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source,duration=1)
        print('\n')
        print("Start Speaking!!")
        machine_speak('listening.. ')
        recordedaudio=recognizer.listen(source, 10, 3)
    try:
        query=recognizer.recognize_google(recordedaudio,language='en-in')
        query = query.lower()
        if 'cherie' in query :
            query = query.replace('cherie', '')
            print('you said'+query)
        else :
            print('you said : '+query)
        if 'hello' in query :
            l1={"hello from the other side!!","Oh, it’s you again, Hi there!","It’s nice to see you again. You are such a beauty!!","Hi, it is really good to hear from you. I hope you and your loved ones are safe and healthy",
                "Hello,it's CHERIE. i was wondering if after all these years you will not come to me. Ha Ha Ha just kidding. How can I help you?? "}
            item1=random.choice(tuple(l1))
            print(item1)
            machine_speak(item1)
        elif 'who are you' in query :
            l2={"My name's CHERIE. I just wish that everyone had a name as cool as mine.","I'm CHERIE a k a your virtual assistant but you can call me your sweetheart too.. "}
            item2=random.choice(tuple(l2))
            print(item2)
            machine_speak(item2)
        elif 'how are you' in query:
            print("Same old, same old.\nYeah,alright. I’m alive!")
            machine_speak("Same old, same old....Yeah,all right... I’m alive!")
        elif 'can you do' in query :
            print("I can play songs for you,tell you some jokes and I'm able to tell you date and time....I also can tell you news, quotes, facts, some free advices. current weather in your city. i can find your ip address. I can also make searches on google and I'm able to find your location or i can locate an area on map.I can open diffent websites like github, gmail, youtube, instagram, stackflow and data science bootcamps and much more. what you will like me to do??")
            machine_speak("I can play songs for you... and I can tell you some jokes, I'm able to tell you date and time........I also can tell you news, quotes, facts, some free advices....current weather in your city. i can find your ip address...I can also make searches on google and... I'm able to find your location or.... i can locate an area on map.....I can open diffent websites like github, gmail, youtube, instagram, Whats App, wikipedia, stackflow and data science boot    camps and much more. what you will like me to do??")
        elif 'who created you' in query:
            print("I was born when Mr Pratik's bright mind created an Assistant, just for you \N{grinning face} ")
            machine_speak("I was born when Mr Prateek's bright mind created an Assistant, just for you")
        elif 'how old are you' in query:
            print("If the secret of my age comes out, it might be used against me.I've had more enemines who have known my age than those who haven't.")
            machine_speak("If the secret of my age comes out, it might be used against me. I've had more enemines who have known my age than those who haven't.")
        elif 'your date of birth' in query:
            print("If the secret of my age comes out, it might be used against me. I've had more enemines who have known my age than those who haven't.")
            machine_speak("If the secret of my age comes out, it might be used against me. I've had more enemines who have known my age than those who haven't.")
        elif 'ip address' in query:
            ip_address = find_ip()
            machine_speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')
        elif 'play' in query:
            song = query.replace('play', '')
            print('Playing' +song)
            machine_speak('Playing' +song)
            pywhatkit.playonyt(song)
            sys.exit()
        elif 'date and time' in query :
            today = date.today()
            time = datetime.now().strftime('%I:%M %p')
            d2 = today.strftime("%B %d, %Y")
            print("Today's Date is ", d2, 'Current time is', time)
            machine_speak('Today is : '+ d2)
            machine_speak('and current time is '+ time)
        elif 'time and date' in query :
            today = date.today()
            time = datetime.now().strftime('%I:%M %p')
            # Textual month, day and year
            d2 = today.strftime("%B %d, %Y")
            print("Today's Date is ", d2, 'Current time is', time)
            machine_speak( 'Current time is '+ time)
            machine_speak('and Today is : '+ d2)

        elif 'time' in query:
            time = datetime.now().strftime('%I:%M %p')
            print('The current time is' +  time)
            machine_speak('The current time is')
            machine_speak(time)
        elif 'date' in query:
            today = date.today()
            print("Today's date:", today)
            # Textual month, day and year
            d2 = today.strftime("%B %d, %Y")
            print("Today's Date is ", d2)
            machine_speak('The todays date is')
            machine_speak(d2)
        elif 'tell me about' in query:
            name = query.replace('tell me about' , '')
            info = wikipedia.summary(name, 1)
            print(info)
            machine_speak(info)
        elif 'wikipedia' in query:
            name = query.replace('wikipedia' , '')
            info = wikipedia.summary(name, 1)
            print(info)
            machine_speak(info)
        elif 'what is' in query:
            name = query.replace('what is ' , '')
            info = wikipedia.summary(name, 1)
            print(info)
            machine_speak(info)
        elif 'who is ' in query:
            name = query.replace('who is' , '')
            info = wikipedia.summary(name, 1)
            print(info)
            machine_speak(info)
        elif 'what is ' in query :
            search = 'https://www.google.com/search?q='+query
            print(' Here is what i found on the internet..')
            machine_speak('searching... Here is what i found on the internet..')
            webbrowser.open(search)
        elif 'joke' in query:
            _joke = pyjokes.get_joke()
            print(_joke)
            machine_speak(_joke)
        elif 'quote' in query:
            quote()
        elif 'fact' in query:
            x = randfacts.get_fact()
            print(x)
            machine_speak(x)
        elif "advice" in query:
            machine_speak(f"Here's an advice for you, sir")
            advice = get_advice()
            machine_speak(advice)
            machine_speak("For your convenience, I am printing it on the screen sir.")
            print(advice)
        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            machine_speak('Here are some headlines from the Times of India,Happy reading')

        elif "weather" in query:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            ip_address = find_ip()
            cityn = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            complete_url = base_url + "appid=" + api_key + "&q=" + cityn
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                machine_speak("weather in"+ cityn)
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                machine_speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                machine_speak(" City Not Found ")
        elif 'search' in query :
            search = 'https://www.google.com/search?q='+query
            machine_speak('searching... ')
            webbrowser.open(search)
        elif "my location" in query:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            machine_speak("You must be somewhere near here, as per Google maps")
        elif 'locate ' in query :
            machine_speak('locating ...')
            loc = query.replace('locate', '')
            if 'on map' in loc :
                loc= loc.replace('on map',' ')
            url = 'https://google.nl/maps/place/'+loc+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc)
            machine_speak('Here is the location of '+loc)
        elif 'on map' in query :
            machine_speak('locating ...')
            loc = query.split(" ")
            print(loc[1])
            url = 'https://google.nl/maps/place/'+loc[1] +'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc[1])
            machine_speak('Here is the location of '+loc[1])

        elif 'location of' in query :
            machine_speak('locating ...')
            loc = query.replace('find location of', '')
            url = 'https://google.nl/maps/place/'+loc+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc)
            machine_speak('Here is the location of '+loc)
        elif 'where is ' in query :
            machine_speak('locating ...')
            loc = query.replace('where is', '')
            url = 'https://google.nl/maps/place/'+loc+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc)
            machine_speak('Here is the location of '+loc)
        elif 'bootcamps' in query :
            search = 'http://tathastu.twowaits.in/index.html#courses'
            machine_speak('opening boot camps')
            webbrowser.open(search)
        elif 'boot camps' in query :
            search = 'http://tathastu.twowaits.in/index.html#courses'
            machine_speak('opening boot camps')
            webbrowser.open(search)
        elif 'python bootcamp' in query :
            search = 'http://tathastu.twowaits.in/kickstart_python.html'
            machine_speak('showing pythonboot camp')
            webbrowser.open(search)
        elif 'data science bootcamp' in query:
            search = 'http://tathastu.twowaits.in/kickstart_data_science.html'
            machine_speak('showing data science and ml bootcamp')
            webbrowser.open(search)
        elif 'open google' in query :
            print('opening google ...')
            machine_speak('opening google..')
            webbrowser.open_new('https://www.google.co.in/')
        elif 'gmail' in query :
            print('opening gmail ...')
            machine_speak('opening gmail..')
            webbrowser.open_new('https://mail.google.com/')
        elif 'open youtube' in query :
            print('opening you tube ...')
            machine_speak('opening you tube..')
            webbrowser.open_new('https://www.youtube.com/')
        elif 'open instagram' in query :
            print('opening instagram ...')
            machine_speak('opening insta gram...')
            webbrowser.open_new('https://www.instagram.com/')
        elif 'open whatsapp' in query :
            print("opening What'sApp ...")
            machine_speak("opening What's  App...")
            webbrowser.open_new('https://web.whatsapp.com/')
        elif 'open stack overflow' in query :
            print('opening stackoverflow ...')
            machine_speak('opening stack overflow...')
            webbrowser.open_new('https://stackoverflow.com/')
        elif 'open github' in query :
            print('opening git hub ...')
            machine_speak('opening git hub...')
            webbrowser.open_new('https://github.com/')
        elif 'bye' in query:
            print('it is really good to hear from you. I hope you and your loved ones are safe and healthy. Byeee Take Care')
            machine_speak('it is really good to hear from you. I hope you and your loved ones are safe and healthy. Bye Take Care')
            sys.exit()
        elif 'thank you' in query :
            print("your welcome")
            machine_speak('your welcome')
        elif 'stop' in query:
            print('I look forward to our next meeting')
            machine_speak("I look forward to our next meeting")
            sys.exit()
        elif 'tata' in query:
            print('good bye!! see you soon')
            machine_speak('good bye!! see you soon')
            sys.exit()
        else:
            print(' Here is what i found on the internet..')
            machine_speak('Here is what i found on the internet..')
            search = 'https://www.google.com/search?q='+query
            webbrowser.open(search)
    except Exception as ex:
        print(ex)
print('Your virtual assistant is Loading ...Please wait!!!')
machine_speak('Your Virtual Assistant is Loading...Please wait!!!')
print('\n')
hello()
while True:
    cherie()
