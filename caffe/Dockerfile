# Not tried. Therefore, I dont know if it will works.

FROM ubuntu:14.04

MAINTAINER Yoshihiro Tanaka <feria.primavera@gmail.com>


RUN apt-get -y update && \
    apt-get install -y python wget vim git && \
    apt-get install -y make bc libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libboost-all-dev libhdf5-serial-dev libblas-dev libatlas-base-dev libgflags-dev libgoogle-glog-dev liblmdb-dev protobuf-compiler libsvm-dev libsvm3 libsvm-toolset && \
    apt-get install -y python-pip python-scipy python-matplotlib python-scikits-learn ipython python-h5py python-leveldb python-networkx python-nose python-pandas python-dateutil python-protobuf python-yaml python-gflags python-skimage cython

RUN adduser --disabled-password --gecos '' huge && \
    adduser huge sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER huge
ENV HOME /home/huge
ENV PYTHONPATH $HOME/caffe/python

WORKDIR $HOME
RUN wget http://developer.download.nvidia.com/compute/cuda/6_5/rel/installers/cuda_6.5.14_linux_64.run && \
    chmod u+x cuda_6.5.14_linux_64.run 

RUN git clone https://github.com/BVLC/caffe
WORKDIR $HOME/caffe
RUN cp Makefile.config.example Makefile.config && \
    make all && \
    make test && \
    make runtest


ENTRYPOINT ["/bin/bash"]
