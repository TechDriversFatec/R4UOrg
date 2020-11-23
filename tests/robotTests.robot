*** Settings ***
Documentation     Testes do R4U.
Library           OperatingSystem
Library           DatabaseLibrary
Library           Selenium2Library
Suite Setup       Connect To Database    dbapiModuleName=psycopg2    dbName=pi    dbUsername=fatec    dbPassword=fatec    dbHost=localhost    dbPort=5432
Suite Teardown    Close Browser

*** Test Cases ***

testCriacaoDeRecomendacao
    ${query}    Execute SQL String    insert into test.Recommendation(id, nome) values (nextval('seq_recommendation'), 'Test')
    ${query}    Query    SELECT * FROM test.Recommendation WHERE NOME = 'Test'
    Should Be Equal    ${query[0][1]}    Test

testConsultaFilmeNome
    ${query}    Query    SELECT * FROM test.FILME WHERE NOME = 'Joker'
    Should Be Equal    ${query[0][1]}    Joker

testConstultaFilmeGenero
    ${query}    Query    SELECT * FROM test.FILME WHERE Genero = 'Action'
    Should Not Be Equal    ${query[0][1]}    Joker

testFrontend
    ${frontIP}    Run    hostname -I | awk '{print $1}'
    Open Browser    http://${frontIP}:8080   Headless Firefox
    Click Element    xpath=.//html/body/div/div[2]/div/button
    Wait Until Element Is Visible    xpath=.//html/body/div/div[2]/div/p[2]
    ${resultFront}    Get Text    xpath=.//html/body/div/div[2]/div/p[2]
    ${query}    Query    SELECT NOME FROM Recommendation WHERE NOME = '${resultFront}'
    Should Be Equal    ${query[0][0]}    ${resultFront}