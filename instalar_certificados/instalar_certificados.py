import os
import subprocess
from time import sleep

directory = r"C:\Users\alisson\Desktop\Try"
 
pfx_files = [f for f in os.listdir(directory) if f.endswith('.pfx')]
 
def extract_password(filename):
    parts = filename.split("=")
    if len(parts) > 1:
        return parts[1].split('.pfx')[0].strip()
    return None
 
def install_certificate(pfx_file, password):
    ps_command = f'certutil -user -f -p {password} -importpfx "{pfx_file}"'
    print(ps_command)
    try:
        subprocess.run(f"cmd /c {ps_command}", check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing {pfx_file}: {e}")
 
for pfx in pfx_files:
    sleep(1)
    install_certificate(pfx_file=pfx, password=extract_password(pfx))