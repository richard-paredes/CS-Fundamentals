const onBlur = (event) => {
    if (!event.currentTarget.value) {
        event.srcElement.classList.add('is-invalid');
    } else {
        event.srcElement.classList.remove('is-invalid');
    }
};

const handleError = (error, message) => { 
    const error_node = document.querySelector('#error-alert');
    const details_node = document.querySelector('#error-details');
    if (message) {
        details_node.innerHTML = message;
    } else {
        details_node.innerHTML = error.message;
    }
    error_node.removeAttribute('hidden');
    
};

const resetForm = (form_id) => {
    document.querySelector(form_id).reset();
};

const hideError = () => {
    document.querySelector('#error-alert').setAttribute('hidden', 'true');
};