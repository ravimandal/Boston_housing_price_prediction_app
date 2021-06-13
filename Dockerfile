# base image
# a little overkill but need it to install dot cli for dtreeviz
FROM ubuntu:latest

# ubuntu installing - python, pip, graphviz
RUN apt-get update &&\
    apt-get install python3.9 -y &&\
    apt-get install python3-pip -y &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

# making directory of app
WORKDIR /app

# copy over requirements
COPY requirements.txt ./requirements.txt

# install pip then packages
RUN pip install -r requirements.txt

# copying all files over
COPY . .

# exposing default port for streamlit
EXPOSE 8501

ENTRYPOINT ["streamlit","run"]

# cmd to launch app when container is run
CMD ["app.py"]

# streamlit-specific commands for config
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'