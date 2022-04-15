# ecommerce
Repo ini untuk belajar Python/Django ecommerce yang diajarkan oleh [Zander's Django E-Commerce Project](https://www.youtube.com/watch?v=s3HuIRD5sUY).
Banyak masalah yang harus diatasi karene perbedaan versi komponen software yang dipakai.

## Rencana Kedepan
* Implementasi semua modul yang diajarkan oleh Zander
* Tambah modul yang kurang atau adaptasi yang sudah ada untuk lebih praktis

## Instal
buat virtual environment
```
python -m venv venv
```
aktivasi virtual environment
```
venv\Scripts\activate
```
instal komponen software yang diperlukan
```
pip install -r requirements.txt
```
jalankan web server
```
python manage.py runserver
```
*web server bisa diakses melalui: localhost:8000*

## Tes
```
pytest
```

###Firefox
* find the firefox browser version
    ```
    Help -> About Firefox
    ```
* cross reference the browser version and geckodriver from [Firefox Source Docs](https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html)
* download geckodriver from [github](https://github.com/mozilla/geckodriver)