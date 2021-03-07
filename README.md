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
5. С другого комп windows через PgAdmin 
