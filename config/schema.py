import strawberry
import typing
from videos import schema as videos_schema
from users import schema as users_schema


@strawberry.type
class Movie:
  pk:int
  title: str
  year: int
  rating: int

@strawberry.type
class Query(videos_schema.Query , users_schema.Query): #여러개를 상속 받을 수 있음
   pass
 


schema = strawberry.Schema(query=Query)