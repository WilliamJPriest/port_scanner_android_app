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
import ipaddress


ports = [443,80, 8080, 8000, 3000, 445, 9050, 123, 21, 19, 23]
open_ports = []

def port_scanner(ip, **kwargs):
        open_ports.clear()
        for port in ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    s.connect((ip, port))
                    open_ports.append(port)
            except:
                pass


class get_ip(Widget):
    ip = ObjectProperty(None)

    def btn(self):
        ip = self.ip.text
        try:
            ip_address_obj = ipaddress.ip_address(ip)
        except:
            popup = Popup(title='Error', content=Label(text='You entered an invalid ip address'), auto_dismiss=False)
            popup.open()
            
        scan = port_scanner(ip=ip)
        if len(open_ports) == 0:
            popup = Popup(title='Error', content=Label(text='did not detect any open ports :('), auto_dismiss=False)
            popup.open()

        else:
            popup = Popup(title='', content=Label(text=str(open_ports)), auto_dismiss=False)
            popup.open()    
        


class MyApp(App):
    def build(self):
        self.title = "Port Scanner"
        return get_ip()

if __name__ == '__main__':
    MyApp().run()
