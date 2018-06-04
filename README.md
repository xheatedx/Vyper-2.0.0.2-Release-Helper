This script helps reduce significantly the amount of labor to fill in Vyper's config.ini file since Vyper has no multiple profile
support at once at the moment. It helps generate multiple profiles in the config.ini format you need per profile if you 
want to run more than 1 profile with specific information.

The script allows you to copy and paste multiple profiles from an Excel sheet into a file and run it to generate the multiple
profiles without having to make any adjustments.

It also generates the accounts.txt file so that you can also copy paste the output straight into Vyper ready to run on Filler and 
the main bot.

To run the script correct just make sure to do the following:

1. Open the config file in the script folder and on the "TARGET_CONF_FILE" variable change its value (The "your script full path here") 
to the full path of the folder you downloaded this script on


2. In the "Profiles From Excel" just paste all profiles from in that file and save it. This is the format you must paste 
the profile information in https://docs.google.com/spreadsheets/d/12uy-sTeGAuifyBCBOQs9LSUhKhlCZBjPAUC20jlW87c/edit?usp=sharing

Your Profiles From Excel file should look something like this (Note that the spaces here are actually tab spaces):

US	BILL	GATES	123 MAIN ST	SUITE 111	LOS ANGELES	CA	90001	2131566464


- If you don't want the gen to generate the accounts.txt then you don't have to worry about anything else. Otherwise check the 
next steps below.

3. Fill in the Accounts for Gen file with ALL the accounts you want to generate for the accounts.txt. The Accounts For Gen.txt must 
have accounts in the email:password format on each line.

4. Fill in the All User Cards.txt with ALL UNIQUE CARDS in the format CARDNUMBER:CVV:EXPMONTH:EXPYEAR:CARDTYPE. I.E. 
4587456965451212:777:05:2050:Visa. 1 card per line.

IMPORTANT NOTE: THE ACCOUNTS FOR GEN.TXT FILE MUST HAVE MORE ACCOUNTS THAN - THE TOTAL AMOUNT OF CARDS IN ALL USER CARDS.TXT * 
THE ACCOUNTS_PER_CARD SETTING IN CONFIG.INI FILE. TO SIMPLIFY, IF YOU HAVE 100 ACCOUNTS AND 50 CARDS, THE ACCOUNTS_PER_CARD SETTING 
CAN NOT BE GREATER THAN 2!!

I will update the script for odd account quantities soon. 

Any questions DM me on twitter @chexmdc
