# Secure AWS Infrastrucure

## Overview
This is my cloud infrastucture and security automation. I am building a cloud infrastucure that runs automated systems and security audits. It then compiles the data and displays it in an easy-to-read / digesable dashbaord. I am using Python for the bulk of the automation and scripting, Terraform to provision the cloud infrastructure. Then eventually CI/CD and a web layer to automate deployment and display the dashboard.

## Current Features
 The current Python system audit collects basic information about the host system, including: 
 
 System Information
 - Hostname 
 - Operating System 
 - Kernel version
 - Local IP address

 Resource Monitoring
 - CPU utilization
 - Memory utilization
 - Disk utilization
 - Resources monitored based on OK / Warning / Critical statuses

 Security Auditing
 - Collects standard Windows Firewall configuration 
 - Checks Domain, Private, and Public firewall profiles
 - Determines whether each profile is enabled
 - Outputs digestible security findings
 

## Architecture
This project collects data from the host system to determine the health and functionality of the host and host-based firewall. The data is then passed through seperate functions for collection, evaluation, and presentation. This is to streamline the output while leaving ample opportunity to expand on the code in the near future. The information is then presented in a way that is easy to comprehend and diagnose.


## Technologies
- VS Code 
- JSON
- Python
- PowerShell
- Git
- GitHub 
- psutil



## Project Roadmap: 
### Phase 1 - Local System Auditing
- [x] Collect system information
- [x] Monitor CPU, memory, and disk utilization
- [x] Classify resource usage by status
- [ ] Expand system and security checks
- [ ] Export audit results in a structured format

### Phase 2 - AWS Infrastructure
- [ ] Build AWS infrastructure
- [ ] Configure networking and compute resources
- [ ] Apply cloud security controls

### Phase 3 - Cloud Security Automation 
- [ ] Integrate Python with AWS API's 
- [ ] Audit AWS resources for security misconfiguration 
- [ ] Generate structured security findings 

### Phase 4 - Dashboard
- [ ] Build an API/web layer
- [ ] Display infrastructure and security findings 
- [ ] Add reporting and visualization

### Phase 5 - Automation and CI/CD
- [ ] Add automated testing 
- [ ] Implemented CI/CD with GitHub actions
- [ ] Automate infrastructure and security validation



## What I'm learning
So far I have used and worked on my skills in:
- Python libraries and modules
- Conditional Logic 
- Functions and Parameters
- Dictionaries and return values
- Function arguments
- Dependency management with pip
- System resource monitoring 
- Git version control 
- Lists and loops
- JSON parsing
- subprocess 
- Structured data 
- Separating collection, evaluation, and display logic
- Basic security auditing