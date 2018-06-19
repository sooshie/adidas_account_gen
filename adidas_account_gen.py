import requests
import random
import string

__emailRoot = "Adidas_"
__emailDomain = "gmail.com"
__passwordRoot = "Adidas"
s = requests.Session()
headers = {"Accept"          : "application/json",
           "Content-Type"    : "application/json; charset=UTF-8",
           "Connection"      : "keep-alive",
           "Accept-Language" : "en-us",
           "Accept-Encoding" : "br, gzip, deflate",
           "User-Agent"      : "adidas/716 CFNetwork/901.1 Darwin/17.6.0"}

def genericLookUp(email):
    '''
    Initial request the app makes to see if an account exists
    Also an easy way to get adidas to set the right cookies 
    '''
    
    data = {"email"         :  email,
            "legalEntity"   : "ADIUS",
            "clientId"      : "293FC0ECC43A4F5804C07A4ABC2FC833",
            "source"        : "90901",
            "countryOfSite" : "US",
            "version"       : "13.0"}
    
    r = s.post("https://srs.adidas.com/scvRESTServices/account/genericLookUp", headers=headers, json=data)
    if r.status_code != 200:
        print("Houston, we have a problem")
        print("Status Code: {}".format(r.status_code))
        print("Response Text: {}".format(r.text))
    
def createAccount(email, password): 
    '''
    Following creates the account

    You can access the oauth token by adding in code for r.json
    ''' 
    data = {"source"                  : "90901",
            "countryOfSite"           : "US",
            "actionType"              : "REGISTRATION",
            "password"                : password,
            "scope"                   : "pii mobile2web",
            "clientId"                : "293FC0ECC43A4F5804C07A4ABC2FC833",
            "email"                   : __email,
            "version"                 : "13.0",
            "minAgeConfirmation"      : "Y",
            "access_token_manager_id" : "jwt"}
    
    r = s.post("https://srs.adidas.com/scvRESTServices/account/createAccount", headers=headers, json=data)
    if r.status_code != 200:
        print("Houston, we have a problem")
        print("Status Code: {}".format(r.status_code))
        print("Response Text: {}".format(r.text))
    
    print(r.text)


# Generate email
__email = __emailRoot + "".join(random.choice(string.ascii_letters + string.digits) for x in range(10)) + "@" + __emailDomain
__password = __passwordRoot + "".join(random.choice(string.ascii_letters) for x in range(2)) + "".join(random.choice(string.digits) for x in range(2))
genericLookUp(__email)
createAccount(__email, __password)
print("Email: {}\nPassword: {}".format(__email, __password))
