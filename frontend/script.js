const API_URL = "http://127.0.0.1:5000/students";

let currentStudentId = null;

// Load students when page opens
document.addEventListener("DOMContentLoaded", () => {
    loadStudents();
});

// ==========================
// Load All Students
// ==========================
async function loadStudents() {

    const response = await fetch(API_URL);
    const students = await response.json();

    const table = document.getElementById("studentTable");

    table.innerHTML = "";

    students.forEach(student => {

        table.innerHTML += `
        <tr>

            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.age}</td>
            <td>${student.email}</td>
            <td>${student.course}</td>

            <td>

                <button
                    class="btn btn-warning btn-sm me-2"
                    onclick="editStudent(${student.id}, '${student.name}', ${student.age}, '${student.email}', '${student.course}')">

                    Edit

                </button>

                <button
                    class="btn btn-danger btn-sm"
                    onclick="deleteStudent(${student.id})">

                    Delete

                </button>

            </td>

        </tr>
        `;
    });

}

// ==========================
// Add Student
// ==========================

async function addStudent() {

    const student = {

        name: document.getElementById("name").value,
        age: Number(document.getElementById("age").value),
        email: document.getElementById("email").value,
        course: document.getElementById("course").value

    };

    const response = await fetch(API_URL, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(student)

    });

    if (response.ok) {

        alert("Student Added Successfully");

        resetForm();

        loadStudents();

    } else {

        alert("Failed to Add Student");

    }

}

// ==========================
// Edit Student
// ==========================

function editStudent(id, name, age, email, course) {

    currentStudentId = id;

    document.getElementById("studentId").value = id;
    document.getElementById("name").value = name;
    document.getElementById("age").value = age;
    document.getElementById("email").value = email;
    document.getElementById("course").value = course;

}

// ==========================
// Update Student
// ==========================

async function updateStudent() {

    if (currentStudentId === null) {

        alert("Select a student first");

        return;

    }

    const student = {

        name: document.getElementById("name").value,
        age: Number(document.getElementById("age").value),
        email: document.getElementById("email").value,
        course: document.getElementById("course").value

    };

    const response = await fetch(`${API_URL}/${currentStudentId}`, {

        method: "PUT",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(student)

    });

    if (response.ok) {

        alert("Student Updated Successfully");

        resetForm();

        loadStudents();

    } else {

        alert("Update Failed");

    }

}

// ==========================
// Delete Student
// ==========================

async function deleteStudent(id) {

    const confirmDelete = confirm("Are you sure you want to delete this student?");

    if (!confirmDelete) return;

    const response = await fetch(`${API_URL}/${id}`, {

        method: "DELETE"

    });

    if (response.ok) {

        alert("Student Deleted Successfully");

        loadStudents();

    } else {

        alert("Delete Failed");

    }

}

// ==========================
// Reset Form
// ==========================

function resetForm() {

    currentStudentId = null;

    document.getElementById("studentId").value = "";
    document.getElementById("name").value = "";
    document.getElementById("age").value = "";
    document.getElementById("email").value = "";
    document.getElementById("course").value = "";

}