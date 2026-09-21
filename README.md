# Secure AWS Infrastrucure

## Overview
This is my cloud infrastucture and security automation. I am building a cloud infrastucure that runs automated systems and security audits. It then compiles the data and displays it in an easy-to-read / digesable dashbaord. I am using Python for the bulk of the automation and scripting, Terraform to provision the cloud infrastructure. Then eventually CI/CD and a web layer to automate deployment and display the dashboard.

## Current Features
 The current Python system audit collects basic information about the host system, including: 
 
 Hostname 
 Operating System 
 Kernel version
 Local IP address
 Memory usage
 Disk usage

The audit also elavuates memory and disk utilization against thresholds and assigns an OK, Warning, or Critical status.

## Architecture



## Technologies
- VS Code 
- Python
- PowerShell
- Git
- Github 
- psutil



## Project Roadmap: 
### Phase 1 - Local System Auditing
- Collect system information
- Monitor memory and disk utilization
- Classify resource usage by status
- Expand system and security checks
- Export audit results in a structured format

### Phase 2 - AWS Infrastructure
- Build AWS infrastructure
- Configure networking and compute resources
- Apply cloud security controls

### Phase 3 - Cloud Security Automation 
- Intergrate Python with AWS API's 
- Audit AWS resources for security misconfiguration 
- Generate strcutured security findings 

### Phase 4 - Dashboard
- Build an API/web layer
- Display infrastructure and security findings 
- Add reporting and visulization

### Phase 5 - Automation and CI/CD
- Add automated testing 
- Implemented CI/CD with GitHub actions
- Automate infrstructure and security validation



## What I'm learning
So far I have used and worked on my skills in:
- Python libraries and modules
- Conditional Logic 
- Functions and Parameters
- Dictionaries and return values
- Function arguments
- Dependancy management with pip
- System resource monitoring 
- Git version control 