 [programmer : ekoabdulaziz96@gmail.com]

informasi : 
 1. file ERD            : ERD.jpg
 2. file models         : app_store/models.py
 3. file controllers    : app_store/views_*.py
 4. file testing        : app_store/tests

Run Program : 
1. pastikan python sudah terisntall dan buka cmd/powershell di tepat diluar folder bismillah_keda
2. siapkan virtualenvironment baru dan aktifkan. (tidak wajib)
    - pip install virtualenv
    - virtualenv venv
    - ./venv/script/activate  (powershell)
4. masuk ke folder program 
    - cd bismillah_keda
3. install requirements program
    - pip install -r requirements.txt
4. persiapan sebelum running
    - python manage.py migrate  [migrasi database sqlite3]
5. jalankan unit test
    - python manage.py test .\app_store\ -v 2   {nilai dua bisa diganti 0-3, utk verbosity/trace}
6. jalankan program
    - python manage.py runserver

struktur folder:
-bismillah_keda
-venv

deployment/production/Operation: https://bismillah-keda.herokuapp.com/ [DB:postgreSQL]