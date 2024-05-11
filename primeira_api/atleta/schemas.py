from typing import Annotated, Optional
from pydantic import Field, PositiveFloat, PositiveInt
from primeira_api.categorias.schemas import CategoriaIn
from primeira_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from primeira_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678999', max_length=11)]
    idade: Annotated[PositiveInt, Field(description='Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=68.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.75)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]

class AtletaIn(Atleta):
    pass

class AtletaOut(OutMixin):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678999', max_length=11)]
    pass

class AtletaOut1(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[PositiveInt], Field(None, description='Idade do atleta', example=25)]
    pass