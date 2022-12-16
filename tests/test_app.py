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
        #test index page
        r = requests.get('http://localhost:5000')
        self.assertEqual(r.status_code, 200)

    # check for the response 200 on the index page
    def test_2(self):
        #test about page
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
        #test add item
        r = requests.get('http://localhost:5000/todos')
        self.assertEqual(r.status_code, 200)
        r = requests.post(url= 'http://localhost:5000/todos', data = data )
        # client = app.test_client()
        #
        # # Use the test client to send a POST request to the add route
        # response = client.post('/add', data={'title': 'Learn Flask'})
        # status code must equal to 302-redirect
        self.assertEqual(r.status_code, 200)

        # response = requests.post('http://localhost:5000/add', data={'title': 'Learn Flask'})
        self.assertEqual(r.json(), data)
    def test_4(self):
        #test update item
        # r = requests.get('http://localhost:5000/delete/0')
        client = app.test_client()
        response = client.get('/update/0')
        # status code must equal to 302-redirect
        self.assertEqual(response.status_code, 302)
        # Use the test client to send a POST request to the add route
        client.post('/update/0', data={'updated_item_text': 'new todo item'})
        self.assertEqual(todo_list[0], 'new todo item')





if __name__ == '__main__':
    unittest.main()
