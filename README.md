# UEFA_CL_Predicciones

dejame en paz, aprobado con un 8

El enlace al repositorio de GitHub es el siguiente: [https://github.com/MiguelGG03/UEFA_CL_Predicciones.git](https://github.com/MiguelGG03/UEFA_CL_Predicciones.git)

## Inicialmente

Inicialmente este proyecto se basaba en un modelo más simple, el cual era un arbol de decisión entrenado con los datos de puntuaciones generales de los equipos de la Champions League de los últimos 8 años.

Este modelo devolvía como ganador al Manchester-City, lo cual tenía sentido por su trayectoría ascendente en los últimos años.

## Cambio de idea

La idea que se desarrolló inicialmente cambió cuando llegó un nuevo enfoque al aula. `"No tiene sentido que las victorias las determine el equipo como tal (la entidad deportiva). La victoria de un equipo esta determinada por muchos otros factores, entre ellos, de los que más peso tienen son los jugadores."`

Desde entonces el efoque del proyecto cambió, porque si es relevante saber qué equipos se enfrentan, porque "el escudo pesa", pero es mucho más importante saber qué jugadores lo hacen, y qué rendimiento están teniendo ultimamente.

Hay muchos otros factores que también son relevantes como los puntos fuertes ydebiles de los propios jugadores, dónde se juegan los partidos, incluso el contexto de algunos jugadores puede ser determinante.

Como llevar un proyecto de predicción tan realista lleva mucho trabajo y por plazos no iba a ser posible desarrollar esto, he decidido hacer algo más minimalista pero con una intención similar.

### Idea incial

Mi idea inicial era desarrollar un GPT o un agente de IA que usase una base de datos para cada jugador (RAG), pero poco después de comenzar me dí cuenta de que era demasiado trabajo igualmente, por lo que lo reducí a una única base de datos que tendría una colección por equipo clasificado.

En cuanto al tema datos, inicialmente pensé en scrapear el transfermarkt con un tutorial que encontré explorando en kaggle. Tambén suponía mucho trabajo, por lo que me limité a la descarga de las estadísticas de los jugadores en la misma competición pero de un año anterior.

Esto cambia un poco la realidad del asunto pero para hacer un proyecto predictivo podría valer. En cuanto a los GPT, decidí reducirlos a un GPT por equipo, los cuales estarían comunicados entre sí para saber que jugadores pesan más frente a otros  que no llevara un lio un único agente.

Finalmente todo esto se vió reducido a un único agente entrenado con la base de datos al completo.

### Base de datos de MongoDB a FAISS

Después de explorar y entender un poco el funcionamiento de los GPT, o en mi caso de LLaMA3, entendí que para crear un RAG de el mismo necesito que mi base de datos sea vectorial, por lo que debo transformar los datos de MongoDB a la base de datos FAISS

### Haciendo un RAG con LLaMA 3

Ya que me resultó imposible transformar la base de datos MongoDB a FAISS, he decicido usar la documentación oficial de LLaMA para poder [hacer un RAG con LLaMA 3](https://docs.llamaindex.ai/en/stable/optimizing/building_rag_from_scratch/)
