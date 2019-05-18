FROM node:latest

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add /usr/src/app/node_modules.bin to PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

ENV REACT_APP_USERS_SERVICE_URL=http://users-service:5000

# install and cache app dependencies
ADD yarn.lock /usr/src/app/yarn.lock
ADD package.json /usr/src/app/package.json
RUN yarn install    
RUN yarn global add live-server  

# add app
ADD . /usr/src/app

# build react app
RUN yarn build

# start app
CMD ["live-server", "build"]