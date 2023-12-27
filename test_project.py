from project import PasswordGenerator
from unittest.mock import patch

class TestPasswordGenerator:

    @patch('builtins.input', side_effect=['Ayad azad', 'Eden hazard', 'David malan', 'Mike tyson'])
    def test_add_name(self, mock_input):
        password_gen = PasswordGenerator()

        generated_first_name = password_gen.add_name()
        assert generated_first_name == 'Ayad azad'

        generated_second_name = password_gen.add_name()
        assert generated_second_name == 'Eden hazard'

        generated_third_name = password_gen.add_name()
        assert generated_third_name == 'David malan'

        generated_fourth_name = password_gen.add_name()
        assert generated_fourth_name == 'Mike tyson'

    @patch('builtins.input', side_effect=['Facebook', 'Linkedin', 'Instagram'])
    def test_add_platform(self, mock_input):
        password_gen = PasswordGenerator()

        generated_first_platform = password_gen.add_platform()
        assert generated_first_platform == 'Facebook'

        generated_second_platform = password_gen.add_platform()
        assert generated_second_platform == 'Linkedin'

        generated_third_platform = password_gen.add_platform()
        assert generated_third_platform == 'Instagram'
