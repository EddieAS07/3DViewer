# Window

## Goals

### What will this feature do?
- It will handle the window of the application and will contain a menu and a renderer.

### How does it add to your program as a whole?
- It is the basis of the graphical interface shown to the user.
- For the above reason, it is essential to the program.

---

## Planning

### User

#### How will your user experience this feature?
- When the application is opened, the user will see the window pop up.
- The user will be able to move it around and interact with widgets inside of it.
- When the user closes the window, the application will end.

#### Describe how the feature will work.
- The window is a draggable element on the screen that houses a menu and a 3D scene.
- The menu contains other menus that help the user perform actions such as opening a file.
- The 3D scene is a display used by APIs to render the 3D model onto the screen.

### Developer

#### How will this feature be implemented?
- A window class will be created that implements a window interface.
- The interface houses code to create and run a window.
- Multiple windowing APIs can implement the window interface, allowing for cross-platform code.

#### How will it fit in with the rest of the project?
- The window class will accept parameters from its constructor that it will use inside of its code.
    - For example, it can take a renderer class and use it to display an image on the screen.

#### How will you test this feature?
- A mock class will be written that implements an interface for a class used by the real implementation.
- The mock can be used to check if it is called within the window class with the correct parameters.

---

## Deadlines

### How long do you think you (or someone else) will need in order to implement this feature?
- *Description here*

**Note: estimates are always inaccurate. As the feature is worked on, you will probably have a better idea of how much time it will need for it to be implemented.**