# Need to install selenium package
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Time is built in to python nothing to install
import time
# Need to install BS4 (BeautifulSoup4)
# pip install bs4
from bs4 import BeautifulSoup
# Need to install Python MySQL Connector
# pip install mysqlclient
# If that doesn't worrk try below (for unbuntu)
# apt-get install python-dev libmysqlclient-dev
# pip install MySQL-python
# Worse case lots of google'ing.
# https://stackoverflow.com/questions/25865270/how-to-install-python-mysqldb-module-using-pip
import MySQLdb

print('Begining Process - Starting Login Routine')

# You will may need a bunch of setttings here for the Chrome driver depending on your server.
# Sometimes you need to set the path or where the binary is located. 

## The below options hide the browser totally.
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
## If you don't want to hide the browser un-comment the line below and comment out the above 3 lines.
# driver = webdriver.Chrome()

custUsername = "Username"
custPassword = "Password"

driver.get("https://us2.my.auvik.com/login")
# Waiting 3 secs for the page to load before moving on, you may need to tweak wait times.
time.sleep(3)
# Finding and clicking on the Microsoft Login Button
driver.find_element_by_xpath("//a[@href='/login/azurev1']").click()
time.sleep(3)
# Selecting the email login input
azureUser = driver.find_element_by_xpath("//input[@type='email']")
# Typing into the email login input
azureUser.send_keys(custUsername)
#clicking that submit / next button
driver.find_element_by_xpath("//input[@type='submit']").click()
# Wait for page to load
time.sleep(3)
# Select the password input box
azurePass = driver.find_element_by_xpath("//input[@type='password']")
# Type the password
azurePass.send_keys(custPassword)
# Click submit again
driver.find_element_by_xpath("//input[@type='submit']").click()
# Wait for page to load
time.sleep(3)
# Click the "No" button for the Keep Me Logged In
driver.find_element_by_xpath("//input[@type='button']").click()
# Wait for Page.
time.sleep(3)
# Finally load the page we are after, url includes client so no clicking/selecting needed.
driver.get("https://cotton.us2.my.auvik.com/#entity/root/dashboard")
## We have to add a long delay here because sometimes the tables are empty and take 5-10 seconds before anything is in them.
time.sleep(15)

print('Initial Page Is Loaded')

# Open connection to the mysql database 
# You need to change these! Login to your database.
db = MySQLdb.connect("IP-ADDRESS","USERNAME","PASSWORD","DATABASE") 
# Making Cursor Object For mySQL Queries 
cursor = db.cursor()
## Since we are keeping the window open and looping forever I am not closing the connection to the database.

def getUseageTable():
    ## Clear mySQl Table of Existing Data
    cursor.execute("TRUNCATE TABLE cotton_auvik_top_device_usage")
    ## Setup the page source code
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ## Get Top Device Useage Table and Break it Apart
    topDeviceTable = soup.find('table',{'class':'backgrid table table-hover widget-top-list-deviceUsage'})
    ## Break down into rows and skip the first row because its headers
    topDeviceRows = topDeviceTable.find_all('tr')[1:]
    # Test for <tr class="empty"> which means a empty table
    if '<tr class="empty">' not in str(topDeviceRows[0]):
        print('Useage Table Not Empty - Gathering Data')
        ## Loop through each row and find the text inside of each td and add to topDeviceData
        for row in topDeviceRows:
            name = row.find('td', class_='pageLink-cell renderable').getText()
            useage = row.find('td', class_='throughput-cell sortable renderable').getText()
            ## Write to SQL Values
            sql = "INSERT INTO cotton_auvik_top_device_usage (name, useage) VALUES (%s, %s)"
            val = (name, useage)
            cursor.execute(sql, val)
            db.commit()
    else:
        # The Table was Empty, Do something here if you like. It can't be empty. You could always delete the else part.
        print("Useage Table Empty")

def getDeviceUtilTable():
    ## Clear mySQl Table of Existing Data
    cursor.execute("TRUNCATE TABLE cotton_auvik_top_device_utilization")
    ## Setup the page source code
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ## Get Top Device Utilization Table and Break it Apart
    topDeviceUtilTable = soup.find('table',{'class':'backgrid table table-hover widget-top-list-deviceUtilization'})
    ## Break down into rows and skip the first row because its headers
    topDeviceUtilRows = topDeviceUtilTable.find_all('tr')[1:]
    ## Loop through each row and find the text inside of each td and add to topDeviceData
    if '<tr class="empty">' not in str(topDeviceUtilRows[0]):
        print('Utilization Table Not Empty - Gathering Data')
        for row in topDeviceUtilRows:
            name = row.find('td', class_='pageLink-cell renderable').getText()
            cpu = row.find('td', class_='percent-cell sortable renderable cpuUtil').getText()
            memory = row.find('td', class_='percent-cell sortable renderable memoryUtil').getText()
            storage = row.find('td', class_='percent-cell sortable renderable diskUtil').getText()
            sql = "INSERT INTO cotton_auvik_top_device_utilization (name, cpu, memory, storage) VALUES (%s, %s, %s, %s)"
            val = (name, cpu, memory, storage)
            cursor.execute(sql, val)
            db.commit()
    else:
        # The Table was Empty, Do something here if you like. It can't be empty. You could always delete the else part.
        print("Utilization Table Empty")

