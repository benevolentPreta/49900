#include "ipfs_server_utils.h"
#include <sys/types.h>
#include <sys/wait.h>
int main(int argc, char **argv)
{
  pid_t pid;
  ipfs_conf_struct conf;
  char *server_folder, *file_name = "conf/ipfs_server.conf";
  int port_number, listen_fd, conn_fd, status;
  struct sockaddr_in remote_address;
  socklen_t addr_size = sizeof(struct sockaddr_in);
  mkzero(conf);
  mkzero(conf.users);
  if (argc != 3)
  {
    fprintf(stderr, "USAGE: ipfs_server <folder> <port>\n");
    exit(1);
  }

  server_folder = argv[1];
  port_number = atoi(argv[2]);

  read_ipfs_conf(file_name, &conf);
  strcpy(conf.server_name, server_folder + 1);
  // Assumption that server_folder begins with a /

  listen_fd = get_ipfs_socket(port_number);

  while (true)
  {
    if ((conn_fd = accept(listen_fd, (struct sockaddr *)&remote_address, &addr_size)) <= 0)
    {
      perror("Error Accepting Connection");
      continue;
    }

    pid = fork();
    if (pid != 0)
    {
      close(conn_fd);
      waitpid(-1, &status, WNOHANG);
    }
    else
    {
      ipfs_command_accept(conn_fd, &conf);
      close(conn_fd);
      break;
    }
  }
  free_ipfs_conf_struct(&conf);
  return 0;
}
