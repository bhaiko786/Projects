// Get elements
const taskInput = document.getElementById('task-input');
const addTaskBtn = document.getElementById('add-task-btn');
const taskList = document.getElementById('task-list');

// Load tasks from local storage
let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

// Function to add task
function addTask(taskName) {
    const task = {
        name: taskName,
        completed: false
    };
    tasks.push(task);
    saveTasks();
    renderTasks();
}

// Function to delete task
function deleteTask(index) {
    tasks.splice(index, 1);
    saveTasks();
    renderTasks();
}

// Function to toggle task completion
function toggleCompletion(index) {
    tasks[index].completed = !tasks[index].completed;
    saveTasks();
    renderTasks();
}

// Function to save tasks to local storage
function saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Function to render tasks
function renderTasks() {
    taskList.innerHTML = '';
    tasks.forEach((task, index) => {
        const taskHtml = `
            <li class="task ${task.completed ? 'completed' : ''}">
                ${task.name}
                <button class="delete-btn" onclick="deleteTask(${index})">Delete</button>
                <input type="checkbox" ${task.completed ? 'checked' : ''} onclick="toggleCompletion(${index})">
            </li>
        `;
        taskList.insertAdjacentHTML('beforeend', taskHtml);
    });
}

// Add event listener to add task button
addTaskBtn.addEventListener('click', () => {
    const taskName = taskInput.value.trim();
    if (taskName) {
        addTask(taskName);
        taskInput.value = '';
    }
});

// Render tasks on page load
renderTasks();