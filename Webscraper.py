'''
-----TROUBLES-----
Some of the troubles I ran into were not quite following what the tutorial was doing. To combat 
against this I would write comments over almost every line of code to keep track of what I 
thought was happening and to write some parts in ways I could make sense of when I wasn't quite
following the tutorial on what they were saying. The second part especially with the second half 
of the program when it is picking out just the Python-related jobs. I also had issues with VSC
recognising the imported modules, but it turns out it was just in some protective mode and wasn't
running them and I just had to authorize it.
'''
'''
-----DESIGN-----
I will solve the problem by learning how to web scrape a website with Python.
To solve the problem I followed a tutorial on web scraping and played around with it to try to figure it out.
I tested to make sure my code was producing the right results.
My code goes through the testing website that is provided in the tutorial and lists out the job listings and 
the ones that are related to Python. It goes through and limits it down to the containers that each listing is
in and cuts out all of the html and limits it just down to the text contents and prints it out to gather the 
information.
'''
'''
-----USER DOCUMENTATION-----
Run the program. When the program runs it will print out each job listing on the website.
It will provide the title, company, location, and application link. After it goes through 
each job listing it will list off the titles of the jobs that are Python related.
'''
'''
Name: Jordyn Kuhn
Date: 10/25/22
CRN: 10230
CIS 216: Python Programming
Time Estimate: 3 hours
'''
#import modules
import requests
from bs4 import BeautifulSoup

def webscrape():
    #Website that's being scraped
    URL = "https://realpython.github.io/fake-jobs/"

    #gets the html data
    page = requests.get(URL)

    #declares the html parser variable
    sandwich = BeautifulSoup(page.content, "html.parser")

    #Find the specific html we're looking for (with the job listings in it)
    results = sandwich.find(id="ResultsContainer")

    #Find the job listings
    jobs = results.find_all("div", class_="card-content")

    #Find the specific info in the job listings and prints it
    for job in jobs:
        #find the title company and location
        title = job.find("h2", class_="title")
        company = job.find("h3", class_="company")
        location = job.find("p", class_="location")

        #print the title company and location
        print("Job Title:", title.text.strip())
        print("Company:",company.text.strip())
        print("Location:",location.text.strip())

        #Find the url associated with the job and only get the second link, since its the application link
        link_url = job.find_all("a")[1]["href"]
        print("Apply:", {link_url})

        print()

    #Find and Print Python Related Jobs
    python_jobs = results.find_all(
        "h2", string=lambda text: "python" in text.lower()
    )

    for jobs in python_jobs:
        print(jobs.text.strip())
    
#run the program
if __name__ == '__main__':
    webscrape()