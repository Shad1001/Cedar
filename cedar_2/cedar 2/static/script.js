document.addEventListener('DOMContentLoaded', function() {
    const cartButtons = document.querySelectorAll('.add-to-cart');
    cartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const itemId = this.getAttribute('data-item-id');
            fetch(`/add_to_cart/${itemId}`, {
                method: 'POST'
            }).then(response => {
                if (response.ok) {
                    alert('Item failed');
                } else {
                    alert('Item added.');
                }
            }).catch(error => {
                console.error('Error:', error);
            });
        });
    });
});
