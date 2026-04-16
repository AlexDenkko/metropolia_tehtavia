'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const target = document.getElementById('target');
const select = document.createElement('select');

for (const student of students) {
  const option = document.createElement('option');
  option.textContent = student.name;
  option.value = student.id;
  select.appendChild(option);
}

target.appendChild(select);
