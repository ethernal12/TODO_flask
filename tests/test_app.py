try:
    import requests
    import unittest
    import json
    from jsonschema import validate
except Exception as e:
    print(e)

def validate_json_syntax(data):
    try:
        return json.loads(data)
    except ValueError:
        print('DEBUG: JSON data contains an error')
        return False

class Tests(unittest.TestCase):

    # check for the response 200 on the index page
    def test_index_page(self):
        r = requests.get('http://localhost:5000')
        schema = {
            "type": "object",
            "properties": {
                "Data": {
                    "type": "string"
                }
            },
            "required": [
                "Data"
            ]
        }
        # data2 = f"Response: {r.json()}"

        data = {'Data' : 'Abouts'}

        try:
            print(validate(data, schema), 'validate')
        except Exception as e:
            print(e)
        self.assertEqual(r.status_code, 200)

    # check for the response 200 on the index page
    def test_about_page(self):
        schema = {
            "type": "object",
            "properties": {
                "Data": {
                    "type": "string"
                }
            },
            "required": [
                "Data"
            ]
        }
        r = requests.get('http://localhost:5000/About')
        data2 = json.loads(r.text)

        self.assertEqual(validate(data2, schema),None)

        self.assertEqual(r.status_code,200)


if __name__ == '__main__':
    unittest.main()
