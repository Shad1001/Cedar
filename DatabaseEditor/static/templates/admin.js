document.getElementById('add_food_item').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = {
        name: document.getElementById('name').value,
        price: parseFloat(document.getElementById('price').value),
        category: document.getElementById('category').value
    };

    fetch('/', {  // Corrected endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('Menu item added successfully!');
        document.getElementById('add_food_item').reset();  // Corrected form ID
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('An error occurred while adding the menu item.');
    });
});