def getInternetTable():
    ## Clear mySQl Table of Existing Data
    cursor.execute("TRUNCATE TABLE cotton_auvik_internet_connections")
    ## Setup the page source code
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ## Get Internet Connections and Break it Apart
    internetConnectionsTable = soup.find('table',{'class':'backgrid table table-hover widget-grid-internetConnection'})
    ## Break down into rows and skip the first row because its headers
    internetConnectionsRows = internetConnectionsTable.find_all('tr')[1:]
    ## Loop through each row and find the text inside of each td and add to internetConnectionsData
    if '<tr class="empty">' not in str(internetConnectionsRows[0]):
        print('Internet Table Not Empty - Gathering Data')
        for row in internetConnectionsRows:
            name = row.find('td', class_='pageLink-cell sortable renderable').getText()
            highLow = row.find('td', class_='maxMinValue-cell renderable').getText()
            average = row.find('td', class_='throughput-stats-cell renderable').getText()
            sql = "INSERT INTO cotton_auvik_internet_connections (name, highLow, average) VALUES (%s, %s, %s)"
            val = (name, highLow, average)
            cursor.execute(sql, val)
            db.commit()
    else:
        # The Table was Empty, Do something here if you like. It can't be empty. You could always delete the else part.
        print("Internet Table Empty")

def emer():
    driver.find_element_by_xpath("//span[contains(@class, 'kpi-title') and contains(text(), 'Emergency')]").click()
    ## Wait 4 seconds for data to load
    time.sleep(4)
    ## Clear mySQl Table of Existing Data
    cursor.execute("TRUNCATE TABLE cotton_auvik_alerts_emergency")
    ##R eset the entire page source code so we can get the data table that was loaded.
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ##Get source of only the table.
    emergencyTable = soup.find('table',{'class':'backgrid table table-hover widget-grid-openAlertsBySeverity'})
    emergencyRows = emergencyTable.find_all('tr')[1:]
    ## Error catching, it will error if thier were no table rows to get. 
    ## I added this test to check for the "There are no open alerts." that shows up.
    ## The test is a basic if string is not in the first row (converted to string) then there must be normal ones to grab.
    if '<tr class="empty">' not in str(emergencyRows[0]):
        print('Emergency Table Not Empty - Gathering Data')
        for row in emergencyRows:
            severity = row.find('td', class_='severity-cell-link sortable renderable').getText()
            ## Gets tricky here. alertName and externalTicketId have the same css.
            ## dismissed and status as well
            eventNameRows = row.find_all('td', class_='eventName-cell sortable renderable')
            enumerationRows = row.find_all('td', class_='enumeration-cell sortable renderable')
            ## Now we have two lists that will have 2 items each. We can grab the rows from them.
            ## 0 for first instance 1 for second instance.
            status = enumerationRows[0].text
            alertName = eventNameRows[0].text
            detectedOn = row.find('td', class_='dateTime-cell sortable renderable').getText()
            enity = row.find('td', class_='pageLink-cell sortable renderable').getText()
            description = row.find('td', class_='eventDescription-cell sortable renderable').getText()
            relatedAlert = row.find('td', class_='relatedEvent-cell sortable renderable').getText()
            dismissed = enumerationRows[1].text
            externalTicketId = eventNameRows[1].text
            dispatched = row.find('td', class_='string-cell sortable renderable dispatched').getText()
            ## Write to SQL the Values, I used the same column names as the variables here. 
            sql = "INSERT INTO cotton_auvik_alerts_emergency (severity, status, alertName, detectedOn, enity, description, relatedAlert, dismissed, externalTicketId, dispatched) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (severity, status, alertName, detectedOn, enity, description, relatedAlert, dismissed, externalTicketId, dispatched)
            cursor.execute(sql, val)
            db.commit()
    else:
        # The Table was Empty, Do something here if you like. It can't be empty. You could always delete the else part.
        print("Emergency Table Empty")

