import os
import dropbox
from dropbox.files import WriteMode


class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFile(self, file_from, file_to):
        drop = dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                local_path = os.path.join(root, fileName)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    drop.files_upload(f.read(), dropbox_path,
                                      mode=WriteMode('overwrite'))


def main():
    access_token = 'sl.AxzcC9LKrIIOenS83jk-eRpT51AJ44MyotHxBOtm8Z_bMojEU7cyMI2tIYey6lmN-o8zlPLexfWBIaB2PYYpbaSx1aIftwmG8kWvFB1dNDC-rJBjHmW4-OptW_4O8_2CamdKfa0'
    transferData = TransferData(access_token)
    file_from = input("Enter the folder path to transfer : -")
    file_to = input("Enter the path to upload to dropbox:- ")
    transferData.uploadFile(file_from, file_to)
    print("File successfully moved")


main()
