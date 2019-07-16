#include <GL/gl.h>
#include <GL/glut.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Point{
	float x;
	float y;
}Point;

void putpixel(int x, int y) {
	glBegin(GL_POINTS);
		glVertex2f(round(x), round(y));
	glEnd();
	glFlush();
}

void drawCircle(int xc, int yc, int x, int y)
{ 
    putpixel(xc+x, yc+y); 
    putpixel(xc-x, yc+y);
    putpixel(xc+x, yc-y); 
    putpixel(xc-x, yc-y); 
    putpixel(xc+y, yc+x); 
    putpixel(xc-y, yc+x); 
    putpixel(xc+y, yc-x); 
    putpixel(xc-y, yc-x);
}

void circleBres(int xc, int yc, int r) 
{ 
    int x = xc, y = yc + r; 
    int d = 3 - 2*r;
    drawCircle(xc, yc, x, y);
    while (y >= x)
    {
    	x++;
    	
        if (d > 0) { 
            y--;
            d = d + 4 * (x - y) + 10; 
        } 
        else
            d = d + 4 * x + 6;
        drawCircle(xc, yc, x, y); 
    }
}

void display() {
	int r;

	printf("\nEnter radius of Outer Circle : ");
	scanf("%d", &r);
	
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0, 1.0, 1.0); // white
	
	circleBres(0,0,r);
	circleBres(0,0,r/2);
	circleBres(0,0,r/3);
	circleBres(2*r/3,0,r/3);
	circleBres((-2)*r/3,0,r/3);
	circleBres(r/3,r/sqrt(3),r/3);
	circleBres(r/3,(-r)/sqrt(3),r/3);
	circleBres(-r/3,r/sqrt(3),r/3);
	circleBres(-r/3,(-r)/sqrt(3),r/3);
}

int main(int argc, char* argv[]) {
   	glutInit(&argc, argv);   
   	glutInitDisplayMode(GLUT_RGB);          // Initialize GLUT
   	glutInitWindowSize(500, 500);   		// Set the window's initial width & height
	glutCreateWindow("Using GL Lines"); 	// Create a window with the given title
	glutInitWindowPosition(50, 50); 		// Position the window's initial top-left corner
	glClearColor(0.0, 0.0, 0.0, 0.0); 		// Set background color to black and opaque
	gluOrtho2D(-250,250,-250,250);			// Set X and Y Axes
    glutDisplayFunc(display); 				// Register display callback handler for window re-paint
    glutMainLoop();           				// Enter the event-processing loop
    return 0;
}
