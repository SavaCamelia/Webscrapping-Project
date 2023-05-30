import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
#import requests
# Launching URL
url = 'https://termene.ro/firme'
# Create new Chrome session
driver = webdriver.Chrome()
driver.get(url)
#Cookies
#time.sleep(2)
wait=WebDriverWait(driver, 20)
element=wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"c-button"))).click()
#element = driver.find_element_by_class_name("c-button")

#Judete
time.sleep(2)
judete = [
  'Arad','Arges','Bacau','Bihor','Bistrita-nasaud','Botosani','Braila','Brasov','Bucuresti','Buzau','Calarasi','Caras-severin','Constanta',
  'Covasna','Dambovita','Dolj','Giurgiu','Gorj','Harghita','Hunedoara','Ialomita','Iasi',"Ilfov","Maramures","Mehedinti","Mures","Neamt","Olt",
  "Prahova","Salaj","Satu mare","Sibiu","Suceava","Teleorman","Timis","Tulcea","Valcea","Vaslui","Vrancea"
]
lista_firme=[]

def changeToNumber(string):
  for ch in string:
      if not ch.isdigit():
          string=string.replace(ch,'')
  string=int(string)
  return string

blabla = 0
while (blabla < 41):
  wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Firme din judetul " + judete[blabla] + "']"))).click()
  #numere = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div/ul/li[1]/a/div").text
  #print(numere)                         #/html/body/div[3]/div[1]/div/div/div/div[7]/div/ul/li[1]/a/div/div
                                        #/html/body/div[3]/div/div[2]/div/ul/li[1]/a/div/div
                                        #/html/body/div[3]/div/div/div/div[2]/div/ul/li[1]/a/div/div
  print('Judetul ' + judete[blabla])
  judet = judete[blabla] #numele judetului
  cities=driver.find_elements_by_class_name("how-card") #determinam numarul de orase din judet

  i=1
  ok=0
  noPage=9
  while i<=len(cities): #parcurgem fiecare oras
    #si de sub numele fiecaruia determinam numarul total de firme existente in acel oras
    all_business=wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div[2]/div/ul/li[" + str(i) + "]/a/div/div/small"))).text
    all_business=changeToNumber(all_business) #transformam numarul de firme din string in int
    print(all_business)
    # numele localitatii
    localitate=wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div[2]/div/ul/li[" + str(i) + "]/a/div/div/h6"))).text
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div/ul/li[" + str(i) + "]"))).click() #accesam orasul i
    j=1
    while j<=all_business:
      # determinam numarul de firme de pe o pagina
      business_on_a_page=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"search-results-grid-item")))
      business_on_a_page=len(business_on_a_page)

      wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div[2]/div/div[" + str(j) + "]/div/div[3]/a"))).click()
      exists = driver.find_elements_by_xpath("/html/body/section/div/div/div/h1") #verificam daca pentru firma curenta se poate deschide pagina
      if len(exists)==0:
        nume_firma=driver.find_element_by_xpath("/html/body/main/section/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/span").text
        cui=driver.find_element_by_xpath("/html/body/main/section/div/div/div/div[1]/div[1]/div/div/div[3]").text
        adresa=driver.find_element_by_xpath("/html/body/main/section/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div/table/tbody/tr[3]/td[2]").text
        cifra_afaceri=driver.find_element_by_xpath("/html/body/main/section/div/div/div/div[1]/div[1]/div/div/div[4]/div[1]/div/div/div[2]").text
        profit_pierdere=driver.find_element_by_xpath("/html/body/main/section/div/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div/div[2]").text
        nr_angajati=driver.find_element_by_xpath("/html/body/main/section/div/div/div/div[1]/div[1]/div/div/div[4]/div[3]/div/div/div[2]").text
        vechime_firma=driver.find_element_by_xpath("/html/body/main/section/div/div/div/div[1]/div[1]/div/div/div[4]/div[4]/div/div/div[2]").text
        nr_inmatriculare=driver.find_element_by_xpath("/html/body/main/section/div/div/div/div[1]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[2]").text
        stare_firma=driver.find_element_by_xpath("/html/body/main/section/div/div/div/div[1]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[2]").text
      else:
        cui = '-'
        nume_firma='-'
        adresa="-"
        cifra_afaceri="-"
        profit_pierdere="-"
        nr_angajati="-"
        vechime_firma="-"
        nr_inmatriculare='-'
        stare_firma="-"
      driver.back()
      business_dict = {"Numele firmei": nume_firma,
                       "CUI": cui[4:],
                       "Judet": judet,
                       "Localitate": localitate,
                       "Adresa": adresa,
                       "Cifra de afaceri": cifra_afaceri,
                       "Profit/Pierdere": profit_pierdere,
                       "Nr. angajati": nr_angajati,
                       "Vechimea firmei": vechime_firma,
                       "Numar de inmatriculare": nr_inmatriculare,
                       "Stare firma": stare_firma
                       }
      lista_firme.append(business_dict)
      #with open('data.json', 'w', encoding='utf8') as json_file:
        #data=json.load(json_file)
      """data.update(business_dict, ensure_ascii=False, separators=(",\n", ":"))
        json_file.seek(0)
        json.dump(data,json_file)"""
      with open('data.json', 'w', encoding='utf8') as json_file:
        json_file.write(json.dumps(lista_firme,indent=4,sort_keys=True,ensure_ascii=False))
      if j==business_on_a_page:
        if j<all_business:
          #wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/nav/div/a[" + str(nr_of_page) + "]"))).click()
          #nr_of_page+=1
          #next_page = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[4]/div/div/nav/div/a[" + str(nr_of_page) + "]")))
          #print(next_page,len(next_page))
          #if len(next_page)==0:
          if ok==0:
            wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div/div/nav/div/a[8]/i"))).click()
            ok=1
          else:
            if noPage<15:
              noPage += 1
            wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/nav/div/a[" + str(noPage) + "]/i"))).click()
          j=1
          all_business-=business_on_a_page
        else:
          wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/nav/ol/li[4]/a"))).click()
      j+=1
    i+=1
  wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/nav/ol/li[3]/a"))).click()
  time.sleep(2)
  blabla = blabla + 1
  break
