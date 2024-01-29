import winreg
caminho_regedit = r"SOFTWARE\Policies\Google\Chrome\AutoSelectCertificateForUrls"
def set_winreg(certificado):

    try:
        # Abre o regedit no caminho certo.
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, caminho_regedit, 0, winreg.KEY_WRITE) as key:
            # Set o valor.
            winreg.SetValueEx(key, "1", 1, winreg.REG_SZ, f'{{"pattern":"https://*","filter":{{"SUBJECT":{{"CN":"{certificado}"}}}}}}')
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
