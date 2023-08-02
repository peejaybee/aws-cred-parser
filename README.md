A module to read BASH files and print the credentials in JSON suitable for 
inclusion in `launch.json`

```
#  this comes from the SSO launch page 
export AWS_ACCESS_KEY_ID="access_key_id"
export AWS_SECRET_ACCESS_KEY="secret_key"
export AWS_SESSION_TOKEN="session_token"
```

becomes

```
{
            "AWS_ACCESS_KEY_ID": "access_key_id",
            "AWS_SECRET_ACCESS_KEY": "secret_key",
            "AWS_SESSION_TOKEN": "session_token"
}

```