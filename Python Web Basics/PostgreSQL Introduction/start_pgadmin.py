import os

print('Create pgAdmin')
print('______________')
port = input('pgAdmin port(5050): ')
user = input('pgAdmin username: ')
password = input('pgAdmin password: ')

os.system(f'cmd /k "docker run -p {port}:80 -e PGADMIN_DEFAULT_EMAIL={user} -e PGADMIN_DEFAULT_PASSWORD={password} -v my-data:/var/lib/pgadmin -d dpage/pgadmin4"')