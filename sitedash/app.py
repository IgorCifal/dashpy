import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import altair as alt


Dados_teste = [
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2020-04-09T08:38:22.040Z",
    "demissao": "None",
    "empregis": "None",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88684,
    "nomcid": "SOROCABA",
    "admissao": "2021-07-19T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21415,
    "nomcid": "QUIRINOPOLIS",
    "admissao": "2020-08-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 85448,
    "nomcid": "MOGI DAS CRUZES",
    "admissao": "2020-11-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SMOKERS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83518,
    "nomcid": "GUARATINGUETA",
    "admissao": "2021-03-22T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88862,
    "nomcid": "TANABI",
    "admissao": "2021-03-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88684,
    "nomcid": "SOROCABA",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-03-22T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18619,
    "nomcid": "ARAGARCAS",
    "admissao": "2021-10-18T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2021-12-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2021-12-13T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88684,
    "nomcid": "SOROCABA",
    "admissao": "2022-04-18T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86568,
    "nomcid": "PIEDADE",
    "admissao": "2023-01-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-01-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 31534,
    "nomcid": "JOAO PINHEIRO",
    "admissao": "2023-04-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21474,
    "nomcid": "RIO VERDE",
    "admissao": "2023-03-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-03-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81345,
    "nomcid": "BATATAIS",
    "admissao": "2023-11-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81086,
    "nomcid": "AVARE",
    "admissao": "2023-11-21T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81370,
    "nomcid": "BAURU",
    "admissao": "2024-01-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 34010,
    "nomcid": "PATOS DE MINAS",
    "admissao": "2024-04-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80829,
    "nomcid": "ARACATUBA",
    "admissao": "2024-04-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2024-09-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 41378,
    "nomcid": "TRES LAGOAS",
    "admissao": "2024-09-23T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81990,
    "nomcid": "CAMPINAS",
    "admissao": "2019-11-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21784,
    "nomcid": "SAO LUIS DE MONTES BELOS",
    "admissao": "2021-02-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-06-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-02-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2022-10-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83631,
    "nomcid": "HORTOLANDIA",
    "admissao": "2024-07-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2024-10-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19917,
    "nomcid": "GOIAS",
    "admissao": "2023-01-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-03-22T00:00:00.000Z",
    "demissao": "None",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2022-03-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40851,
    "nomcid": "NOVA ANDRADINA",
    "admissao": "2024-11-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 56995,
    "nomcid": "LONDRINA",
    "admissao": "2024-11-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18511,
    "nomcid": "ANAPOLIS",
    "admissao": "2021-03-22T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19321,
    "nomcid": "CERES",
    "admissao": "2021-09-20T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21318,
    "nomcid": "PORANGATU",
    "admissao": "2021-11-22T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 20818,
    "nomcid": "NIQUELANDIA",
    "admissao": "2023-12-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-10-15T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83186,
    "nomcid": "FRANCISCO MORATO",
    "admissao": "2022-10-17T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2024-12-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - ADM",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21474,
    "nomcid": "RIO VERDE",
    "admissao": "2024-06-18T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - ADM GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 20303,
    "nomcid": "JATAI",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - ADM GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39209,
    "nomcid": "UBERABA",
    "admissao": "2023-10-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83097,
    "nomcid": "FERNANDOPOLIS",
    "admissao": "2023-02-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - JBZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88323,
    "nomcid": "SAO JOSE DO RIO PRETO",
    "admissao": "2023-02-24T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - JBZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 20575,
    "nomcid": "MINEIROS",
    "admissao": "2025-01-07T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87599,
    "nomcid": "SALTO",
    "admissao": "2025-02-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83178,
    "nomcid": "FRANCA",
    "admissao": "2022-09-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - CTR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81990,
    "nomcid": "CAMPINAS",
    "admissao": "2025-02-18T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86665,
    "nomcid": "PIRACICABA",
    "admissao": "2021-07-19T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80616,
    "nomcid": "AMERICANA",
    "admissao": "2023-06-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19070,
    "nomcid": "CALDAS NOVAS",
    "admissao": "2025-03-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 85464,
    "nomcid": "MOGI MIRIM",
    "admissao": "2022-01-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 85464,
    "nomcid": "MOGI MIRIM",
    "admissao": "2022-02-07T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86908,
    "nomcid": "PORTO FERREIRA",
    "admissao": "2022-06-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-08-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84140,
    "nomcid": "ITAPETININGA",
    "admissao": "2025-02-18T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81990,
    "nomcid": "CAMPINAS",
    "admissao": "2025-02-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-04-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80870,
    "nomcid": "ARARAQUARA",
    "admissao": "2021-05-17T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86665,
    "nomcid": "PIRACICABA",
    "admissao": "2025-04-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-05-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40207,
    "nomcid": "CAMPO GRANDE",
    "admissao": "2025-05-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-05-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2025-06-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 95583,
    "nomcid": "CEILANDIA",
    "admissao": "2025-05-20T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - DF",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86762,
    "nomcid": "PITANGUEIRAS",
    "admissao": "2023-11-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-06-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-08-15T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 34851,
    "nomcid": "POCOS DE CALDAS",
    "admissao": "2019-11-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MG",
    "codempresa": 2,
    "descricao": "ARAPIRACA"
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-11-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80640,
    "nomcid": "AMPARO",
    "admissao": "2022-06-13T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-11-17T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21474,
    "nomcid": "RIO VERDE",
    "admissao": "2023-06-19T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-05-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81612,
    "nomcid": "BOTAFOGO",
    "admissao": "2023-08-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87980,
    "nomcid": "SANTO ANDRE",
    "admissao": "2021-10-18T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40207,
    "nomcid": "CAMPO GRANDE",
    "admissao": "2025-06-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-06-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-12-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-06-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-06-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "AUTO POSTO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 85880,
    "nomcid": "NOVA ODESSA",
    "admissao": "2025-07-15T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-03-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-04-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-04-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 20281,
    "nomcid": "JANDAIA",
    "admissao": "2025-07-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21474,
    "nomcid": "RIO VERDE",
    "admissao": "2025-08-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 41378,
    "nomcid": "TRES LAGOAS",
    "admissao": "2025-08-19T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84352,
    "nomcid": "ITU",
    "admissao": "2025-09-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2025-07-22T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-08-15T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87327,
    "nomcid": "RIBEIRAO PRETO",
    "admissao": "2025-08-19T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - RWR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2020-11-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2023-04-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-01-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-06-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2021-04-12T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87041,
    "nomcid": "PRESIDENTE PRUDENTE",
    "admissao": "2023-05-08T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-11-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-11-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 31240,
    "nomcid": "ITURAMA",
    "admissao": "2025-09-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2025-09-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81329,
    "nomcid": "BARUERI",
    "admissao": "2024-07-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-11-21T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-08-15T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2021-07-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-02-20T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2025-07-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-05-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81531,
    "nomcid": "BOITUVA",
    "admissao": "2025-10-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-11-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84417,
    "nomcid": "JACAREI",
    "admissao": "2023-09-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88749,
    "nomcid": "SUZANO",
    "admissao": "2025-06-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 15890,
    "nomcid": "BRASILIA",
    "admissao": "2020-12-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - DF",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-05-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-08-15T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-04-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-11-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84115,
    "nomcid": "ITANHAEM",
    "admissao": "2021-09-13T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81612,
    "nomcid": "BOTAFOGO",
    "admissao": "2025-11-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87211,
    "nomcid": "REGISTRO",
    "admissao": "2022-07-18T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-11-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2009-11-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "AUTO POSTO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82163,
    "nomcid": "CARAGUATATUBA",
    "admissao": "2024-10-15T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-05-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82163,
    "nomcid": "CARAGUATATUBA",
    "admissao": "2023-11-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 108384,
    "nomcid": "EMBU DAS ARTES",
    "admissao": "2025-11-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-11-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-11-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-06-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "AUTO POSTO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-09-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CONVENIENCIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86045,
    "nomcid": "OSASCO",
    "admissao": "2025-07-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2025-12-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2025-12-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SMOKERS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2022-11-07T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2025-03-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-03-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88323,
    "nomcid": "SAO JOSE DO RIO PRETO",
    "admissao": "2022-12-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-07-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-09-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84492,
    "nomcid": "JALES",
    "admissao": "2026-01-13T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - JBZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2015-07-13T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2014-04-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "None",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": "None",
    "nomcid": "None",
    "admissao": "2023-04-24T00:00:00.000Z",
    "demissao": "None",
    "empregis": "None",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2017-06-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2014-06-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 89559,
    "nomcid": "VOTUPORANGA",
    "admissao": "2016-08-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "ARAPIRACA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-01-12T07:48:00.000Z",
    "demissao": "None",
    "empregis": "None",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-05-13T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 8,
    "descricao": "FILIAL BRASILIA"
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2015-10-15T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SMOKERS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-09-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2014-06-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - RWR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2017-08-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2015-01-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 85235,
    "nomcid": "MARILIA",
    "admissao": "2015-09-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81370,
    "nomcid": "BAURU",
    "admissao": "2014-10-13T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2015-01-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87327,
    "nomcid": "RIBEIRAO PRETO",
    "admissao": "2022-06-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - RWR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2019-10-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2015-05-20T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81124,
    "nomcid": "BADY BASSITT",
    "admissao": "2022-09-17T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - JBZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2020-11-23T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2016-11-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "ARAPIRACA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80870,
    "nomcid": "ARARAQUARA",
    "admissao": "2016-11-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2016-09-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88323,
    "nomcid": "SAO JOSE DO RIO PRETO",
    "admissao": "2022-09-17T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - JBZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2016-03-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83178,
    "nomcid": "FRANCA",
    "admissao": "2022-09-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - CTR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2016-12-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80829,
    "nomcid": "ARACATUBA",
    "admissao": "2024-09-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "LIKEBRANDS",
    "codempresa": 10,
    "descricao": "FILIAL RIO"
  },
  {
    "codcid": 85413,
    "nomcid": "MIRASSOL",
    "admissao": "2022-09-17T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - JBZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86045,
    "nomcid": "OSASCO",
    "admissao": "2016-10-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-10-08T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80616,
    "nomcid": "AMERICANA",
    "admissao": "2016-12-15T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-04-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84034,
    "nomcid": "IRAPURU",
    "admissao": "2017-02-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83178,
    "nomcid": "FRANCA",
    "admissao": "2021-03-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88331,
    "nomcid": "SAO JOSE DOS CAMPOS",
    "admissao": "2021-03-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2017-03-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87041,
    "nomcid": "PRESIDENTE PRUDENTE",
    "admissao": "2017-03-08T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-11-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39209,
    "nomcid": "UBERABA",
    "admissao": "2022-07-18T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - ADM",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84921,
    "nomcid": "LIMEIRA",
    "admissao": "2021-03-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 28797,
    "nomcid": "DIVINOPOLIS",
    "admissao": "2017-06-26T00:00:00.000Z",
    "demissao": "None",
    "empregis": "None",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88315,
    "nomcid": "SAO JOSE DO RIO PARDO",
    "admissao": "2017-07-31T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SMOKERS",
    "codempresa": 6,
    "descricao": "CIFAL GO"
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2018-01-08T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2017-10-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "None",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88137,
    "nomcid": "SAO BERNARDO DO CAMPO",
    "admissao": "2021-03-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 8,
    "descricao": "FILIAL BRASILIA"
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2021-03-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2021-03-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 8,
    "descricao": "FILIAL BRASILIA"
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2018-04-12T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2018-04-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84522,
    "nomcid": "JANDIRA",
    "admissao": "2025-01-07T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84700,
    "nomcid": "JUNDIAI",
    "admissao": "2018-05-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2018-05-07T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2018-05-23T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 31224,
    "nomcid": "ITUIUTABA",
    "admissao": "2023-01-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - ADM",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 20257,
    "nomcid": "ITUMBIARA",
    "admissao": "2018-07-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 3,
    "descricao": "CIFAL MINAS"
  },
  {
    "codcid": 15890,
    "nomcid": "BRASILIA",
    "admissao": "2019-03-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - DF",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88200,
    "nomcid": "SAO JOAO DA BOA VISTA",
    "admissao": "2019-01-21T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2019-02-25T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2019-01-28T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81019,
    "nomcid": "ASSIS",
    "admissao": "2021-03-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-08-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2019-04-22T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-01-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - RWR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88684,
    "nomcid": "SOROCABA",
    "admissao": "2019-05-20T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SMOKERS",
    "codempresa": 6,
    "descricao": "CIFAL GO"
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2019-06-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 29866,
    "nomcid": "FRUTAL",
    "admissao": "2022-09-23T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - ADM",
    "codempresa": 2,
    "descricao": "ARAPIRACA"
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2019-08-26T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 20303,
    "nomcid": "JATAI",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - ADM GO",
    "codempresa": 3,
    "descricao": "CIFAL MINAS"
  },
  {
    "codcid": 15890,
    "nomcid": "BRASILIA",
    "admissao": "2019-10-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - DF",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2020-01-08T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2019-12-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2020-02-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-09-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2020-02-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81655,
    "nomcid": "BRAGANCA PAULISTA",
    "admissao": "2020-03-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 85308,
    "nomcid": "MAUA",
    "admissao": "2020-03-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 20443,
    "nomcid": "LUZIANIA",
    "admissao": "2020-03-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 3,
    "descricao": "CIFAL MINAS"
  },
  {
    "codcid": 105953,
    "nomcid": "AGUAS LINDAS DE GOIAS",
    "admissao": "2020-03-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 3,
    "descricao": "CIFAL MINAS"
  },
  {
    "codcid": 19283,
    "nomcid": "CATALAO",
    "admissao": "2020-03-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 3,
    "descricao": "CIFAL MINAS"
  },
  {
    "codcid": 25151,
    "nomcid": "ARAXA",
    "admissao": "2023-01-12T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - ADM",
    "codempresa": 2,
    "descricao": "ARAPIRACA"
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2020-05-25T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 3,
    "descricao": "CIFAL MINAS"
  },
  {
    "codcid": 39209,
    "nomcid": "UBERABA",
    "admissao": "2022-07-25T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - ADM",
    "codempresa": 2,
    "descricao": "ARAPIRACA"
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-11-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86991,
    "nomcid": "PRAIA GRANDE",
    "admissao": "2025-11-17T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2025-11-13T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-11-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-11-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88714,
    "nomcid": "SUMARE",
    "admissao": "2020-07-13T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2020-07-20T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-06-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-12-02T10:27:50.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87050,
    "nomcid": "PRESIDENTE VENCESLAU",
    "admissao": "2021-07-19T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-03-15T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-08-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87041,
    "nomcid": "PRESIDENTE PRUDENTE",
    "admissao": "2021-07-19T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-09-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80691,
    "nomcid": "ANDRADINA",
    "admissao": "2021-10-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18449,
    "nomcid": "ALTO PARAISO DE GOIAS",
    "admissao": "2021-09-20T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 22047,
    "nomcid": "TRINDADE",
    "admissao": "2022-02-07T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-12-20T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2022-03-07T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87327,
    "nomcid": "RIBEIRAO PRETO",
    "admissao": "2022-03-21T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87327,
    "nomcid": "RIBEIRAO PRETO",
    "admissao": "2022-06-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87327,
    "nomcid": "RIBEIRAO PRETO",
    "admissao": "2022-06-13T00:00:00.000Z",
    "demissao": "None",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40797,
    "nomcid": "NAVIRAI",
    "admissao": "2022-06-20T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2022-07-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88323,
    "nomcid": "SAO JOSE DO RIO PRETO",
    "admissao": "2022-07-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 85936,
    "nomcid": "NOVO HORIZONTE",
    "admissao": "2022-08-08T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-08-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 15890,
    "nomcid": "BRASILIA",
    "admissao": "2022-09-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - DF",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83178,
    "nomcid": "FRANCA",
    "admissao": "2022-09-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-06-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84980,
    "nomcid": "LOUVEIRA",
    "admissao": "2022-10-17T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-11-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21865,
    "nomcid": "SENADOR CANEDO",
    "admissao": "2022-11-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40320,
    "nomcid": "COXIM",
    "admissao": "2023-01-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18511,
    "nomcid": "ANAPOLIS",
    "admissao": "2023-01-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-01-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "ASTECA SHOP 12",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-10-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40207,
    "nomcid": "CAMPO GRANDE",
    "admissao": "2023-04-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-04-17T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40207,
    "nomcid": "CAMPO GRANDE",
    "admissao": "2023-04-17T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-05-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86746,
    "nomcid": "PIRASSUNUNGA",
    "admissao": "2023-06-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-05-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "AUTO POSTO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-09-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CONVENIENCIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-08-15T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2023-11-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-10-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-11-21T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-11-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-12-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "AUTO POSTO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 22047,
    "nomcid": "TRINDADE",
    "admissao": "2024-02-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81370,
    "nomcid": "BAURU",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81787,
    "nomcid": "CABREUVA",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84409,
    "nomcid": "JABOTICABAL",
    "admissao": "2024-02-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2024-05-07T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-09-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2024-12-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-02-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CONVENIENCIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39209,
    "nomcid": "UBERABA",
    "admissao": "2025-07-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - ADM",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87386,
    "nomcid": "RIO CLARO",
    "admissao": "2025-07-15T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2025-07-15T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-09-17T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CONVENIENCIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-10-07T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88099,
    "nomcid": "SANTOS",
    "admissao": "2025-10-07T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-10-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88099,
    "nomcid": "SANTOS",
    "admissao": "2025-10-07T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-10-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81990,
    "nomcid": "CAMPINAS",
    "admissao": "2025-10-21T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88161,
    "nomcid": "SAO CARLOS",
    "admissao": "2025-10-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2025-10-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "ASTECA SHOP 12",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87041,
    "nomcid": "PRESIDENTE PRUDENTE",
    "admissao": "2025-10-21T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2025-11-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SMOKERS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-11-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88331,
    "nomcid": "SAO JOSE DOS CAMPOS",
    "admissao": "2025-11-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19780,
    "nomcid": "FORMOSA",
    "admissao": "2025-12-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-12-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83631,
    "nomcid": "HORTOLANDIA",
    "admissao": "2025-12-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-12-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2025-12-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2025-12-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80616,
    "nomcid": "AMERICANA",
    "admissao": "2026-01-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 22047,
    "nomcid": "TRINDADE",
    "admissao": "2026-01-13T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21474,
    "nomcid": "RIO VERDE",
    "admissao": "2026-01-20T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2026-02-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87327,
    "nomcid": "RIBEIRAO PRETO",
    "admissao": "2016-11-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88862,
    "nomcid": "TANABI",
    "admissao": "2022-07-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TBSTORE - ADM",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2026-02-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81256,
    "nomcid": "BARRA BONITA",
    "admissao": "2024-10-08T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81795,
    "nomcid": "CACAPAVA",
    "admissao": "2024-11-12T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2019-10-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 3,
    "descricao": "CIFAL MINAS"
  },
  {
    "codcid": 84700,
    "nomcid": "JUNDIAI",
    "admissao": "2020-07-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-07-21T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88323,
    "nomcid": "SAO JOSE DO RIO PRETO",
    "admissao": "2019-10-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82171,
    "nomcid": "CARAPICUIBA",
    "admissao": "2020-05-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2020-04-14T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86070,
    "nomcid": "OURINHOS",
    "admissao": "2020-07-13T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2020-10-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2020-10-13T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-06-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83895,
    "nomcid": "INDAIATUBA",
    "admissao": "2020-11-23T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40959,
    "nomcid": "PARANAIBA",
    "admissao": "2020-12-07T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2021-01-18T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-02-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-02-08T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-04-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-05-17T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2021-04-12T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-11-04T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 15890,
    "nomcid": "BRASILIA",
    "admissao": "2021-07-05T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - DF",
    "codempresa": 18,
    "descricao": "FILIAL TO"
  },
  {
    "codcid": 83712,
    "nomcid": "IBITINGA",
    "admissao": "2025-09-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 15890,
    "nomcid": "BRASILIA",
    "admissao": "2022-05-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - DF",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86045,
    "nomcid": "OSASCO",
    "admissao": "2022-01-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-08-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "AUTO POSTO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81370,
    "nomcid": "BAURU",
    "admissao": "2024-03-19T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87670,
    "nomcid": "SANTA BARBARA D'OESTE",
    "admissao": "2025-02-11T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80888,
    "nomcid": "ARARAS",
    "admissao": "2025-04-15T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88510,
    "nomcid": "SAO VICENTE",
    "admissao": "2025-05-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-06-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-07-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2025-08-19T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87980,
    "nomcid": "SANTO ANDRE",
    "admissao": "2025-08-19T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88161,
    "nomcid": "SAO CARLOS",
    "admissao": "2025-10-01T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2025-12-16T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21695,
    "nomcid": "SANTO ANTONIO DO DESCOBERTO",
    "admissao": "2025-05-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-06-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-09-02T00:00:00.000Z",
    "demissao": "None",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88684,
    "nomcid": "SOROCABA",
    "admissao": "2025-10-07T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-10-07T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83178,
    "nomcid": "FRANCA",
    "admissao": "2026-01-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2026-01-06T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88137,
    "nomcid": "SAO BERNARDO DO CAMPO",
    "admissao": "2026-02-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81329,
    "nomcid": "BARUERI",
    "admissao": "2026-02-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82163,
    "nomcid": "CARAGUATATUBA",
    "admissao": "2026-02-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2026-02-09T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2026-01-21T00:00:00.000Z",
    "demissao": "None",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2026-02-03T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2026-02-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84131,
    "nomcid": "ITAPECERICA DA SERRA",
    "admissao": "2026-02-10T00:00:00.000Z",
    "demissao": "None",
    "empregis": "CIFAL - SP",
    "codempresa": "None",
    "descricao": "None"
  },
  {
    "codcid": 39586,
    "nomcid": "VICOSA",
    "admissao": "2021-11-22T00:00:00.000Z",
    "demissao": "2024-05-07T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-12-14T00:00:00.000Z",
    "demissao": "2024-05-09T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-04-18T00:00:00.000Z",
    "demissao": "2024-07-16T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-06-20T00:00:00.000Z",
    "demissao": "2024-03-11T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-04-03T00:00:00.000Z",
    "demissao": "2024-05-02T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81302,
    "nomcid": "BARRETOS",
    "admissao": "2023-06-05T00:00:00.000Z",
    "demissao": "2024-06-23T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 55298,
    "nomcid": "CURITIBA",
    "admissao": "2023-06-05T00:00:00.000Z",
    "demissao": "2024-06-18T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-07-03T00:00:00.000Z",
    "demissao": "2024-05-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-07-03T00:00:00.000Z",
    "demissao": "2024-03-01T00:00:00.000Z",
    "empregis": "UM3MEIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-07-17T00:00:00.000Z",
    "demissao": "2024-03-15T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2023-07-21T00:00:00.000Z",
    "demissao": "2024-08-01T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-09-18T00:00:00.000Z",
    "demissao": "2024-06-16T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-05-14T00:00:00.000Z",
    "demissao": "2024-05-19T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 54879,
    "nomcid": "CASCAVEL",
    "admissao": "2023-10-02T00:00:00.000Z",
    "demissao": "2024-04-03T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 25666,
    "nomcid": "BELO HORIZONTE",
    "admissao": "2023-10-16T00:00:00.000Z",
    "demissao": "2024-05-07T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 38547,
    "nomcid": "SETE LAGOAS",
    "admissao": "2023-11-06T00:00:00.000Z",
    "demissao": "2024-03-07T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 77755,
    "nomcid": "PALHOCA",
    "admissao": "2021-10-27T00:00:00.000Z",
    "demissao": "2024-02-06T00:00:00.000Z",
    "empregis": "CIFAL - SC",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 77755,
    "nomcid": "PALHOCA",
    "admissao": "2023-12-12T00:00:00.000Z",
    "demissao": "2024-03-20T00:00:00.000Z",
    "empregis": "CIFAL - SC",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81370,
    "nomcid": "BAURU",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "2024-03-19T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-01-16T00:00:00.000Z",
    "demissao": "2024-03-12T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-03-19T00:00:00.000Z",
    "demissao": "2024-04-08T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 35440,
    "nomcid": "RIBEIRAO DAS NEVES",
    "admissao": "2024-03-19T00:00:00.000Z",
    "demissao": "2024-05-02T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-04-04T00:00:00.000Z",
    "demissao": "2024-04-04T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 42889,
    "nomcid": "VARZEA GRANDE",
    "admissao": "2024-04-16T00:00:00.000Z",
    "demissao": "2024-08-05T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-05-14T00:00:00.000Z",
    "demissao": "2024-06-27T00:00:00.000Z",
    "empregis": "ASTECA SHOP 17",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-06-04T00:00:00.000Z",
    "demissao": "2024-07-24T00:00:00.000Z",
    "empregis": "AUTO POSTO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-05-07T00:00:00.000Z",
    "demissao": "2024-08-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 41637,
    "nomcid": "BARRA DO BUGRES",
    "admissao": "2024-07-02T00:00:00.000Z",
    "demissao": "2024-08-05T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-07-10T00:00:00.000Z",
    "demissao": "2024-08-23T00:00:00.000Z",
    "empregis": "ASTECA SHOP 17",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2022-04-04T00:00:00.000Z",
    "demissao": "2024-06-06T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 58068,
    "nomcid": "PARANAGUA",
    "admissao": "2023-07-10T00:00:00.000Z",
    "demissao": "2024-06-12T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81990,
    "nomcid": "CAMPINAS",
    "admissao": "2023-07-01T00:00:00.000Z",
    "demissao": "2024-08-15T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2021-02-01T00:00:00.000Z",
    "demissao": "2024-07-18T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 75680,
    "nomcid": "BLUMENAU",
    "admissao": "2021-08-16T10:35:28.000Z",
    "demissao": "2024-05-14T00:00:00.000Z",
    "empregis": "CIFAL - SC",
    "codempresa": 21,
    "descricao": "FRANQUIA FRARIBE"
  },
  {
    "codcid": 25666,
    "nomcid": "BELO HORIZONTE",
    "admissao": "2021-08-23T13:23:09.000Z",
    "demissao": "2024-05-08T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 2,
    "descricao": "ARAPIRACA"
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-07-01T00:00:00.000Z",
    "demissao": "2024-07-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 56995,
    "nomcid": "LONDRINA",
    "admissao": "2021-12-20T00:00:00.000Z",
    "demissao": "2024-03-16T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18325,
    "nomcid": "VITORIA",
    "admissao": "2021-12-06T00:00:00.000Z",
    "demissao": "2024-03-13T00:00:00.000Z",
    "empregis": "CIFAL - ES",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88323,
    "nomcid": "SAO JOSE DO RIO PRETO",
    "admissao": "2021-12-13T00:00:00.000Z",
    "demissao": "2024-05-13T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-03-01T00:00:00.000Z",
    "demissao": "2024-05-05T00:00:00.000Z",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 63118,
    "nomcid": "RIO DE JANEIRO",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "2024-09-03T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-11-07T00:00:00.000Z",
    "demissao": "2024-09-09T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 41866,
    "nomcid": "CUIABA",
    "admissao": "2023-01-09T00:00:00.000Z",
    "demissao": "2024-04-04T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 42188,
    "nomcid": "LUCAS DO RIO VERDE",
    "admissao": "2023-02-06T00:00:00.000Z",
    "demissao": "2024-08-05T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88323,
    "nomcid": "SAO JOSE DO RIO PRETO",
    "admissao": "2023-02-13T00:00:00.000Z",
    "demissao": "2024-04-23T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-08-01T00:00:00.000Z",
    "demissao": "2024-04-09T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2023-03-06T00:00:00.000Z",
    "demissao": "2024-04-23T00:00:00.000Z",
    "empregis": "ASTECA SHOP 13",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-02-16T00:00:00.000Z",
    "demissao": "2024-06-01T00:00:00.000Z",
    "empregis": "ASTECA SHOP 17",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88099,
    "nomcid": "SANTOS",
    "admissao": "2023-06-12T00:00:00.000Z",
    "demissao": "2024-04-23T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 56995,
    "nomcid": "LONDRINA",
    "admissao": "2023-06-12T00:00:00.000Z",
    "demissao": "2024-06-20T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-05-02T00:00:00.000Z",
    "demissao": "2024-09-23T00:00:00.000Z",
    "empregis": "AUTO POSTO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-05-09T00:00:00.000Z",
    "demissao": "2024-04-12T00:00:00.000Z",
    "empregis": "AUTO POSTO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-10-16T00:00:00.000Z",
    "demissao": "2024-02-28T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 42803,
    "nomcid": "TANGARA DA SERRA",
    "admissao": "2023-10-16T00:00:00.000Z",
    "demissao": "2024-05-08T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82236,
    "nomcid": "CATANDUVA",
    "admissao": "2023-10-16T00:00:00.000Z",
    "demissao": "2024-09-16T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2023-10-16T00:00:00.000Z",
    "demissao": "2024-08-27T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-09-18T00:00:00.000Z",
    "demissao": "2024-03-11T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-10-09T00:00:00.000Z",
    "demissao": "2024-03-01T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40738,
    "nomcid": "MIRANDA",
    "admissao": "2023-10-09T00:00:00.000Z",
    "demissao": "2024-05-07T00:00:00.000Z",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81639,
    "nomcid": "BOTUCATU",
    "admissao": "2023-11-06T00:00:00.000Z",
    "demissao": "2024-09-25T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88919,
    "nomcid": "TAQUARITINGA",
    "admissao": "2023-11-06T00:00:00.000Z",
    "demissao": "2024-06-14T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-11-21T00:00:00.000Z",
    "demissao": "2024-05-06T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 63118,
    "nomcid": "RIO DE JANEIRO",
    "admissao": "2021-10-27T00:00:00.000Z",
    "demissao": "2024-07-01T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-12-19T00:00:00.000Z",
    "demissao": "2024-05-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-02-19T00:00:00.000Z",
    "demissao": "2024-06-03T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 85235,
    "nomcid": "MARILIA",
    "admissao": "2024-03-19T00:00:00.000Z",
    "demissao": "2024-06-11T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-03-12T00:00:00.000Z",
    "demissao": "2024-05-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88331,
    "nomcid": "SAO JOSE DOS CAMPOS",
    "admissao": "2024-03-19T00:00:00.000Z",
    "demissao": "2024-06-16T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18678,
    "nomcid": "ARAGUAINA",
    "admissao": "2024-05-07T00:00:00.000Z",
    "demissao": "2024-05-21T00:00:00.000Z",
    "empregis": "CIFAL - TO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2024-04-02T00:00:00.000Z",
    "demissao": "2024-04-02T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 42781,
    "nomcid": "SINOP",
    "admissao": "2024-06-04T00:00:00.000Z",
    "demissao": "2024-08-06T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-06-04T00:00:00.000Z",
    "demissao": "2024-09-05T00:00:00.000Z",
    "empregis": "CONVENIENCIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-09-10T00:00:00.000Z",
    "demissao": "2024-09-17T00:00:00.000Z",
    "empregis": "CONVENIENCIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-09-03T00:00:00.000Z",
    "demissao": "2024-10-17T00:00:00.000Z",
    "empregis": "ASTECA SHOP 17",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "2024-12-30T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-06-21T00:00:00.000Z",
    "demissao": "2024-10-03T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-11-21T00:00:00.000Z",
    "demissao": "2024-11-21T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 89508,
    "nomcid": "VIRADOURO",
    "admissao": "2023-12-04T00:00:00.000Z",
    "demissao": "2024-10-03T00:00:00.000Z",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2021-09-20T00:00:00.000Z",
    "demissao": "2024-10-08T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "2024-10-04T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-08-07T00:00:00.000Z",
    "demissao": "2025-03-17T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2021-05-17T00:00:00.000Z",
    "demissao": "2024-10-14T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84603,
    "nomcid": "JAU",
    "admissao": "2022-05-16T00:00:00.000Z",
    "demissao": "2024-10-14T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 20575,
    "nomcid": "MINEIROS",
    "admissao": "2023-02-06T00:00:00.000Z",
    "demissao": "2024-10-10T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-04-10T00:00:00.000Z",
    "demissao": "2024-10-14T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88595,
    "nomcid": "SERTAOZINHO",
    "admissao": "2023-11-06T00:00:00.000Z",
    "demissao": "2024-10-15T00:00:00.000Z",
    "empregis": "TBSTORE - RWR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-11-27T00:00:00.000Z",
    "demissao": "2024-10-14T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-12-19T00:00:00.000Z",
    "demissao": "2024-11-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88684,
    "nomcid": "SOROCABA",
    "admissao": "2024-05-14T00:00:00.000Z",
    "demissao": "2024-10-16T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80888,
    "nomcid": "ARARAS",
    "admissao": "2024-08-06T00:00:00.000Z",
    "demissao": "2024-10-22T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-02-06T00:00:00.000Z",
    "demissao": "2024-11-01T00:00:00.000Z",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2024-10-01T00:00:00.000Z",
    "demissao": "2024-11-14T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-06-21T00:00:00.000Z",
    "demissao": "2024-11-18T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88137,
    "nomcid": "SAO BERNARDO DO CAMPO",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "2024-11-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-02-19T00:00:00.000Z",
    "demissao": "2024-12-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-07-02T00:00:00.000Z",
    "demissao": "2024-11-19T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81990,
    "nomcid": "CAMPINAS",
    "admissao": "2024-08-13T00:00:00.000Z",
    "demissao": "2024-12-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-11-05T00:00:00.000Z",
    "demissao": "2024-12-01T00:00:00.000Z",
    "empregis": "CONVENIENCIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 85545,
    "nomcid": "MONTE AZUL PAULISTA",
    "admissao": "2021-09-03T00:00:00.000Z",
    "demissao": "2024-11-28T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81710,
    "nomcid": "BRODOWSKI",
    "admissao": "2024-12-10T00:00:00.000Z",
    "demissao": "2024-12-10T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-05-08T00:00:00.000Z",
    "demissao": "2024-12-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 85545,
    "nomcid": "MONTE AZUL PAULISTA",
    "admissao": "2024-06-20T00:00:00.000Z",
    "demissao": "2024-08-13T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 6823,
    "nomcid": "JUAZEIRO",
    "admissao": "2021-12-06T00:00:00.000Z",
    "demissao": "2024-12-23T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2024-03-19T00:00:00.000Z",
    "demissao": "2024-12-13T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2025-01-07T00:00:00.000Z",
    "demissao": "2025-01-07T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-07-18T00:00:00.000Z",
    "demissao": "2024-12-06T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-01-16T00:00:00.000Z",
    "demissao": "2025-01-02T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86045,
    "nomcid": "OSASCO",
    "admissao": "2024-09-10T00:00:00.000Z",
    "demissao": "2024-12-09T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82651,
    "nomcid": "DIADEMA",
    "admissao": "2024-11-12T00:00:00.000Z",
    "demissao": "2024-12-10T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2024-10-15T00:00:00.000Z",
    "demissao": "2025-01-12T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-11-21T00:00:00.000Z",
    "demissao": "2025-01-04T00:00:00.000Z",
    "empregis": "ASTECA SHOP 17",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82171,
    "nomcid": "CARAPICUIBA",
    "admissao": "2024-10-15T00:00:00.000Z",
    "demissao": "2025-01-12T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88099,
    "nomcid": "SANTOS",
    "admissao": "2024-01-16T00:00:00.000Z",
    "demissao": "2025-01-13T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83895,
    "nomcid": "INDAIATUBA",
    "admissao": "2025-01-21T00:00:00.000Z",
    "demissao": "2025-01-29T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-07-26T00:00:00.000Z",
    "demissao": "2025-01-17T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2022-02-07T00:00:00.000Z",
    "demissao": "2025-01-24T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-07-18T00:00:00.000Z",
    "demissao": "2025-01-22T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-04-03T00:00:00.000Z",
    "demissao": "2025-02-12T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 25666,
    "nomcid": "BELO HORIZONTE",
    "admissao": "2024-04-25T00:00:00.000Z",
    "demissao": "2025-02-21T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 85448,
    "nomcid": "MOGI DAS CRUZES",
    "admissao": "2024-11-12T00:00:00.000Z",
    "demissao": "2025-02-21T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 41645,
    "nomcid": "BARRA DO GARCAS",
    "admissao": "2021-09-27T00:00:00.000Z",
    "demissao": "2024-08-05T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-03-02T00:00:00.000Z",
    "demissao": "2025-02-21T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84140,
    "nomcid": "ITAPETININGA",
    "admissao": "2024-11-05T00:00:00.000Z",
    "demissao": "2025-02-19T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-08-08T00:00:00.000Z",
    "demissao": "2025-03-07T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81990,
    "nomcid": "CAMPINAS",
    "admissao": "2022-09-19T00:00:00.000Z",
    "demissao": "2025-03-03T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "2025-03-03T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-01-24T00:00:00.000Z",
    "demissao": "2025-03-07T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-07-17T00:00:00.000Z",
    "demissao": "2025-03-07T00:00:00.000Z",
    "empregis": "AUTO POSTO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88099,
    "nomcid": "SANTOS",
    "admissao": "2025-03-11T00:00:00.000Z",
    "demissao": "2025-04-24T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-08-06T00:00:00.000Z",
    "demissao": "2025-03-21T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-09-03T00:00:00.000Z",
    "demissao": "2025-03-19T00:00:00.000Z",
    "empregis": "ASTECA SHOP 15",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 85235,
    "nomcid": "MARILIA",
    "admissao": "2024-08-06T00:00:00.000Z",
    "demissao": "2025-03-18T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83739,
    "nomcid": "IBITIUVA",
    "admissao": "2025-04-01T00:00:00.000Z",
    "demissao": "2025-04-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86045,
    "nomcid": "OSASCO",
    "admissao": "2022-04-04T00:00:00.000Z",
    "demissao": "2025-04-22T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83194,
    "nomcid": "FRANCO DA ROCHA",
    "admissao": "2023-12-04T00:00:00.000Z",
    "demissao": "2025-04-02T00:00:00.000Z",
    "empregis": "ASTECA SHOP 12",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88099,
    "nomcid": "SANTOS",
    "admissao": "2024-06-04T00:00:00.000Z",
    "demissao": "2025-04-14T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 89540,
    "nomcid": "VOTORANTIM",
    "admissao": "2025-01-14T00:00:00.000Z",
    "demissao": "2025-04-16T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-02-04T00:00:00.000Z",
    "demissao": "2025-04-09T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87327,
    "nomcid": "RIBEIRAO PRETO",
    "admissao": "2022-06-11T00:00:00.000Z",
    "demissao": "2025-04-09T00:00:00.000Z",
    "empregis": "TBSTORE - RWR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2021-11-08T00:00:00.000Z",
    "demissao": "2025-04-22T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86720,
    "nomcid": "PIRAPORA DO BOM JESUS",
    "admissao": "2025-01-07T00:00:00.000Z",
    "demissao": "2025-04-06T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-01-17T00:00:00.000Z",
    "demissao": "2025-05-05T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2025-02-11T00:00:00.000Z",
    "demissao": "2025-05-11T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40401,
    "nomcid": "DOURADOS",
    "admissao": "2023-07-10T00:00:00.000Z",
    "demissao": "2024-06-06T00:00:00.000Z",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88099,
    "nomcid": "SANTOS",
    "admissao": "2025-04-01T00:00:00.000Z",
    "demissao": "2025-04-24T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86762,
    "nomcid": "PITANGUEIRAS",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "2025-04-25T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 20052,
    "nomcid": "INDIARA",
    "admissao": "2022-07-04T00:00:00.000Z",
    "demissao": "2025-04-22T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-03-06T00:00:00.000Z",
    "demissao": "2025-05-05T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-06-04T00:00:00.000Z",
    "demissao": "2025-05-05T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-11-27T00:00:00.000Z",
    "demissao": "2025-05-21T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40207,
    "nomcid": "CAMPO GRANDE",
    "admissao": "2023-12-04T00:00:00.000Z",
    "demissao": "2025-05-20T00:00:00.000Z",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40207,
    "nomcid": "CAMPO GRANDE",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "2025-05-20T00:00:00.000Z",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21695,
    "nomcid": "SANTO ANTONIO DO DESCOBERTO",
    "admissao": "2021-11-08T00:00:00.000Z",
    "demissao": "2025-05-19T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2025-02-20T00:00:00.000Z",
    "demissao": "2025-05-20T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40207,
    "nomcid": "CAMPO GRANDE",
    "admissao": "2025-05-20T00:00:00.000Z",
    "demissao": "2025-05-26T00:00:00.000Z",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-11-14T00:00:00.000Z",
    "demissao": "2025-05-28T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "2025-05-26T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81990,
    "nomcid": "CAMPINAS",
    "admissao": "2024-02-06T00:00:00.000Z",
    "demissao": "2025-06-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 95583,
    "nomcid": "CEILANDIA",
    "admissao": "2020-12-14T00:00:00.000Z",
    "demissao": "2025-06-26T00:00:00.000Z",
    "empregis": "CIFAL - DF",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2025-03-18T00:00:00.000Z",
    "demissao": "2025-06-17T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21032,
    "nomcid": "PALMEIRAS DE GOIAS",
    "admissao": "2025-05-13T00:00:00.000Z",
    "demissao": "2025-05-13T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2025-05-21T00:00:00.000Z",
    "demissao": "2025-06-06T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 89508,
    "nomcid": "VIRADOURO",
    "admissao": "2023-06-01T00:00:00.000Z",
    "demissao": "2025-07-11T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81990,
    "nomcid": "CAMPINAS",
    "admissao": "2021-08-02T00:00:00.000Z",
    "demissao": "2025-06-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87980,
    "nomcid": "SANTO ANDRE",
    "admissao": "2024-03-05T00:00:00.000Z",
    "demissao": "2025-08-04T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86045,
    "nomcid": "OSASCO",
    "admissao": "2025-02-11T00:00:00.000Z",
    "demissao": "2025-08-04T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88161,
    "nomcid": "SAO CARLOS",
    "admissao": "2025-04-01T00:00:00.000Z",
    "demissao": "2025-08-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88684,
    "nomcid": "SOROCABA",
    "admissao": "2025-06-10T00:00:00.000Z",
    "demissao": "2025-07-24T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2020-12-14T00:00:00.000Z",
    "demissao": "2025-07-18T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 41378,
    "nomcid": "TRES LAGOAS",
    "admissao": "2021-08-09T00:00:00.000Z",
    "demissao": "2025-07-23T00:00:00.000Z",
    "empregis": "CIFAL - MS",
    "codempresa": 19,
    "descricao": "FRANQUIA FRAFRAN"
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-04-19T00:00:00.000Z",
    "demissao": "2025-08-11T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 41378,
    "nomcid": "TRES LAGOAS",
    "admissao": "2025-07-01T00:00:00.000Z",
    "demissao": "2025-08-04T00:00:00.000Z",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-03-06T00:00:00.000Z",
    "demissao": "2025-08-15T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-04-06T00:00:00.000Z",
    "demissao": "2025-08-11T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "2025-08-11T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-01-16T00:00:00.000Z",
    "demissao": "2025-08-07T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-07-15T00:00:00.000Z",
    "demissao": "2025-08-28T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2023-12-04T00:00:00.000Z",
    "demissao": "2025-08-22T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-07-02T00:00:00.000Z",
    "demissao": "2025-08-26T00:00:00.000Z",
    "empregis": "ASTECA SHOP 12",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21474,
    "nomcid": "RIO VERDE",
    "admissao": "2021-02-22T00:00:00.000Z",
    "demissao": "2025-08-19T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-04-10T00:00:00.000Z",
    "demissao": "2025-09-03T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 85448,
    "nomcid": "MOGI DAS CRUZES",
    "admissao": "2025-04-08T00:00:00.000Z",
    "demissao": "2025-09-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 95613,
    "nomcid": "NUCLEO BANDEIRANTE",
    "admissao": "2023-02-13T00:00:00.000Z",
    "demissao": "2025-09-04T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-02-19T00:00:00.000Z",
    "demissao": "2025-09-15T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-12-01T00:00:00.000Z",
    "demissao": "2025-09-15T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2020-08-03T00:00:00.000Z",
    "demissao": "2025-12-11T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88978,
    "nomcid": "TAUBATE",
    "admissao": "2022-05-23T00:00:00.000Z",
    "demissao": "2025-09-25T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2025-05-06T00:00:00.000Z",
    "demissao": "2025-09-25T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-06-10T00:00:00.000Z",
    "demissao": "2025-10-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-07-01T00:00:00.000Z",
    "demissao": "2025-09-28T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-08-15T00:00:00.000Z",
    "demissao": "2025-09-28T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "2025-10-06T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81990,
    "nomcid": "CAMPINAS",
    "admissao": "2023-11-06T00:00:00.000Z",
    "demissao": "2025-10-06T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88137,
    "nomcid": "SAO BERNARDO DO CAMPO",
    "admissao": "2022-03-14T00:00:00.000Z",
    "demissao": "2025-10-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-07-01T00:00:00.000Z",
    "demissao": "2025-10-06T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-07-08T00:00:00.000Z",
    "demissao": "2025-10-05T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87041,
    "nomcid": "PRESIDENTE PRUDENTE",
    "admissao": "2023-05-08T00:00:00.000Z",
    "demissao": "2025-10-20T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2025-01-21T00:00:00.000Z",
    "demissao": "2025-10-20T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-03-11T00:00:00.000Z",
    "demissao": "2025-10-15T00:00:00.000Z",
    "empregis": "CONVENIENCIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-07-22T00:00:00.000Z",
    "demissao": "2025-10-19T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88510,
    "nomcid": "SAO VICENTE",
    "admissao": "2024-10-15T00:00:00.000Z",
    "demissao": "2025-11-03T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83585,
    "nomcid": "GUARULHOS",
    "admissao": "2025-10-21T00:00:00.000Z",
    "demissao": "2025-11-04T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2025-02-11T00:00:00.000Z",
    "demissao": "2025-11-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83577,
    "nomcid": "GUARUJA",
    "admissao": "2025-04-01T00:00:00.000Z",
    "demissao": "2025-11-03T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-05-20T00:00:00.000Z",
    "demissao": "2025-10-27T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84352,
    "nomcid": "ITU",
    "admissao": "2025-04-15T00:00:00.000Z",
    "demissao": "2025-11-04T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86045,
    "nomcid": "OSASCO",
    "admissao": "2025-05-06T00:00:00.000Z",
    "demissao": "2025-12-26T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-05-14T00:00:00.000Z",
    "demissao": "2026-01-06T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2024-11-05T00:00:00.000Z",
    "demissao": "2025-11-13T00:00:00.000Z",
    "empregis": "TBSTORE - ADM",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-08-15T00:00:00.000Z",
    "demissao": "2025-11-12T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 15890,
    "nomcid": "BRASILIA",
    "admissao": "2025-09-02T00:00:00.000Z",
    "demissao": "2025-11-30T00:00:00.000Z",
    "empregis": "CIFAL - DF",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-11-01T00:00:00.000Z",
    "demissao": "2025-07-04T00:00:00.000Z",
    "empregis": "CONVENIENCIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "2025-11-28T00:00:00.000Z",
    "empregis": "AUTO POSTO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86703,
    "nomcid": "PIRANGI",
    "admissao": "2024-09-03T00:00:00.000Z",
    "demissao": "2025-06-02T00:00:00.000Z",
    "empregis": "AUTO POSTO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-05-14T00:00:00.000Z",
    "demissao": "2025-12-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 15890,
    "nomcid": "BRASILIA",
    "admissao": "2024-02-06T00:00:00.000Z",
    "demissao": "2025-12-01T00:00:00.000Z",
    "empregis": "CIFAL - DF",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-04-02T00:00:00.000Z",
    "demissao": "2025-12-05T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2024-12-10T00:00:00.000Z",
    "demissao": "2025-12-01T00:00:00.000Z",
    "empregis": "TBSTORE - ADM",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88781,
    "nomcid": "TABOAO DA SERRA",
    "admissao": "2025-04-15T00:00:00.000Z",
    "demissao": "2025-12-15T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-09-09T00:00:00.000Z",
    "demissao": "2025-12-07T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2025-10-21T00:00:00.000Z",
    "demissao": "2025-12-26T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2025-05-21T00:00:00.000Z",
    "demissao": "2026-01-09T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-09-09T00:00:00.000Z",
    "demissao": "2025-12-22T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2025-10-07T00:00:00.000Z",
    "demissao": "2026-01-05T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83178,
    "nomcid": "FRANCA",
    "admissao": "2021-11-08T00:00:00.000Z",
    "demissao": "2026-01-13T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-09-10T00:00:00.000Z",
    "demissao": "2026-01-17T00:00:00.000Z",
    "empregis": "CONVENIENCIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2022-06-13T00:00:00.000Z",
    "demissao": "2026-01-28T00:00:00.000Z",
    "empregis": "ASTECA SHOP 12",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-02-16T00:00:00.000Z",
    "demissao": "2026-01-28T00:00:00.000Z",
    "empregis": "ASTECA SHOP 15",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "2026-01-19T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-07-18T00:00:00.000Z",
    "demissao": "2026-01-20T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-09-03T00:00:00.000Z",
    "demissao": "2026-01-28T00:00:00.000Z",
    "empregis": "ASTECA SHOP 15",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2014-06-17T00:00:00.000Z",
    "demissao": "2024-02-09T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2015-03-02T00:00:00.000Z",
    "demissao": "2024-04-12T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2014-06-17T00:00:00.000Z",
    "demissao": "2024-02-23T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2014-06-02T00:00:00.000Z",
    "demissao": "2025-02-14T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87386,
    "nomcid": "RIO CLARO",
    "admissao": "2015-06-15T00:00:00.000Z",
    "demissao": "2025-06-03T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2015-12-14T00:00:00.000Z",
    "demissao": "2024-04-03T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-12-01T00:00:00.000Z",
    "demissao": "2024-03-08T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2016-01-11T00:00:00.000Z",
    "demissao": "2024-11-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-08-26T00:00:00.000Z",
    "demissao": "2024-03-01T00:00:00.000Z",
    "empregis": "UM3MEIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-03-11T00:00:00.000Z",
    "demissao": "2025-02-27T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 8,
    "descricao": "FILIAL BRASILIA"
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2019-10-10T00:00:00.000Z",
    "demissao": "2024-05-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84492,
    "nomcid": "JALES",
    "admissao": "2023-02-02T00:00:00.000Z",
    "demissao": "2025-12-16T00:00:00.000Z",
    "empregis": "TBSTORE - JBZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2022-10-27T00:00:00.000Z",
    "demissao": "2024-12-17T00:00:00.000Z",
    "empregis": "TBSTORE - ADM",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88099,
    "nomcid": "SANTOS",
    "admissao": "2023-01-09T00:00:00.000Z",
    "demissao": "2025-10-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2019-03-18T00:00:00.000Z",
    "demissao": "2024-04-11T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2017-10-06T00:00:00.000Z",
    "demissao": "2024-05-19T00:00:00.000Z",
    "empregis": "UM3MEIA",
    "codempresa": 10,
    "descricao": "FILIAL RIO"
  },
  {
    "codcid": 35823,
    "nomcid": "SABARA",
    "admissao": "2018-02-19T00:00:00.000Z",
    "demissao": "2024-05-08T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 2,
    "descricao": "ARAPIRACA"
  },
  {
    "codcid": 39217,
    "nomcid": "UBERLANDIA",
    "admissao": "2022-10-27T00:00:00.000Z",
    "demissao": "2024-11-14T00:00:00.000Z",
    "empregis": "TBSTORE - ADM",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88161,
    "nomcid": "SAO CARLOS",
    "admissao": "2021-03-11T00:00:00.000Z",
    "demissao": "2025-08-05T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87327,
    "nomcid": "RIBEIRAO PRETO",
    "admissao": "2018-04-30T00:00:00.000Z",
    "demissao": "2024-05-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80640,
    "nomcid": "AMPARO",
    "admissao": "2021-03-11T00:00:00.000Z",
    "demissao": "2025-04-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21474,
    "nomcid": "RIO VERDE",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "2024-08-22T00:00:00.000Z",
    "empregis": "TBSTORE - ADM GO",
    "codempresa": 3,
    "descricao": "CIFAL MINAS"
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "2024-10-22T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-08-13T00:00:00.000Z",
    "demissao": "2025-01-27T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 55298,
    "nomcid": "CURITIBA",
    "admissao": "2021-12-06T00:00:00.000Z",
    "demissao": "2024-06-18T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "2024-05-19T00:00:00.000Z",
    "empregis": "ASTECA SHOP 17",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18678,
    "nomcid": "ARAGUAINA",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "2024-03-12T00:00:00.000Z",
    "empregis": "CIFAL - TO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2018-09-10T00:00:00.000Z",
    "demissao": "2024-11-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86665,
    "nomcid": "PIRACICABA",
    "admissao": "2018-12-03T00:00:00.000Z",
    "demissao": "2025-02-03T00:00:00.000Z",
    "empregis": "SMOKERS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82236,
    "nomcid": "CATANDUVA",
    "admissao": "2024-09-10T00:00:00.000Z",
    "demissao": "2025-08-21T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-01-01T00:00:00.000Z",
    "demissao": "2024-05-05T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83178,
    "nomcid": "FRANCA",
    "admissao": "2022-09-02T00:00:00.000Z",
    "demissao": "2024-08-13T00:00:00.000Z",
    "empregis": "TBSTORE - CTR",
    "codempresa": 8,
    "descricao": "FILIAL BRASILIA"
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-10-16T00:00:00.000Z",
    "demissao": "2025-06-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84522,
    "nomcid": "JANDIRA",
    "admissao": "2019-06-10T00:00:00.000Z",
    "demissao": "2025-04-22T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82163,
    "nomcid": "CARAGUATATUBA",
    "admissao": "2019-07-22T00:00:00.000Z",
    "demissao": "2024-11-11T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 61174,
    "nomcid": "BARRA MANSA",
    "admissao": "2019-08-12T00:00:00.000Z",
    "demissao": "2024-09-03T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2019-11-06T00:00:00.000Z",
    "demissao": "2025-05-13T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-08-01T00:00:00.000Z",
    "demissao": "2024-09-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86045,
    "nomcid": "OSASCO",
    "admissao": "2020-03-09T00:00:00.000Z",
    "demissao": "2024-08-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81990,
    "nomcid": "CAMPINAS",
    "admissao": "2020-06-08T00:00:00.000Z",
    "demissao": "2024-08-05T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-04-01T00:00:00.000Z",
    "demissao": "2025-11-07T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-09-01T00:00:00.000Z",
    "demissao": "2024-06-18T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-11-01T00:00:00.000Z",
    "demissao": "2025-05-13T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80640,
    "nomcid": "AMPARO",
    "admissao": "2021-02-22T00:00:00.000Z",
    "demissao": "2024-03-04T00:00:00.000Z",
    "empregis": "None",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81990,
    "nomcid": "CAMPINAS",
    "admissao": "2021-03-01T00:00:00.000Z",
    "demissao": "2024-06-03T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2021-06-01T00:00:00.000Z",
    "demissao": "2024-10-02T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 42587,
    "nomcid": "RONDONOPOLIS",
    "admissao": "2021-06-01T00:00:00.000Z",
    "demissao": "2024-08-05T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 20,
    "descricao": "FRANQUIA FRASJRP"
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-06-02T00:00:00.000Z",
    "demissao": "2025-10-17T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-06-02T00:00:00.000Z",
    "demissao": "2024-11-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-02-01T00:00:00.000Z",
    "demissao": "2024-06-20T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 42889,
    "nomcid": "VARZEA GRANDE",
    "admissao": "2021-08-02T13:55:11.000Z",
    "demissao": "2024-02-15T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 20,
    "descricao": "FRANQUIA FRASJRP"
  },
  {
    "codcid": 84352,
    "nomcid": "ITU",
    "admissao": "2021-08-09T11:24:00.000Z",
    "demissao": "2024-04-08T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-08-04T00:00:00.000Z",
    "demissao": "2024-10-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19070,
    "nomcid": "CALDAS NOVAS",
    "admissao": "2021-07-05T00:00:00.000Z",
    "demissao": "2025-05-20T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 3,
    "descricao": "CIFAL MINAS"
  },
  {
    "codcid": 19780,
    "nomcid": "FORMOSA",
    "admissao": "2021-06-21T00:00:00.000Z",
    "demissao": "2025-10-13T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 3,
    "descricao": "CIFAL MINAS"
  },
  {
    "codcid": 32972,
    "nomcid": "MONTES CLAROS",
    "admissao": "2021-09-20T00:00:00.000Z",
    "demissao": "2024-05-09T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-06-04T00:00:00.000Z",
    "demissao": "2025-09-29T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-01-01T00:00:00.000Z",
    "demissao": "2024-04-03T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 61700,
    "nomcid": "DUQUE DE CAXIAS",
    "admissao": "2021-11-08T00:00:00.000Z",
    "demissao": "2024-03-11T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-11-17T00:00:00.000Z",
    "demissao": "2024-03-19T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 63371,
    "nomcid": "SAO GONCALO",
    "admissao": "2021-10-18T13:25:22.000Z",
    "demissao": "2024-09-04T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 4,
    "descricao": "TABACO MANIA"
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-02-07T00:00:00.000Z",
    "demissao": "2024-04-12T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 63118,
    "nomcid": "RIO DE JANEIRO",
    "admissao": "2022-01-17T00:00:00.000Z",
    "demissao": "2024-09-04T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 63118,
    "nomcid": "RIO DE JANEIRO",
    "admissao": "2021-12-06T00:00:00.000Z",
    "demissao": "2024-06-05T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 57304,
    "nomcid": "MARINGA",
    "admissao": "2021-12-13T00:00:00.000Z",
    "demissao": "2024-09-10T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86045,
    "nomcid": "OSASCO",
    "admissao": "2023-01-03T00:00:00.000Z",
    "demissao": "2024-03-11T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2023-04-01T00:00:00.000Z",
    "demissao": "2024-05-17T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-02-21T00:00:00.000Z",
    "demissao": "2024-03-15T00:00:00.000Z",
    "empregis": "ASTECA SHOP 11",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-04-06T00:00:00.000Z",
    "demissao": "2024-09-06T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-03-07T00:00:00.000Z",
    "demissao": "2024-12-01T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-10-27T00:00:00.000Z",
    "demissao": "2024-03-11T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-04-01T00:00:00.000Z",
    "demissao": "2024-02-16T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-08-01T00:00:00.000Z",
    "demissao": "2024-07-28T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86045,
    "nomcid": "OSASCO",
    "admissao": "2022-04-04T00:00:00.000Z",
    "demissao": "2024-04-24T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2022-04-04T00:00:00.000Z",
    "demissao": "2025-12-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19992,
    "nomcid": "GURUPI",
    "admissao": "2022-05-16T00:00:00.000Z",
    "demissao": "2024-06-11T00:00:00.000Z",
    "empregis": "CIFAL - TO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 60968,
    "nomcid": "ANGRA DOS REIS",
    "admissao": "2022-05-23T00:00:00.000Z",
    "demissao": "2024-09-03T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-03-05T00:00:00.000Z",
    "demissao": "2024-04-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 28797,
    "nomcid": "DIVINOPOLIS",
    "admissao": "2022-06-20T00:00:00.000Z",
    "demissao": "2024-05-08T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-12-01T00:00:00.000Z",
    "demissao": "2024-04-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18139,
    "nomcid": "SERRA",
    "admissao": "2022-06-06T00:00:00.000Z",
    "demissao": "2024-03-12T00:00:00.000Z",
    "empregis": "CIFAL - ES",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 28096,
    "nomcid": "CONTAGEM",
    "admissao": "2022-06-20T00:00:00.000Z",
    "demissao": "2024-03-07T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-11-13T00:00:00.000Z",
    "demissao": "2024-04-12T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-11-01T00:00:00.000Z",
    "demissao": "2025-09-29T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 63118,
    "nomcid": "RIO DE JANEIRO",
    "admissao": "2022-08-01T00:00:00.000Z",
    "demissao": "2024-05-02T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-07-20T00:00:00.000Z",
    "demissao": "2024-03-12T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 41866,
    "nomcid": "CUIABA",
    "admissao": "2022-08-01T00:00:00.000Z",
    "demissao": "2024-09-04T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 95583,
    "nomcid": "CEILANDIA",
    "admissao": "2022-07-18T00:00:00.000Z",
    "demissao": "2024-08-06T00:00:00.000Z",
    "empregis": "CIFAL - DF",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 89036,
    "nomcid": "TERRA ROXA",
    "admissao": "2023-05-18T00:00:00.000Z",
    "demissao": "2024-03-18T00:00:00.000Z",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "2024-05-06T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-05-04T00:00:00.000Z",
    "demissao": "2024-04-03T00:00:00.000Z",
    "empregis": "UM3MEIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-02-02T00:00:00.000Z",
    "demissao": "2024-09-16T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-08-22T00:00:00.000Z",
    "demissao": "2024-04-01T00:00:00.000Z",
    "empregis": "UM3MEIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-05-07T00:00:00.000Z",
    "demissao": "2024-05-17T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-10-09T00:00:00.000Z",
    "demissao": "2024-03-12T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 61298,
    "nomcid": "CABO FRIO",
    "admissao": "2022-09-19T00:00:00.000Z",
    "demissao": "2024-09-03T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 30767,
    "nomcid": "IPATINGA",
    "admissao": "2022-10-17T00:00:00.000Z",
    "demissao": "2024-05-07T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-11-21T00:00:00.000Z",
    "demissao": "2024-04-17T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 89508,
    "nomcid": "VIRADOURO",
    "admissao": "2023-05-09T00:00:00.000Z",
    "demissao": "2024-03-18T00:00:00.000Z",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2022-11-07T00:00:00.000Z",
    "demissao": "2024-03-11T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 41866,
    "nomcid": "CUIABA",
    "admissao": "2022-11-07T00:00:00.000Z",
    "demissao": "2024-08-05T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 42781,
    "nomcid": "SINOP",
    "admissao": "2022-11-14T00:00:00.000Z",
    "demissao": "2024-03-26T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-11-14T00:00:00.000Z",
    "demissao": "2024-03-11T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2022-11-21T00:00:00.000Z",
    "demissao": "2024-05-02T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-03-01T00:00:00.000Z",
    "demissao": "2024-05-23T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-01-01T00:00:00.000Z",
    "demissao": "2024-06-03T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-12-19T00:00:00.000Z",
    "demissao": "2024-11-13T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-01-16T00:00:00.000Z",
    "demissao": "2024-05-19T00:00:00.000Z",
    "empregis": "UM3MEIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80888,
    "nomcid": "ARARAS",
    "admissao": "2023-01-16T00:00:00.000Z",
    "demissao": "2024-05-21T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88323,
    "nomcid": "SAO JOSE DO RIO PRETO",
    "admissao": "2023-06-01T00:00:00.000Z",
    "demissao": "2024-06-12T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-07-01T00:00:00.000Z",
    "demissao": "2024-05-14T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82171,
    "nomcid": "CARAPICUIBA",
    "admissao": "2023-11-14T00:00:00.000Z",
    "demissao": "2024-03-11T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 53627,
    "nomcid": "ALMIRANTE TAMANDARE",
    "admissao": "2023-01-16T00:00:00.000Z",
    "demissao": "2024-06-18T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-01-23T00:00:00.000Z",
    "demissao": "2025-08-27T00:00:00.000Z",
    "empregis": "CONVENIENCIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88323,
    "nomcid": "SAO JOSE DO RIO PRETO",
    "admissao": "2023-01-23T00:00:00.000Z",
    "demissao": "2024-04-09T00:00:00.000Z",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-03-06T00:00:00.000Z",
    "demissao": "2024-08-12T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86045,
    "nomcid": "OSASCO",
    "admissao": "2023-03-20T00:00:00.000Z",
    "demissao": "2024-03-06T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-06-02T00:00:00.000Z",
    "demissao": "2024-04-15T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-03-20T00:00:00.000Z",
    "demissao": "2024-05-17T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82236,
    "nomcid": "CATANDUVA",
    "admissao": "2023-04-10T00:00:00.000Z",
    "demissao": "2024-08-28T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 37273,
    "nomcid": "SAO JOAO DEL REI",
    "admissao": "2023-04-03T00:00:00.000Z",
    "demissao": "2024-05-07T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-02-01T00:00:00.000Z",
    "demissao": "2024-05-06T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 58459,
    "nomcid": "PONTA GROSSA",
    "admissao": "2023-04-10T00:00:00.000Z",
    "demissao": "2024-06-19T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 28096,
    "nomcid": "CONTAGEM",
    "admissao": "2023-05-08T00:00:00.000Z",
    "demissao": "2024-05-08T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82651,
    "nomcid": "DIADEMA",
    "admissao": "2023-05-08T00:00:00.000Z",
    "demissao": "2024-08-13T00:00:00.000Z",
    "empregis": "ASTECA SHOP 15",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82538,
    "nomcid": "COTIA",
    "admissao": "2023-06-05T00:00:00.000Z",
    "demissao": "2024-07-05T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 63118,
    "nomcid": "RIO DE JANEIRO",
    "admissao": "2023-06-05T00:00:00.000Z",
    "demissao": "2024-09-03T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 94579,
    "nomcid": "TAQUARALTO",
    "admissao": "2023-06-12T00:00:00.000Z",
    "demissao": "2024-06-12T00:00:00.000Z",
    "empregis": "CIFAL - TO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88900,
    "nomcid": "TAQUARAL",
    "admissao": "2023-06-05T00:00:00.000Z",
    "demissao": "2025-04-14T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2023-07-10T00:00:00.000Z",
    "demissao": "2024-02-07T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18678,
    "nomcid": "ARAGUAINA",
    "admissao": "2023-08-07T00:00:00.000Z",
    "demissao": "2024-06-11T00:00:00.000Z",
    "empregis": "CIFAL - TO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87327,
    "nomcid": "RIBEIRAO PRETO",
    "admissao": "2023-08-01T00:00:00.000Z",
    "demissao": "2024-04-05T00:00:00.000Z",
    "empregis": "TBSTORE - RWR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2015-06-01T00:00:00.000Z",
    "demissao": "2024-02-11T00:00:00.000Z",
    "empregis": "AUTO POSTO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 80829,
    "nomcid": "ARACATUBA",
    "admissao": "2023-08-01T00:00:00.000Z",
    "demissao": "2024-05-19T00:00:00.000Z",
    "empregis": "UM3MEIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-09-11T00:00:00.000Z",
    "demissao": "2024-08-15T00:00:00.000Z",
    "empregis": "CONVENIENCIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-08-14T00:00:00.000Z",
    "demissao": "2024-06-10T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-08-07T00:00:00.000Z",
    "demissao": "2024-07-01T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "2024-06-05T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84352,
    "nomcid": "ITU",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "2024-04-05T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-10-02T00:00:00.000Z",
    "demissao": "2024-09-10T00:00:00.000Z",
    "empregis": "SMOKERS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40207,
    "nomcid": "CAMPO GRANDE",
    "admissao": "2023-10-09T00:00:00.000Z",
    "demissao": "2024-04-03T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 21474,
    "nomcid": "RIO VERDE",
    "admissao": "2023-11-06T00:00:00.000Z",
    "demissao": "2024-07-01T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86045,
    "nomcid": "OSASCO",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "2024-05-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 63118,
    "nomcid": "RIO DE JANEIRO",
    "admissao": "2023-09-11T00:00:00.000Z",
    "demissao": "2024-09-26T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-10-02T00:00:00.000Z",
    "demissao": "2024-03-14T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "2024-09-04T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 56995,
    "nomcid": "LONDRINA",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "2024-04-04T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-11-13T00:00:00.000Z",
    "demissao": "2024-03-11T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-11-13T00:00:00.000Z",
    "demissao": "2024-08-06T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 63118,
    "nomcid": "RIO DE JANEIRO",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "2024-09-04T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-12-04T00:00:00.000Z",
    "demissao": "2025-05-28T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-12-19T00:00:00.000Z",
    "demissao": "2024-05-06T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 42587,
    "nomcid": "RONDONOPOLIS",
    "admissao": "2023-11-06T00:00:00.000Z",
    "demissao": "2024-07-01T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-11-27T00:00:00.000Z",
    "demissao": "2025-05-21T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-12-04T00:00:00.000Z",
    "demissao": "2024-12-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-05-07T00:00:00.000Z",
    "demissao": "2024-08-09T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-12-19T00:00:00.000Z",
    "demissao": "2024-04-18T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82171,
    "nomcid": "CARAPICUIBA",
    "admissao": "2024-03-12T00:00:00.000Z",
    "demissao": "2024-09-04T00:00:00.000Z",
    "empregis": "SMOKERS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-12-15T00:00:00.000Z",
    "demissao": "2024-03-13T00:00:00.000Z",
    "empregis": "ASTECA SHOP 11",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 63924,
    "nomcid": "VOLTA REDONDA",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "2024-09-03T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 61700,
    "nomcid": "DUQUE DE CAXIAS",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "2024-09-04T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86991,
    "nomcid": "PRAIA GRANDE",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "2024-06-25T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 63118,
    "nomcid": "RIO DE JANEIRO",
    "admissao": "2024-05-01T00:00:00.000Z",
    "demissao": "2024-09-04T00:00:00.000Z",
    "empregis": "CIFAL - RJ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 55760,
    "nomcid": "FOZ DO IGUACU",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "2024-05-16T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86762,
    "nomcid": "PITANGUEIRAS",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "2024-06-19T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 42587,
    "nomcid": "RONDONOPOLIS",
    "admissao": "2024-01-16T00:00:00.000Z",
    "demissao": "2024-08-05T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-01-09T00:00:00.000Z",
    "demissao": "2024-07-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84417,
    "nomcid": "JACAREI",
    "admissao": "2024-02-06T00:00:00.000Z",
    "demissao": "2024-11-13T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 93866,
    "nomcid": "PALMAS",
    "admissao": "2024-02-06T00:00:00.000Z",
    "demissao": "2024-06-03T00:00:00.000Z",
    "empregis": "CIFAL - TO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-02-01T00:00:00.000Z",
    "demissao": "2024-04-30T00:00:00.000Z",
    "empregis": "ASTECA SHOP 17",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 28053,
    "nomcid": "CONSELHEIRO LAFAIETE",
    "admissao": "2024-02-06T00:00:00.000Z",
    "demissao": "2024-05-05T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "2025-05-09T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18511,
    "nomcid": "ANAPOLIS",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "2024-04-04T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81302,
    "nomcid": "BARRETOS",
    "admissao": "2024-02-06T00:00:00.000Z",
    "demissao": "2024-03-22T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-02-06T00:00:00.000Z",
    "demissao": "2024-05-05T00:00:00.000Z",
    "empregis": "CONVENIENCIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "2024-05-19T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 86762,
    "nomcid": "PITANGUEIRAS",
    "admissao": "2024-02-19T00:00:00.000Z",
    "demissao": "2024-09-18T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "2024-09-03T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 77127,
    "nomcid": "JOINVILLE",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "2024-05-15T00:00:00.000Z",
    "empregis": "CIFAL - SC",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-03-05T00:00:00.000Z",
    "demissao": "2024-05-27T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 56995,
    "nomcid": "LONDRINA",
    "admissao": "2024-03-05T00:00:00.000Z",
    "demissao": "2024-05-15T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88099,
    "nomcid": "SANTOS",
    "admissao": "2024-03-05T00:00:00.000Z",
    "demissao": "2024-07-16T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2024-03-05T00:00:00.000Z",
    "demissao": "2024-03-06T00:00:00.000Z",
    "empregis": "ASTECA SHOP 17",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 54623,
    "nomcid": "CAMBE",
    "admissao": "2024-06-04T00:00:00.000Z",
    "demissao": "2024-09-10T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 85545,
    "nomcid": "MONTE AZUL PAULISTA",
    "admissao": "2024-03-05T00:00:00.000Z",
    "demissao": "2024-06-13T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-12-23T00:00:00.000Z",
    "demissao": "2025-02-24T00:00:00.000Z",
    "empregis": "CONVENIENCIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-07-01T00:00:00.000Z",
    "demissao": "2025-08-14T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-07-15T00:00:00.000Z",
    "demissao": "2025-10-14T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-10-21T00:00:00.000Z",
    "demissao": "2025-12-11T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-10-14T00:00:00.000Z",
    "demissao": "2025-10-23T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-11-17T00:00:00.000Z",
    "demissao": "2026-01-06T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19780,
    "nomcid": "FORMOSA",
    "admissao": "2025-10-07T00:00:00.000Z",
    "demissao": "2025-12-04T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-05-07T00:00:00.000Z",
    "demissao": "2025-05-13T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-02-01T00:00:00.000Z",
    "demissao": "2024-09-03T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 34010,
    "nomcid": "PATOS DE MINAS",
    "admissao": "2019-10-21T00:00:00.000Z",
    "demissao": "2024-04-17T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 2,
    "descricao": "ARAPIRACA"
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2020-06-22T00:00:00.000Z",
    "demissao": "2024-08-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-01-17T00:00:00.000Z",
    "demissao": "2024-08-01T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84352,
    "nomcid": "ITU",
    "admissao": "2020-12-21T00:00:00.000Z",
    "demissao": "2025-10-08T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2021-01-18T00:00:00.000Z",
    "demissao": "2025-12-17T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88137,
    "nomcid": "SAO BERNARDO DO CAMPO",
    "admissao": "2021-02-01T00:00:00.000Z",
    "demissao": "2025-07-24T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 42587,
    "nomcid": "RONDONOPOLIS",
    "admissao": "2023-03-06T00:00:00.000Z",
    "demissao": "2024-02-06T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 55298,
    "nomcid": "CURITIBA",
    "admissao": "2021-02-15T00:00:00.000Z",
    "demissao": "2024-06-18T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-01-01T00:00:00.000Z",
    "demissao": "2024-08-02T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 42889,
    "nomcid": "VARZEA GRANDE",
    "admissao": "2021-02-22T00:00:00.000Z",
    "demissao": "2024-08-05T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39209,
    "nomcid": "UBERABA",
    "admissao": "2022-07-25T00:00:00.000Z",
    "demissao": "2025-06-03T00:00:00.000Z",
    "empregis": "TBSTORE - ADM",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-02-01T00:00:00.000Z",
    "demissao": "2024-04-12T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-03-01T00:00:00.000Z",
    "demissao": "2024-03-18T00:00:00.000Z",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-10-27T00:00:00.000Z",
    "demissao": "2025-11-02T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-01-16T00:00:00.000Z",
    "demissao": "2024-05-19T00:00:00.000Z",
    "empregis": "UM3MEIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 55298,
    "nomcid": "CURITIBA",
    "admissao": "2021-04-26T00:00:00.000Z",
    "demissao": "2024-08-15T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-10-01T00:00:00.000Z",
    "demissao": "2024-04-09T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 56065,
    "nomcid": "GUARAPUAVA",
    "admissao": "2021-07-05T00:00:00.000Z",
    "demissao": "2024-06-05T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 5,
    "descricao": "DISTRIBUIDORA"
  },
  {
    "codcid": 41718,
    "nomcid": "CACERES",
    "admissao": "2021-07-19T13:44:46.000Z",
    "demissao": "2024-04-16T00:00:00.000Z",
    "empregis": "CIFAL - MT",
    "codempresa": 20,
    "descricao": "FRANQUIA FRASJRP"
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2021-11-22T00:00:00.000Z",
    "demissao": "2024-10-09T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 25666,
    "nomcid": "BELO HORIZONTE",
    "admissao": "2021-12-01T00:00:00.000Z",
    "demissao": "2024-05-20T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2021-12-06T00:00:00.000Z",
    "demissao": "2024-05-06T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2022-04-04T00:00:00.000Z",
    "demissao": "2024-05-19T00:00:00.000Z",
    "empregis": "UM3MEIA",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 58459,
    "nomcid": "PONTA GROSSA",
    "admissao": "2022-05-02T00:00:00.000Z",
    "demissao": "2024-06-19T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 83585,
    "nomcid": "GUARULHOS",
    "admissao": "2022-05-23T00:00:00.000Z",
    "demissao": "2025-11-04T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-02-01T00:00:00.000Z",
    "demissao": "2024-04-15T00:00:00.000Z",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 75396,
    "nomcid": "ARAQUARI",
    "admissao": "2022-08-15T00:00:00.000Z",
    "demissao": "2024-03-06T00:00:00.000Z",
    "empregis": "CIFAL - SC",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-02-06T00:00:00.000Z",
    "demissao": "2024-08-01T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-02-06T00:00:00.000Z",
    "demissao": "2024-10-04T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 59749,
    "nomcid": "SAO JOSE DOS PINHAIS",
    "admissao": "2023-04-03T00:00:00.000Z",
    "demissao": "2024-05-21T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 105953,
    "nomcid": "AGUAS LINDAS DE GOIAS",
    "admissao": "2023-04-10T00:00:00.000Z",
    "demissao": "2024-03-21T00:00:00.000Z",
    "empregis": "CIFAL - DF",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-05-08T00:00:00.000Z",
    "demissao": "2024-04-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-05-15T00:00:00.000Z",
    "demissao": "2025-04-09T00:00:00.000Z",
    "empregis": "LIKEBRANDS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-06-19T00:00:00.000Z",
    "demissao": "2024-03-12T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 82171,
    "nomcid": "CARAPICUIBA",
    "admissao": "2023-06-19T00:00:00.000Z",
    "demissao": "2024-02-14T00:00:00.000Z",
    "empregis": "SMOKERS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2023-08-01T00:00:00.000Z",
    "demissao": "2025-11-24T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 56995,
    "nomcid": "LONDRINA",
    "admissao": "2023-08-14T00:00:00.000Z",
    "demissao": "2024-09-10T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84417,
    "nomcid": "JACAREI",
    "admissao": "2023-08-21T00:00:00.000Z",
    "demissao": "2025-11-17T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 40207,
    "nomcid": "CAMPO GRANDE",
    "admissao": "2023-08-01T00:00:00.000Z",
    "demissao": "2024-06-05T00:00:00.000Z",
    "empregis": "CIFAL - MS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 31640,
    "nomcid": "JUIZ DE FORA",
    "admissao": "2023-08-01T00:00:00.000Z",
    "demissao": "2024-05-07T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 30767,
    "nomcid": "IPATINGA",
    "admissao": "2023-09-04T00:00:00.000Z",
    "demissao": "2024-05-13T00:00:00.000Z",
    "empregis": "CIFAL - MG",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 87955,
    "nomcid": "SANTANA DE PARNAIBA",
    "admissao": "2023-11-06T00:00:00.000Z",
    "demissao": "2024-03-06T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 60097,
    "nomcid": "SARANDI",
    "admissao": "2024-02-06T00:00:00.000Z",
    "demissao": "2024-06-03T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88331,
    "nomcid": "SAO JOSE DOS CAMPOS",
    "admissao": "2024-02-06T00:00:00.000Z",
    "demissao": "2024-02-06T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-02-06T00:00:00.000Z",
    "demissao": "2024-05-05T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-02-19T00:00:00.000Z",
    "demissao": "2025-09-15T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 22047,
    "nomcid": "TRINDADE",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "2024-05-19T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 19887,
    "nomcid": "GOIANIA",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "2024-05-19T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2024-03-05T00:00:00.000Z",
    "demissao": "2024-03-11T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 57304,
    "nomcid": "MARINGA",
    "admissao": "2024-06-18T00:00:00.000Z",
    "demissao": "2024-09-10T00:00:00.000Z",
    "empregis": "CIFAL - PR",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-04-01T00:00:00.000Z",
    "demissao": "2025-06-29T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88099,
    "nomcid": "SANTOS",
    "admissao": "2025-07-01T00:00:00.000Z",
    "demissao": "2025-08-14T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-08-15T00:00:00.000Z",
    "demissao": "2025-11-12T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-10-07T00:00:00.000Z",
    "demissao": "2025-10-13T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-04-15T00:00:00.000Z",
    "demissao": "2025-09-05T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2025-07-01T00:00:00.000Z",
    "demissao": "2025-08-19T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2025-09-10T00:00:00.000Z",
    "demissao": "2025-10-17T00:00:00.000Z",
    "empregis": "ASTECA SHOP 12",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 84522,
    "nomcid": "JANDIRA",
    "admissao": "2023-07-10T00:00:00.000Z",
    "demissao": "2024-10-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 18546,
    "nomcid": "APARECIDA DE GOIANIA",
    "admissao": "2024-02-20T00:00:00.000Z",
    "demissao": "2026-01-29T00:00:00.000Z",
    "empregis": "CIFAL - GO",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2026-01-20T00:00:00.000Z",
    "demissao": "2026-01-29T00:00:00.000Z",
    "empregis": "SOLLUS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2025-01-07T00:00:00.000Z",
    "demissao": "2026-02-02T00:00:00.000Z",
    "empregis": "CIFAL - SP",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 81388,
    "nomcid": "BEBEDOURO",
    "admissao": "2025-09-02T00:00:00.000Z",
    "demissao": "2026-02-02T00:00:00.000Z",
    "empregis": "TRANSVELOZ",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 88412,
    "nomcid": "SAO PAULO",
    "admissao": "2023-09-11T00:00:00.000Z",
    "demissao": "2026-02-02T00:00:00.000Z",
    "empregis": "ASTECA SHOP 12",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  },
  {
    "codcid": 39209,
    "nomcid": "UBERABA",
    "admissao": "2025-11-11T00:00:00.000Z",
    "demissao": "2026-02-02T00:00:00.000Z",
    "empregis": "SMOKERS",
    "codempresa": 1,
    "descricao": "CIFAL COMERCIAL "
  }
]


# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Dashboard RH - People Analytics",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILO CSS ---
st.markdown("""
<style>
    [data-testid="stMetricValue"] {
        font-size: 24px;
    }
    .css-1d391kg {
        padding-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. DADOS (Do Teste.py) ---



# --- 1. PROCESSAMENTO DOS DADOS ---
@st.cache_data
def load_and_process_data(data):
    df = pd.DataFrame(data)
    
    # Converter datas e remover fuso horário
    for col in ['admissao', 'demissao']:
        df[col] = df[col].replace('None', pd.NaT)
        df[col] = pd.to_datetime(df[col], errors='coerce').dt.tz_localize(None)
    
    return df

# Carregar dados iniciais
df_raw = load_and_process_data(Dados_teste)

# --- 2. FILTROS NA SIDEBAR ---
st.sidebar.header("🔍 Filtros")

empresa_opcoes = ["Todas"] + sorted(df_raw["descricao"].dropna().unique().tolist())
empresa_selecionada = st.sidebar.selectbox("Empresa", options=empresa_opcoes)

cidade_opcoes = ["Todas"] + sorted(df_raw["nomcid"].dropna().unique().tolist())
cidade_selecionada = st.sidebar.selectbox("Cidade", options=cidade_opcoes)

# Aplicar Filtros ao DataFrame que será usado em todo o dashboard
df_filtered = df_raw.copy()
if empresa_selecionada != "Todas":
    df_filtered = df_filtered[df_filtered["descricao"] == empresa_selecionada]
if cidade_selecionada != "Todas":
    df_filtered = df_filtered[df_filtered["nomcid"] == cidade_selecionada]

# --- 3. FUNÇÃO DE AGREGAÇÃO (LÓGICA DE 3 ANOS) ---
def aggregate_monthly(df_in):
    if df_in.empty:
        return pd.DataFrame()
        
    max_date = datetime.now() 
    min_date_limit = max_date - pd.DateOffset(years=2) # Pega o ano atual + 2 anteriores
    
    first_admission = df_in['admissao'].min()
    min_date = max(min_date_limit, first_admission) if pd.notna(first_admission) else min_date_limit

    dates = pd.date_range(start=min_date, end=max_date, freq='MS')
    results = []
    
    for date in dates:
        m_start, m_end = date, date + pd.offsets.MonthEnd(0)
        
        admissoes = df_in[(df_in['admissao'] >= m_start) & (df_in['admissao'] <= m_end)].shape[0]
        desligamentos = df_in[(df_in['demissao'] >= m_start) & (df_in['demissao'] <= m_end)].shape[0]
        ativos = df_in[(df_in['admissao'] <= m_end) & ((df_in['demissao'].isna()) | (df_in['demissao'] > m_end))].shape[0]
        
        results.append({
            'Mês': m_start.strftime('%b/%Y'),
            'Data': m_start,
            'Total Colaboradores': ativos,
            'Admissões': admissoes,
            'Desligamentos': desligamentos,
            'Turnover %': round((desligamentos / ativos * 100), 2) if ativos > 0 else 0
        })
    return pd.DataFrame(results)

df_dashboard = aggregate_monthly(df_filtered)

# --- 4. CÁLCULO DE MÉTRICAS ---
if not df_dashboard.empty:
    total_ativos_atual = df_dashboard.iloc[-1]['Total Colaboradores']
    total_adm_periodo = df_dashboard['Admissões'].sum()
    total_des_periodo = df_dashboard['Desligamentos'].sum()
    media_turnover = df_dashboard['Turnover %'].mean()
else:
    total_ativos_atual = total_adm_periodo = total_des_periodo = media_turnover = 0

# --- 5. EXIBIÇÃO DASHBOARD ---

# Cards de Métricas
col1, col2, col3, col4 = st.columns(4)
col1.metric("👨‍💼 Ativos Atual", total_ativos_atual)
col2.metric("📥 Admissões (Período)", total_adm_periodo)
col3.metric("🚪 Desligamentos (Período)", total_des_periodo)
col4.metric("Turnover Médio", f"{media_turnover:.1f}%")

st.markdown("---")

# Gráficos um embaixo do outro
if not df_dashboard.empty:
    # 1. Evolução Headcount
    st.subheader("📈 Evolução do Headcount")
    fig_line = px.line(df_dashboard, x='Mês', y='Total Colaboradores', markers=True, line_shape='spline')
    fig_line.update_traces(line_color='#3498db', line_width=3)
    st.plotly_chart(fig_line, use_container_width=True)

    # 2. Admissões vs Desligamentos Geral
    st.subheader("📊 Admissões vs Desligamentos (Histórico)")
    fig_bar = go.Figure(data=[
        go.Bar(name='Admissões', x=df_dashboard['Mês'], y=df_dashboard['Admissões'], marker_color='#2ecc71'),
        go.Bar(name='Desligamentos', x=df_dashboard['Mês'], y=df_dashboard['Desligamentos'], marker_color='#e74c3c')
    ])
    fig_bar.update_layout(barmode='group', height=400)
    st.plotly_chart(fig_bar, use_container_width=True)
else:
    st.info("Sem dados para o filtro selecionado.")

st.markdown("---")

# --- 6. DETALHAMENTO POR ANO (ÚLTIMOS 3 ANOS) ---
ano_atual = datetime.now().year
for ano in [ano_atual - 2, ano_atual - 1, ano_atual]:
    st.markdown(f"### 📅 Comparativo Mensal: {ano}")
    
    # Filtragem específica para o gráfico anual usando o dataframe filtrado da sidebar
    df_ano_adm = df_filtered[df_filtered["admissao"].dt.year == ano]
    df_ano_dem = df_filtered[df_filtered["demissao"].dt.year == ano]
    
    meses = range(1, 13)
    adm_mes = df_ano_adm.groupby(df_ano_adm["admissao"].dt.month).size().reindex(meses, fill_value=0)
    dem_mes = df_ano_dem.groupby(df_ano_dem["demissao"].dt.month).size().reindex(meses, fill_value=0)
    
    grafico_long = pd.DataFrame({
        "Mes": meses,
        "Contratações": adm_mes.values,
        "Demissões": dem_mes.values
    }).melt(id_vars="Mes", var_name="Tipo", value_name="Quantidade")

    chart = alt.Chart(grafico_long).mark_bar().encode(
        x=alt.X("Mes:O", axis=alt.Axis(labelExpr="['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'][datum.value-1]")),
        y=alt.Y("Quantidade:Q"),
        color=alt.Color("Tipo:N", scale=alt.Scale(domain=["Contratações", "Demissões"], range=["#2ecc71", "#e74c3c"])),
        xOffset="Tipo:N"
    ).properties(height=300)
    
    st.altair_chart(chart, use_container_width=True)

# --- 7. TABELA FINAL ---
st.markdown("### 📋 Detalhamento dos Colaboradores")
st.dataframe(
    df_filtered[['codcid', 'nomcid', 'admissao', 'demissao', 'empregis', 'descricao']],
    use_container_width=True,
    column_config={
        "admissao": st.column_config.DateColumn("Admissão", format="DD/MM/YYYY"),
        "demissao": st.column_config.DateColumn("Demissão", format="DD/MM/YYYY"),
    }
)
