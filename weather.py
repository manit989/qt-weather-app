import requests
from widget import Widget
from PySide6.QtWidgets import QApplication 
from opencage.geocoder import OpenCageGeocode

app = QApplication()
widget = Widget()

widget.show()
app.exec()





