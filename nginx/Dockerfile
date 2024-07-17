FROM nginx:latest

COPY nginx.conf.template /etc/nginx/templates/nginx.conf.template

CMD /bin/bash -c "envsubst '\$${NGINX_SERVER_NAME}' < /etc/nginx/templates/nginx.conf.template > /etc/nginx/nginx.conf && exec nginx -g 'daemon off;'"
