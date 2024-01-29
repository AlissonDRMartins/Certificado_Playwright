from regedit import set_winreg
from automation import automacao_vincular_ecnpj


def main():
    # Itera sobre o arquivo txt
    for certificado in open("certificados.txt", "r", encoding="utf-8"):
        certificado = certificado.strip("\n")
        cnpj = certificado.split(':')[1]

            # Alterar regedit
        set_winreg(certificado)
            # Automacao
        automacao_vincular_ecnpj(cnpj)

if __name__ == "__main__":
    main()
