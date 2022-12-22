try:
    import requests
    import unittest
    import json
    from jsonschema import validate
    from app import app
    from app import todo_list
except Exception as e:
    print(e)

todo_length = 0


class Tests(unittest.TestCase):

    # check for the response 200 on the index page
    def test_1(self):
        # test all routes statuses
        index = requests.get('http://localhost:5000')

        self.assertEqual(index.status_code, 200)

    # check for the response 200 on the index page
    def test_2(self):
        # test about page
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

        self.assertEqual(validate(data2, schema), None)

        self.assertEqual(r.status_code, 200)

    def test_3(self):
        data = {'title': 'new todo'}
        # test add item
        req2 = requests.post(url='http://localhost:5000/todos', data=data)
        req3 = requests.get(url='http://localhost:5000/todos')

        self.assertEqual(req2.status_code, 200)
        # if new todo item is in the todo_list
        self.assertIn(data['title'], req3.json())

    def test_4(self):
        #test update item
        data = {'title': 'new todo_update'}
        req = requests.put(url='http://localhost:5000/todos/0', data=data)
        req1 = requests.get(url='http://localhost:5000/todos/0', data=data)
        self.assertEqual(req.status_code, 200)
        self.assertEqual(data, req1.json())
    def test_5(self):
        #test delete item
        req  =requests.delete(url='http://localhost:5000/todo/0')
        req1 = requests.get(url='http://localhost:5000/todos/')
        self.assertEqual(req.status_code, 200)
        self.assertEqual(len(req1.json()), 0)

if __name__ == '__main__':
    unittest.main()
