import kivy
# import JSON
from firebase import firebase

url = "https://coronacation.firebaseio.com/"
fb = firebase.FirebaseApplication(url)
# print(fb.get('/',None))

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition,SlideTransition
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.graphics import Color,Rectangle
from kivy.uix.image import Image



Builder.load_file('./styler.kv') 

class OtherScreen(Screen):


	def __init__(self, **kwargs):
		super(OtherScreen, self).__init__(**kwargs)
		


class LoginScreen(Screen):
	def __init__(self, **kwargs):
		super(LoginScreen, self).__init__(**kwargs)
		
	def SignIn(self):
		
		self.username = self.ids.txt1.text
		self.password = self.ids.txt2.text

		self.ids.txt1.text = ""
		self.ids.txt2.text = ""


		if self.name!="" and self.password!="":

			data = fb.get('/users/',None)
			if data ==None or (self.username not in data.keys() or data[self.username]['password'] != self.password):
				message = "INVALID REQUEST!!! Either username or paassword is incorrect."
				print (message)
				PPopup(content = Label(text=message),size_hint=(0.6,0.6),size=(400,400)).open()
				return
			else:
				message = "Correct Credentials!!! Signing in........."
				print (message)
				PPopup(content = Label(text=message),size_hint=(0.6,0.6),size=(400,400)).open()

				self.manager.transition = SlideTransition(direction="left")
				self.manager.current = "screen2"

		return


class PPopup(Popup):
	def __init__(self, **kwargs):
		super(PPopup, self).__init__(**kwargs)
		Clock.schedule_once(self.dismiss_popup,3)
	
	def dismiss_popup(self,dt):
		self.dismiss()


class SignUpScreen(Screen):
	def __init__(self, **kwargs):
		super(SignUpScreen, self).__init__(**kwargs)
		
	def SignUp(self):
		
		self.name = self.ids.txt1.text
		self.email = self.ids.txt2.text
		self.username = self.ids.txt3.text
		self.password = self.ids.txt4.text
		self.roll = self.ids.txt6.text

		if self.ids.txt4.text != self.ids.txt5.text:
			self.ids.txt4.text = ""
			self.ids.txt5.text = ""
			message = "passwords do not match!! Try Again !!"
			print (message)
			PPopup(content = Label(text=message),size_hint=(0.6,0.6),size=(400,400)).open()
			
			return

		self.ids.txt1.text = ""
		self.ids.txt2.text = ""
		self.ids.txt3.text = ""
		self.ids.txt4.text = ""
		self.ids.txt5.text = ""
		self.ids.txt6.text = ""



		if self.name!="" and self.email!="" and self.username!="" and self.password!="" and self.roll!="":

			data = fb.get('/users/',None)
			message = "Signing You Up ............" + str(self.ids.txt1.text)
			print(message)
			PPopup(content = Label(text=message),size_hint=(0.6,0.6),size=(400,400)).open()
			if (data!=None and self.username in data.keys()):

				message = "INVALID REQUEST!!!! User already exits with username :" + self.username
				print (message)
				PPopup(content = Label(text=message),size_hint=(0.6,0.6),size=(400,400)).open()
			
				return
			else:
				fb.patch("/users/",{  str(self.username) :  {"name":str(self.name),"email":self.email,"username":self.username,"password":self.password,"roll":self.roll } })
				message = ":) :) :) Sign In Successfull  :)  :) :) "
				print (message)
				PPopup(content = Label(text=message),size_hint=(0.6,0.6),size=(400,400)).open()
				self.manager.transition = SlideTransition(direction="left")
				self.manager.current = "screen1"

		return


class Manager(ScreenManager):

	screen_one = ObjectProperty(None)
	screen_two = ObjectProperty(None)
	screen_three = ObjectProperty(None)


class MyApp(App):
	def build(self):
		# return Label(text="ABC")
		m = Manager(transition=NoTransition())
		return m

if __name__ == "__main__":
	MyApp().run()
	pass

