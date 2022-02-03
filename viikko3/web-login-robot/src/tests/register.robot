*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page


*** Test Cases ***

Register With Valid Username And Password
    Set Username  PlayerTwo
    Set Password  pLAYERtWO
    Set Confirm   pLAYERtWO
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Reset
    Set Username  Pl
    Set Password  pLAYERtWO
    Set Confirm   pLAYERtWO
    Submit Credentials
    Register Should Fail With Message  Username 3 sign minimum
    

Register With Valid Username And Too Short Password
    Reset
    Set Username  PlayerThree
    Set Password  pLAYER
    Set Confirm   pLAYER
    Submit Credentials
    Register Should Fail With Message  Password length atleast 8
    

Register With Nonmatching Password And Password Confirmation
    Reset
    Set Username  PlayerFour
    Set Password  pLAYERfOUR
    Set Confirm   pLAYERfour
    Submit Credentials
    Register Should Fail With Message  Passwords do not match
    

*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open
    
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Confirm
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}

Submit Credentials
    Click button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Register Page
    Create User  PlayerOne  pLAYERoNE
    Go To Register Page
    Register Page Should Be Open
