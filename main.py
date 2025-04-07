import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from urllib.parse import urlparse

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.lineEdit.setPlaceholderText("https://elenta.lt")
        
        self.pushButton.clicked.connect(self.scrape_and_save)
        
    def is_valid_url(self, url):
        try:
            result = urlparse(url)
            
            return all([
                result.scheme == 'https',  
                result.netloc == 'elenta.lt',  
                bool(result.netloc)  
            ])
        except ValueError:
            return False
        
    def scrape_and_save(self):
        self.textBrowser.clear()
        
        url_input = self.lineEdit.text().strip()
        
        if not url_input:
            self.textBrowser.append("Prašau įvesti adresą, prasidedantį https://elenta.lt!")
            return
            

        if not self.is_valid_url(url_input):
            if not url_input.startswith("https://"):
                self.textBrowser.append("Klaida: URL turi prasidėti su https://")
            elif "elenta.lt" not in url_input:
                self.textBrowser.append("Klaida: URL turi būti elenta.lt domenas!")
            else:
                self.textBrowser.append("Klaida: Netinkamas URL formatas! Pvz.: https://elenta.lt")
            return
            
        
        if not url_input.endswith("/"):
            url_input += "/"

        full_url = f"{url_input}skelbimai/auto-moto/auto-aparatura"
        
        self.lineEdit_2.setText(full_url)
        self.label_2.setText("Pilnas scrapinamas URL:")
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            self.textBrowser.append(f"Scrapinama: {full_url}")
            response = requests.get(full_url, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            listings = soup.find_all('li', id=lambda x: x and x.startswith('unit-'))
            
            if not listings:
                self.textBrowser.append("Nerasta skelbimų šioje kategorijoje!")
                return
                
            listing_count = len(listings)
            total_value = 0.0
            data = []
            
            for listing in listings:
                title = listing.find('h3', class_='ad-hyperlink')
                title_text = title.text.strip() if title else "Be pavadinimo"
                
                price = listing.find('span', class_='price-box')
                price_text = price.text.strip() if price else "Kaina nenurodyta"
                
                if price_text != "Kaina nenurodyta":
                    try:
                        price_value = float(price_text.replace('€', '').replace(',', '.').strip())
                        total_value += price_value
                    except ValueError:
                        self.textBrowser.append(f"Klaida konvertuojant kainą: {price_text}")
                
                data.append([title_text, price_text])
                
                output = f"Pavadinimas: {title_text}\nKaina: {price_text}\n{'-'*50}"
                self.textBrowser.append(output)
            
            filename = f"elenta_scrape_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Pavadinimas', 'Kaina']) 
                writer.writerows(data)
            
            summary_message = (
                f"\nApdorota skelbimų: {listing_count}\n"
                f"Bendra visų skelbimų vertė: {total_value:.2f} €"
            )
            self.textBrowser.append(summary_message)
            self.textBrowser.append(f"Duomenys išsaugoti į failą: {filename}")
            
        except requests.exceptions.RequestException as e:
            self.textBrowser.append(f"Klaida jungiantis prie tinklapio: {str(e)}")
        except Exception as e:
            self.textBrowser.append(f"Įvyko klaida: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())