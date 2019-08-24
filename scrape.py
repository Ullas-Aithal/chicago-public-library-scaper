import requests, json
from bs4 import BeautifulSoup

#Get username and password from config.json file
with open('config.json') as json_file:
    config = json.load(json_file)
payload = {}
payload["name"] = config["username"]
payload["user_pin"] = config["password"]

def getCheckedoutItems():
    #Get the login page
    session_requests = requests.session()
    login_url = "https://chipublib.bibliocommons.com/user/login?destination=https%3A%2F%2Fwww.chipublib.org"
    result = session_requests.get(login_url)

    #Get csrf token
    soup2 = BeautifulSoup(result.content, 'html.parser')
    payload["authenticity_token"] = soup2.find("meta", {"name" : "csrf-token"}).get("content").strip()

    #Post login credentials and csrf token and create a session
    result = session_requests.post(
        login_url, 
        data = payload, 
        headers = dict(referer=login_url)
    )

    #Get checked-out items
    url = "https://chipublib.bibliocommons.com/v2/checkedout/out"
    result = session_requests.get(
        url, 
        headers = dict(referer = url)
    )
    
    #---------------Local debugging-------------
    #Pipe the above result to a file and read from it instead of hitting the website every time while you debug
    #html_doc = open("result.html", "r")
    #soup = BeautifulSoup(html_doc.read(), 'html.parser')
    #-------------------------------------------
    soup = BeautifulSoup(result.content, 'html.parser')

    #Get books
    books = soup.find_all("div", {"class" : "cp-batch-actions-list-item"})
    response = []
    for book in books:
        responseItem = {}

        #Get book title
        book_title = book.find(  "span", {"class": "title-content"}).contents[0].strip() 
        responseItem["book_title"] = book_title
    

        #Get days remaining for book
        due_date_notice = book.find ("span", {"class": "due-date-notice"})
        days_remaining = due_date_notice.find("span").contents[0].strip()
        responseItem["days_remaining"] = days_remaining
        
        #Get due date for book
        checked_out_due_on = book.find ("div", {"class": "cp-checked-out-due-on"})
        due_date = checked_out_due_on.find("span", {"class" : "cp-short-formatted-date"}).contents[0].strip() 
        responseItem["due_date"] = due_date

        #Add item to response object
        response.append(responseItem)
    return response

print(getCheckedoutItems())

