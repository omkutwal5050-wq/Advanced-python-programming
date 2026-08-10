"""
Hospital Patient Management System
Maintains patient records categorized as General or Special patients.
"""

from abc import ABC, abstractmethod


# ---------------- Base Patient Class ----------------
class Patient(ABC):
    def __init__(self, patient_id, name, treatment_cost):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost

    @abstractmethod
    def category(self):
        """Return the category of the patient."""
        pass

    def final_cost(self):
        """Return the final treatment cost (can be overridden by subclasses)."""
        return self.treatment_cost

    def __str__(self):
        return (f"ID: {self.patient_id} | Name: {self.name} | "
                f"Category: {self.category()} | "
                f"Treatment Cost: Rs.{self.treatment_cost} | "
                f"Final Cost: Rs.{self.final_cost()}")


# ---------------- General Patient ----------------
class GeneralPatient(Patient):
    def category(self):
        return "General"

    def final_cost(self):
        # No extra charges for general ward patients
        return self.treatment_cost


# ---------------- Special Patient ----------------
class SpecialPatient(Patient):
    SPECIAL_CARE_CHARGE = 1500  # flat extra charge for special/private ward

    def category(self):
        return "Special"

    def final_cost(self):
        # Special ward patients pay an additional care charge
        return self.treatment_cost + self.SPECIAL_CARE_CHARGE


# ---------------- Hospital Class ----------------
class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient '{patient.name}' (ID: {patient.patient_id}) added successfully.")

    def find_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None
# om kutwal sy-12 roll no. 70
    def display_all_records(self):
        print(f"\n--- Patient Records: {self.name} ---")
        if not self.patients:
            print("No patient records found.")
            return
        for patient in self.patients:
            print(patient)

    def display_by_category(self, category):
        print(f"\n--- {category} Patients: {self.name} ---")
        filtered = [p for p in self.patients if p.category().lower() == category.lower()]
        if not filtered:
            print(f"No {category} patients found.")
        for patient in filtered:
            print(patient)


def print_menu():
    print("\n===== HOSPITAL PATIENT MANAGEMENT SYSTEM =====")
    print("1. Add a General patient")
    print("2. Add a Special patient")
    print("3. Display all patient records")
    print("4. Display only General patients")
    print("5. Display only Special patients")
    print("6. Search patient by ID")
    print("7. Exit")
    print("================================================")


def main():
    hospital = Hospital("City Care Hospital")

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            patient_id = input("Enter patient ID: ").strip()
            name = input("Enter patient name: ").strip()
            try:
                cost = float(input("Enter treatment cost: ").strip())
            except ValueError:
                print("Invalid cost entered.")
                continue
            hospital.add_patient(GeneralPatient(patient_id, name, cost))

        elif choice == "2":
            patient_id = input("Enter patient ID: ").strip()
            name = input("Enter patient name: ").strip()
            try:
                cost = float(input("Enter treatment cost: ").strip())
            except ValueError:
                print("Invalid cost entered.")
                continue
            hospital.add_patient(SpecialPatient(patient_id, name, cost))

        elif choice == "3":
            hospital.display_all_records()

        elif choice == "4":
            hospital.display_by_category("General")

        elif choice == "5":
            hospital.display_by_category("Special")

        elif choice == "6":
            patient_id = input("Enter patient ID to search: ").strip()
            patient = hospital.find_patient(patient_id)
            if patient:
                print(patient)
            else:
                print("Patient not found.")

        elif choice == "7":
            print("Exiting the Hospital Patient Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
