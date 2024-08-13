# Use an official FreeRADIUS base image
FROM freeradius/freeradius-server:latest

# Install LDAP and required packages
RUN apt-get update && \
    apt-get install -y freeradius-ldap ldap-utils

# Copy the configuration files into the container
COPY mods-available/ldap /etc/freeradius/3.0/mods-available/ldap
COPY mods-enabled/ /etc/freeradius/3.0/mods-enabled/
COPY sites-available/default /etc/freeradius/3.0/sites-available/default

# Enable the LDAP module
RUN ln -s /etc/freeradius/3.0/mods-available/ldap /etc/freeradius/3.0/mods-enabled/ldap

# Expose the FreeRADIUS ports
EXPOSE 1812/udp 1813/udp

# Start the FreeRADIUS server in the foreground
CMD ["freeradius", "-f", "-l", "stdout"]

