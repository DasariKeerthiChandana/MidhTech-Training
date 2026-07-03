function showReport() {
  class Student {
    constructor(id, name, marks) {
      this.id = id;
      this.name = name;
      this.marks = marks;
      if (marks >= 90) this.grade = "Grade A";
      else if (marks >= 75) this.grade = "Grade B";
      else if (marks >= 60) this.grade = "Grade C";
      else this.grade = "Fail";
    }
  }
  let students = [];
  students.push(new Student(101, "Rahul", 95));
  students.push(new Student(102, "Priya", 82));
  students.push(new Student(103, "Kiran", 67));
  students.push(new Student(104, "Suresh", 45));
  students.push(new Student(105, "Anitha", 91));
  console.clear();
  console.log("----- STUDENT REPORT -----");
  students.forEach((s) => {
    console.log(`ID:${s.id} | ${s.name} | ${s.marks} | ${s.grade}`);
  });
  let topper = students[0];
  students.forEach((s) => {
    if (s.marks > topper.marks) topper = s;
  });
  console.log("\nTopper:", topper.name, "(", topper.marks, ")");
  console.log("\nPassed Students:");
  students
    .filter((s) => s.marks >= 60)
    .forEach((s) => {
      console.log(s.name);
    });
  console.log("\nFailed Students:");
  students
    .filter((s) => s.marks < 60)
    .forEach((s) => {
      console.log(s.name);
    });
  let total = 0;
  students.forEach((s) => {
    total += s.marks;
  });
  console.log("\nAverage Marks:", total / students.length);
  console.log("Total Passed:", students.filter((s) => s.marks >= 60).length);
  console.log("Total Failed:", students.filter((s) => s.marks < 60).length);
}
