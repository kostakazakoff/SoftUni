docker run -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=kosta@kazakoff.bg -e PGADMIN_DEFAULT_PASSWORD=Alabala123 -v my-data:/var/lib/pgadmin -d dpage/pgadmin4