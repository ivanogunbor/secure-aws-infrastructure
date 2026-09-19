import socket
import platform
hostname = socket.gethostname()
print("Host Name:",hostname)
operating_system = platform.system()
print ("Operating System:", operating_system)
kernel = platform.release()
print("Kernel Release:", kernel)
