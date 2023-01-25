# Note Scripting App

This is a python notes scripting App which uses an API

## Installation
```
pip install -r requirments.txt
```

## Usage

* Create note

```
python main.py create-note "note-content"
```

* Fetch notes

```
python main.py fetch-notes
```

* Delete note

```
python main.py delete-note <id-of-note>
```

* Update note

```
python main.py update-note <id-of-note> "new note content"
```

## Note

note content should be in json format
```
{"content": content}
```
