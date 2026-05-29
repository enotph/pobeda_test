document.addEventListener('DOMContentLoaded', () => {
  loadUsers();

  document.getElementById('add-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    const res = await fetch('/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email })
    });

    if (res.ok) {
      alert('Добавлен!');
      document.getElementById('add-form').reset();
      bootstrap.Modal.getInstance(document.getElementById('addModal')).hide();
      loadUsers();
    } else {
      alert('Ошибка');
    }
  });

  async function loadUsers() {
    const res = await fetch('/users');
    const users = await res.json();
    const tbody = document.getElementById('users-table-body');
    tbody.innerHTML = '';

    users.forEach(user => {
      const tr = document.createElement('tr');
      tr.innerHTML = `<td>${user.id}</td><td>${user.name}</td><td>${user.email}</td>`;
      tr.onclick = () => showDetails(user);
      tbody.appendChild(tr);
    });
  }

  function showDetails(user) {
    document.getElementById('user-info').innerHTML = `
      <p><strong>ID:</strong> ${user.id}</p>
      <p><strong>Имя:</strong> ${user.name}</p>
      <p><strong>Email:</strong> ${user.email}</p>
    `;
    new bootstrap.Modal(document.getElementById('viewModal')).show();
  }
});