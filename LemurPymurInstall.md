## Indri 5.0 on Mac OS X ##

Download Indri 5.0 from [sourceforge](http://sourceforge.net/projects/lemur/) and decompress
```
/usr/libexec/java_home #returns JAVA_HOME location
sh configure --enable-summarization --enable-java --enable-swig --with-javahome=/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
make # run make clean
sudo make install
```

## Indri 5.0 on CentOS 5 ##

Download and install Sun JDK
http://www.trading-shim.org/faq/?java

Download Indri 5.0 from [sourceforge](http://sourceforge.net/projects/lemur/) and decompress

```

sudo yum install gcc gcc-c++ swig automake autoconf libtool flex bison byacc gdb zlib-devel
sh configure --enable-summarization --enable-java --enable-swig --with-javahome=/usr/java/latest/
make # run make clean
sudo make install
```

## Configuring Indri for Site Search ##

Indri's Site Search component: http://www.lemurproject.org/lemur/SiteSearch.php

## Lemur 4.12 on Ubuntu 10.10 ##

Download lemur-4.12 from the Lemur Project website (http://www.lemurproject.org/)
```
sudo apt-get install build-essential zlib1g-dev
./configure --enable-summarization --enable-distrib --enable-cluster
make # run make clean
sudo make install
```

## Pymur on Ubuntu 10.10 ##

Pymur (a Python interface to The Lemur Toolkit) project website: http://findingscience.com/pymur/

```
sudo apt-get install git-core libtool automake python-dev
git clone git://github.com/bmuller/pymur.git
cd pymur
sudo ./make_shared_lemur.sh
sh autogen.sh
make
sudo make install
```