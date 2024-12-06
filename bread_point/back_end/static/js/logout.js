document.querySelector('.logout-link').addEventListener('click', function(event) {
    event.preventDefault();

    fetch('http://127.0.0.1:5000/logout', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        window.location.href = '/'; 
    })
    .catch(error => {
        console.error('Error:', error);
    });
});