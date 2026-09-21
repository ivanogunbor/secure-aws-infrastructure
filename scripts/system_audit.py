import socket
import platform
import shutil
import psutil
def get_system_info():
     hostname = socket.gethostname()
     print("Host Name:",hostname)

     operating_system = platform.system()
     print ("Operating System:", operating_system)

     kernel = platform.release()
     print("Kernel Release:", kernel)

     ip_address = socket.gethostbyname(hostname)
     print(f"Ip Address: {ip_address}")
def get_resource_usage():
     total, used, free = shutil.disk_usage("c:\\")
     disk_percentage = (used / total) * 100
     disk_percentage = round(disk_percentage, 1)
     print(f"Disk Usage {disk_percentage}%")

     memory_percentage = psutil.virtual_memory().percent
     print(f"Memory Usage: {memory_percentage}%")

get_system_info()
get_resource_usage()


