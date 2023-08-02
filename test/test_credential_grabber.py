from src.credential_grabber import credential_grabber


class TestCredentialGrabber:

    subject = credential_grabber.CredentialGrabber()

    def test_get_credentials(self):
        creds = self.subject.get_credentials()

        assert creds['AWS_ACCESS_KEY_ID'] == 'access_key_id'
        assert creds['AWS_SECRET_ACCESS_KEY'] == 'secret_key'
        assert creds['AWS_SESSION_TOKEN'] == 'session_token'

    def test_extract_quoted_string(self):
        string_contents = self.subject.extract_quoted_string('"fubar"')
        assert string_contents == 'fubar'

    def test_find_latest_filename(self):

        filename = self.subject.find_latest_filename()
        assert filename == 'credentials_2.sh'
