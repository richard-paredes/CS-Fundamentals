/*******************************************************
 * Homework 2: OpenGL                                  *
 *-----------------------------------------------------*
 * First, you should fill in problem1(), problem2(),   *
 * and problem3() as instructed in the written part of *
 * the problem set.  Then, express your creativity     *
 * with problem4()!                                    *
 *                                                     *
 * Note: you will only need to add/modify code where   *
 * it says "TODO".                                     *
 *                                                     *
 * The left mouse button rotates, the right mouse      *
 * button zooms, and the keyboard controls which       *
 * problem to display.                                 *
 *                                                     *
 * For Linux/OS X:                                     *
 * To compile your program, just type "make" at the    *
 * command line.  Typing "make clean" will remove all  *
 * computer-generated files.  Run by typing "./hw2"    *
 *                                                     *
 * For Visual Studio:                                  *
 * You can create a project with this main.cpp and     *
 * build and run the executable as you normally would. *
 *******************************************************/

#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>

#if __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

using namespace std;

bool leftDown = false, rightDown = false;
int lastPos[2];
float cameraPos[4] = { 0,1,4,1 };
int windowWidth = 640, windowHeight = 480;
double yRot = 0;
int curProblem = 1; // TODO: change this number to try different examples

float specular[] = { 1.0, 1.0, 1.0, 1.0 };
float shininess[] = { 50.0 };

void problem1() {
	// TODO: Your code here!
	for (int i = 0; i < 10; i++) 
	{
		glPushMatrix();
		glRotatef(36*i, 0, 0, i);
		glTranslatef(1, 0, 0);
		glutSolidTeapot(0.2);
		glPopMatrix();
	}
}

void problem2() {
	// TODO: Your code here!
	for (int i = 0; i < 15; i++)
	{
		glPushMatrix();
		glTranslatef(-2.125 + (i * 0.25), 0.125, 0);
		for (int j = 0; j < i; j++) 
		{
			glPushMatrix();
			glTranslatef(0, 0.004*j*i, 0);
			glutSolidCube(0.25);
			glPopMatrix();
		}
		glPopMatrix();
	}
}

void problem3() {
	// TODO: Your code here!
	for (int i = 0; i < 7; i++)
	{
		glPushMatrix();
		glTranslatef(-0.5*i + 0.5, 1.5 - 0.5*i, 0);
		for (int j = 0; j < i; j++)
		{
			glPushMatrix();
			glTranslatef(j, 0, 0);
			glutSolidTeapot(0.2);
			glPopMatrix();
		}
		glPopMatrix();
	}
}

void problem4() {
	// TODO: Your code here!
	glPushMatrix();
	
	glBegin(GL_TRIANGLES);
		glColor3f(1, 1, 1); glVertex3f(-0.25, 0.75, 0);
		glColor3f(1, 0, 1); glVertex3f(0, 1.25, 0);
		glColor3f(1, 1, 1); glVertex3f(0.25, 0.75, 0);
	glEnd();
	glBegin(GL_TRIANGLES);
		glColor3f(1, 1, 1); glVertex3f(-0.5, 0.25, 0);
		glColor3f(1, 0, 1); glVertex3f(-0.25, 0.75, 0);
		glColor3f(1, 1, 1); glVertex3f(0, 0.25, 0);
	glEnd();
	glBegin(GL_TRIANGLES);
		glColor3f(1, 1, 1); glVertex3f(0, 0.25, 0);
		glColor3f(1, 0, 1); glVertex3f(0.25, 0.75, 0);
		glColor3f(1, 1, 1); glVertex3f(0.5, 0.25, 0);
	glEnd();
	glRotatef(-60, 1, 0, 0);
	glTranslatef(0, -0.5, 0);

	glPushMatrix(); 
	// palm
	glRotatef(-20, 1, 0, 0);
	glTranslatef(0, 0.25, 0);
	glScalef(0.5, 0.5, 0.1);
	glutSolidCube(1);
		
	// thumb
	glPushMatrix(); 
	glRotatef(-30, 0, 0, 1);
	glTranslatef(-0.5, -0.5, 0);
	glScalef(0.5, 0.3, 1);
	glutSolidCube(1);
	glPushMatrix();
	glRotatef(-20, 0, 0, 1);
	glTranslatef(-0.6, 0, 0);
	glScalef(0.5, 1, 1);
	glutSolidCube(1);
	glPopMatrix();
	glPopMatrix();

	// index
	glPushMatrix(); 
	glScalef(2, 2, 10);
	glRotatef(5, 1, 0, 0);
	glScalef(0.5, 0.5, 0.1);
	glTranslatef(-0.4, 0.75, 0);
	glScalef(0.2, 0.5, 1);
	glutSolidCube(1);
	glPushMatrix();
	glScalef(5, 2, 1);
	glTranslatef(0.4, -0.75, 0);
	glScalef(2, 2, 10);
	glRotatef(10, 1, 0, 0);
	glTranslatef(-0.4, 0.75, 0);
	glScalef(0.2, 0.5, 1);
	glScalef(0.5, 0.5, 0.1);
	glTranslatef(2, -0.5, -1);
	glutSolidCube(1);
	glPushMatrix();
	glScalef(1, 0.75, 1);
	glTranslatef(0, 0.5, 0);
	glutSolidCube(1);
	glPopMatrix();
	glPopMatrix();
	glPopMatrix();

	// middle
	glPushMatrix(); 
	glScalef(2, 2, 10);
	glRotatef(5, 1, 0, 0);
	glScalef(0.5, 0.5, 0.1);
	glTranslatef(-0.125, 0.75, 0);
	glScalef(0.2, 1, 1);
	glutSolidCube(1);
	glPushMatrix();
	glScalef(5, 1, 1);
	glTranslatef(0., -0.75, 0);
	glScalef(2, 2, 10);
	glRotatef(10, 1, 0, 0);
	glTranslatef(-0.1, 0.75, 0);
	glScalef(0.2, 1, 1);
	glScalef(0.5, 0.5, 0.1);
	glTranslatef(1, -0.5, -1);
	glutSolidCube(1);
	glPushMatrix();
	glScalef(1, 0.75, 1);
	glTranslatef(0, 0.5, 0);
	glutSolidCube(1);
	glPopMatrix();
	glPopMatrix();
	glPopMatrix();

	// ring
	glPushMatrix(); 
	glScalef(2, 2, 10);
	glRotatef(5, 1, 0, 0);
	glScalef(0.5, 0.5, 0.1);
	glTranslatef(0.1, 0.75, 0);
	glScalef(0.2, 0.5, 1);
	glutSolidCube(1);
	glPushMatrix();
	glScalef(5, 2, 1);
	glTranslatef(0., -0.75, 0);
	glScalef(2, 2, 10);
	glRotatef(10, 1, 0, 0);
	glTranslatef(-0.1, 0.75, 0);
	glScalef(0.2, 0.5, 1);
	glScalef(0.5, 0.5, 0.1);
	glTranslatef(1, -0.5, -1);
	glutSolidCube(1);
	glPushMatrix();
	glScalef(1, 0.75, 1);
	glTranslatef(0, 0.5, 0);
	glutSolidCube(1);
	glPopMatrix();
	glPopMatrix();
	glPopMatrix();

	// pinky
	glPushMatrix(); 
	glScalef(2, 2, 10);
	glRotatef(5, 1, 0, 0);
	glScalef(0.5, 0.5, 0.1);
	glTranslatef(0.4, 0.65, 0);
	glScalef(0.2, 0.35, 1);
	glutSolidCube(1);
	glPushMatrix();
	glScalef(5, 3.33, 1);
	glTranslatef(0., -1, 0);
	glScalef(2, 2, 10);
	glRotatef(10, 1, 0, 0);
	glTranslatef(-0.1, 0.75, 0);
	glScalef(0.2, 0.35, 1);
	glScalef(0.5, 0.5, 0.1);
	glTranslatef(1, -0.5, -1);
	glutSolidCube(1);
	glPushMatrix();
	glScalef(1, 0.75, 1);
	glTranslatef(0, 0.5, 0);
	glutSolidCube(1);
	glPopMatrix();
	glPopMatrix();
	glPopMatrix();
	glPopMatrix();

	glPopMatrix();
}

