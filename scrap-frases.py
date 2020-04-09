import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys
import pandas as pd
"""
    cria um dataset com frases e autores
"""


def main(argv):
    # criando diretorio para salvar o dataset
    if not os.path.exists("dataset"):
        os.mkdir("dataset")
     

    
    # ocultando navegador
    op = webdriver.FirefoxOptions()
    op.add_argument('-headless')
    
    driver = webdriver.Firefox(options=op)
    
    data = []
    for pagina in range(30):
        if pagina > 0:
            driver.get("https://www.pensador.com/curtas_frases_de_amor/" + str(pagina+1)+"/")
        else:
            driver.get("https://www.pensador.com/curtas_frases_de_amor/")
        
        
        elem = driver.find_elements_by_class_name("thought-card")
        print("pagina {}".format(pagina+1) )
        c = 0
        for item in elem:
            frase = item.find_element_by_xpath(".//p[@class='frase fr']").text
            autor = item.find_element_by_xpath(".//span[@class='autor']").text
            data_aux = [str(frase), str(autor)]
            data.append(data_aux)
            print(c)

            c = c + 1
            
        
    df = pd.DataFrame(data, columns=['Frase', 'Autor'])
    df.to_csv('frases_de_amor_curtas', index=False)
    
    
    
 
    
    
    
    
    
    
    print("Everything is done!")
    driver.close()

if __name__ == "__main__":
    main(sys.argv[1:])
