// A simple server in the internet domain using TCP
// The port nu1mber is passed as an argument

// Please note this is a C program
// It compiles without warnings with gcc

#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <iostream>
#include <vector>
#include <sys/wait.h>

using namespace std;

void verify_args(int argc);
void fireman(int a);
const char * get_fibonacci_code(int rank);
vector<int> generate_fibonacci_series(int max);
void process_request(int newsockfd, int n);

int main(int argc, char *argv[])
{
    verify_args(argc);

    int sockfd, newsockfd, portno, clilen;
    sockaddr_in serv_addr, cli_addr;

    int n;
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        cout << "ERROR opening socket" << endl;
        exit(0);
    }

    bzero((char *) &serv_addr, sizeof(serv_addr));
    portno = atoi(argv[1]);
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(portno);

    if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) {
        cout << "ERROR on binding" << endl;
        exit(0);
    }
    listen(sockfd,5);
    signal(SIGCHLD, fireman);
    clilen = sizeof(cli_addr);

    while (true) {
        newsockfd = accept(sockfd, (sockaddr *) &cli_addr, (socklen_t *)&clilen);
        process_request(newsockfd, n);
    }

    return 0;
}

void process_request(int newsockfd, int n) {
    pid_t pid;
    if ((pid = fork()) == 0) {
        if (newsockfd < 0) {
            cout << "ERROR on accept" << endl;
            _exit(0);
        }
        int request;
        n = read(newsockfd, &request, sizeof(request));

        if (n < 0) {
            cout << "ERROR reading from socket" << endl;
            _exit(0);
        }
        request = ntohl(request);

        const char* fibonacci_code = get_fibonacci_code(request);
        n = write(newsockfd, fibonacci_code, sizeof(fibonacci_code));
        if (n < 0) {
            cout << "ERROR writing to socket" << endl;
            _exit(0);
        }
        _exit(0);
    }
}

void verify_args(int argc) {
    if (argc < 2) {
        cout <<"ERROR, no port provided" << endl;
        exit(1);
    }
}

const char* get_fibonacci_code(int rank) {
    vector<int> fibonacci_series = generate_fibonacci_series(rank);

    string fibonacci_code_builder = "1";
    int curr_idx = fibonacci_series.size() - 1;
    while (curr_idx > 1)
    {
        if (rank > 0 && fibonacci_series[curr_idx] <= rank)
        {
            rank -= fibonacci_series[curr_idx];
            fibonacci_code_builder = "1" + fibonacci_code_builder;
        }
        else
        {
            fibonacci_code_builder = "0" + fibonacci_code_builder;
        }
        curr_idx--;
    }

    return fibonacci_code_builder.c_str();
}

vector<int> generate_fibonacci_series(int max) {
    vector<int> fibonacci_series({0, 1});
    int first = 0;
    int second = 1;
    while (fibonacci_series[first] + fibonacci_series[second] <= max)
    {
        fibonacci_series.push_back(fibonacci_series[first] + fibonacci_series[second]);
        first++;
        second++;
    }
    return fibonacci_series;
}

void fireman(int a) {
    while (waitpid(-1, NULL, WNOHANG) > 0) {}
}