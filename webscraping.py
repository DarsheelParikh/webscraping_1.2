from bs4 import BeautifulSoup
import time
import csv
start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/chromedriver")
browser.get(start_url)
time.sleep(10)
def scrape():
    headers = ["V.Mag, Proper Name, Bayer Designation, Distance, Spectral Class, Mass, Radius, Luminosity"]
    star_data = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for td_tag in soup.find_all("td",attrs= {"sun"}):
        tr_tags = td_tag.find_all("tr")
        temp_list = []
        for index, tr_tag in  enumerate(tr_tags):
            if index== 0:
                temp_list.append(tr_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(tr_tag.contents[0])
                except:
                    temp_list.append("")
        planet_data.append(temp_list)
    browser.find_element_by_xpath("//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a").click()
    with open("scapper2.csv","w")as f:
        csvwriter= csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerow(planets_data)
scrape()
