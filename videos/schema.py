import strawberry
import typing
from . import types
from . import queries

@strawberry.type
class Query:
  all_videos: typing.List[types.Video] = strawberry.field(resolver=queries.get_all_videos)