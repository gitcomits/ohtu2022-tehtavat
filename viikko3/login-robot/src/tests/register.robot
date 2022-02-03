*** Settings ***
Resource  resource.robot  
Test Setup  Input New Command And Create User

*** Test Cases ***
#Register With Valid Username And Password
#    Create User  player1  ready123
#    Input Login Command
 
#Register With Already Taken Username And Valid Password
#    Create User  kalle  kalle123
#    Input Login Command
#    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Create User  ca  kalle123
#    Input Login Command
    Output Should Contain  Username 3 sign minimum

#Register With Valid Username And Too Short Password
#    Create User  calle  kalle
#    Input Login Command
#    Output Should Contain  Password length atleast 8
    
#Register With Valid Username And Long Enough Password Containing Only Letters
#    Create User  galle  galle123
#    Input Login Command
#    Input Credentials  username  password
    Output Should Contain  Registration OK



*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input Login Command