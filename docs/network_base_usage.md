# DISTRIBUTED-FILE-SYSTEM -

An implementation of interplanetary file system in C with user management which stores files across multiple servers and retrieve the files stored when required. Files are split into multiple chunks (depending on number of servers) and each of those chunks are partitioned across the servers on the basis of hash-value of the file contents. A chunk is stored on more than one servers to account for server failure(s) if any.

Implementation also supports handling multiple clients with valid user name and password in parallel (see conf/ipfs_server.conf and conf/ipfs_client.conf for user validation format).

# PREREQ -

### Dir Structure:

* Linux systems may need pkgs: `libpcap-dev` , and `libssl-dev` installed
* Assuming repository cloned
* Create (make) additional directories: `bin` , `log` , `SERVER1` , `SERVER2` , `SERVER3` , `SERVER4` 

# USAGE -

### Compiling:

  + `make ipfs_server` : Compiles the server instance in `bin/ipfs_server` 
  + `make ipfs_client` : Compiles the client instance in `bin/ipfs_client` 
  + `make client` : Compiles the client instance in `bin/ipfs_client` and starts the client instance (reading configuration file from `conf/ipfs_client.conf` )
  + `make clear` : Clears the content of DFS directories
  + `make kill` : Kills the running server instance
  + `make clean` : Deletes previously created binary files
  + `make start` : Starts four server instances and stores logs corresponding to each instance in `logs/` folder
  + `make run` : Starts `tail -f` on `logs/` directory
  + `make all` : Runs ` clean ipfs_server ipfs_client start run` targets

### Starting Server:

  To start all the servers at once use `make start` or to manually start ith server use following command:

`bin/ipfs_server /SERVER<i> <ith port number>` 

  Server reads its configuration file which has user name and passwords from `conf/ipfs_server.conf` 

### Starting Client:

  To start client via make file use `make client` or to manually start the client use following command:

`bin/ipfs_client <configuration-file-path>` 

  Configration file is a required arguement, refer to `conf/ipfs_server.conf` for sample configuration file

# COMMANDS -

After successfully compiling and running servers and client, following commands can be sent to servers via clients command line prompt

### GET

Used to fetch the remote file from servers into a local directory. This gives an error in case not enough servers are running to get the file properly or in case remote-file-path or local-file-path doesn't exist.

Syntax: `GET <local-file-path> <remote-file-path>` 

### PUT

Used to put a local file onto servers. This gives an error in case remote-file-path or local-file-path does not exsts. _Please do not execute this command when not all the servers are up and running._

Syntax: `PUT <local-file-path> <remote-file-path` 

### LIST

Lists all the files and folders in give directory. Gives an error when requested remote folder does not exists. Along with file name it also shows whether or not file can be successfully downloaded from the servers. If file cannot be downloaded properly the command append `INCOMPLETE` with the file name.

Syntax: `LIST <remote-folder-name>` 

### MKDIR

Makes a directory or sub-directories in the path sent. Gives an error when requested folder already exists. _Note: This command must be run with all servers running, or downed servers brought back online will NOT see the director -- fixing this is a project goal._

Syntax: `MKDIR <remote-folder-name>` 
