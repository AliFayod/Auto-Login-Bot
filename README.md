# Auto Login Gmail BOT
Please specify the path of chromedriver.exe in the instruction: 
```
browser = webdriver.Chrome(executable_path="chromedriver.exe")
```

## How it work

In this project, we are automatically logged into the Gmail account
You can log in with one or more accounts in succession, which is contained in the .txt file
Just put the usernames in the .txt file and add the file path to the following instruction: 
```
with open('Path For User.TXT') as openfileobject:
```
And add the password to the instructions if it's a static password:
```
password = "PassWord"
```
In addition to entering a number in the event of a request from the phone numbers file .txt
which will include the path within the instruction: 
```
number_txt = open("Path for Number.TXT", "r")
```
After each login, the cookies and proxy switch will be deleted from the .txt proxy file after adding the file path to the instruction:
```
ip_txt = open("Path for Ip.TXT", "r")
```
Note: Any stage can be dispensed with by commenting the useless instruction .

Note: When we want to login with only one account, please do not use rings .