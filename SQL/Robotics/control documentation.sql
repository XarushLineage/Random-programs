Title: Robot Movement Control

Description: design and implement a program that controls the movement of a simulated robot in a 2D grid. The robot can move forward, backward, turn left, turn right, and stop. The program will take commands from the user and display the current position and direction of the robot.

Requirements:

    Design a data structure that represents the state of the robot, including its position, direction, and whether it is moving or stopped. You can use a record or a tuple to store this information.

    Write functions that allow the user to control the movement of the robot. The functions should take a command as input and update the state of the robot accordingly. The following commands should be supported:
        Forward: Move the robot one unit forward in the current direction.
        Backward: Move the robot one unit backward in the current direction.
        TurnLeft: Turn the robot 90 degrees to the left.
        TurnRight: Turn the robot 90 degrees to the right.
        Stop: Stop the robot from moving.

    Write a function that displays the current state of the robot, including its position, direction, and whether it is moving or stopped.

    Implement a simple user interface that allows the user to enter commands and displays the current state of the robot. You can use the getLine function to read input from the user and the putStrLn function to display output to the console.

    Add error handling to your program to handle invalid commands or movements that would cause the robot to go out of bounds of the 2D grid. If an error occurs, display an error message and do not update the state of the robot.

    Test your program with different input scenarios, such as moving the robot in a straight line, making turns, and stopping and starting the robot. Ensure that the program handles all possible errors and produces the correct output.
