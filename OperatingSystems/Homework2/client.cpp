// Please note this is a C program
// It compiles without warnings with gcc
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <pthread.h>
#include <unordered_map>
#include <fstream>

using namespace std;

struct SymbolFrequency {
    char symbol;
    int frequency;
};

struct Input {
    int numSymbols;
    vector<SymbolFrequency> symbolFrequencies;
    string compressedFileName;
};

struct ThreadRequestArgs {
    char symbol;
    int frequency;
    int request;
    int port;
    char* hostname;
    unordered_map<string, char> *fibonacci_codes;
};

Input process_input();
bool sort_by_frequency_desc(SymbolFrequency a, SymbolFrequency b);
void verify_args(int argc, char *const *argv);
void* send_request(void* ptr);
void decompress_file(string filename, unordered_map<string, char> &fibonacci_codes);
void send_multi_threaded_requests(char *const *argv, const Input &input, unordered_map<string, char> &fibonacci_codes, vector<ThreadRequestArgs> &threadArgs);

int main(int argc, char *argv[])
{
    verify_args(argc, argv);
    Input input = process_input();
    sort(input.symbolFrequencies.begin(), input.symbolFrequencies.end(), sort_by_frequency_desc);
    static unordered_map<string, char> fibonacci_codes;
    static vector<ThreadRequestArgs> threadArgs = vector<ThreadRequestArgs>(input.numSymbols);
    send_multi_threaded_requests(argv, input, fibonacci_codes, threadArgs);
    decompress_file(input.compressedFileName, fibonacci_codes);
    return 0;
}

void verify_args(int argc, char *const *argv) {
    if (argc < 3) {
        cout << "usage " << argv[0] << " hostname port\n";
        exit(0);
    }
}
Input process_input() {
    Input input;

    string line;

    getline(cin, line);
    input.numSymbols = stoi(line);
    input.symbolFrequencies.resize(input.numSymbols);
    for (int i = 0; i < input.numSymbols; i++) {
        getline(cin, line);
        input.symbolFrequencies[i].symbol = line[0];
        input.symbolFrequencies[i].frequency = stoi(line.substr(2));
    }
    getline(cin, input.compressedFileName);

    return input;
}
bool sort_by_frequency_desc(SymbolFrequency a, SymbolFrequency b) {
    if (a.frequency == b.frequency)
        return a.symbol > b.symbol;
    return a.frequency > b.frequency;
}
void send_multi_threaded_requests(char *const *argv, const Input &input, unordered_map<string, char> &fibonacci_codes, vector<ThreadRequestArgs> &threadArgs) {
    pthread_t *tid = new pthread_t[input.numSymbols];
    for (int i = 0; i < input.numSymbols; i++) {
        threadArgs[i].hostname = argv[1];
        threadArgs[i].port = stoi(argv[2]);
        threadArgs[i].request = i + 1;
        threadArgs[i].fibonacci_codes = &fibonacci_codes;
        threadArgs[i].frequency = input.symbolFrequencies[i].frequency;
        threadArgs[i].symbol = input.symbolFrequencies[i].symbol;
        pthread_create(&tid[i], NULL, send_request, (void *) &threadArgs[i]);
    }
    for (int i = 0; i < input.numSymbols; i++) {
        pthread_join(tid[i], NULL);
    }
    delete [] tid;
}
void* send_request(void *ptr) {
    ThreadRequestArgs* threadArgs = (ThreadRequestArgs *) ptr;

    int sockfd, portno, n;
    sockaddr_in serv_addr;
    hostent *server;

    portno = threadArgs->port;
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        cout <<"ERROR opening socket" << endl;
        return NULL;
    }

    server = gethostbyname(threadArgs->hostname);
    if (server == NULL) {
        cout << "ERROR, no such host" << endl;
        return NULL;
    }

    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr, (char *)&serv_addr.sin_addr.s_addr, server->h_length);
    serv_addr.sin_port = htons(portno);

    if (connect(sockfd,(sockaddr *)&serv_addr,sizeof(serv_addr)) < 0) {
        cout << "ERROR connecting" << endl;
        return NULL;
    }

    int request = htonl(threadArgs->request);
    n = write(sockfd, &request, sizeof(request));
    if (n < 0) {
        cout <<"ERROR writing to socket" << endl;
        return NULL;
    }

    char buffer[256];
    bzero(buffer,256);
    n = read(sockfd,buffer,255);
    if (n < 0) {
        cout << "ERROR reading from socket" << endl;
        return NULL;
    }

    threadArgs->fibonacci_codes->insert(make_pair(buffer, threadArgs->symbol));
    return NULL;
}
void decompress_file(string filename, unordered_map<string, char> &fibonacci_codes) {
    ifstream compressed_file(filename);

    if (compressed_file.is_open()) {
        string compressed_message;
        getline(compressed_file, compressed_message);

        string decompressed_message, current_code;
        int start, current;
        unordered_map<string, char>::iterator key_value_pair;
        current = 1;
        while (start < compressed_message.size()) {
            current_code = compressed_message.substr(start, current - start + 1);
            key_value_pair = fibonacci_codes.find(current_code);
            if (key_value_pair != fibonacci_codes.end()) {
                decompressed_message += key_value_pair->second;
                current++;
                start = current;
            }
            current++;
        }
        cout << "Decompressed message = " << decompressed_message << endl;
    } else {
        cout << "Failed to open file." << endl;
    }
}
