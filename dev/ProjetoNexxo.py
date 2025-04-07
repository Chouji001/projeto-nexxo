# Projeto Nexxo - Captura de Tela com Selenium
# Este script utiliza Selenium para abrir uma URL em um navegador e tirar um print da tela.
from selenium import webdriver  # Biblioteca para automação do navegador
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time  # Biblioteca para pausas no código

def get_driver(browser="chrome"):
    """
    Função para inicializar o WebDriver para o navegador escolhido.

    Parâmetro:
    - browser (str): O nome do navegador ('chrome', 'firefox').

    Retorna:
    - driver (webdriver): Instância do WebDriver configurada.
    """
    
    if browser.lower() == "chrome":
        # Configurações específicas para o Chrome
        options = ChromeOptions()
        options.add_argument("--headless")  # Modo sem interface gráfica ( faz rodar em segundo plano)
        options.add_argument("--window-size=1280,720")  # Define tamanho da janela
        
        # Configura o serviço do ChromeDriver corretamente
        service = ChromeService(ChromeDriverManager().install())

        # Inicializa o ChromeDriver
        driver = webdriver.Chrome(service=service, options=options)

    elif browser.lower() == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")  # Modo sem interface gráfica ( faz rodar em segundo plano)
        options.add_argument("--width=1280")  # Largura da tela 
        options.add_argument("--height=720")  # Altura da tela
        #Diferente do Chrome, o Firefox não tem a opção de --window-size, mas sim --width e --height 
        # Configura o serviço do GeckoDriver corretamente
        service = FirefoxService(GeckoDriverManager().install())

        # Inicializa o GeckoDriver corretamente
        driver = webdriver.Firefox(service=service, options=options)
    
    else:
        # Se o navegador não for suportado, exibe um erro
        raise ValueError("Navegador não suportado! Escolha: 'chrome' ou 'firefox'.")

    return driver

def capture_screenshot(url, browser="chrome"):
    """
    Função que abre a URL no navegador escolhido e tira um print da tela.

    Parâmetros:
    - url (str): A URL a ser acessada.
    - browser (str): O navegador a ser utilizado ('chrome' ou 'firefox').

    Retorno:
    - Salva a imagem do print no diretório do script.
    """
    
    # Inicializa o WebDriver com base no navegador escolhido
    driver = get_driver(browser)
    
    # Acessa a URL especificada pelo usuário
    driver.get(url)
    
    # Espera 5 segundos para garantir que a página carregue completamente, pode ser ajustado, mas prefiro deixar entre 3 e 5 segundos
    time.sleep(5)

    # Define o nome do arquivo de saída (print)
    screenshot_name = f"screenshot_{browser}.png"

    # Salva a captura de tela no diretório atual, o diretório pode ser alterado
    driver.save_screenshot(screenshot_name)

    # Fecha o navegador
    driver.quit()
    
    print(f"Screenshot salvo como {screenshot_name}")

# Solicita ao usuário que escolha o navegador
browser = input("Escolha o navegador (chrome, firefox): ").strip().lower()

# Solicita ao usuário que digite a URL desejada
url = input("Digite a URL: ").strip()
# Ambom input poderiam ter sido colocados no inicio do script sem afetar o funcionamento do código
# Chama a função para capturar o print da tela
capture_screenshot(url, browser)
