# Async code VS Sync code

## compare async and sync

In assginment0 there are two python files: One has an example f sync code and the other one has an example of async code.

async_marriage.py take least time rather than sync_marriage.py

### download_printer_ai

In this file I write a code and I suppose that there  would be three prolong processes like downloading and printing and an AI process.

To handle these three process I use async in processes that not related to each other.

when I want to use a process which results is needed for other functions, I call that process with "await" to wait for its result.

# Use three API with async

In assignment1 I use async to handle using three api and beside that I try to increase the running speed of the code.

To run ```main.py``` in this folder you need to make a .env file and put and api_key in it which name is "API_KEY_RHYME".
