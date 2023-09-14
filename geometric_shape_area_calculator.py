#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    circle_pi = math.pi # DO NOT MODIFY, this line of code is assigning the variable 'circle_pi' equal to Pi ~3.14

    # TODO: In terminal, print Welcome to the geometric shape area calculator!
    print('Welcome to the grometric shape area calculator!')
    
    # User Options
    Circle = 1
    Rectangle = 2
    Triangle = 3
    
    # TODO: Using one print statement, use string concatenation to print the options only 
    # as a single string (make sure to add a space between each option)
    print(Circle + ' ' + Rectangle + ' ' + Triangle)

    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.
    choice = input('Select a shape by entering 1, 2, or 3')
    print(choice)


    # TODO: Convert the variable 'choice' to an integer data type.
    choice = int(choice)

    # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.  If converted correctly, the output in Terminal should read 'True'.
    print(type(choice))
    
  
    if choice == 1:  #DO NOT REMOVE THE 'IF'
        # Calculate the area of a circle

        # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
        radius = input('What is the radius of the circle?')
        # TODO: Convert 'radius' to float.
        radius = float(radius)
        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
        area = (circle_pi * (radius **  2)) 
        # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared.  
        # Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math.  

    elif choice == 2: # DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a rectangle
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        length = input('What is the length of the rectangle?')
        width = input('What is the length of the rectangle?')
        # TODO: Convert both 'length' and 'width' to float.
        length = float(length)
        width = float(width)
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        area = (length * width)
        # HINT: The formula to find the area of a rectangle: length times width

    elif choice == 3: #DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a triangle
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        base = input('What is the base length of the triangle?')
        height = input('What is the height of the triangle?')
        # TODO: Convert both 'base' and 'height' to float.
        base = float(base)
        height = float(height)
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        area = ((1/2) * (base * height))
        # HINT: The formula to find the area of a Triangle: half times base times height

    else:
        # TODO: If the user enters anything other than 1, 2 or 3, print statement "Invalid choice ."
        print('Invalid choice .')
    
    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific.
    print('First locate the after class section of the class date of the assignment: ex. w3d2\nThen click on the "Begin assignment" link to be taken to GitHub classroom\nThen click "Accept assignment" to generate your repo URL\nThen click your repo URL to be to your assignment repo URL homepage\nThen copy the URL located in the green "Code" button\nThen open your powershell\nThen cd into the correct folder that stores your class assignments\nThen type the command "git clone" and paste your URL after clone, being sure there is a space in between "clone" and your URL\nThen open VSCode\nThen use "File+Open Folder" to open your repo folder\nOnce your assignment is open in VSCode, locate the README file\nFollow all instructions on the README file\nOnce your code has passed the unittest, make sure to comment out all functions\nthen save your code and use "git add", "git commit", and "git push" to turn your assignment in to the github autograder\nOnce your repo gets the green checkmark, copy your repo URL and paste it into the assignment submission on Canvas.') 


if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY
