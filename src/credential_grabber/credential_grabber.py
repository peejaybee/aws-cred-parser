import json
import os


class CredentialGrabber:

    def find_latest_filename(self) -> str:
        dirents = os.scandir('credential_files')
        filename = ''
        modtime = 0
        for dirent in dirents:
            stat = dirent.stat()
            this_mtime = stat.st_mtime
            if this_mtime > modtime:
                modtime = this_mtime
                filename = dirent.name

        return filename

    def extract_quoted_string(self, quoted_string):
        return quoted_string[1:-1]

    def get_credentials(self):

        filename = f'credential_files/{self.find_latest_filename()}'
        cred_dict = {}
        with open(filename, encoding='utf-8') as f:
            for ln in f:
                parts = ln.split(' ')[1].split('=')
                cred_dict[parts[0]] = self.extract_quoted_string(
                    parts[1].replace('\n', '')
                    )
        return cred_dict


if __name__ == '__main__':
    creds = CredentialGrabber().get_credentials()
    print(json.dumps(creds, indent=12))
