#include "FibonacciCoder.h"
#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <pthread.h>
#include <unistd.h>
#include <bits/stdc++.h>

using namespace std;

struct SymbolFrequency {
    char symbol;
    int frequency = 0;
    string code;
};

struct InputArgs {
    static string search_string;    
    static string alphabet;
};
struct FibonacciCodes {
    static vector<SymbolFrequency> symbols;
};
struct ThreadedFrequencyArgs {
    char symbol;
    int index;
};
struct ThreadedCodeArgs {
    int rank;
    int index;
};

string InputArgs::alphabet;
string InputArgs::search_string;
vector<SymbolFrequency> FibonacciCodes::symbols;

void process_input();
bool sort_by_frequency_desc(SymbolFrequency a, SymbolFrequency b);
bool sort_by_symbol_asc(SymbolFrequency a, SymbolFrequency b);
int calculate_symbol_frequency(char symbol);
vector<int> generate_fibonacci_series(int max);
void* get_symbol_code(void *arguments);
void* get_symbol_frequency(void *arguments);
void set_symbol_frequencies();
void set_symbol_codes();
void print_symbol_codes();

int main(int argc, char const *argv[])
{
    process_input();
    set_symbol_frequencies();    
    sort(FibonacciCodes::symbols.begin(),  FibonacciCodes::symbols.end(), sort_by_frequency_desc);
    set_symbol_codes();
    sort(FibonacciCodes::symbols.begin(), FibonacciCodes::symbols.end(), sort_by_symbol_asc);
    print_symbol_codes();

    return 0;
}

void process_input()
{
    string file_name;
    cin >> InputArgs::alphabet;
    cin >> file_name;
    ifstream input_stream(file_name);
    getline(input_stream, InputArgs::search_string);
    // FibonacciCodes::symbols = new SymbolFrequency[InputArgs::alphabet.size()];
    FibonacciCodes::symbols.resize(InputArgs::alphabet.size());
}

bool sort_by_frequency_desc(SymbolFrequency a, SymbolFrequency b)
{
    if (a.frequency == b.frequency) {
        return a.symbol > b.symbol;
    }
    return a.frequency > b.frequency;
}

bool sort_by_symbol_asc(SymbolFrequency a, SymbolFrequency b)
{
    return a.symbol < b.symbol;
}

vector<int> generate_fibonacci_series(int max)
{
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

int calculate_symbol_frequency(char symbol)
{
    int frequency = 0;
    for (int i = 0; i < InputArgs::search_string.length(); i++) {
       if (InputArgs::search_string[i] == symbol) frequency += 1;
    }
    return frequency;
}

void* get_symbol_frequency(void *arguments)
{
    ThreadedFrequencyArgs *args = (ThreadedFrequencyArgs*) arguments;
    
    SymbolFrequency s_freq;
    s_freq.symbol = args->symbol;
    s_freq.frequency = calculate_symbol_frequency(args->symbol);
    
    FibonacciCodes::symbols[args->index] = s_freq;
    return NULL;
}

void set_symbol_frequencies()
{    
    pthread_t *tid = new pthread_t[InputArgs::alphabet.size()];
    ThreadedFrequencyArgs *args = new ThreadedFrequencyArgs[InputArgs::alphabet.size()];

    for (int i = 0; i < InputArgs::alphabet.size(); i++) 
    {
        args[i].symbol = InputArgs::alphabet[i];
        args[i].index = i;
        if (pthread_create(&tid[i], NULL, get_symbol_frequency, (void *)&args[i]))
        {
            cout << "Error creating thread to fetch symbol frequency" << endl;
            return;
        }
    }   
    
    for (int i = 0; i < InputArgs::alphabet.size(); i++) 
    {
        pthread_join(tid[i], NULL);
    }
}

void* get_symbol_code(void *arguments) 
{
    ThreadedCodeArgs *args = ((ThreadedCodeArgs*)arguments); // the index is the rank; adjust from 0-based
    vector<int> fibonacci_series = generate_fibonacci_series(args->rank);

    string fibonacci_code = "1";
    int curr_idx = fibonacci_series.size() - 1;
    while (curr_idx > 1) 
    {
        if (args->rank > 0 && fibonacci_series[curr_idx] <= args->rank) {
            args->rank -= fibonacci_series[curr_idx];
            fibonacci_code = "1" + fibonacci_code;
        } 
        else {
            fibonacci_code = "0" + fibonacci_code;
        }
        curr_idx--;
    }
    FibonacciCodes::symbols[(args->index)].code = fibonacci_code;
    return NULL;
}

void set_symbol_codes()
{
    pthread_t *tid = new pthread_t[InputArgs::alphabet.size()];
    ThreadedCodeArgs *args = new ThreadedCodeArgs[InputArgs::alphabet.size()];

    for (int i = 0; i < InputArgs::alphabet.size(); i++)
    {
        args[i].index = i;
        args[i].rank = i + 1;
        if (pthread_create(&tid[i], NULL, get_symbol_code, (void *)&args[i]))
        {
            cout << "Error creating thread to fetch Fibonacci code" << endl;
            return;
        }
    }

    for (int i = 0; i < InputArgs::alphabet.size(); i++)
    {
        pthread_join(tid[i], NULL);
    }
}

void print_symbol_codes()
{
    for (int i = 0; i < InputArgs::alphabet.size(); i++) 
    {
        cout << "Symbol: " << FibonacciCodes::symbols[i].symbol << ", Frequency: " << FibonacciCodes::symbols[i].frequency << ", Code: " << FibonacciCodes::symbols[i].code << endl;
    }
}