def crit():
    ## Click on Critical Link
    driver.find_element_by_xpath("//a[@href='#entity/root/2']").click()
    ## Wait 4 seconds for data to load
    time.sleep(4)
    ## Clear mySQl Table of Existing Data
    cursor.execute("TRUNCATE TABLE cotton_auvik_alerts_critical")
    ## Reset the entire page source code so we can get the data table that was loaded.
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ## Get source of only the table.
    criticalTable = soup.find('table',{'class':'backgrid table table-hover widget-grid-openAlertsBySeverity'})
    criticalRows = criticalTable.find_all('tr')[1:]
    if '<tr class="empty">' not in str(criticalRows[0]):
        print('Critical Table Not Empty - Gathering Data')
        for row in criticalRows:
            severity = row.find('td', class_='severity-cell-link sortable renderable').getText()
            ## Gets tricky here. alertName and externalTicketId have the same css.
            ## dismissed and status as well
            eventNameRows = row.find_all('td', class_='eventName-cell sortable renderable')
            enumerationRows = row.find_all('td', class_='enumeration-cell sortable renderable')
            ## Now we have two lists that will have 2 items each. We can grab the rows from them.
            ## 0 for first instance 1 for second instance.
            status = enumerationRows[0].text
            alertName = eventNameRows[0].text
            detectedOn = row.find('td', class_='dateTime-cell sortable renderable').getText()
            enity = row.find('td', class_='pageLink-cell sortable renderable').getText()
            description = row.find('td', class_='eventDescription-cell sortable renderable').getText()
            relatedAlert = row.find('td', class_='relatedEvent-cell sortable renderable').getText()
            dismissed = enumerationRows[1].text
            externalTicketId = eventNameRows[1].text
            dispatched = row.find('td', class_='string-cell sortable renderable dispatched').getText()
            ## Write to SQL the Values, I used the same column names as the variables here. 
            sql = "INSERT INTO cotton_auvik_alerts_critical (severity, status, alertName, detectedOn, enity, description, relatedAlert, dismissed, externalTicketId, dispatched) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (severity, status, alertName, detectedOn, enity, description, relatedAlert, dismissed, externalTicketId, dispatched)
            cursor.execute(sql, val)
            db.commit()
    else:
        # The Table was Empty, Do something here if you like.
        print("Crit Table Empty")

def warn():
    driver.find_element_by_xpath("//a[@href='#entity/root/3']").click()
    ## Wait 4 seconds for data to load
    time.sleep(4)
    ## Clear mySQl Table of Existing Data
    cursor.execute("TRUNCATE TABLE cotton_auvik_alerts_warning")
    ## Reset the entire page source code so we can get the data table that was loaded.
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ## Get source of only the table.
    warningTable = soup.find('table',{'class':'backgrid table table-hover widget-grid-openAlertsBySeverity'})
    warningRows = warningTable.find_all('tr')[1:]
    if '<tr class="empty">' not in str(warningRows[0]):
        print('Warning Table Not Empty - Gathering Data')
        for row in warningRows:
            severity = row.find('td', class_='severity-cell-link sortable renderable').getText()
            ## Gets tricky here. alertName and externalTicketId have the same css.
            ## dismissed and status as well
            eventNameRows = row.find_all('td', class_='eventName-cell sortable renderable')
            enumerationRows = row.find_all('td', class_='enumeration-cell sortable renderable')
            ## Now we have two lists that will have 2 items each. We can grab the rows from them.
            ## 0 for first instance 1 for second instance.
            status = enumerationRows[0].text
            alertName = eventNameRows[0].text
            detectedOn = row.find('td', class_='dateTime-cell sortable renderable').getText()
            enity = row.find('td', class_='pageLink-cell sortable renderable').getText()
            description = row.find('td', class_='eventDescription-cell sortable renderable').getText()
            relatedAlert = row.find('td', class_='relatedEvent-cell sortable renderable').getText()
            dismissed = enumerationRows[1].text
            externalTicketId = eventNameRows[1].text
            dispatched = row.find('td', class_='string-cell sortable renderable dispatched').getText()
            ## Write to SQL the Values, I used the same column names as the variables here. 
            sql = "INSERT INTO cotton_auvik_alerts_warning (severity, status, alertName, detectedOn, enity, description, relatedAlert, dismissed, externalTicketId, dispatched) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (severity, status, alertName, detectedOn, enity, description, relatedAlert, dismissed, externalTicketId, dispatched)
            cursor.execute(sql, val)
            db.commit()
    else:
        # The Table was Empty, Do something here if you like.
        print("Warning Table Empty")

