import socket
import platform
import shutil
import psutil
import subprocess
import json


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
     cpu_percentage = psutil.cpu_percent(interval=1)
     memory_percentage = psutil.virtual_memory().percent


     resource_usage = {"disk_usage": disk_percentage,
                        "memory_usage": memory_percentage,
                        "cpu_usage": cpu_percentage
                        }

     return resource_usage



system_info = get_system_info()
resource_usage = get_resource_usage()

memory = resource_usage["memory_usage"]
disk = resource_usage["disk_usage"]
cpu = resource_usage["cpu_usage"]

def get_status (percentage):
    if percentage >= 90:
        return "Critical"

    elif percentage >= 80:
        return "Warning"

    else: 
        return "Ok"



def get_firewall_status():
    command ="get-netfirewallprofile | select-object name, Enabled | convertto-json"
    program = "powershell"
    result = subprocess.run([program,
                         "-Command",
                         command],
                         capture_output = True,
                         text = True,)
    firewall_data = json.loads(result.stdout)
    return firewall_data


def evaluate_firewall(firewall_data):
    findings = []
    for profile in firewall_data:
        if profile["Enabled"] == 1:
            firewall_status = "OK"
        else:
            firewall_status = "Warning!"

        finding = { 
                    "name": profile['name'],
                    "enabled": profile['Enabled'],
                    "status": firewall_status,
                    }
        
        findings.append(finding)
    return findings


def display_firewall_findings(findings):
    for finding in findings:
        print (f"{finding['name']} Firewall: Enabled = {finding['enabled']} {finding['status']}")


    

    








memory_status = get_status(memory)
disk_status = get_status(disk)
cpu_status = get_status(cpu)
firewall_data = get_firewall_status()
firewall_findings = evaluate_firewall(firewall_data)











print (f"Host Name: {system_info['hostname']}")
      
print (f"Memory Usage: {memory}% [{memory_status}]")
print (f"Disk Usage: {disk}% [{disk_status}]")
print (f"CPU Usage: {cpu}% [{cpu_status}] ")
display_firewall_findings(firewall_findings)