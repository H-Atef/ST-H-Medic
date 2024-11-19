from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import threading
import pandas as pd
from typing import Dict

import importlib

module1='medicine_mapper.web_scraping_resources'

wb=importlib.import_module(module1)


import queue

class DrugEyeActvIngScraper():
    def __init__(self):
        self.url = "http://www.drugeye.pharorg.com/drugeyeapp/android-search/drugeye-android-live-go.aspx"

    def process_input(self, active_ingredients_dict: Dict):
        active_ingredients = [values[:4] for keys, values in active_ingredients_dict.items()]
        diseases = list(active_ingredients_dict.keys())
        return active_ingredients, diseases

    def scrape_data_by_actv_ing(self, active_ingredient):
        try:
            driver = wb.WebScarpingToolInit().initialize_driver("google")
            driver.get(self.url)

            input_field = driver.find_element(By.NAME, "ttt")
            input_field.send_keys(active_ingredient)
            driver.find_element(By.ID, "b1").click()
            driver.find_element(By.ID, "BG").click()
            table = driver.find_element(By.ID, "MyTable")
            table.location_once_scrolled_into_view
            table_html = table.get_attribute('outerHTML')
            
            data = self._extract_data(table_html)
            return data
        except Exception as e:
            return {}
        finally:
            driver.close()

    def scrape_multiple_data(self, active_ingredients_dict):
        results = {}
        threads = []
        result_queue = queue.Queue()  # Thread-safe queue to collect results

        def thread_function(disease, active_ingredient):
            # Scrape data for this active ingredient and store in the result queue
            data = self.scrape_data_by_actv_ing(active_ingredient)
            result_queue.put((disease, active_ingredient, data))

        for disease, active_ingredients in active_ingredients_dict.items():
            for active_ingredient in active_ingredients[:4]:  # Only first 4 active ingredients
                thread = threading.Thread(target=thread_function, args=(disease, active_ingredient))
                threads.append(thread)
                thread.start()

        for thread in threads:
            thread.join()

        # Collect results from the queue
        while not result_queue.empty():
            disease, active_ingredient, data = result_queue.get()
            if disease not in results:
                results[disease] = {}
            results[disease][active_ingredient] = data

        return results

    def _extract_data(self, table_html):
        soup = BeautifulSoup(table_html, 'lxml')
        drug_names = []
        generic_names = []
        drug_classes = []
        similars = []
        alternatives = []

        rows = soup.find_all('tr')

        for i in range(len(rows) - 1):
            first_cell = rows[i].find('td')
            next_cell = rows[i + 1].find('td')

            if first_cell.has_attr("title"):
                q = first_cell.get('title')
                similars.append(self.url + "?gname=" + q + "geno")
                alternatives.append(self.url + "?gname=" + q + "alto")

            if next_cell.has_attr("style"):
                next_cell_style = next_cell.get('style')
                next_cell_style = next_cell_style[:next_cell_style.index(";")]

            if first_cell.has_attr("style"):
                cell_style = first_cell.get('style')
                cell_style = cell_style[:cell_style.index(";")]

                if 'color:Blue' == cell_style:
                    drug_names.append(first_cell.text)

                if 'color:Green' == cell_style:
                    drug_classes.append(first_cell.text)

                if 'color:Black' == cell_style:
                    generic_names.append(first_cell.text)

                if 'color:Blue' == cell_style and next_cell_style == 'color:Green':
                    generic_names.append("-")

                if 'color:Black' == cell_style and next_cell_style == 'color:BlueViolet':
                    drug_classes.append("-")

        last_cell = rows[-1].find('td')
        if last_cell.has_attr("title"):
            q = last_cell.get('title')
            similars.append(self.url + "?gname=" + q + "geno")
            alternatives.append(self.url + "?gname=" + q + "alto")

        data = {
            'drug_name': drug_names,
            'generic_name': generic_names,
            'drug_class': drug_classes,
            'similars': similars,
            'alternatives': alternatives
        }

        return data

# # Test the scraper with sample input
# scraper = DrugEyeActvIngScraper()

# output_example = {'common cold': ['Echinacea', 'Paracetamol (Acetaminophen)', 'Zinc Supplements', 'Ibuprofen', 'Vitamin C', 'Diphenhydramine']}

# json11 = scraper.scrape_multiple_data(output_example)

# import json
# with open('ex.json', 'w+') as file:
#     json.dump(json11, file)