def info():
    driver.find_element_by_xpath("//a[@href='#entity/root/4']").click()
    ## Wait 4 seconds for data to load
    time.sleep(4)
    ## Clear mySQl Table of Existing Data
    cursor.execute("TRUNCATE TABLE cotton_auvik_alerts_informational")
    ## Reset the entire page source code so we can get the data table that was loaded.
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ## Get source of only the table.
    infoTable = soup.find('table',{'class':'backgrid table table-hover widget-grid-openAlertsBySeverity'})
    infoRows = infoTable.find_all('tr')[1:]
    if '<tr class="empty">' not in str(infoRows[0]):
        print('Info Table Not Empty - Gathering Data')
        for row in infoRows:
            severity = row.find('td', class_='severity-cell-link sortable renderable').getText()
            eventNameRows = row.find_all('td', class_='eventName-cell sortable renderable')
            enumerationRows = row.find_all('td', class_='enumeration-cell sortable renderable')
            status = enumerationRows[0].text
            alertName = eventNameRows[0].text
            detectedOn = row.find('td', class_='dateTime-cell sortable renderable').getText()
            enity = row.find('td', class_='pageLink-cell sortable renderable').getText()
            description = row.find('td', class_='eventDescription-cell sortable renderable').getText()
            relatedAlert = row.find('td', class_='relatedEvent-cell sortable renderable').getText()
            dismissed = enumerationRows[1].text
            externalTicketId = eventNameRows[1].text
            dispatched = row.find('td', class_='string-cell sortable renderable dispatched').getText()
            sql = "INSERT INTO cotton_auvik_alerts_informational (severity, status, alertName, detectedOn, enity, description, relatedAlert, dismissed, externalTicketId, dispatched) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (severity, status, alertName, detectedOn, enity, description, relatedAlert, dismissed, externalTicketId, dispatched)
            cursor.execute(sql, val)
            db.commit()
    else:
        # The Table was Empty, Do something here if you like.
        print("Info Table Empty")

def pause():
    driver.find_element_by_xpath("//a[@href='#entity/root/5']").click()
    ## Wait 5 seconds for data to load
    time.sleep(5)
    ## Clear mySQl Table of Existing Data
    cursor.execute("TRUNCATE TABLE cotton_auvik_alerts_paused")
    ## Reset the entire page source code so we can get the data table that was loaded.
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ## Get source of only the table.
    pauseTable = soup.find('table',{'class':'backgrid table table-hover widget-grid-currentPausedAlerts_kpi'})
    pauseRows = pauseTable.find_all('tr')[1:]
    if '<tr class="empty">' not in str(pauseRows[0]):
        print('Pause Table Not Empty - Gathering Data')
        for row in pauseRows:
            severity = row.find('td', class_='severity-cell-link sortable renderable').getText()
            alertName = row.find('td', class_='string-cell sortable renderable specName').getText()
            enity = row.find('td', class_='eventEntity-cell sortable renderable').getText()
            numOfTriggers = row.find('td', class_='string-cell sortable renderable configuredNumberOfTimes').getText()
            pauseWindowLength = row.find('td', class_='string-cell sortable renderable configuredCheckPeriod').getText()
            initiatedBy = row.find('td', class_='string-cell sortable renderable pauseInitiatedBy').getText()
            ## These two have the same class so there is no way to tell them apart.
            ## We will use the find_all instead and make a list and grab them that way.
            ## Same as we did above.  
            dateTimeRows = row.find_all('td', class_='dateTime-cell sortable renderable')
            ## Now we grab the text from 0 the first instance.
            pauseStart = dateTimeRows[0].text
            ## Now we grab the text from 1 the second instance.
            scheduledPauseEnd = dateTimeRows[1].text
            ## Write to SQL the Values, I used the same column names as the variables here. 
            sql = "INSERT INTO cotton_auvik_alerts_paused (severity, alertName, enity, numOfTriggers, pauseWindowLength, initiatedBy, pauseStart, scheduledPauseEnd) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (severity, alertName, enity, numOfTriggers, pauseWindowLength, initiatedBy, pauseStart, scheduledPauseEnd)
            cursor.execute(sql, val)
            db.commit()
    else:
        # The Table was Empty, Do something here if you like.
        print("Paused Table Empty")

# Main Loop. This will run forever and pause/sleep for 5 mins before running again.
# This is at the bottom because it calls the funtions we made above. They had to exist before we could use them.
loopCount = 0
while True:
    ## Increment the counter so we can tell how many times the script has run.
    loopCount+=1
    print("Starting Proccess - Number of Runs: " + str(loopCount))
    ## Run our main page table scrapes.
    getUseageTable()
    getDeviceUtilTable()
    getInternetTable()
    ## Click that emergency button and scrape the other tables.
    emer()
    crit()
    warn()
    info()
    pause()
    print("Ending Process - Sleeping for 5 Mins")
    time.sleep(300)
