from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from requests_html import HTMLSession
from tqdm import tqdm
from utils import *
import unittest


url_top = "https://www.levels.fyi/comp.html"
all_rows = []

session = HTMLSession()
resp = session.get(url_top)
resp.html.render()

category_jobs = {a.full_text:True for a in resp.html.find("option")}

options = webdriver.ChromeOptions()
#options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--headless') 
#options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)


#category_jobs["Management Consultant"] = False
#category_jobs["Investment Banker"] = False
#category_jobs["Business Analyst"] = False
#category_jobs["Solution Architect"] = False
#category_jobs["Mechanical Engineer"] = False
#category_jobs["Hardware Engineer"] = False
#category_jobs["Civil Engineer"] = True
#category_jobs["Biomedical Engineer"] = False
#category_jobs["Sales"] = False
#category_jobs["Recruiter"] = False
#category_jobs["Marketing Operations"] = False
#category_jobs["Marketing"] = False
#category_jobs["Human Resources"] = False
#category_jobs["Accountant"] = False
#category_jobs["Technical Program Manager"] = False
#category_jobs["Product Manager"] = False
#category_jobs["Product Designer"] = False
#category_jobs["Data Scientist"] = False
#category_jobs["Software Engineering Manager"] = False
#category_jobs["Software Engineer"] = False


for category in [k for k,v in category_jobs.items() if v][::-1]:
    
    print(category)
    category_rows = []
    curr_url = url_top + "?track=" + category
    resp = session.get(curr_url)
    resp.html.render()
    
    nbr_clicks_to_make = 0
    while nbr_clicks_to_make == 0:
        n_total_rows = int(resp.html.find(".pagination-info")[0].full_text.split('of ')[1].split(' ')[0])
        nbr_clicks_to_make = (n_total_rows // 10) + (n_total_rows % 10 != 0)
        print(nbr_clicks_to_make)
    
    driver.get(curr_url)
    
    for _ in tqdm(range(nbr_clicks_to_make)):

        soup = BeautifulSoup(driver.page_source, "html.parser")
        for tr in soup.find_all("tr", attrs={"data-has-detail-view":"true"}):
            for i, td in enumerate(tr.find_all("td")[1:]):
                td = td.text.strip().replace("\n\n", " ").split("\n")
                if i == 0:
                    comp_name = td[0]
                    d = td[1].split("|")
                    date = format_date(d[1].strip())
                    res = list(map(str.strip, d[0].split(',')))
                    if len(res) == 2:
                        res += ["United States"]
                    comp_city, comp_region , comp_country = res[:3]
                elif i == 1:
                    if len(td) == 1:
                        tag = td if type(td) != list else td[0]
                        level = np.NaN
                    else:
                        level, tag = td
                elif i == 2:
                    yrs_comp, yrs_xp = list(map(str.strip, td[0].split('/')))
                else:
                    d = td[0].replace("  ", "").split(' ')
                    dec, nego_up = 0, 0
                    if len(d) == 7:
                        nego_up = format_salary(d[0][2:])
                        dec = 1
                    try:
                        tot_salary = format_salary(d[dec])
                        base_salary = format_salary(d[dec+1])
                        stock_salary = format_salary(d[dec+3])
                        bonus_salary = format_salary(d[dec+5])
                    except IndexError:
                        tot_salary = format_salary(d[dec])
                        base_salary = np.NaN
                        stock_salary = np.NaN
                        bonus_salary = np.NaN
                    
            category_rows.append([category, comp_name, comp_country,
                            comp_region, comp_city, date, level,
                            tag, yrs_comp, yrs_xp, tot_salary, 
                            base_salary, stock_salary, bonus_salary, nego_up])
            
        
        element = driver.find_element(By.CSS_SELECTOR, 'li.page-item:last-child')
        #element = driver.find_element(By.CSS_SELECTOR, 'li.page-item:last-child>a:nth-child(1)')
        
        driver.execute_script("arguments[0].click();", element)
        #element.click()
        
        sleep(750/1000)
        
    print(len(category_rows), n_total_rows)
    df_tmp = pd.DataFrame(category_rows, columns=df_columns)
    df_tmp.to_csv("./db/" + category.replace(" ", "") + ".csv", index=False)

    all_rows.extend(category_rows)

df = pd.DataFrame(all_rows, columns=df_columns)
df.to_csv("./db/ALL_DATABASE.csv", index=False)
display(df)
