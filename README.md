# Postgres
Удалённый доступ к PostgreSQL
в ubuntu:
1. # /etc/postgresql/13/main/postgresql.conf
    Изменить/добавить listen_addresses = '*' , убрать впереди знак #
2. # /etc/postgresql/9.1/main/pg_hba.conf
    добавить вниз hostssl  all  postgreadmin  0.0.0.0/0  md5
    
3. Войти в 
    vvv@WS-7104:~$ sudo -i -u postgres
    ввод пароля
    postgres@WS-7104:~$ createuser -s -r -d -P postgreadmin
    exit
4. vvv@WS-7104:~$ service postgresql restart
5. С другого комп windows через PgAdmin или Запуск Postgres.py ->
        
        Запуск Postgres.py
 import psycopg2

con = psycopg2.connect(
  database="vvvnik",
  user="postgreadmin",
  password="123",
  host="192.168.0.150",
  port="5432"
)
print("Database opened successfully")
cur = con.cursor()
cur.execute('''CREATE TABLE STUDENT
     (ADMISSION INT PRIMARY KEY NOT NULL,
     NAME TEXT NOT NULL,
     AGE INT NOT NULL,
     COURSE CHAR(50),
     DEPARTMENT CHAR(50));''')

cur.execute(
  "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3423, 'John', 18, 'Computer Science', 'ICT')"
)

print("Record inserted successfully")

con.commit()
con.close() 


