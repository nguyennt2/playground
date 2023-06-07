
FROM node:18-alpine

# copy the source tree and the pom.xml to our new container
COPY ./ ./

RUN npm install

CMD ["npm", "run", "start"]
