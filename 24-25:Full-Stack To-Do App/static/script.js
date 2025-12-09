// JavaScript code that will fetch data from the API and manipulate the HTML page.

//The "Read" Functionality (Displaying Initial Tasks):
function loadTasks() {
    fetch('http://127.0.0.1:5000/tasks')
    .then(response => response.json())
    .then(tasks => {
        // Get a reference to <ul> element
        const taskListUl = document.getElementById("task-list");
        // Clear the list first in case you call this function multiple times
        taskListUl.innerHTML = ''; 
        // Loop through the array of task strings
        tasks.forEach(task => {
            // Create a new <li> element
            const li = document.createElement('li');
            // Set its text content to be the current task
            li.textContent = task;
            // Append the new <li> to the <ul>
            taskListUl.appendChild(li);
        });
    });
}

const addTaskButton = document.getElementById('add-task-btn');
const taskInput = document.getElementById('task-input');

function handleAddTaskClick() {
    // Get and validate the input
    const taskText = taskInput.value.trim();
    if (taskText === "") {
        return; 
    }

    const taskData = { task: taskText };
    const fetchOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(taskData) 
    };

    // 2. Make the fetch call
    fetch('http://127.0.0.1:5000/tasks', fetchOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);

            // Get a reference to the <ul> element.
            const taskList = document.getElementById('task-list');

            // Create a brand new, empty <li> element.
            const newListItem = document.createElement('li');

            // Set the text content of the new <li> to be our task text.
            newListItem.textContent = taskText;

            // Append the newly created <li> to the end of the <ul>.
            taskList.appendChild(newListItem);

        })
        .catch(error => {
            console.error('Error:', error);
        });

    // 3. Clear the input box
    taskInput.value = "";
}

addTaskButton.addEventListener('click', handleAddTaskClick);

// Finally, call this function when the page loads.
// The standard way to do this is to listen for the 'DOMContentLoaded' event.
document.addEventListener('DOMContentLoaded', loadTasks);