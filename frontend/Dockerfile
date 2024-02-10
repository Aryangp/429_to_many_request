FROM node:18-alpine 
RUN apk update && \
    apk add --no-cache g++ make python3 py3-pip libc6-compat

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD npm run dev