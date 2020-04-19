from kivy.uix.popup import Popup
from kivy.uix.label import Label

popup = Popup(title='Test popup',
    content=Label(text='Hello world'),
    size_hint=(None, None), size=(400, 400))

popup.open()