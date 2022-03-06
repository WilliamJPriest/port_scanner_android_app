from re import MULTILINE
import kivy
kivy.require("1.0.6")
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import socket
import core


class get_ip(Widget):
    ip = ObjectProperty(None)

    def btn(self):
        ip = self.ip.text
        if len(ip) == 0:
            scan = core.Scan()
        else:
            scan = core.Scan(ip=ip)
        run = scan.run()
        popup = Popup(title='', content=Label(text=str(run)), auto_dismiss=False)
        popup.open()


class MyApp(App):
    def build(self):
        self.title = "Port Scanner"
        return get_ip()

if __name__ == '__main__':
    MyApp().run()
