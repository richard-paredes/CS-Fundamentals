/*
 * C++ Program to Implement Hash Tables chaining 
 * with Singly Linked Lists
 */
#include <iostream>
#include <cstdlib>
#include <string>
#include <cstdio>
using namespace std;
const int TABLE_SIZE = 128;

/*
 * HashNode Class Declaration
 */
class HashNode
{
public:
    int key;
    int value;
    HashNode *next;
    HashNode(int key, int value)
    {
        this->key = key;
        this->value = value;
        this->next = NULL;
    }
};

/*
 * HashMap Class Declaration
 */
class HashMap
{
private:
    HashNode **htable;

public:
    HashMap()
    {
        // initialize htable as an array of pointers to HashNode
        // of TABLE_SIZE. All pointers should be null.
        htable = new HashNode *[TABLE_SIZE];
        for (int i = 0; i < TABLE_SIZE; i++)
        {
            htable[i] = NULL;
        }
    }

    ~HashMap()
    {
        //delete the hash table
        for (int i = 0; i < TABLE_SIZE; i++)
        {
            HashNode *curr = htable[i];
            HashNode *temp = NULL;
            while (curr != NULL)
            {
                temp = curr;
                curr = curr->next;
                delete temp;
            }
        }
        delete[] htable;
    }
    /*
         * Hash Function
         */
    int HashFunc(int key)
    {
        //complete hash function (module)
        return key % TABLE_SIZE;
    }

    /*
         * Insert Element at a key
         */
    void Insert(int key, int value)
    {
        //Complete insertion of value in chain at index = key
        int hashKey = HashFunc(key);
        int pos = 0;
        HashNode *node = new HashNode(key, value);
        HashNode *curr = htable[hashKey];
        // initialize an empty chain
        if (curr == NULL)
        {
            htable[hashKey] = node;
        }
        // add to the chain
        else
        {
            pos++;
            while (curr->next != NULL)
            {
                curr = curr->next;
                pos++;
            }
            curr->next = node;
        }
        cout << "ADDED " << node->key << ": " << node->value << " AT LOCATION - [" << hashKey << "].[" << pos << "]" << endl;
    }
    /*
         * Remove Element at a key
         */
    void Remove(int key)
    {
        //delete last element in chain at index = key
        int hashKey = HashFunc(key);
        HashNode *curr = htable[hashKey];
        if (curr == NULL)
        {
            cout << "No Element found at key " << key << endl;
        }
        else
        {
            HashNode *prev = NULL;
            while (curr->next != NULL)
            {
                prev = curr;
                curr = curr->next;
            }
            delete curr;
            if (prev == NULL) // only one node was at the hashkey location
            {
                htable[hashKey] = NULL;
            }
            else
            {
                prev->next = NULL;
            }
            cout << "Element Deleted" << endl;
        }
    }
    /*
         * Search Element at a key
         */
    int Search(int key)
    {
        //Print all elements at index = key
        int hashKey = HashFunc(key);

        HashNode *curr = htable[hashKey];
        if (curr == NULL)
        {
            return -1;
        }
        else
        {
            while (curr != NULL)
            {
                if (curr->key == key)
                {
                    cout << curr->value << " ";
                }
                curr = curr->next;
            }
            return 0;
        }
    }
};