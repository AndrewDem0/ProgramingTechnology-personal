import unittest
from grades_management import children_list, subject_best_children

class TestGradesManagement(unittest.TestCase):
    
    def setUp(self):
        # Підготовка тестових даних
        self.data = {
            ('8-A', 'Soroka I.I.'): {
                'Math': [12, 10, 8, 9],
                'Ukr literature': [9, 7],
                'Chemistry': [6, 8, 7],
                'Physics': [11, 12, 11, 12],
                'PE': [10, 10, 10, 10]
            },
            ('8-A', 'Nikson A.V.'): {
                'Math': [12, 11, 10, 7],
                'Ukr literature': [10, 11],
                'Chemistry': [9, 8, 10],
                'Physics': [10, 10, 7, 6],
                'PE': [7, 8, 9, 10]
            },
            ('5-C', 'Kozak A.S.'): {
                'Math': [9, 10, 10, 10],
                'Ukr literature': [9, 10],
                'History': [6, 10, 11, 8],
                'English': [5, 12, 10, 11],
                'PE': [9, 8, 6, 4]
            },
            ('5-B', 'Moliga T.P.'): {
                'Math': [11, 11, 11, 10],
                'Ukr literature': [12, 10, 11],
                'History': [10, 10, 11, 12],
                'English': [11, 10, 12, 10, 11],
                'PE': [10, 10, 10, 10]
            },
            ('5-C', 'Vinnichenko D.R.'): {
                'Math': [10, 10, 10, 10],
                'Ukr literature': [11, 10],
                'History': [9, 10, 11, 12],
                'English': [11, 12, 7, 9, 10],
                'PE': [5, 5, 8, 9]
            }
        }

    def test_children_list(self):

        result = children_list(self.data, '5-C')
        expected = ['Kozak A.S.', 'Vinnichenko D.R.']
        self.assertEqual(result, expected)

        result = children_list(self.data, '8-A')
        expected = ['Soroka I.I.', 'Nikson A.V.']
        self.assertEqual(result, expected)

        result = children_list(self.data, '10-A')  # Класу не існує
        expected = []
        self.assertEqual(result, expected)

    def test_subject_best_children(self):

        result = subject_best_children(self.data, 'Math')
        expected = {'8': ['Soroka I.I.', 'Nikson A.V.'], '5': ['Moliga T.P.']}
        self.assertEqual(result, expected)

        result = subject_best_children(self.data, 'Chemistry')
        expected = {'8': ['Nikson A.V.']}
        self.assertEqual(result, expected)

        result = subject_best_children(self.data, 'History')
        expected = {'5': ['Moliga T.P.', 'Vinnichenko D.R.']}
        self.assertEqual(result, expected)

        result = subject_best_children(self.data, 'Media Training')  # Предмет не існує
        expected = {}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()