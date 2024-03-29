from Infrastructure.departmant_repo import DepartmentRepository
from Aplication.controller import HospitalController
from ui.console import HospitalUI


def start():
    # Create repository
    repo = DepartmentRepository()

    # Create controller, provide repository
    controller = HospitalController(repo)

    # Create UI, provide controller
    ui = HospitalUI(controller)
    ui.main_menu()


if __name__ == "__main__":
    start()
