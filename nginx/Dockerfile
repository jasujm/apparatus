FROM nginx:1.17
RUN mkdir -p /etc/nginx/conf.d/include
ADD conf /etc/nginx/
COPY start.sh /usr/bin
CMD ["/usr/bin/start.sh"]
