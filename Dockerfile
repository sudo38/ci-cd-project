FROM nginx
COPY index.html /usr/share/nginx/html/index.html
COPY main.py /usr/share/nginx/html/main.py

EXPOSE 8080