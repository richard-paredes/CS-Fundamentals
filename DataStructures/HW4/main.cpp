#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <climits>
#include "Queue.h"

using namespace std;

struct PoliceVertex
{
	int x;
	int y;
	int traversals;
};
const char Wall = 'W';
const char Police = 'P';

queue<PoliceVertex> getPoliceVertices(char *input[], int *output[], const int num_of_rows, const int num_of_cols);
void calculatePolicePatrolPaths(char *input[], int *output[], queue<PoliceVertex> &policeVertices, const int num_of_rows, const int num_of_cols);
bool canPatrolLeft(char *input[], int *output[], PoliceVertex &police, const int num_of_rows);
bool canPatrolRight(char *input[], int *output[], PoliceVertex &police, const int num_of_rows);
bool canPatrolUp(char *input[], int *output[], PoliceVertex &police, const int num_of_cols);
bool canPatrolDown(char *input[], int *output[], PoliceVertex &police, const int num_of_cols);
bool finishPatrol(char *input[], int *output[], PoliceVertex &police);

void findShortestDistance(char *input[], int *output[], int num_of_rows, int num_of_cols)
{
	// You need to complete this function. You can add additional functions if you need
	// ALGORITHM:
	// 1. find i,j positions for each police (P) and load into a queue
	queue<PoliceVertex> policeVertices = getPoliceVertices(input, output, num_of_rows, num_of_cols);

	// 2. While queue is not empty need to go through and do a breadth-first search for the adjacent vertices for the ENTIRE map
	calculatePolicePatrolPaths(input, output, policeVertices, num_of_rows, num_of_cols);
}
bool loadGraph(std::string file_name, char ***input, int &num_of_rows, int &num_of_cols)
{

	ifstream f(file_name);

	if (f.fail())
	{
		std::cout << "Couldn't open the file: " << file_name << std::endl;
		return false;
	}
	//Read file into input and update num_of_rows and num_of_cols
	f >> num_of_rows >> num_of_cols;
	string line;
	char letter;
	getline(f, line);
	(*input) = new char *[num_of_rows];
	for (int i = 0; i < num_of_rows; i++)
	{
		(*input)[i] = new char[num_of_cols];
		getline(f, line);
		stringstream ss(line);
		for (int j = 0; j < num_of_cols; j++)
		{
			ss >> letter;
			(*input)[i][j] = letter;
		}
	}
	return true;
}

int main(int argc, char **argv)
{
	int num_of_rows, num_of_cols;
	string file_name = "input.txt";
	char **input_adj_matrix;

	loadGraph(file_name, &input_adj_matrix, num_of_rows, num_of_cols);

	std::cout << "The input adjacent matrix graph: " << std::endl;
	for (int i = 0; i < num_of_rows; i++)
	{
		for (int j = 0; j < num_of_cols; j++)
		{
			cout << std::setw(3) << input_adj_matrix[i][j];
		}
		cout << endl;
	}

	int **output_adj_matrix = new int *[num_of_rows];
	for (int i = 0; i < num_of_rows; i++)
	{
		output_adj_matrix[i] = new int[num_of_cols];
	}

	findShortestDistance(input_adj_matrix, output_adj_matrix, num_of_rows, num_of_cols);

	std::cout << "\nThe shortest way from each patrolman: " << std::endl;
	for (int i = 0; i < num_of_rows; i++)
	{
		for (int j = 0; j < num_of_cols; j++)
		{
			cout << std::setw(3) << output_adj_matrix[i][j];
		}
		cout << endl;
	}

	return 0;
}

// will contain queue that has positions of police vertices in matrix
queue<PoliceVertex> getPoliceVertices(char *input[], int *output[], const int num_of_rows, const int num_of_cols)
{
	const int maxPolice = num_of_rows * num_of_cols;
	queue<PoliceVertex> policeVertices(maxPolice);
	for (int i = 0; i < num_of_rows; i++)
	{
		for (int j = 0; j < num_of_cols; j++)
		{
			if (input[i][j] == Police)
			{
				output[i][j] = 0;
				PoliceVertex p;
				p.x = i;
				p.y = j;
				p.traversals = 0;
				policeVertices.enqueue(p);
			}
			else
			{
				output[i][j] = (input[i][j] == Wall) ? -1 : INT_MAX;
			}
		}
	}
	return policeVertices;
}

void calculatePolicePatrolPaths(char *input[], int *output[], queue<PoliceVertex> &policeVertices, const int num_of_rows, const int num_of_cols)
{
	while (!policeVertices.is_empty())
	{
		PoliceVertex lPolice = policeVertices.front();
		PoliceVertex rPolice = lPolice;
		PoliceVertex uPolice = lPolice;
		PoliceVertex dPolice = lPolice;
		policeVertices.dequeue();
		// cout << "Current vertex: " << lPolice.x << "," << lPolice.y << " | Traversed " << lPolice.traversals << endl;
		if (canPatrolLeft(input, output, lPolice, 0))
		{
			// cout << "Can go left." << endl;
			policeVertices.enqueue(lPolice);
		}
		if (canPatrolRight(input, output, rPolice, num_of_cols - 1))
		{
			// cout << "Can go right." << endl;
			policeVertices.enqueue(rPolice);
		}
		if (canPatrolUp(input, output, uPolice, 0))
		{
			// cout << "Can go up." << endl;
			policeVertices.enqueue(uPolice);
		}
		if (canPatrolDown(input, output, dPolice, num_of_rows - 1))
		{
			// cout << "Can go down." << endl;
			policeVertices.enqueue(dPolice);
		}
		// cout << endl;
	}
	// cout << "Done!" << endl;
}

bool canPatrolLeft(char *input[], int *output[], PoliceVertex &police, const int boundary)
{
	if (police.y == boundary)
		return false;
	else
	{
		police.y--;
		return finishPatrol(input, output, police);
	}
}
bool canPatrolRight(char *input[], int *output[], PoliceVertex &police, const int boundary)
{
	if (police.y == boundary)
		return false;
	else
	{
		police.y++;
		return finishPatrol(input, output, police);
	}
}
bool canPatrolUp(char *input[], int *output[], PoliceVertex &police, const int boundary)
{
	if (police.x == boundary)
		return false;
	else
	{
		police.x--;
		return finishPatrol(input, output, police);
	}
}
bool canPatrolDown(char *input[], int *output[], PoliceVertex &police, const int boundary)
{
	if (police.x == boundary)
		return false;
	else
	{
		police.x++;
		return finishPatrol(input, output, police);
	}
}

bool finishPatrol(char *input[], int *output[], PoliceVertex &police)
{
	police.traversals++;
	if (input[police.x][police.y] == Wall || police.traversals >= output[police.x][police.y])
	{
		return false;
	}
	else
	{
		output[police.x][police.y] = police.traversals;
		return true;
	}
}
