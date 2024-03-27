document.getElementById('add_food_item').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = {
<<<<<<< HEAD
=======
        //id : document.getElementById('id').value,
>>>>>>> 41809003d0e7a1f056bb2f49b89c86c60d747688
        name: document.getElementById('name').value,
        price: parseFloat(document.getElementById('price').value),
        category: document.getElementById('category').value
    };

<<<<<<< HEAD
    fetch('/', {  // Corrected endpoint
=======
    fetch('/add-food-item', {
>>>>>>> 41809003d0e7a1f056bb2f49b89c86c60d747688
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
<<<<<<< HEAD
        document.getElementById('add_food_item').reset();  // Corrected form ID
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('An error occurred while adding the menu item.');
    });
});
=======
        document.getElementById('addMenuItemForm').reset();
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('An error adding the menu item.');
    });
});
>>>>>>> 41809003d0e7a1f056bb2f49b89c86c60d747688
