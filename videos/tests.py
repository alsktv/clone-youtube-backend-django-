from rest_framework.test import APITestCase   #이건 어따가 사용하는 거지? api를 테스트 하는대 사용 할 듯.
from rest_framework_simplejwt.tokens import RefreshToken
from . import models
from users.models import User


class TestVideos(APITestCase):

  def setUp(self):   #test하기 전 setUp 함수를 먼저 실행해줌
    models.Video.objects.create(
        video = "fjdkfj",
        name = "fff",
        description = "fdfdfdfdf",
        view_count = 3, 
    )
  
  def test_all_videos(self):

    response = self.client.get("/api/v1/videos/" )  #client이용하면 http요청을 보내서 값을 가져옴. 이후 그것을 가상의 데이터베이스에 저장함.
    data = response.json()

    self.assertEqual(response.status_code , 200 , "Status code isn't 200")

    self.assertIsInstance(data , list)

    self.assertEqual(len(data) ,1)
    self.assertEqual(data[0]["name"] ,"fff" )

  def test_create_video(self):
    response = self.client.post("/api/v1/videos/" , data={
                                                 "video":"fff",
                                                 "name":"ffffff",
                                                 "description":"eeee",
                                                          }) 
    data = response.json()

    self.assertEqual(response.status_code , 200 , "not 200 status code")


