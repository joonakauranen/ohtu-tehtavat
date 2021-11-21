*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page2

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallee
    Set Password  kalle123  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123  kalle123
    Submit Credentials
    #Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  kallekalle
    Set Password  k1  k1
    Submit Credentials
    #Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  kallekallek
    Set Password  kalle123  kalle1233
    Submit Credentials
    Register Should Fail With Message  Password not matching

*** Keywords ***

Register Should Succeed
    Register Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open2
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}  ${password_confirmation}
    Input Password  password  ${password}  ${password_confirmation}

Create User And Go To Login Page2
    Register Page Should Be Open
    Register Page Should Be Open2
