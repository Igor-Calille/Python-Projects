document.addEventListener('DOMContentLoaded', (event) => {
    // Example of form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                alert('Por favor, preencha todos os campos obrigatórios.');
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Example of adding dynamic content
    const dynamicButton = document.getElementById('dynamicButton');
    if (dynamicButton) {
        dynamicButton.addEventListener('click', () => {
            const dynamicContent = document.getElementById('dynamicContent');
            const newContent = document.createElement('p');
            newContent.textContent = 'Conteúdo adicionado dinamicamente!';
            dynamicContent.appendChild(newContent);
        });
    }
});
