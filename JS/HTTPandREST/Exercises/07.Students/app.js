function attachEvents() {
  const table = document.querySelector('#results tbody');
  const submitBtn = document.getElementById('submit');
  const BASE_URL = 'http://localhost:3030/jsonstore/collections/students'
  const [fName, lName, fNumber, grade] = document.querySelectorAll('.inputs input');
  getDatabase();

  submitBtn.addEventListener('click', () => createStudent());

  function createStudent() {
    if (fName.value && lName.value && fNumber.value && grade.value) {
      
      let newStudent = {
        'firstName': fName.value,
        'lastName': lName.value,
        'facultyNumber': fNumber.value,
        'grade': grade.value
      }
      const headers = { 'Content-Type': 'application/json' };
      fetch(BASE_URL, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(newStudent)
      })
      .then(() => getDatabase())
      .catch(err => console.log(err));

      Array.from([fName, lName, fNumber, grade]).forEach(tag => tag.value = '')
    }
  }

  function getDatabase() {
    fetch(BASE_URL)
      .then(res => res.json())
      .then(data => outputData(data))
      .catch(err => console.log(err));
  }

  function outputData(data) {
    while (table.firstChild) { table.removeChild(table.lastChild) }
    Object.values(data).forEach(student => {
      const tr = document.createElement('tr');
      const tdFname = document.createElement('td');
      const tdLname = document.createElement('td');
      const tdFnumber = document.createElement('td');
      const tdGrade = document.createElement('td');

      tdFname.textContent = student.firstName;
      tdLname.textContent = student.lastName;
      tdFnumber.textContent = student.facultyNumber;
      tdGrade.textContent = student.grade;

      [tdFname, tdLname, tdFnumber, tdGrade].forEach(tag => tr.appendChild(tag))
      table.appendChild(tr)
    })
  }
}

attachEvents();