import socket
import ipaddress

class Scan:
    def __init__(self, ports=[443, 80, 8080, 8000, 3000, 445, 9050, 21, 19, 23, 22, 8081], ip='127.0.0.1', **kwargs):
        self.ports = ports
        self.ip = ip
        self.open_ports = []

    def is_valid(self):
        try:
            ip_address_obj = ipaddress.ip_address(self.ip)
            return True
        except:
            return False

    def is_empty(self):
        return len(self.open_ports) == 0:
        
    def scan(self):
        for port in self.ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    s.connect((self.ip, port))
                    self.open_ports.append(port)
            except:
                pass
        if self.is_empty():
            return self.open_ports
        else:
            return 'all ports are closed :('

    def run(self):
        if self.is_valid():
            return self.scan()
        else:
            return "Invalid IP Address"
