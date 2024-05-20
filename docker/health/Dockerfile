# Step1 : Base image
FROM ubuntu:latest

# Step2 : nginx install
RUN apt -y update && apt -y upgrade && apt -y install nginx curl
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

# Step3
COPY index.html /var/www/html

# Step4
HEALTHCHECK --interval=10s --timeout=3s CMD curl -f http://localhost || exit 1

# Step 5
CMD ["nginx"]
