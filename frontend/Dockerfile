FROM node:latest
COPY . .
RUN npm install
RUN npm run build --production
RUN npm install -g serve
CMD serve -s build
EXPOSE 5000
