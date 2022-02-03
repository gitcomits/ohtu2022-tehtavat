*** Settings ***
Resource  resource.robot  
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  playerQ  ready123
    Output Should Contain  New user registered 
 
Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123 
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ca  kalle123
    Output Should Contain  Username 3 sign minimum

Register With Valid Username And Too Short Password
    Input Credentials  calle  kalle
    Output Should Contain  Password length atleast 8
    
Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  galle  galle123
    Output Should Contain  New user registered  



*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command