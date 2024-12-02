# Use the official MariaDB image as the base image
FROM mariadb:latest

# Set environment variables for Galera
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV CLUSTER_NAME=my_galera_cluster
ENV NODE_NAME=node1
ENV WSREP_CLUSTER_ADDRESS=gcomm://
ENV WSREP_NODE_ADDRESS=auto

# Install Galera-specific packages (already included in MariaDB)
# MariaDB ships with Galera support, so no additional packages are needed here.
RUN apt-get install -y galera-4 rsync lsof

# Copy the custom Galera configuration
COPY ./my_galera.cnf /etc/mysql/conf.d/my_galera.cnf

# Expose the Galera ports:
# - 3306 for MySQL/MariaDB
# - 4567 for Galera cluster replication
# - 4568 for IST (Incremental State Transfer)
# - 4444 for SST (State Snapshot Transfer)
EXPOSE 3306 4567 4568 4444

# Command to start MariaDB and Galera
CMD ["mysqld"]