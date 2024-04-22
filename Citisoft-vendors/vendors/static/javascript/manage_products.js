const deleteButtons = document.querySelectorAll('.delete');

deleteButtons.forEach(button => {
    button.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent default form-like submission

        const productId = button.dataset.productId; 
        if (confirm('Are you sure you want to delete this product?')) {
            // Make AJAX request to the Django delete view
            fetch(`/vendors/products/delete/${productId}/`, {
                method: 'DELETE',  
            })
            .then(response => {
                if (response.ok) {
                    button.parentNode.parentNode.remove(); // Remove the product <li>
                } else {
                    alert('Error deleting product.'); 
                }
            })
            .catch(error => {
                console.error('Error deleting:', error);
            });
        }
    });
});
