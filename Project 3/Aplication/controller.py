from utils.validation import int_input
from Infrastructure.departmant_repo import DepartmentRepository
from Infrastructure.patient_repo import PatientRepository
from Domain.departmant import Department
from Domain.patient import Patient


class HospitalController:
    """
    Controller for CRUD operations on a Department List.
    """

    def __init__(self, repo):
        """
        Create a new instance of HospitalController
        with an instance of DepartmentRepository.
        """
        self.__repo = repo

    def read_department(self):
        """
        Read input from the user and return a Department
        """
        print("\nReading department info.")
        identifier = int_input("ID = ")
        name = input("name = ")
        bed_count = int_input("bed count = ")

        patients = self.read_patient_repo()

        return Department(identifier, name, bed_count, patients)

    def read_patient_repo(self):
        """
        Read input from the user and return a PatientRepository
        """
        patient_repo = PatientRepository()
        while True:
            choice = input("\nRead a patient? (Yes/No): ")
            if not choice.lower().startswith("y"):
                break

            patient_repo.add_patient(self.read_patient())

        return patient_repo

    def read_patient(self):
        """
        Read input from the user and return a Patient
        """
        first_name = input("first name = ")
        last_name = input("last name = ")
        pnc = int_input("pnc = ")
        disease = input("disease = ")

        return Patient(first_name, last_name, pnc, disease)

    def add_department(self):
        """
        Add a new department to the repository
        """
        department = self.read_department()
        self.__repo.add_department(department)
        print("INFO: The department has been added to the repository.")

    def update_department_with_id(self):
        """
        Update a department with a given identifier
        """
        identifier = int_input("ID = ")
        department = self.read_department()

        self.__repo.update_department(identifier, department)
        print("INFO: The department has been updated.")

    def update_patient_with_name(self):
        """
        Update a patient with a given name
        """
        first_name = input("first name = ")
        last_name = input("last name = ")

        print("\nReading new patient info.")
        patient = self.read_patient()
        for department in self.__repo.get_departments():
            department.get_patients().update_patient(first_name, last_name, patient)

        print("INFO: The patient has been updated.")

    def delete_department_with_id(self):
        """
        Delete a department with a given identifier
        """
        identifier = int_input("ID = ")

        self.__repo.delete_department(identifier)
        print("INFO: The department has been deleted.")

    def delete_patient_with_name(self):
        """
        Delete a patient with a given name
        """
        first_name = input("first name = ")
        last_name = input("last name = ")

        for department in self.__repo.get_departments():
            department.get_patients().delete_patient(first_name, last_name)

        print("INFO: The patient has been deleted.")

    def get_departments_with_patients_less_than(self):
        """
        Display the departments with the number
        of patients lower than a given number
        """
        number = int_input("number = ")
        matching = self.__repo.get_departments_with_patient_count_less_than(number)

        if len(matching) == 0:
            print("There are no departments matching the criterion.")
        else:
            for match in matching:
                print(match)

    def get_patients_with_name_prefix(self):
        """
        Display the patients whose name start
        with a given prefix
        """
        prefix = input("prefix = ")

        message = ""
        for department in self.__repo.get_departments():
            patient_repo = department.get_patients()

            for patient in patient_repo.get_patients_whose_name_begin_with(prefix):
                message += str(patient) + "\n"

        if len(message) == 0:
            print("There are no patients matching the criterion.")
        else:
            print(message[:-1])

    def get_departments_with_bed_count(self):
        """
        Display the departments that have
        a given number of beds
        """
        number = int_input("number = ")
        matching = self.__repo.get_departments_with_bed_count(number)

        if len(matching) == 0:
            print("There are no departments matching the criterion.")
        else:
            for match in matching:
                print(match)
