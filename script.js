document.getElementById('passwordForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const site = document.getElementById('site').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (site && username && password) {
        addPassword(site, username, password);
        document.getElementById('passwordForm').reset();
    }
});

function addPassword(site, username, password) {
    const passwordList = document.getElementById('passwordList');
    const div = document.createElement('div');
    
    const siteSpan = document.createElement('span');
    siteSpan.textContent = `Site: ${site}`;
    
    const usernameSpan = document.createElement('span');
    usernameSpan.textContent = `Username: ${username}`;
    
    const passwordSpan = document.createElement('span');
    passwordSpan.textContent = `Password: ${password}`;
    
    div.appendChild(siteSpan);
    div.appendChild(usernameSpan);
    div.appendChild(passwordSpan);
    
    passwordList.appendChild(div);
}