void problem5() {
	glPushMatrix();
	glTranslatef(2.0, 0.0, 0.0);
	glScalef(2.0, 1.0, 1.0);
	glutSolidSphere(1.0, 10, 10);
	glPopMatrix();
}

void display() {
	glClearColor(0, 0, 0, 0);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	glDisable(GL_LIGHTING);
	glEnable(GL_DEPTH_TEST);
	glBegin(GL_LINES);
	glColor3f(1, 0, 0); glVertex3f(0, 0, 0); glVertex3f(1, 0, 0); // x axis
	glColor3f(0, 1, 0); glVertex3f(0, 0, 0); glVertex3f(0, 1, 0); // y axis
	glColor3f(0, 0, 1); glVertex3f(0, 0, 0); glVertex3f(0, 0, 1); // z axis
	glEnd(/*GL_LINES*/);

	glEnable(GL_LIGHTING);
	glShadeModel(GL_SMOOTH);
	glMaterialfv(GL_FRONT, GL_SPECULAR, specular);
	glMaterialfv(GL_FRONT, GL_SHININESS, shininess);
	glEnable(GL_LIGHT0);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glViewport(0, 0, windowWidth, windowHeight);

	float ratio = (float)windowWidth / (float)windowHeight;
	gluPerspective(50, ratio, 1, 1000);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	gluLookAt(cameraPos[0], cameraPos[1], cameraPos[2], 0, 0, 0, 0, 1, 0);

	glLightfv(GL_LIGHT0, GL_POSITION, cameraPos);

	glRotatef(yRot, 0, 1, 0);

	if (curProblem == 1) problem1();
	if (curProblem == 2) problem2();
	if (curProblem == 3) problem3();
	if (curProblem == 4) problem4();
	if (curProblem == 5) problem5();

	glutSwapBuffers();
}

void mouse(int button, int state, int x, int y) {
	if (button == GLUT_LEFT_BUTTON) leftDown = (state == GLUT_DOWN);
	else if (button == GLUT_RIGHT_BUTTON) rightDown = (state == GLUT_DOWN);

	lastPos[0] = x;
	lastPos[1] = y;
}

void mouseMoved(int x, int y) {
	if (leftDown) yRot += (x - lastPos[0]) * .1;
	if (rightDown) {
		for (int i = 0; i < 3; i++)
			cameraPos[i] *= pow(1.1, (y - lastPos[1]) * .1);
	}


	lastPos[0] = x;
	lastPos[1] = y;
	glutPostRedisplay();
}

void keyboard(unsigned char key, int x, int y) {
	curProblem = key - '0';
	if (key == 'q' || key == 'Q' || key == 27) {
		exit(0);
	}
	glutPostRedisplay();
}

void reshape(int width, int height) {
	windowWidth = width;
	windowHeight = height;
	glutPostRedisplay();
}

int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(windowWidth, windowHeight);
	glutCreateWindow("HW2");

	glutDisplayFunc(display);
	glutMotionFunc(mouseMoved);
	glutMouseFunc(mouse);
	glutReshapeFunc(reshape);
	glutKeyboardFunc(keyboard);

	glutMainLoop();

	return 0;
}
