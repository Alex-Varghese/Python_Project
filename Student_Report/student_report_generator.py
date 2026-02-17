import csv
import os

INPUT_FILE = "students_data.txt"
OUTPUT_FILE = "report.txt"

class student:
    def __init__(self, student_id, name, scores):
        self.student_id = student_id
        self.name = name
        self.scores = {subject: int(score) for subject, score in scores.items()}

    @property
    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def get_score(self, subject):
        return self.scores.get(subject, 0)


class report_generator:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.students = []
        self.subjects = ["Math", "Physics", "Chemistry", "Biology"]

    def load_data(self):
        if not os.path.exists(self.input_path):
            print(f"Error: {self.input_path} does not exist.")
            return False

        try:
            with open(self.input_path, "r", newline='') as f:
                reader = csv.reader(f)
                
                header = next(reader, None) 
                
                for row in reader:
                    if len(row) < 6: continue 
                    scores = {
                        "Math": row[2],
                        "Physics": row[3],
                        "Chemistry": row[4],
                        "Biology": row[5]
                    }
                    self.students.append(student(row[0], row[1], scores))
            return True
        except ValueError as e:
            print(f"Data Error: Could not convert a score to integer. {e}")
            return False

    def _write_section_header(self, file_handle, title):
        """Helper to write formatted headers."""
        file_handle.write("\n" + "-" * 90 + "\n")
        file_handle.write(f" {title}\n")
        file_handle.write("-" * 90 + "\n")

    def generate_report(self):
        if not self.students:
            print("No student data to report.")
            return

        print(f"Generating report to {self.output_path}...")
        
        with open(self.output_path, "w") as f:
            f.write("\n" + "=" * 90 + "\n")
            f.write(" COMPREHENSIVE REPORT ".center(90) + "\n")
            f.write("=" * 90 + "\n\n")
            self._write_student_table(f)
            f.write(f"\n Total number of students: {len(self.students)}\n")
            self._write_individual_averages(f)
            self._write_top_performers(f)
            self._write_class_subject_averages(f)
            self._write_overall_average(f)
            self._write_high_low_scores(f)
            self._write_distinctions(f)

    def _write_student_table(self, f):
        self._write_section_header(f, "student Marksheet Details")
        border = "+---------+----------------+------+---------+-----------+---------+"
        f.write(f"{border}\n")
        f.write("| ID      | Name           | Math | Physics | Chemistry | Biology |\n")
        f.write(f"{border}\n")

        for s in self.students:
            f.write(f"| {s.student_id:<7} | {s.name:<14} | {s.get_score('Math'):<4} | "
                    f"{s.get_score('Physics'):<7} | {s.get_score('Chemistry'):<9} | "
                    f"{s.get_score('Biology'):<7} |\n")
        f.write(f"{border}\n")

    def _write_individual_averages(self, f):
        self._write_section_header(f, "Calculation on Individual student Averages")
        for i, s in enumerate(self.students, 1):
            f.write(f" {i}. {s.name}'s average score : {s.average:.2f}\n")

    def _write_top_performers(self, f):
        self._write_section_header(f, "Top 3 Performers (Based on Average)")
        # Sort students by average descending
        sorted_students = sorted(self.students, key=lambda s: s.average, reverse=True)
        
        for i, s in enumerate(sorted_students[:3], 1):
            f.write(f" {i}. {s.name} : {s.average:.2f}\n")

    def _write_class_subject_averages(self, f):
        self._write_section_header(f, "Calculation on Class Subject Averages")
        
        for i, subject in enumerate(self.subjects, 1):
            total = sum(s.get_score(subject) for s in self.students)
            avg = total / len(self.students)
            f.write(f" {i}. Class average score on {subject}: {avg:.2f}\n")

    def _write_overall_average(self, f):
        # Calculate total average of all students
        total_avg = sum(s.average for s in self.students) / len(self.students)
        f.write("\n Calculation on Total Class Averages\n")
        f.write(f" Total class average score : {total_avg:.2f}\n")

    def _write_high_low_scores(self, f):
        self._write_section_header(f, "Highest and Lowest Scores per Subject")
        
        count = 1
        for subject in self.subjects:
            scores = [s.get_score(subject) for s in self.students]
            f.write(f" {count}. Highest score on {subject:<9}: {max(scores)}\n")
            f.write(f" {count+1}. Lowest score on {subject:<10}: {min(scores)}\n")
            count += 2

    def _write_distinctions(self, f):
        self._write_section_header(f, "students Scoring Above 90")

        for subject in self.subjects:
            f.write(f"\n Subject: {subject}\n")
            found = False
            count = 1
            for s in self.students:
                score = s.get_score(subject)
                if score > 90:
                    f.write(f"  {count}. {s.name} : {score}\n")
                    count += 1
                    found = True
            
            if not found:
                f.write("  None\n")

if __name__ == "__main__":
    app = report_generator(INPUT_FILE, OUTPUT_FILE)
    
    if app.load_data():
        app.generate_report()
        
        # Verify output
        if os.path.exists(OUTPUT_FILE):
            print("\n--- Report Preview (First 10 lines) ---")
            with open(OUTPUT_FILE, 'r') as f:
                for _ in range(5):
                    print(f.readline().strip())
