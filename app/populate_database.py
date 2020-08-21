from describe.word.models import (
    Base,
    CategoryModel,
    db_session,
    DefinitionModel,
    engine,
    LanguageModel,
    WordModel,
)


Base.metadata.create_all(bind=engine)

entities = [
    WordModel(
        word="Foo",
        definition=[
            DefinitionModel(text="This is a foo description"),
            DefinitionModel(text="This is another foo description")
        ],
        language=[
            LanguageModel(name="english")
        ],
        category=[
            CategoryModel(topic="other")
        ]
    ),
]

for entity in entities:
    db_session.add(entity)

db_session.commit()
