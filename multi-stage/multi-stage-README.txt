Optimise your 🐬 docker image by 95% not just in size but also in security.


1. 𝗨𝘀𝗲 𝗠𝘂𝗹𝘁𝗶-𝗦𝘁𝗮𝗴𝗲 𝗯𝘂𝗶𝗹𝗱𝘀.

Stage 1 will build an artifact consisting of all the required libraries & dependencies. Stage 2 will use a slim/scratch base image and copy only the artifact from Stage 1 resulting in up to 95% less image size.

2. 𝗣𝗶𝗰𝗸 𝘀𝗹𝗶𝗺 𝘃𝗲𝗿𝗶𝗳𝗶𝗲𝗱 𝗯𝗮𝘀𝗲 𝗶𝗺𝗮𝗴𝗲𝘀.

Slim images don’t have any unnecessary components like shell utilities, libraries, or metadata. It will reduce the size and the attack surface area.

3. 𝗕𝗲𝗻𝗲𝗳𝗶𝘁 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗟𝗮𝘆𝗲𝗿 𝗖𝗮𝗰𝗵𝗶𝗻𝗴.

Always order the instructions from least changing to most changing i.e. use COPY instruction much later in the Dockerfile.

4. 𝗨𝘀𝗲 𝗹𝗲𝘀𝘀 𝗹𝗮𝘆𝗲𝗿𝘀. 

Commands like RUN COPY ADD create layers. Fewer layers = Small Size = Faster Build Times.

5. 𝗡𝗲𝘃𝗲𝗿 𝗿𝘂𝗻 𝗶𝗺𝗮𝗴𝗲𝘀 𝗮𝘀 𝘁𝗵𝗲 𝗿𝗼𝗼𝘁 𝘂𝘀𝗲𝗿.

By default, every image runs with root privileges, so make sure you run the image as a non-pseudo user[may break your application, some processes need root privileges]

6. 𝗦𝗰𝗮𝗻 𝗶𝗺𝗮𝗴𝗲𝘀 𝗳𝗼𝗿 𝘃𝘂𝗹𝗻𝗲𝗿𝗮𝗯𝗶𝗹𝗶𝘁𝗶𝗲𝘀 using tools like Trivy & Scout.

Avoid CRITICAL and HIGH vulnerabilities.

Tip: To see individual layers of an image use tools like Dive


Do share your thoughts on it ♻️

