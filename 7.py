class Printer:
    def start(self):
        print("Printer is starting")


class Scanner:
    def start(self):
        print("Scanner is starting")


class Camera:
    def start(self):
        print("Camera is starting")


def start_device(device):
    device.start()


printer = Printer()
scanner = Scanner()
camera = Camera()

start_device(printer)
start_device(scanner)
start_device(camera)
