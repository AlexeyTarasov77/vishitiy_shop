document.addEventListener('DOMContentLoaded', function() {
    const phoneInput = document.getElementById('number_phone');
    phoneInput.addEventListener('input', validatePhoneNumber);
});

function validatePhoneNumber(event) {
    const input = event.target;
    const validCharacters = /^[0-9+\-()\s]*$/;
    
    if (!validCharacters.test(input.value)) {
        // Удаляем все недопустимые символы
        input.value = input.value.replace(/[^0-9+\-()\s]/g, '');
    }
}


document.addEventListener('DOMContentLoaded', function() {
    const commentInput = document.getElementById('comment');
    
    commentInput.addEventListener('input', function() {
        const maxLength = 100;
        if (commentInput.value.length > maxLength) {
            commentInput.value = commentInput.value.slice(0, maxLength);
        }
    });
});