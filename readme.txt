## 1. bootstrap.sh - this file calls dateapi/run.py 
2. run.py calls app.py
3. app.py model folder is called to create db tables
4. app.py call routes enables (/login, /product, etc) paths  
5. routes calls services for ancilliary service in the background if necessary

