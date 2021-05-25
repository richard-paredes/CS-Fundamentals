#pragma once
#include <string>

class Ticket
{

private:
    int priority;
    std::string clientType;

public:
    static int ticketNumberAdmin, ticketNumberStudent, ticketNumberFaculty;
    int _ticketNumberAdmin, _ticketNumberStudent, _ticketNumberFaculty;
    Ticket();
    Ticket(int _client_type);

    int getPriority();
    void setPriority(int);
    std::string getClientType();
};
