#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <iostream>
#include <sys/wait.h>

#define MESSAGESIZE 500

struct message
{
    char message[MESSAGESIZE];
    char symbol;
};

void fireman(int)
{
    while (waitpid(-1, NULL, WNOHANG) > 0)
        std::cout << "A child process ended" << std::endl;
}

int main()
{

    signal(SIGCHLD, fireman);
    while (true)
    {

        if (fork() == 0)
        {
            std::cout << "A child process started" << std::endl;
            sleep(5);
            _exit(0);
        }
        std::cout << "Press enter to continue" << std::endl;
        std::cin.get();
    }
    return 0;
}