FROM cae-artifactory.jpl.nasa.gov:16003/gov/nasa/jpl/cae/cae-centos7-simple-build-container
RUN apt-get update && \
    apt-get -y install gcc g++ make libffi-dev openssl-dev
