import os
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

target_conf_file = config['MAIN']['TARGET_CONF_FILE']
MAXA = config['MAIN']['ACCOUNTS_PER_CARD']

f1 = open("Profiles From Excel.txt","r")
list1 = []
for line in f1:
    list1.append(line.split("\t"))
for profile in list1:
    print "Profile :", profile

shipping = {
        "Country": "",
        "FirstName" : "",
        "LastName" : "",
        "AddressLine1" : "",
        "AddressLine2" : "",
        "City" : "",
        "State" : "",
        "Zipcode" : "",
        "PhoneNumber" : ""
        }

billing = {
        "CardType" : "",
        "CardNumber" : "",
        "ExpirationMonth" : "",
        "ExpirationYear" : "",
        "FirstName" : "",
        "LastName" : "",
        "AddressLine1" : "",
        "AddressLine2" : "",
        "AddressLine3" : "",
        "City" : "",
        "PostalCode" : "",
        "State" : "",
        "PhoneNumber" : ""
}

shipping0 = shipping
dict_ls =[]
d3 = []
c=0

check_conf_folder = os.path.isdir(target_conf_file+"\\Config Profiles")
if check_conf_folder:
    print "Found Config Folder"
    pass
else:
    os.mkdir('Config Profiles')

for item in list1:
    current_sh = shipping
    current_bi = billing
    current_sh.update({"Country":list1[c][0]})
    current_sh.update({"FirstName":list1[c][1]})
    current_sh.update({"LastName":list1[c][2]})
    current_sh.update({"AddressLine1":list1[c][3]})
    current_sh.update({"AddressLine2":list1[c][4]})
    current_sh.update({"City":list1[c][5]})
    current_sh.update({"State":list1[c][6]})
    current_sh.update({"Zipcode":list1[c][7]})
    current_sh.update({"PhoneNumber":list1[c][8]})

    current_bi.update({"FirstName":list1[c][1]})
    current_bi.update({"LastName":list1[c][2]})
    current_bi.update({"AddressLine1":list1[c][3]})
    current_bi.update({"AddressLine2":list1[c][4]})
    current_bi.update({"City":list1[c][5]})
    current_bi.update({"State":list1[c][6]})
    current_bi.update({"PostalCode":list1[c][7]})
    current_bi.update({"PhoneNumber":list1[c][8]})
    if current_bi["CardType"]:
        current_bi.update({"CardType":list1[c][9]})

    print "Adding shipping to config profile",c,"...",current_sh
    print "Adding billing to config profile",c,"...",current_bi
    cs = current_sh
    cb = current_bi
    current_sh_str = str(current_sh)
    current_bi_str = str(current_bi)
    config = "[shipping]\n" \
            +"country = "+cs["Country"]+"\n" \
            +"firstname = "+cs["FirstName"]+"\n" \
            +"lastname = "+cs["LastName"]+"\n" \
            +"addressline1 = "+cs["AddressLine1"]+"\n" \
            +"addressline2 = "+cs["AddressLine2"]+"\n" \
            +"city = "+cs["City"]+"\n" \
            +"state = "+cs["State"]+"\n" \
            +"zipcode = "+cs["Zipcode"]+"\n" \
            +"phonenumber = "+cs["PhoneNumber"]+"\n" \
            +"\n"+"[billing]\n" \
            +"cardtype = \n"+"cardnumber = \n" \
            +"expirationmonth = \n" \
            +"expirationyear = \n" \
            +"firstname = "+cb["FirstName"]+"\n" \
            +"lastname = "+cb["LastName"]+"\n" \
            +"addressline1 = "+cb["AddressLine1"]+"\n" \
            +"addressline2 = "+cb["AddressLine2"]+"\n" \
            +"city = "+cb["City"]+"\n" \
            +"postalcode = "+cb["PostalCode"]+"\n" \
            +"state = "+cb["State"]+"\n" \
            +"phonenumber = "+cb["PhoneNumber"]+"\n" \
            +"\n"+"[Settings]"+"\n" \
            +"retries = 3\n" \
            +"jig_apt = False\n" \
            +"jig_name = False\n" \
            +"jig_addy = False\n" \
            +"good_ones = out.txt\n" \
            +"bad_ones = failed.txt\n" \
            +"debug_file = debug.log\n"
    print config
    dict_ls.append(current_sh.copy())
    dict_ls.append(current_bi.copy())
    d3.append(config)
    f2 = open(target_conf_file+"\Config Profiles\Vyper Config Profile "+str(c)+".txt","w")
    f2.write(config)
    print
    c = c + 1
print "after shipping0",shipping0
print "List d3 :", d3
f2.write(str(d3))

MAXA = int(MAXA)
cards_file = open("All User Cards.txt","r")
cards = []
for card in cards_file:
    cards.append(card)
# Removes \n from list strings and returns the same list
cards = ", ".join(cards)
cards = cards.replace('"', '')
cards = cards.replace("\n","")
cards = cards.split(", ")
print "Getting cards..."
print cards
mass_cards = []
for card in cards:
    for i in range(0,MAXA):
        mass_cards.append(card)

accounts_for_gen = open("Accounts For Gen.txt","r")
accounts = []
for account in accounts_for_gen:
    accounts.append(account)
accounts = ", ".join(accounts)
accounts = accounts.replace('"', '')
accounts = accounts.replace("\n","")
accounts = accounts.split(", ")
filler = open("Vyper Filler Accounts File.txt","w")
for i in range(0,len(mass_cards)):
    filler.write(accounts[i]+":"+mass_cards[i]+"\n")
accounts_for_gen.close()
filler.close()
