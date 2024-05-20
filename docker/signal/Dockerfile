# Base image
FROM ontouchstart/io.js

# action
COPY ./sig_test.js .
COPY ./package.json .

# port
EXPOSE 8000

# exec
ENTRYPOINT ["node", "sig_test"]