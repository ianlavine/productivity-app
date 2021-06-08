/* Get user input for login screen */
const loginForm = document.querySelector("#login_form");
const emailInput = document.querySelector("#email");
const passwordInput = document.querySelector("#password");
const msg = document.querySelector(".msg");
const userList = document.querySelector("#users");

loginForm.addEventListener("submit", onSubmit);

function onSubmit(e) {
    e.preventDefault();

    if (emailInput.value === '' || passwordInput.value === ''){
        msg.classList.add('error');
        msg.innerHTML = "Please enter all fields"

        setTimeout(() => msg.remove(), 3000);
    } else {
        const li = document.createElement('li');
        li.appendChild(document.createTextNode(
        `${emailInput.value} :  ${passwordInput.value}`));

        userList.appendChild(li);

        // Clear fields
        emailInput.value = ''
        passwordInput.value = ''
    }
}