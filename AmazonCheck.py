import requests
from bs4 import BeautifulSoup
import smtplib


header = {"userAgent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'} #user agent taken from the web

productlist = dict() #creating a dict that will contain the different product links and the price the user wants them to fall under



def inputlinks():#this function uses a while and continues to prompt the user for product links and their desired price, and then stores them in a dictionary as key value pairs
    URL = ""
    while URL!="done":
        URL=input("Enter an amazon product link, or enter done if done")
        if URL == "done":
            break
        price = float(input("Enter the maximum price you are willing to pay"))
        productlist.update({URL:price})
        
def email(URL):#this function uses the smtplib library in order to execute the function of sending the mail, and takes one parameter which is the URL link of the product 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()#using ehlo to setup the server connection 
    server.starttls()
    server.ehlo()
    server.login('nandukrv@gmail.com','ztdcekxvkmoenztw')#logging into email using a specific password setup for this particular device 

    subject = "Price DROP"
    body = URL
    message = f"Subject: {subject}\n\n{body}"#defining the subject, body, and message 

    server.sendmail("nandukrv@gmail.com","nandukrv@gmail.com",message)#sending the email to oneself 

    server.quit
 
def priceCheck():

    for i,j in productlist.items():
        page = requests.get(i, headers=header)#loops through the dictionary and sets the page variable to the link which i represents,
        #and sets the headers to the user agent defined above as global variable 
        soup = BeautifulSoup(page.content, 'html.parser')#uses beautiful soup to parse the html
        productName = soup.find(id = "productTitle").get_text()
        price = soup.find(id = "priceblock_ourprice").get_text()  
        aprice = float(price[1:6])#aprice variable removes the dollar sign from the amazon page and gets the float value of the price 

        if(aprice <= j):#if the price is less than the desired user price which is represented by j, then the email will be sent and the product name and price will be displayed in the program
            email(i)
            print(productName.strip())
            print(aprice)

inputlinks()

priceCheck()
#calling the functions to execute the program
    
#uses soup to frin the product name
#uses soup to get the price
