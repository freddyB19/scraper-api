import strawberry

from . import types

@strawberry.type
class Query:
	@strawberry.field
	def user(self) -> types.User:
		return types.User(name = "freddy", age = 27)

