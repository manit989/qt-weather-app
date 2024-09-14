# WEATHER QT APP
#### Video Demo:  https://youtu.be/I2pCLRvKNrs
#### Description:

##### Introduction
- I have created a weather qt GUI app using PySide6 in python.
- It's crosss platform although it need to be compiled using pyinstaller on the - respective machine.

##### Installation
- Download python
- install pip
- using pip install follwing dependencies:-
-   PySide6
-   opengeocode
-   requests
- clone project using git 
- open project folder

##### Running
- while in the project directory open terminal and execute "python3 weather.py"
- it will open a window which will have a search bar.
- enter yout city name in search bar.
- If entered city is invalid user will get a text below search bar that entered city name is invalid.
- If entered city name is valid user will get weather info below search bar.

##### Use of weather.py
- weather.py is just barebones and it just executes application
- and asign weather widget that will be shown.

##### Use of widget.py
- I have created multiple widgets within main widget
- search widget will have search bar and a button through which user can enter it's city name.
- labels bar and button inside the search layout will be in horizontal layout.
- second widget which will have weather will be created only if user entered valid city name.
- I am using opengeocode to get latitude and longitude by using city name which user entered.
- If user entered invalid city name opengeocode will return empty list.
- If block will check if list returned by opengeocode is empty.
- If list is empty a new widget will be created.
- In new widget there will be label containing "Invalid city name"
- Then above new widget will be added in main app layout.
- If city name is valid we will get latitude and longigtude using opengeocode.
- Then i have put latitude and longitude inside url.
- i have used requests library and entered url to get a dictionary containing all weather information.
- Now a new weather widget will be created coontaining all weather info.
- All the info inside weather widget will be in Vertical layout.
- If user entered invalid city name a text will appear below search bar which will show "Invalid City Name"
- currently weather widget will only show temperature, humidity, minimum temperatur, maximum temperature and feels like.
- main app layout which is containing all other children layout is following Vertical Layout.

##### Use of Each python library
###### requests
- I used requests library to get dictionary containing weather info from openweathermap.
###### opengeocode
- I used open Geocode to get latitude and longigtudes from city name.
###### QApplication
- I used QApplication to create the main app.
###### QTextEdit
- I used QTextEdit to create search bar in which user will enter city name
###### QPushButton
- I used QPushButton to create button which will fetch text from search bar and use it as city name
###### QVBoxLayout
- I used QVBoxLayout to set layout oh main master app layout and weather layout.
###### QHBoxLayout
- I use QHBoxLayout to set layout of search widget.
###### widget
- widget library is made manually using culmination of all other above library this contains main app layout and all other logic.

##### IMPORTANT NOTE
- To run this app on windows, mac or linux please install following python libraries:-
-   PySide6
-   requests
-   opengeocode
- I am using my own api and it's free api so it has some limits to use your own api please edit api key in  widget.py def weather_button function accordingly.
