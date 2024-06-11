const addBirthdayForm = document.querySelector('#add-birthday');

document.addEventListener('DOMContentLoaded', () => {
    loadBirthdays();
    addBirthdayForm.addEventListener('submit', addBirthday);
});

async function loadBirthdays() {
    try {
        const response = await fetch('/birthdays', {
            method: 'GET',
        });

        const data = await response.json();

        if (response.ok) {
            console.log(data);
            displayBirthdays(data);
        } else {
            console.error(data);
        }

    } catch (e) {
        console.error(`Network error: ${e}.`);
    }
}

function displayBirthdays(birthdays) {
    const container = document.querySelector('#birthdays');
    container.innerHTML = '';

    birthdays.forEach(birthday => {

        const birthdayElement = document.createElement('div');

        birthdayElement.innerHTML = `
            <img src="${birthday.picture}" alt="Profile Picture">
            <p>First Name: ${birthday.first_name}</p>
            <p>Last Name: ${birthday.last_name || 'N/A'}</p>
            <p>Nickname: ${birthday.nickname || 'N/A'}</p>
            <p>Birthdate: ${birthday.birthdate}</p>
            <p>Notes: ${birthday.notes || 'No notes available'}</p>
        `;

        container.appendChild(birthdayElement);
    });
}

function addBirthday(event) {
    event.preventDefault();

    const userMessages = document.querySelectorAll('p');
    userMessages.forEach(message => message.remove());

    sendBirthdayData();
}

async function sendBirthdayData() {
    const formData = new FormData(addBirthdayForm);
    formData.append('csrfmiddlewaretoken', getCookie('csrftoken'));

    try {
        const response = await fetch('/add/birthday', {
            method: 'POST',
            body: formData,
            credentials: 'same-origin',
        });

        const data = await response.json();

        if (response.ok) {
            handleSuccess(data.message);
            console.log(data);
        } else {
            displayFormErrors(JSON.parse(data.errors));
            console.error(data.errors);
        }

    } catch (e) {
        console.error(`Network error: ${e}.`);
    }
}

function handleSuccess(message) {
    addBirthdayForm.reset();
    const messageElement = document.createElement('p');
    messageElement.innerHTML = message;
    addBirthdayForm.append(messageElement);
}

function displayFormErrors(errors) {
    // Display non-field errors
    if (Object.keys(errors).length === 1) {
        errors['__all__']?.forEach(error => {
            const errorElement = document.createElement('p');
            errorElement.innerHTML = error.message;
            addBirthdayForm.insertBefore(errorElement, addBirthdayForm.children[0]);
        });
    }

    // Display field-specific errors
    for (const [field, errorDetails] of Object.entries(errors)) {
        const formFieldElement = document.querySelector(`[name=${field}]`);
        if (formFieldElement) {
            errorDetails.forEach(error => {
                const errorElement = document.createElement('p');
                errorElement.innerHTML = error.message;
                formFieldElement.parentElement.append(errorElement);
            });
        }
    }
}

// https://docs.djangoproject.com/en/5.0/howto/csrf/#acquiring-the-token-if-csrf-use-sessions-and-csrf-cookie-httponly-are-false
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
