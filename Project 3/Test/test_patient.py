from Domain.patient import Patient


class PatientTest(unittest.TestCase):
    """
    Test the Patient class.
    """

    def test_create(self):
        """
        Test Patient creation
        """
        patient = Patient("Denis", "Hartagan", 500, "Common Cold")

        """
        Test getters
        """
        self.assertEqual(patient.get_first_name(), "Denis")
        self.assertEqual(patient.get_last_name(), "Hartagan")
        self.assertEqual(patient.get_pnc(), 500)
        self.assertEqual(patient.get_disease(), "Common Cold")
        self.assertEqual(str(patient), "Patient David Horvath with pnc 500 and disease Common Cold.")

        """
        Test setters
        """
        patient.set_first_name("Michael")
        patient.set_last_name("Black")
        patient.set_pnc(200)
        patient.set_disease("Scoliosis")

        self.assertEqual(patient.get_first_name(), "Michael")
        self.assertEqual(patient.get_last_name(), "Black")
        self.assertEqual(patient.get_pnc(), 200)
        self.assertEqual(patient.get_disease(), "Scoliosis")
        self.assertEqual(str(patient), "Patient Michael Black with pnc 200 and disease Scoliosis.")


if __name__ == "__main__":
    unittest.main()
