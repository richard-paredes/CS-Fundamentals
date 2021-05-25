/*******************************************************
 * Homework 1: Rasterization                           *
 *-----------------------------------------------------*
 * Here you will implement the circle rasterization    *
 * method decribed in the handout.                                           *
 * To compile this in linux:                           *
 *        g++ hw1.cpp                                  *
 * Then, run the program as follows:                   *
 *        ./a.out 200                                  *
 * to generate a 200x200 image containing a circular   *
 * arc.  Note that the coordinate system we're using   *
 * places pixel centers at integer coordinates and     *
 * has the origin at the lower left.                   *
 * Your code will generate a .ppm file containing the  *
 * final image. These images can be viewed using       *
 * "display" in Linux or Irfanview in Mac/Windows.     *
 *******************************************************/

#include <iostream>
#include <fstream>
#include <cstdio>
#include <cassert>
using namespace std;

// We'll store image info as globals; not great programming practice
// but ok for this short program.
int image_size;
bool **image;

void renderPixel(int x, int y)
{
    assert(x >= 0 && y >= 0 && x <= image_size && y <= image_size);
    image[x][y] = 1;
}

void rasterizeArc()
{
    int x, y, d, radius, deltaE, deltaSE;

    // Render the r = 150, y >= 0 semicircle
    radius = 150;
    deltaE = 3;
    deltaSE = -2 * radius + 5;
    x = image_size / 2;
    y = image_size / 2 + radius;
    d = 1 - radius;
    renderPixel(x, y);
    renderPixel(y, x);
    renderPixel(x, image_size - y);
    renderPixel(y, image_size - x);

    while (y > x)
    {
        if (d < 0)
        {
            d += deltaE;
            deltaE += 2;
            deltaSE += 2;
        }
        else
        {
            d += deltaSE;
            deltaE += 2;
            deltaSE += 4;
            y--;
        }
        x++;
        renderPixel(x, y);
        renderPixel(y, x);
        renderPixel(x, image_size - y);
        renderPixel(y, image_size - x);
    }

    // Render the r = 100, x >= 0 semicircle
    radius = 100;
    deltaE = 3;
    deltaSE = -2 * radius + 5;

    x = image_size / 2;
    y = image_size / 2 + radius;
    d = 1 - radius;
    renderPixel(x, y);
    renderPixel(y, x);
    renderPixel(image_size - y, x);
    renderPixel(image_size - x, y);

    while (y > x)
    {
        if (d < 0)
        {
            d += deltaE;
            deltaE += 2;
            deltaSE += 2;
        }
        else
        {
            d += deltaSE;
            deltaE += 2;
            deltaSE += 4;
            y--;
        }
        x++;
        renderPixel(x, y);
        renderPixel(y, x);
        renderPixel(image_size - y, x);
        renderPixel(image_size - x, y);
    }
}

// You shouldn't need to change anything below this point.

int main(int argc, char *argv[])
{
        if (argc != 2) {
        cout << "Usage: " << argv[0] << " circleSize\n";
        return 0;
    }

#ifdef _WIN32
    sscanf_s(argv[1], "%d", &image_size);
#else
    sscanf(argv[1], "%d", &image_size);
#endif
    if (image_size <= 0) {
        cout << "Image must be of positive size.\n";
        return 0;
    }
    // reserve image as 2d array
    image = new bool *[image_size + 1];
    for (int i = 0; i <= image_size; i++)
        image[i] = new bool[image_size + 1]{0};

    rasterizeArc();

    char filename[50];
#ifdef _WIN32
    sprintf_s(filename, 50, "circle.ppm");
#else
    sprintf(filename, "circle.ppm");
#endif

    ofstream outfile(filename);
    outfile << "P3\n# " << filename << "\n";
    outfile << image_size + 1 << ' ' << image_size + 1 << ' ' << 1 << endl;

    for (int i = 0; i <= image_size; i++)
        for (int j = 0; j <= image_size; j++)
            outfile << image[image_size - i][j] << " 0 0\n";

    // delete image data
    for (int i = 0; i <= image_size; i++)
        delete[] image[i];
    delete[] image;

    return 0;
}
