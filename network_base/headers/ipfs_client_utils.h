#include "netutils.h"
#include "utils.h"
#include <arpa/inet.h>
#include <assert.h>
#include <netinet/in.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#ifndef IPFSCUTILS_H
#define IPFSCUTILS_H

#define IPFSC_SERVER_CONF "Server"
#define IPFSC_USERNAME_CONF "Username"
#define IPFSC_PASSWORD_CONF "Password"
#define IPFSC_PASSWORD_DELIM ": "
#define IPFSC_USERNAME_DELIM ": "

#define IPFSC_LIST_CMD "LIST"
#define IPFSC_GET_CMD "GET "
#define IPFSC_PUT_CMD "PUT "
#define IPFSC_MKDIR_CMD "MKDIR "
enum IPFSCConstants {
  PASSWORD_FLAG = 0,
  USERNAME_FLAG = 1
};

typedef struct ipfs_client_server_struct {
  char* name;
  char* address;
  int port;
} ipfs_client_server_struct;

typedef struct ipfs_client_conf_struct {
  ipfs_client_server_struct* servers[MAXSERVERS];
  user_struct* user;
  int server_count;
} ipfs_client_conf_struct;

int get_ipfs_client_socket(ipfs_client_server_struct*);
bool ipfs_client_command_validator(char*, int, file_attr_struct*);
void ipfs_client_command_handler(int*, int, char*, ipfs_client_conf_struct*);
bool ipfs_client_command_builder(char*, const char*, file_attr_struct*, user_struct*, int);
void ipfs_client_command_exec(int*, char*, int, file_attr_struct*, int, ipfs_client_conf_struct*);
void fetch_remote_dir_info(int*, int);
int fetch_remote_file_info(int*, int, server_chunks_collate_struct*);
void fetch_remote_splits(int*, int, file_split_struct*, int);
bool create_ipfs_client_to_dfs_connections(int*, ipfs_client_conf_struct*);
void get_output_list_command(server_chunks_collate_struct*);
bool auth_ipfs_client_to_dfs_connections(int*, ipfs_client_conf_struct*);
void setup_ipfs_client_to_dfs_connections(int**, ipfs_client_conf_struct*);
void tear_ipfs_client_to_dfs_connections(int*, ipfs_client_conf_struct*);
void read_ipfs_client_conf(char*, ipfs_client_conf_struct*);
bool check_ipfs_client_server_struct(ipfs_client_server_struct**);
void insert_ipfs_client_server_conf(char*, ipfs_client_conf_struct*);
void insert_ipfs_client_user_conf(char*, ipfs_client_conf_struct*, char*, int);
bool split_file_to_pieces(char*, file_split_struct*, int);
bool combine_file_from_pieces(file_attr_struct*, file_split_struct*);
void print_ipfs_client_conf_struct(ipfs_client_conf_struct*);
void free_ipfs_client_conf_struct(ipfs_client_conf_struct*);
void free_ipfs_client_server_struct(ipfs_client_server_struct*);
#endif
