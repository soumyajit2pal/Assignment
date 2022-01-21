from .configurations import getConfig

class ApiResources:
    CreateNewRepo_POST = 'user/repos'
    deleteRepo_DELETE = 'repos/' + getConfig()['con_config']['username'] + '/'
    getSpecificRepo_GET = 'repos/' + getConfig()['con_config']['username'] + '/'
    updaterepo_PATCH = '/repos/' + getConfig()['con_config']['username'] + '/'
