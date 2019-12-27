FROM nginx:1.17
RUN mkdir -p /etc/nginx/conf.d/include
ADD conf /etc/nginx/
COPY *.sh /usr/bin/
CMD ["/usr/bin/start.sh"]
