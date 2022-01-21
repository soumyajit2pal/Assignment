def CreateRepoPayload(repo_name, description):
    body = {

        "name": repo_name,
        "description": description,
        "homepage": "https://github.com",
        "private": 'true'
    }
    return body


def UpdateRepoPayload():
    body ={
        "description": "Updating repo details here",
        "private": 'true'
    }
    return body
