// Data Initialization
let projects = ["Project Alpha", "Project Beta"];
let tasks = ["Define Requirements", "Develop Features"];
let completedTasks = 0;

// Render Functions
function renderProjects() {
  const projectList = document.getElementById("project-list");
  projectList.innerHTML = "";
  projects.forEach((project) => {
    const li = document.createElement("li");
    li.textContent = project;
    projectList.appendChild(li);
  });
}

function renderTasks() {
  const taskList = document.getElementById("task-list");
  taskList.innerHTML = "";
  tasks.forEach((task, index) => {
    const li = document.createElement("li");
    li.textContent = task;
    li.addEventListener("click", () => completeTask(index));
    taskList.appendChild(li);
  });
}

// Add Project
function addProject() {
  const projectName = prompt("Enter Project Name:");
  if (projectName) {
    projects.push(projectName);
    renderProjects();
  }
}

// Add Task
function addTask() {
  const taskName = prompt("Enter Task Name:");
  if (taskName) {
    tasks.push(taskName);
    renderTasks();
    updateProgress();
  }
}

// Complete Task
function completeTask(index) {
  tasks.splice(index, 1);
  completedTasks++;
  renderTasks();
  updateProgress();
}

// Update Progress Bar
function updateProgress() {
  const progress = document.getElementById("progress");
  const progressText = document.getElementById("progress-text");
  const total = projects.length + completedTasks;
  const percentage = total > 0 ? Math.round((completedTasks / total) * 100) : 0;
  progress.style.width = `${percentage}%`;
  progressText.textContent = `Progress: ${percentage}%`;
}

// Initialize
renderProjects();
renderTasks();
updateProgress();
