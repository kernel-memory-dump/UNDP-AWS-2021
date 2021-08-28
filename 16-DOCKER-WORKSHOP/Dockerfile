
# 1. WE NEED A base-image for our own image, let's go with bare-boned Linux+NodeJS

# Use official node image as the base image
FROM node:latest as build

# each linux System has it's own file system structure
# Let's setup a directory inside the container as our working directory
WORKDIR /usr/local/app

# Copy the source code from our host to container
COPY ./src/ /usr/local/app/

# Install all the dependencies inside the container
RUN npm install

# CHECK code quality 
RUN npm run lint
#RUN npm run test

# Generate the build of the application inside the container
RUN npm run build


# Stage 2: Serve app with nginx server inside the container

# Use official nginx image as the base image
FROM nginx:latest

# Copy the build output to replace the default nginx contents.
COPY --from=build /usr/local/app/dist/ /usr/share/nginx/html

# Expose port 80
EXPOSE 80
