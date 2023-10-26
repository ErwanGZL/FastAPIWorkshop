console.log("Hello");

let checkboxes = document.getElementsByName('checkbox-task');

checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', () => {
        const taskId = checkbox.getAttribute('id');

        fetch('/task/toggle', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ task_id: taskId })
        })
            .then(response => {
                if (response.ok) {
                    location.reload();
                } else {
                    throw new Error('Failed to check task');
                }
            })
            .catch(error => {
                console.error(error);
            });
    });
});
