let students = [];

function addstudent() {
  let name = document.getElementById("name").value;
  if (name == "") {
    alert("Enter Student Name");
    return;
  }

  let student = {
    name: name,
  };

  students.push(student);

  let output = "";
  for (let i = 0; i < students.length; i++) {
    output += "<li>";
    output += students[i].name;
    output += " <button onclick='delstudent(" + i + ")'>Delete</button>";
    output += "</li>";
  }

  document.getElementById("list").innerHTML = output;

  document.getElementById("name").value = "";
}

function delstudent(index) {
  students.splice(index, 1);

  let output = "";

  for (let i = 0; i < students.length; i++) {
    output += "<li>";
    output += students[i].name;
    output += " <button onclick='delstudent(" + i + ")'>Delete</button>";
    output += "</li>";
  }
  document.getElementById("list").innerHTML = output;
}
