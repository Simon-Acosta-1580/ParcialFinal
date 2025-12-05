from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class JugadorBase(SQLModel):
    name: str = Field(index=True, description="Nombre del jugador", unique=True)
    number: int = Field(default=0, description="Numero del jugador", unique=True)
    year: int = Field(default=0, description="Año en qe nacio el jugador")
    img: Optional[str] = Field(default=None, description="Foto del jugador")
    born: str = Field(index=True, description="Nacionalidad del jugador")
    status: bool = Field(default=True, description="Activo o Inactivo")
    height: float = Field(default=0.0, description="Altura del jugador")
    peso: float = Field(default=0.0, description="Peso del jugador")
    pie: str = Field(index=True, description="Pie dominante del jugador")
    posicion: str = Field(index=True, description="Posicion del jugador")
    valor: float = Field(default=0.0, description="Altura del jugador")
    ingreso: int = Field(default=0, description="Año en que llego el jugador")
    statusFisico: str = Field(default="sin lesion", description="Posicion del jugador")
    suspendido: bool = Field(default= False, description= "Jugador suspendido o no suspndido" )

class EstadisticaBase(SQLModel):
    tiempoCancha: int = Field(default=0, description="Tiempo en cancha del jugador")
    goles: int = Field(default=0, description="Goles del jugador")
    faltas: int = Field(default=0, description="Faltas del jugador")
    targetas: int = Field(default=0, description="Faltas del jugador")
    jugador_id: Optional[int] = Field(default=None, primary_key="jugador.id")

class PartidoBase(SQLModel):
    marcador: str = Field(index=True, description="goles de sigmotoa FC - goles del otro equipo")
    resultado: str = Field(index=True, description="Victoria, Derrota, Empate")
    tandaPenal: Optional[str]= Field(index=True, description="marcador de la tanda, goles de sigmotoa FC - goles del otro equipo")
    Localidad: str = Field(index=True, description="Local o Visitante")
    estadistica_id: Optional[int] = Field(default=None, foreign_key="estadistica.id")