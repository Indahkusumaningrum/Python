import pandas as pd
from calculation import hitung_diskon, hitung_total

# Data berdasarkan soal dan ditambah 5 data baru
data = {
    "Courses": ["Spark", "Hadoop", "Pandas", "Java", "Pyspark", "Deep Learning", 
                "Big Data Analytics", "Data Visualization", "Web Development", "DevOps"],
    "Categories": ["DS", "DS", "PI", "PI", "DS", "DS", "DS", "PI", "PI", "Non-PI"],
    "Fee": [20000, 25000, 30000, 22000, 26000, 32000, 35000, 28000, 20000, 27000],
    "Duration": [30, 40, 35, 60, 60, 45, 50, 30, 60, 40],
    "Percentage Discount": [5, 10, 5, 5, 5, 7, 10, 5, 5, 5]
}


def dataFrame():
    # Membuat DataFrame
    df = pd.DataFrame(data)

    # Menambahkan kolom 'Total' ke DataFrame dengan fungsi dari file terpisah
    df.apply(hitung_diskon, axis=1)
    df['Total'] = df.apply(hitung_total, axis=1)
    return df

# Menampilkan DataFrame
print(dataFrame())