import strawberry
from .types import UserType
from .quries import get_user

@strawberry.type
class Query :
  user : UserType = strawberry.field(resolver = get_user)