# Use an official OpenJDK image as a base image
FROM openjdk:17-alpine
WORKDIR /app
COPY target/your-app.jar .
EXPOSE 8080
CMD ["java", "-jar", "your-app.jar"]
