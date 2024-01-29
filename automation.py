from playwright.sync_api import sync_playwright
from time import sleep
from chrome_helpers import open_chrome, close_chrome

def write_error(cnpj: str, fail: str, error_type: str) -> None:
        file = open("output.txt", "a")
        file.write(f"{cnpj};{fail};{error_type}\n")
        file.close()


def automacao_vincular_ecnpj(cnpj):

    open_chrome()

    sleep(10)

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        default_context = browser.contexts[0]
        page = default_context.pages[0]
        try:
            page.goto("https://sso.acesso.gov.br/login?client_id=portal-logado.estaleiro.serpro.gov.br&authorization_id=18bfdd40ef7")
            page.click("#cert-digital")
            try:
                button = page.wait_for_selector('#enter-2fa-code', timeout=2500)
                error_type = '2FA'
                fail = 'T'
            except Exception as e:
                try:
                    button = page.wait_for_selector("text=Concordo", timeout=2500)  # Timeout in milliseconds
                    button.click()
                except Exception as e:
                    pass
                #Autoriza as infos
                try:
                    button = page.wait_for_selector('//*[@id="authorize-info"]/div[2]/button[2]', timeout=2500)
                    button.click()
                except Exception as e:
                    pass
                try:
                    page.click(".sc-iGgWBj.iSfBDE:text('Vincular empresas via e-CNPJ')", timeout=2500)
                    try:
                        button = page.wait_for_selector("text=Autorizar", timeout=2500)  # Timeout in milliseconds
                        button.click()
                    except Exception as e:
                        pass
                    page.click("text=Vincular empresa do e-CNPJ")
                    page.click("xpath=//button[contains(text(), 'Vincular')]")
                    error_type = 'no_error'
                    fail = 'F'
                    sleep(2)
                except Exception as e:
                    error_type = 'already_registered'
                    fail = 'T'
        except Exception as e:
            error_type = 'unknown'
            fail = 'T'
        write_error(cnpj=cnpj, fail=fail, error_type=error_type) 

    close_chrome()