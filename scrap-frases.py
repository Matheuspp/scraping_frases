import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys
import pandas as pd
"""
    cria um dataset com frases e autores
    baixe o geckdriver para que o código funcione
"""



def main(argv):
    
    
    # ocultando navegador
    op = webdriver.FirefoxOptions()
    op.add_argument('-headless')    
    driver = webdriver.Firefox(options=op)
    
    data = [] # cria uma lista vazia para a lista de frases e autores

    # a configuração específica deste site permite divide os dados em varias paginas
    # podemos mudar o número de paginas até o limite existente na página
    for pagina in range(30): # escolhi 30
        if pagina > 0:
            driver.get("https://www.pensador.com/frases_de_motivacao/" + str(pagina+1)+"/") # não esxiste pagina 1
        else:
            driver.get("https://www.pensador.com/frases_de_motivacao/")
        
        
        elem = driver.find_elements_by_class_name("thought-card") # os divs com os frases e autores de mesma classe
        print("pagina {}".format(pagina+1) )
        c = 0
        for item in elem: # interando sob os divs da pagina
            # cada div tem a frase e o autor
            frase = item.find_element_by_xpath(".//p[@class='frase fr']").text
            autor = item.find_element_by_xpath(".//span[@class='autor']").text
            data_aux = [str(frase), str(autor)] # armazenando em uma lista
            data.append(data_aux) # preenchendo outra lista 
            print(c)

            c = c + 1
            
        
    df = pd.DataFrame(data, columns=['Frase', 'Autor']) # trasnformando em um dataframe
    df.to_csv('frases_de_motivacao', index=False) # salvando um arquivo csv dataset
     
    print("Everything is done!")
    driver.close()

if __name__ == "__main__":
    main(sys.argv[1:])
