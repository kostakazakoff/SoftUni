import os

print('Create a PostgreSQL Docker Container')
print('____________________________________')
port = input('Port(5432): ')
user = input('Postgress database user: ')
password = input('Password: ')
volume = input('Data Volume name: ')
container_name = input('Container name: ')

os.system(f'cmd /k "docker run -p {port}:5432 -e POSTGRES_USER={user} -e POSTGRES_PASSWORD={password} -d -v {volume}:/var/lib/postgresql/data --name {container_name} postgres:latest"')
