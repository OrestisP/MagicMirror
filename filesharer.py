from filestack import Client

class FileSharer:
    '''
    uploads files into the cloud of filestack, creates a link and then allows us to send
    the link to others so that they can download the file.
    '''
    def __init__(self, filepath, api_key='AWqboQP1cQ4e4sKLo0JQ9z'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url