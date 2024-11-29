document.addEventListener('DOMContentLoaded', function() {
    const dayCheckboxes = document.querySelectorAll('.day-checkbox');

    dayCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const label = this.parentElement;
            const span = label.querySelector('span');
            if (this.checked) {
                span.style.backgroundColor = '#007bff';
                span.style.color = 'white';
            } else {
                span.style.backgroundColor = '#f0f0f0';
                span.style.color = 'black';
            }
        });
    });
});