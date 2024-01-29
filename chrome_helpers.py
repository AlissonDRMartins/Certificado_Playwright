import subprocess



def open_chrome():

    chrome_shortcut_path = r"C:\Users\alisson\Desktop\chrome.exe - Atalho.lnk"

    command = f'Start-Process "{chrome_shortcut_path}" -ArgumentList "--incognito"'

    subprocess.run(["powershell", "-Command", command], shell=True)


def close_chrome():

    command = "taskkill /IM chrome.exe /F"
    subprocess.run(command, shell=True)