# AIPMT 2016 / NEET 2016 Participating Institutions List
Please find the list here: [NEET Colleges](http://shahidhk.github.io/mcc-web-scrapping/NEET-Colleges.csv)   
Download link: [NEET Colleges Download CSV](https://github.com/shahidhk/mcc-web-scrapping/raw/master/NEET-Colleges.csv)

# mcc-web-scrapping
Web scrapping NEET AIQ participating colleges list from Medical Counseling Commettee (MCC) website

## Motivation
The counselling process for AIPMT/NEET 2016 has just began and it is of utmost importance that the student is informed about all the colleges that are available. But, the Medical Counselling Committee (MCC) Website is so badly designed in such a way that the user has to click on each college link and it opens up details in a new window.

So, I decided to write a web scrapper to gather information regarding all institutions.

Since the page loaded information via ajax calls, Selenium webdriver was used to mimic user action and to render the page. Python bindings were used to select and save relevant information to a CSV file.


## Disclaimer 
This data is collected from MCC website (http://www.mcc.nic.in/MCCRes/Institute-Profile). The csv file provided here or the data collected by python code may not contain all the data provided in the website. Also, there is no guarantees made ragarding the correctness of data. I will not be responsible for any decision made on grounds of the data provided here. Please refer to MCC website for final confirmation.

- Data is owned by MCC

## Credits
- [Selenium - Web Browser Automation](http://www.seleniumhq.org/) 
- [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/getting-started)
