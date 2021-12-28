# 3D Viewer
## Project contributors
- Eddie Soto

## Goals

### Project Goals
1. To design a program that can render a 3D model.
2. To learn about different OS's windowing APIs.
3. To learn about different OS's graphics APIs.

### Recipients
- Eddie Soto (me)

---

## Planning

### Features (Minimum Valuable Product)
- Window that renders an .obj file
- Menu to open an .obj file
- Keyboard shortcuts to move around the model
- Move mouse to move the camera around

### User

#### User Experience
- When the application is opened, the user will see a blank scene with no model being rendered.
- The user will go to the menu and select Open > Load model.
- A file select dialog will prompt the user to open a .obj file.
- When the model is selected, the window will reload and show the model.
- The user can use either WASD or the arrow keys to move around the model.
- The user can move the mouse to rotate the camera and see the model from another perspective. 

### Developer

#### Tools:
- The C++ Programming Language
    - MSVC compiler
- WinAPI
- OpenGL
    - Versions 3 and up (no immediate mode)

#### Outline of implementation
- A window class will  display a window on the screen using the OS's window API.
    - A menu class will put a menu on the OS's screen.
    - An input class will handle keyboard inputs and signal other classes accordingly.
- A renderer class will contain the code to render graphics on the screen.
    - A shader class will contain the code to apply transformations to vertices and fragments.
    - A camera class will move the scene around in response to movements.
    - A model loader class will read a model and get its data.
- A file class will contain the code to read and write to files.
- A logger class will log debug information about the program to a file.

---

## Deadlines

### Duration: About **2-3 months** to implement everything correctly.

#### **Obviously, projects will never, ever, go 100% according to plan, because life just gets in the way.**

### Feature duration:
- Window: 3-6 weeks
- Menu: 1-2 weeks
- Model: 2-4 weeks
- Keyboard shortcuts: 2-4 weeks
- Mouse: 2-4 weeks

#### **Note: your estimates will probably be highly inaccurate. As you work on the features, you can refine the time needed here as you gain more experience on what you are working on.**
