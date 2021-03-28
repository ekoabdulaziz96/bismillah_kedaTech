 [programmer : ekoabdulaziz96@gmail.com]

informasi : 
 1. file ERD            : ERD.jpg
 2. file models         : app_store/models.py
 3. file controllers    : app_store/views_*.py
 3. file api            : app_store/api    --> [views and serializer]
 4. file testing        : app_store/tests          
                          app_store/tests/api 

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

NB:
- deployment/production: https://bismillah-keda-tech.herokuapp.com/app-store/api/ [DB:postgreSQL]
- github public : https://github.com/ekoabdulaziz96/bismillah_kedaTech