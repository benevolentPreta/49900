#include "netutils.h"
#include "utils.h"
#include <arpa/inet.h>
#include <assert.h>
#include <netinet/in.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/fcntl.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/unistd.h>
#ifndef IPFSSUTILS_H
#define IPFSSUTILS_H

#define FOLDER_NOT_FOUND_ERROR "Requested folder does not exists on server"
#define FOLDER_EXISTS_ERROR "Requested folder already exists on server"
#define FILE_NOT_FOUND_ERROR "Requested file does not exists on server"
#define AUTH_FAILED_ERROR "Invalid Username/Password. Please try again"
enum IPFSSConstants
{
  MAXUSERS = 10,
  MAXCONNECTION = 10,
  FOLDER_NOT_FOUND = 1,
  FOLDER_EXISTS = 2,
  FILE_NOT_FOUND = 3,
  AUTH_FAILED = 4
};

typedef struct ipfs_server_conf_struct
{
  char server_name[MAXCHARBUFF];
  user_struct *users[MAXUSERS];
  int user_count;
} ipfs_server_conf_struct;

typedef struct ipfs_server_recv_command_struct
{
  int flag;
  user_struct user;
  char folder[MAXCHARBUFF]; // Folder always ends with "/" and doesn't begin with one
  char file_name[MAXCHARBUFF];
} ipfs_server_recv_command_struct;

int get_ipfs_server_socket(int);
bool auth_ipfs_server_user(user_struct *, ipfs_server_conf_struct *);
void send_error_helper(int, const char *);
void send_error(int, int);
void read_ipfs_server_conf(char *, ipfs_server_conf_struct *);
void insert_ipfs_server_user_conf(char *, ipfs_server_conf_struct *);
void ipfs_server_command_accept(int, ipfs_server_conf_struct *);
bool ipfs_server_command_decode_and_auth(char *, const char *, ipfs_server_recv_command_struct *, ipfs_server_conf_struct *);
bool ipfs_server_command_exec(int, ipfs_server_recv_command_struct *, ipfs_server_conf_struct *, int);
void create_ipfs_server_directory(char *);
void ipfs_server_directory_creator(char *, ipfs_server_conf_struct *);
void print_ipfs_server_conf_struct(ipfs_server_conf_struct *);
void free_ipfs_server_conf_struct(ipfs_server_conf_struct *);
#endif
