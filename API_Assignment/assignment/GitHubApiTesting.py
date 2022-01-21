from payLoad import *
from restAPIUtility import RestApi
from utility.resources import  ApiResources
from payLoad import CreateRepoPayload
class GITHub(RestApi):


    # this will return all repo of user
    def getAllReposOfUser(self):
        self.url = self.baseURL+ 'user/repos'
        self.statusCode, self.response = self.GET_Method(self.url, self.auth,)
        with open('getAllReposOfUser.txt', 'w') as f:
            f.write(str(self.response))
        print(self.statusCode)

# To create new repo
    def CreateNewRepo(self, name_repo):

        self.name_repo = name_repo
        self.url = self.baseURL+ ApiResources.CreateNewRepo_POST
        self.payload = CreateRepoPayload(self.name_repo, 'This is test repo for tetsing api')
        self.headers = {"Content-Type":"application/json; charset=utf-8"}
        self.statusCode, self.response = self.POST_Method(self.url, self.payload, self.auth, self.headers)
        with open('CreateNewRepo_response.txt', 'w') as f:
            f.write(str(self.response))
        print(self.statusCode)

# It will return all Public and Private repo
    def getPublic_Private_Any_repo_Details(self, name_repo):
        self.name_repo = name_repo
        self.url = self.baseURL+ ApiResources.getSpecificRepo_GET+self.name_repo
        self.statusCode, self.response = self.GET_Method(self.url, self.auth,)
        with open('getPublic_Private_Any_repo_Details.txt', 'w') as f:
            f.write(str(self.response))
        print(self.statusCode)

# It will update repo details like you can make repo private or public/ Descriptions
    def UpdateRepoUsingPATCHMethod(self, name_repo):
        self.name_repo = name_repo
        self.url = self.baseURL+ ApiResources.getSpecificRepo_GET+self.name_repo
        self.payload = UpdateRepoPayload()
        self.headers = {"Content-Type":"application/json; charset=utf-8"}
        self.statusCode, self.response = self.PATCH_Method(self.url, self.payload, self.auth, self.headers)
        with open('UpdateRepoUsingPATCHMethod.txt', 'w') as f:
            f.write(str(self.response))
        print(self.statusCode)

# it will delete repo

    def DeleteGITHubRepo(self, name_repo):
         self.name_repo = name_repo
         self.url = self.baseURL+ ApiResources.deleteRepo_DELETE+self.name_repo
         print(self.url)
         self.statusCode = self.DELETE_METHOD(self.url, self.auth)
         assert self.statusCode == 204
         if self.statusCode == 204:
             print("Deletion Done")
             assert self.statusCode == 204
         else:
            print(self.statusCode)


git = GITHub()
git.getAllReposOfUser()
git.CreateNewRepo("TestingRepo")
git.getPublic_Private_Any_repo_Details("TestingRepo")
git.UpdateRepoUsingPATCHMethod("TestingRepo")
git.DeleteGITHubRepo("TestingRepo")

