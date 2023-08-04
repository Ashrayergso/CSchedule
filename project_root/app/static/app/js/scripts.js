```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    // Function to handle form submission
    function handleFormSubmit(event) {
        event.preventDefault();

        // Get form data
        const formData = new FormData(event.target);
        const data = Object.fromEntries(formData);

        // Send a POST request to the server
        fetch('/assignCrewToShips/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('Assignment successful!');
            } else {
                alert('Assignment failed. Please try again.');
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }

    // Attach event listener to form
    const form = document.querySelector('#assignmentForm');
    form.addEventListener('submit', handleFormSubmit);
});
```