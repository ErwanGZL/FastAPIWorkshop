console.log("Hello");

// Get all delete buttons
let deleteBtns = document.getElementsByName('delete-task-btn');

// Add event listener to each delete button
deleteBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        // Get the task ID from the button id attribute
        const taskId = btn.getAttribute('id');

        // Send a POST request to the server to delete the task
        fetch('/task/delete', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ task_id: taskId })
        })
            .then(response => {
                if (response.ok) {
                    // Reload the page to show the updated task list
                    location.reload();
                } else {
                    throw new Error('Failed to delete task');
                }
            })
            .catch(error => {
                console.error(error);
            });
    });
});
