Task Manager DRF Project
Purpose:
Task Tracker API using DRF. The purpose is to provide a programmatic way to manage tasks, allowing for seamless integration with other tools or scripts.

How It Works:
The API is a set of URLs that we can interact with. It understands and responds to certain commands, like adding a new task, updating an existing task, or fetching a list of tasks, and deleting a task.

Adding a Task:
 We add tasks using a simple command line or script. For example:
curl -X POST http://127.0.0.1:8000/api/tasks/ -H "Content-Type: application/json" -d '{"title": "New Task", "description": "Description for the new task", "completed": false}'
 
  This command tells the API to create a new task with the specified details.

Updating a Task:
 To mark a task as completed, we use a similar command:
 
  curl -X PUT http://127.0.0.1:8000/api/tasks/<task_id>/ -H "Content-Type: application/json" -d '{"title": "Updated Task", "description": "Updated description", "completed": true}'
(Sometimes these commends might throw errors at time we should add \ before “. like \”title\”.)
  This command updates an existing task, changing its title, description, and completion status.
Deleting a Task:
 To Delete, we use a similar command:
curl -X DELETE "http://127.0.0.1:8000/api/tasks/<task_id>/"

The API provides a flexible way to manage tasks programmatically.
