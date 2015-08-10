FROM ubuntu:14.10
MAINTAINER Matheus Vill matheusvill@gmail.com

RUN echo "deb http://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
RUN apt-get update && apt-get install -y --force-yes vim wget tar git openjdk-7-jdk sbt
RUN wget http://downloads.typesafe.com/scala/2.11.6/scala-2.11.6.tgz && \
	wget http://ftp.unicamp.br/pub/apache/spark/spark-1.4.1/spark-1.4.1-bin-hadoop2.6.tgz 
RUN mkdir /usr/local/src/scala && \
    mkdir /usr/local/src/spark

RUN tar xvf scala-2.11.6.tgz -C /usr/local/src/scala/ && \
    tar xvf spark-1.4.1-bin-hadoop2.6.tgz -C /usr/local/src/spark 
RUN rm -f scala-2.11.6.tgz && \
    rm -f spark-1.4.1-bin-hadoop2.6.tgz
RUN echo "export SCALA_HOME=/usr/local/src/scala/scala-2.11.6" >> ~/.bashrc && \
    echo "export PATH=/usr/local/src/scala/scala-2.11.6/bin:$PATH" >> ~/.bashrc && \
    /bin/bash -c "source ~/.bashrc"

