import socket
import platform
import shutil
import psutil
def get_system_info():
     hostname = socket.gethostname()

     operating_system = platform.system()

     kernel = platform.release()

     ip_address = socket.gethostbyname(hostname)
    
     system_info = {"hostname": hostname, 
                    "operating_system": operating_system,
                    "kernel_release": kernel,
                    "ip_address": ip_address
                    }
     
     return system_info
def get_resource_usage():
     total, used, free = shutil.disk_usage("c:\\")
     disk_percentage = (used / total) * 100
     disk_percentage = round(disk_percentage, 1)
     
     memory_percentage = psutil.virtual_memory().percent

     resource_usage = {"disk_usage": disk_percentage,
                     "memory_usage": memory_percentage}
     return resource_usage


system_info = get_system_info()
resource_usage = get_resource_usage()

memory = resource_usage["memory_usage"]
disk = resource_usage["disk_usage"]

def get_status (percentage):
    if percentage >= 90:
        return "Critical"

    elif percentage >= 80:
        return "Warning"

    else: 
        return "Ok"

memory_status = get_status(memory)
disk_status = get_status(disk)

print (f"Host Name: {system_info['hostname']}")
      
print (f"Memory Usage: {memory}% [{memory_status}]")
print (f"Disk Usage: {disk}% [{disk_status}]")