document.getElementById('add_food_item').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = {
        //id : document.getElementById('id').value,
        name: document.getElementById('name').value,
        price: parseFloat(document.getElementById('price').value),
        category: document.getElementById('category').value
    };

    fetch('/add-food-item', {
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
        document.getElementById('addMenuItemForm').reset();
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('An error adding the menu item.');
    });
});