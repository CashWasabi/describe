import graphene
from describe.word.models import (
    CategoryModel,
    db_session,
    DefinitionModel,
    LanguageModel,
    WordModel,
)
from graphene import relay
from graphene_sqlalchemy import (
    SQLAlchemyConnectionField,
    SQLAlchemyObjectType,
)


db_session = db_session


class LanguageNode(SQLAlchemyObjectType):
    class Meta:
        model = LanguageModel
        interfaces = (relay.Node, )


class LanguageConnection(relay.Connection):
    class Meta:
        node = LanguageNode


class CategoryNode(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel
        interfaces = (relay.Node, )


class CategoryConnection(relay.Connection):
    class Meta:
        node = CategoryNode


class DefinitionNode(SQLAlchemyObjectType):
    class Meta:
        model = DefinitionModel
        interfaces = (relay.Node, )


class DefinitionConnection(relay.Connection):
    class Meta:
        node = DefinitionNode


class WordNode(SQLAlchemyObjectType):
    class Meta:
        model = WordModel
        interfaces = (relay.Node, )


class WordConnection(relay.Connection):
    class Meta:
        node = WordNode


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    language = SQLAlchemyConnectionField(LanguageConnection)
    tags = SQLAlchemyConnectionField(TagConnection)
    definitions = SQLAlchemyConnectionField(DefinitionConnection)
    words = SQLAlchemyConnectionField(WordConnection)


schema = graphene.Schema(query=Query)
