import requests
import sys

def create_note(content):
    url = 'https://63a52acf821953d4f2c41d5e.mockapi.io/api/v1/notes'
    data = {"content": content}
    response = requests.post(url, json=data)
    print(response.json())

def fetch_notes():
    url = 'https://63a52acf821953d4f2c41d5e.mockapi.io/api/v1/notes'
    response = requests.get(url)
    print(response.json())

    
def delete_note(id):
    note_id = sys.argv[1]
    url = f'https://63a52acf821953d4f2c41d5e.mockapi.io/api/v1/notes/{note_id}'
    response = requests.delete(url)
    print(response.json())


def update_note(id, content):
    note_id = sys.argv[2]
    url = f'https://63a52acf821953d4f2c41d5e.mockapi.io/api/v1/notes/{note_id}'
    data = {"content": content}
    response = requests.put(url, json=data)
    print(response.json())

if __name__ == "__main__":
    if sys.argv[1] == "create-note":
        create_note(sys.argv[2])
    elif sys.argv[1] == "fetch-notes":
        fetch_notes()
    elif sys.argv[1] == "delete-note":
        delete_note(sys.argv[2])
    elif sys.argv[1] == "update-note":
        update_note(sys.argv[2], sys.argv[3])
    else:
        print("Invalid command.\n Use 'create-note', 'fetch-notes', 'delete-note', or 'update-note'.")
