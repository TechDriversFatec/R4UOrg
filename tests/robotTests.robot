*** Settings ***


*** Test Cases ***
testSoma
    ${productPrice1}    Set Variable    1
    ${productPrice2}    Set Variable    3
    ${calculatedTotalPrice}     Evaluate    ${productPrice2}+${productPrice1}
    ${calculatedTotalPrice}    Convert To String    ${calculatedTotalPrice}    
    Should Be Equal    ${calculatedTotalPrice}    4

test2
    Log    Test