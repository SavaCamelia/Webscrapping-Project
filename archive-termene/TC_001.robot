*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${Browser}    Chrome
${URL}  https://termene.ro/firme/



*** Test Cases ***

Open_browser
    open browser    ${URL}    ${Browser}
Wait
    wait until element is visible    xpath: /html/body/div[2]/div/div[1]/div[2]/a
Click
    click element    xpath: /html/body/div[2]/div/div[1]/div[2]
Judete_Arad
    click element    xpath: /html/body/div[3]/div/div/div/ul/li[1]
Localitati_Vladimirescu
    scroll element into view    xpath: /html/body/div[3]/div/div/div/div[2]/div/ul/li[1]
Click_Vladimirescu
    click element   xpath: /html/body/div[3]/div/div/div/div[2]/div/ul/li[1]/a
Firma
    click element    xpath: /html/body/div[3]/div/div/div/div[2]/div[2]/div/div[1]/div/div[3]/a

*** Keywords ***
