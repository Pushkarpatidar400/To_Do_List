# To-Do List Manager
A simple To-Do List Manager where users can add tasks, mark them as completed, and delete them. The user also has the option to view tasks filtered by their completion and non completion status using python with Flask Framework which is running on server http://127.0.0.1:5000/ .

Functionalities :-
1. Enable users to add new tasks with a description and due date.
   
   ![image](https://github.com/Pushkarpatidar400/To_Do_List/assets/118051799/61b54508-2f39-44a1-af84-6e1d0ef46cca)

2. Allow tasks to be marked as 'completed'.
   Here is the list of all my uncompleted task , if i click on "mark as Completed" task will shift to "completed task".
   
   ![image](https://github.com/Pushkarpatidar400/To_Do_List/assets/118051799/ba06b889-a10e-4474-aa6e-13e719911646)

   Now In completed Task section
   
   ![image](https://github.com/Pushkarpatidar400/To_Do_List/assets/118051799/b82a3b6b-853c-4756-8c03-0005244c062c)

4. Provide an option to delete tasks.
   Here I have a option for deleting a Task if I click on that the task will be deleted.
   
   ![image](https://github.com/Pushkarpatidar400/To_Do_List/assets/118051799/ae452bc9-1b18-4bee-bc5a-a4f76dc75e23)

   After Deleting :
   
   ![image](https://github.com/Pushkarpatidar400/To_Do_List/assets/118051799/969cc3fc-3346-4564-8006-c2cfcc411e30)
   
6. Implement the ability to view tasks, either all at once or filtered by 'completed' or 'pending'
   Completed Task :
   ![image](https://github.com/Pushkarpatidar400/To_Do_List/assets/118051799/a56036ff-35a2-420e-ba06-438c55df5e13)

   Pending Task:
   ![image](https://github.com/Pushkarpatidar400/To_Do_List/assets/118051799/87c56ab6-f403-4a78-90fe-1ea1923970ba)

Prerequisites:-
* Python 3.6 or higher

**Usage :-**

Run the main script:
Command :- python app.py

Use the following option in UI to interact with the To-Do List Manager:

add_task: Add a new task. Example: Add Task: "Buy groceries, Due: 2023-09-20"
![image](https://github.com/Pushkarpatidar400/To_Do_List/assets/118051799/5b9f5823-e5cf-4cc3-9a36-62b57e98dd34)

mark_completed: Mark a task as completed. Example: Mark Completed: "Buy groceries"
![image](https://github.com/Pushkarpatidar400/To_Do_List/assets/118051799/59ca298f-c327-4906-b90b-3b84e302779a)

view_tasks: View tasks. Options: "Show completed", "Show Not Completed"
undo: Undo the last action.
![image](https://github.com/Pushkarpatidar400/To_Do_List/assets/118051799/5b9f5823-e5cf-4cc3-9a36-62b57e98dd34)

redo: Redo the last undone action.
![image](https://github.com/Pushkarpatidar400/To_Do_List/assets/118051799/59ca298f-c327-4906-b90b-3b84e302779a)
quit: Quit the application.


**Design Patterns**:

Memento Pattern: Implemented to enable undo and redo actions.
Builder Pattern: Used for constructing tasks with optional attributes like due date.









