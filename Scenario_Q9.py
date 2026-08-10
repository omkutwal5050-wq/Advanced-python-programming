"""
Course Management System
Maintains course information categorized as Short-Term or Long-Term courses.
"""

from abc import ABC, abstractmethod


# ---------------- Base Course Class ----------------
class Course(ABC):
    def __init__(self, course_name, duration, fee):
        self.course_name = course_name
        self.duration = duration   # duration in months
        self.fee = fee

    @abstractmethod
    def category(self):
        """Return the category of the course."""
        pass

    def final_fee(self):
        """Return the final fee (can be overridden by subclasses)."""
        return self.fee

    def __str__(self):
        return (f"Course: {self.course_name} | Duration: {self.duration} month(s) | "
                f"Category: {self.category()} | "
                f"Fee: Rs.{self.fee} | Final Fee: Rs.{self.final_fee()}")


# ---------------- Short-Term Course ----------------
class ShortTermCourse(Course):
    def category(self):
        return "Short-Term"

    def final_fee(self):
        # No extra charges for short-term courses
        return self.fee


# ---------------- Long-Term Course ----------------
class LongTermCourse(Course):
    MATERIAL_CHARGE = 2000  # flat extra charge for study material/resources

    def category(self):
        return "Long-Term"

    def final_fee(self):
        # Long-term courses include additional material charges
        return self.fee + self.MATERIAL_CHARGE


# ---------------- Institute Class ----------------
class Institute:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"Course '{course.course_name}' added successfully.")

    def find_course(self, course_name):
        for course in self.courses:
            if course.course_name.lower() == course_name.lower():
                return course
        return None
# om kutwal sy-12 roll no. 70
    def display_all_courses(self):
        print(f"\n--- All Courses: {self.name} ---")
        if not self.courses:
            print("No courses found.")
            return
        for course in self.courses:
            print(course)

    def display_by_category(self, category):
        print(f"\n--- {category} Courses: {self.name} ---")
        filtered = [c for c in self.courses if c.category().lower() == category.lower()]
        if not filtered:
            print(f"No {category} courses found.")
        for course in filtered:
            print(course)


def print_menu():
    print("\n===== COURSE MANAGEMENT SYSTEM =====")
    print("1. Add a Short-Term course")
    print("2. Add a Long-Term course")
    print("3. Display all courses")
    print("4. Display only Short-Term courses")
    print("5. Display only Long-Term courses")
    print("6. Search course by name")
    print("7. Exit")
    print("======================================")


def main():
    institute = Institute("Bright Future Institute")

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            course_name = input("Enter course name: ").strip()
            duration = input("Enter duration (in months): ").strip()
            try:
                fee = float(input("Enter course fee: ").strip())
            except ValueError:
                print("Invalid fee entered.")
                continue
            institute.add_course(ShortTermCourse(course_name, duration, fee))

        elif choice == "2":
            course_name = input("Enter course name: ").strip()
            duration = input("Enter duration (in months): ").strip()
            try:
                fee = float(input("Enter course fee: ").strip())
            except ValueError:
                print("Invalid fee entered.")
                continue
            institute.add_course(LongTermCourse(course_name, duration, fee))

        elif choice == "3":
            institute.display_all_courses()

        elif choice == "4":
            institute.display_by_category("Short-Term")

        elif choice == "5":
            institute.display_by_category("Long-Term")

        elif choice == "6":
            course_name = input("Enter course name to search: ").strip()
            course = institute.find_course(course_name)
            if course:
                print(course)
            else:
                print("Course not found.")

        elif choice == "7":
            print("Exiting the Course Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
