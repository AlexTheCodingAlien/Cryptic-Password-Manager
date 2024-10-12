document.addEventListener('DOMContentLoaded', loadPasswords);

document.getElementById('passwordForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const site = document.getElementById('site').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    if (site && username && password) {
        addPassword(site, username, password);
        savePassword(site, username, password);
        document.getElementById('passwordForm').reset();
    }
});

// Add password to the UI
function addPassword(site, username, password) {
    const passwordList = document.getElementById('passwordList');
    const div = document.createElement('div');
    div.classList.add('password-item');
    
    const passwordInfo = document.createElement('span');
    passwordInfo.textContent = `Site: ${site}, Username: ${username}, Password: ${password}`;
    
    const deleteBtn = document.createElement('button');
    deleteBtn.classList.add('delete-btn');
    deleteBtn.textContent = 'Delete';
    deleteBtn.onclick = function() {
        removePassword(site);
        div.remove();
    };
    
    div.appendChild(passwordInfo);
    div.appendChild(deleteBtn);
    passwordList.appendChild(div);
}

// Save password to local storage
function savePassword(site, username, password) {
    let passwords = getPasswords();
    passwords.push({ site, username, password });
    localStorage.setItem('passwords', JSON.stringify(passwords));
}

// Load passwords from local storage
function loadPasswords() {
    const passwords = getPasswords();
    passwords.forEach(({ site, username, password }) => {
        addPassword(site, username, password);
    });
}

// Get passwords from local storage
function getPasswords() {
    return JSON.parse(localStorage.getItem('passwords')) || [];
}

// Remove password from local storage
function removePassword(site) {
    let passwords = getPasswords();
    passwords = passwords.filter(p => p.site !== site);
    localStorage.setItem('passwords', JSON.stringify(passwords));
}
