FROM fedora:rawhide
MAINTAINER Vadim Rutkovsky <vrutkovs@redhat.com>

# Install dependencies
RUN dnf install -y python3-gi
