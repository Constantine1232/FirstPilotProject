from selenium import webdriver

baseURL = "https://www.aviasales.ru/?gclid=EAIaIQobChMIrcWMvYPX1wIVApQYCh150wp6EAAYASAAEgJRDPD_BwE"
driver = webdriver.Chrome()

class findelementsonthepage():

    def OpenSite(self):
        driver.get(baseURL)



    def findMyCity(self):
        myCity = driver.find_elements_by_css_selector('#origin').clear().send_keys('kharkiv')
        if myCity is not None:
            print('first step')
        return myCity

    def findCityDestination(self):
        CityDestination = driver.find_elements_by_css_selector('#destination')
        if CityDestination is not None:
            print('second step')
        return CityDestination

    def startDatedield(self):

        departdate = driver.find_elements_by_css_selector('#depart_date')
        if departdate is not None:
            print('third step')
        return departdate

    def endDateField(self):
        endDate = driver.find_elements_by_css_selector('#return_date')
        if endDate is not None:
            print('third step')
        return endDate

    def PassagersNumber(self):
        number = driver.find_elements_by_css_selector('.of_dropdown__over')
        if number is not None:
            print("fourth step")
        return number

c = findelementsonthepage()

c.OpenSite()
c.findMyCity()
c.findCityDestination()
c.startDatedield()
c.endDateField()
c.PassagersNumber()
