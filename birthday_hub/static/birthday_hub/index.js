const addBirthdayForm = document.querySelector('#add-birthday');

document.addEventListener('DOMContentLoaded', () => {

    addBirthdayForm.addEventListener('submit', addBirthday);
});

function addBirthday(event) {
    event.preventDefault();
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
        console.log(await response.json());
    } catch (e) {
        console.error(e);
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
