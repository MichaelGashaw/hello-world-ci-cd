import unittest
from io import StringIO
import sys
from hello_world import main

class TestHelloWorld(unittest.TestCase):
    def test_output(self):
        """Test if the main function prints 'Hello, World!' correctly."""
        captured_output = StringIO()  # Create a new StringIO object to capture output
        sys.stdout = captured_output   # Redirect stdout to capture print statements
        main()                         # Call the function
        sys.stdout = sys.__stdout__     # Reset stdout to default
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")  # Check output

if __name__ == "__main__":
    unittest.main()
