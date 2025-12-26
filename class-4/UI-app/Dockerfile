# 1. Base Image: Choose a suitable one for your UI framework and dependencies
FROM node:16-alpine  # Example for a React app
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000  # Adjust as needed
CMD ["npm", "start"]  # Replace with your start script
