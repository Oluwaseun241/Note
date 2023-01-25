import request

def create_note(content):
    url = 'https://63a52acf821953d4f2c41d5e.mockapi.io/api/v1/notes'
    data = {"content": content}
    response = request.post(url, json=data)
    print(response.json())

def fetch_notes():

    
def delete_note(id):


def update_note(id, content)
