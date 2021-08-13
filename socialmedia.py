from selenium import webdriver
import time
import PySimpleGUI as sg

opti=['Instagram','Facebook','Twitter','Github']

# Instagram login system
def instalogin(username,password):
    site='https://www.instagram.com'
    driver.get(site)
    time.sleep(5)
    u=driver.find_element_by_css_selector("._2hvTZ[name='username']")
    u.send_keys(username)
    p=driver.find_element_by_css_selector("._2hvTZ[name='password']")
    p.send_keys(password)
    time.sleep(2)
    login=driver.find_element_by_css_selector(".Igw0E")
    login.click()


## Facebook login system
def fblogin(username,password):
    site='https://www.facebook.com/'
    driver.get(site)
    time.sleep(5)
    
    u=driver.find_element_by_id('email')
    p=driver.find_element_by_id('pass')
    btn=driver.find_element_by_css_selector('button[data-testid="royal_login_button"]')
    
    u.send_keys(username)
    p.send_keys(password)
    time.sleep(2)
    btn.click()
    
## Twitter login system
def twitlogin(username,password):
    site='https://twitter.com/login'
    driver.get(site)
    time.sleep(5)

    u=driver.find_element_by_css_selector('input[name="session[username_or_email]"]')
    p=driver.find_element_by_css_selector('input[name="session[password]"]')
    btn=driver.find_element_by_css_selector('div[data-testid="LoginForm_Login_Button"]')
    
    u.send_keys(username)
    p.send_keys(password)
    time.sleep(2)
    btn.click()

## Github login system
def gitlogin(username,password):
    site='https://github.com/login'

    driver.get(site)
    time.sleep(5)

    u=driver.find_element_by_id('login_field')
    p=driver.find_element_by_id('password')
    btn=driver.find_element_by_css_selector('input[name="commit"]')
    
    u.send_keys(username)
    p.send_keys(password)
    time.sleep(2)
    btn.click()

## Gmail logins
def gmlogin(username,password):
    ##remaining
    site='https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
  
    driver.get(site)
    time.sleep(5)

    u=driver.find_element_by_id('identifierId')
    u.send_keys(username)
    driver.find_element_by_class_name('VfPpkd-RLmnJb').click()
    time.sleep(3)
    p=driver.find_element_by_id('password')
    btn=driver.find_element_by_css_selector('input[name="commit"]')
    
    
    p.send_keys(password)
    time.sleep(2)
    btn.click()


def guitake():
    lay=[[sg.InputCombo(opti,default_value='select final location',enable_events=True,key='location',size=(55,4))],
         [sg.Text('Username/Email',key='utext'),sg.Input(key='uname')],
         [sg.Text('Password',key='ptext'),sg.Text('',size=(3,1)),sg.Input(key='passs')],
         [sg.Text('',size=(10,1)),sg.Button('Login',size=(30,1))]]
    window=sg.Window('Social Media Login/Sign-Up', layout=lay)
    while True:
        event,values=window.read()
        if(event==sg.WIN_CLOSED or event=='Exit'):
            break
        if event=='Login':
            loc=window['location'].get()
            un=window['uname'].get()
            ps=window['passs'].get()
            if(loc in opti and un!='' and ps !=''):
                l=opti.index(loc)
                if(l==0):
                    instalogin(un,ps)
                elif(l==1):
                    fblogin(un,ps)
                elif l==2:
                    twitlogin(un,ps)
                elif l==3:
                    gitlogin(un,ps)
                elif l==4:
                    gmlogin(un,ps)
                
            else:
                sg.popup('Invalid Attempt!!!!',auto_close=True,auto_close_duration=1)

    window.close()

if __name__=='_main_':
    driver=webdriver.Firefox(executable_path='geckodriver')
    guitake()

