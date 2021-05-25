#include <iostream>
#include "LinkedList.h"

template <typename T>
LinkedList<T>::LinkedList()
{
    head = NULL;
    tail = NULL;
    count = 0;
}

template <typename T>
void LinkedList<T>::append(const T &data)
{
    Node<T> *node = new Node<T>;
    node->data = data;
    node->next = NULL;

    if (head == NULL)
    {
        head = node;
        tail = node;
        count++;
    }
    else
    {
        tail->next = node;
        tail = node;
        count++;
    }
}

template <typename T>
void LinkedList<T>::prepend(const T &data)
{
    Node<T> *node = new Node<T>;
    node->data = data;
    node->next = head;
    head = node;
    if (tail == NULL)
        tail = node;
}

template <typename T>
void LinkedList<T>::remove(const T &data)
{
    Node<T> *prev = NULL;
    Node<T> *current = head;

    while (current != NULL)
    {
        if (current->data == data)
            break;
        prev = current;
        current = current->next;
    }

    if (current == head) // remove head
    {
        head == (count > 0) ? current->next : NULL;
        delete current;
        count--;
    }
    else if (current == tail) // remove tail
    {
        tail = prev;
        delete current;
        count--;
    }
    else if (current != NULL) // remove in between
    {
        prev->next = current->next;
        delete current;
        count--;
    }
}

template <typename T>
void LinkedList<T>::clear()
{
    Node<T> *current;
    while (head != NULL)
    {
        current = head;
        head = head->next;
        delete current;
    }
    tail = NULL;
    count = 0;
}

template <typename T>
void LinkedList<T>::print() const
{
    Node<T> *current = head;
    while (current != NULL)
    {
        std::cout << current->data << " ";
        current = current->next;
    }
}

// https://bytefreaks.net/programming-2/c/c-undefined-reference-to-templated-class-function#:~:text=cpp%20)%20files%2C%20if%20you%20compile,reference%20to%20error%20at%20linking.&text=The%20code%20in%20the%20template,that%20are%20needed%20by%20main.
