from google_play_scraper import reviews_all, Sort
import csv
import pandas as pd

def scrap_reviews(app_id, lang='id', country='id', sort=Sort.MOST_RELEVANT, count=4000, file_name='reviews.csv'):
    """
    Fungsi untuk melakukan scraping ulasan dari Google Play Store dan menyimpannya dalam file CSV.
    
    Args:
    app_id (str): ID aplikasi yang ulasannya akan diambil (contoh: 'com.byu.id').
    lang (str): Bahasa ulasan (default: 'id' untuk Bahasa Indonesia).
    country (str): Negara ulasan (default: 'id' untuk Indonesia).
    sort (Sort): Urutan ulasan (default: Sort.MOST_RELEVANT).
    count (int): Jumlah maksimum ulasan yang ingin diambil (default: 4000).
    file_name (str): Nama file CSV untuk menyimpan hasil (default: 'reviews.csv').
    
    Returns:
    pd.DataFrame: DataFrame yang berisi ulasan yang di-scrape.
    """
    
    reviews = reviews_all(
        app_id,         
        lang=lang,      
        country=country, 
        sort=sort,      
        count=count     
    )
    
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Review']) 
        for review in reviews:
            writer.writerow([review['content']])
    
    reviews_df = pd.DataFrame(reviews)
    reviews_df.to_csv(file_name, index=False)
    
    return reviews_df