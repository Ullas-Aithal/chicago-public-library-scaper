# Chicago Public Library (CPL) scraper

This python script will scrape cpl website to get the checked out items and due dates for the books you've borrowed. This script returns a json array of your books:

```json
[
  {
    "book_title": "Cracking the Coding Interview",
    "days_remaining": "17 days remaining",
    "due_date": "Sep 10, 2019"
  },
  {
    "book_title": "Vicious",
    "days_remaining": "19 days remaining",
    "due_date": "Sep 12, 2019"
  }
]
```
## How the script works

* The script gets the login page first and extracts the csrf-token. 
* Then this crsf-token along with user credentials is POSTed
* The session is now created. Another request is made to get the checked out items
*  Using BeautifulSoup the page is scraped to get the div items holding all the information required for each book

## Installation
Enter your cpl user name and password in config.json file.

```json
{
  "username" : "<<user_name>>",
  "password" : "<<password>>"
}

```


This is a python3 script and the scraping is done using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#) package. 

Install the requirements:

```bash
pip3 install requests, beautifulsoup4
```

## Usage

```python
python3 scarpe.py
```

You can also make this as an api call using [Flask](https://www.fullstackpython.com/flask.html). You can look at my other project where I'm using this script as an api call using flask (link to be up soon)

## Future features

Add hold item status to the json

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
