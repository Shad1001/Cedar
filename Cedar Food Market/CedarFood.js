document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.orderButton').forEach(function(button) {
        button.addEventListener('click', function() {
            addToCart.call(this, this.getAttribute('data-item'));
        });
    });
});



function addToCart(item) {
    const cart = document.getElementById('orderNow');
    const imageSrc = this.getAttribute('data-image');
     

    if (cart) {
        if (cart.innerHTML.trim() === 'Your cart is empty') {
            cart.innerHTML = ''; 
        }

       
        const itemHTML = `
            <div class="cart-item">
                <img src="${imageSrc}" alt="${item}" width="50" height="50">
                <p>${item} </p>
            </div>
        `;

        cart.innerHTML += itemHTML; 
    } 
}


