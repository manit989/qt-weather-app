import requests
from opencage.geocoder import OpenCageGeocode
from PySide6.QtWidgets import QLineEdit, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        
        # search widgets
        search = QHBoxLayout()
        uinput = QLabel(f"Enter city name")
        self.cname = QLineEdit()
        sbutton = QPushButton("get weather")
        sbutton.clicked.connect(self.get_weather)
        
        # search layout
        search.addWidget(uinput)
        search.addWidget(self.cname)
        search.addWidget(sbutton)
        
        
        # app layout
        self.app = QVBoxLayout()
        self.app.addLayout(search)
        
        self.setLayout(self.app)
        
    def get_weather(self):
        place = self.cname.text()
        
        OCG = OpenCageGeocode('5ca351dd14d74c4486f836fb2ef4a2ad')
        results = OCG.geocode(place)
        if len(results)==0:
            self.inccit = QLabel("Invalid City Name")
            inv = QVBoxLayout()
            inv.addWidget(self.inccit)
            self.app.addLayout(inv)
            self.setLayout(self.app)
            return
        lat=str(results[0]['geometry']['lat'])
        lon=str(results[0]['geometry']['lng'])
        
        url = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid=376e63cbfdb6a1e7d5ce481bd450add8"
        
        response=requests.get(url)
        weather=response.json()
        
        # weather widget
        temp = QLabel(f"temperature: {weather['main']['temp']}")
        tempfeel = QLabel(f"feels like: {weather['main']['feels_like']}")
        tempmin = QLabel(f"minimum temperature: {weather['main']['temp_min']}")
        tempmax = QLabel(f"maximum temperature: {weather['main']['temp_max']}")
        humidity = QLabel(f"Humidity: {weather['main']['humidity']}")
        
        weath = QVBoxLayout()
        
        weath.addWidget(temp)
        weath.addWidget(tempfeel)
        weath.addWidget(tempmin)
        weath.addWidget(tempmax)
        weath.addWidget(humidity)
        
        self.app.addLayout(weath)
        self.setLayout(self.app)
        
        
        
        
        
        

        
        
        