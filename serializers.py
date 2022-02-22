from typing import Optional, List

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel


class CommentsModel(BaseModel):
    id: int
    user_id: int
    post_id: int
    body: str


class PostModel(BaseModel):
    id: int
    user_id: int
    title: str
    body: str
    comments: Optional[List[CommentsModel]]
    # comments: list[CommentsModel] | None


class UserModel(BaseModel):
    id: int
    name: str
    address: str
    phone_number: str
    sex: str
    posts: Optional[List[PostModel]]
    comments: Optional[List[CommentsModel]]
    # posts: list[PostModel] | None
    # comments: list[CommentsModel] | None


class CommentGrapheneModel(PydanticObjectType):
    class Meta:
        model = CommentsModel


class PostGrapheneModel(PydanticObjectType):
    class Meta:
        model = PostModel


class UserGrapheneModel(PydanticObjectType):
    class Meta:
        model = UserModel


class CommentGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = CommentsModel
        exclude_fields = ('id', )


class PostGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = PostModel
        exclude_fields = ('id', 'comments')


class UserGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ('id', 'posts', 'comments')
