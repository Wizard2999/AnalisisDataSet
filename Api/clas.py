from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field
from typing import Literal
import joblib
import pandas as pd
from fastapi import HTTPException




# Una variable binaria puede ser:
# binaria: int = Field(ge=0, le=1)
# O, binaria: bool
class ModelInput(PydanticBaseModel):
    '''
    Clase que define las entradas del modelo
    
    '''
    Area_Conocimiento: Literal[
        'ECONOMÍA, ADMINISTRACIÓN CONTADURIA Y AFINES', 'NINGUNA',
        'CIENCIAS DE LA EDUCACIÓN', 'BELLAS ARTES', 'NO INDICA',
        'INGENIERÍA, ARQUITECTURA Y AFINES', 'CIENCIAS SOCIALES Y HUMANAS',
        'CIENCIAS DE LA SALUD', 'AGRONOMÍA, VETERINARIA Y AFINES',
        'MATEMÁTICAS Y CIENCIAS NATURALES', '(NO REGISTRA)',
        'COCINA Y CULINARIA', 'AGRONOMÍA, VETERINARIA Y ZOOTECNIA',
        'AVIACIÓN']
    Sub_Area_Conocimiento: Literal['CONTADURÍA PÚBLICA', 'NINGUNA', 'EDUCACIÓN', 'MÚSICA',
        'NO INDICA', 'ADMINISTRACIÓN', 'INGENIERÍA QUÍMICA Y AFINES',
        'INGENIERÍA INDUSTRIAL Y AFINES',
        'INGENIERÍA EN SISTEMAS, TELEMÁTICA Y AFINES', 'DERECHO Y AFINES',
        'MEDICINA', 'ARQUITECTURA', 'INGENIERÍA CIVIL Y AFINES',
        'OTROS ESTUDIOS EN CIENCIAS SOCIALES Y HUMANAS',
        'OTRO PROGRAMA DE BELLAS ARTES',
        'PERIODISMO, COMUNICACIÓN SOCIAL Y AFINES',
        'INGENIERÍA DE PETRÓLEOS',
        'INGENIERÍA ELECTRÓNICA, TELECOMUNICACIONES Y AFINES',
        'ENFERMERÍA', 'PSICOLOGÍA Y AFINES', 'PUBLICIDAD Y AFINES',
        'DISEÑO', 'OTRO PROGRAMA DE SALUD',
        'INGENIERÍA AGROINDUSTRIAL, ALIMENTOS Y AFINES', 'AVIACIÓN',
        'AGRONOMÍA', 'INGENIERÍA MECÁNICA Y AFINES', 'OTRAS INGENIERÍAS',
        'ARTES PLÁSTICAS, VISUALES Y AFINES',
        'LENGUAS MODERNAS, FILOLOGÍA, LINGÜÍSTICA Y AFINES', 'ODONTOLOGÍA',
        'ECONOMÍA', 'QUÍMICA Y AFINES', 'INGENIERÍA ELÉCTRICA Y AFINES',
        'ANTROPOLOGÍA O ARTES LIBERALES',
        'INGENIERÍA AMBIENTAL, SANITARIA Y AFINES',
        'SALUD OCUPACIONAL (HSEQ)', 'SOCIOLOGÍA, TRABAJO SOCIAL Y AFINES',
        'FILOSOFÍA, TEOLOGÍA Y AFINES',
        'INGENIERÍA ADMINISTRATIVA Y AFINES', 'COCINA Y CULINARIA',
        'MEDICINA VETERINARIA', 'TERAPIAS', 'NUTRICIÓN Y DIETÉTICA',
        'INSTRUMENTACIÓN QUIRÚRGICA',
        'CIENCIA POLÍTICA Y/O RELACIONES INTERNACIONALES',
        'MATEMÁTICAS, ESTADÍSTICA Y AFINES', 'GEOGRAFÍA O HISTORIA',
        'BIOLOGÍA, MICROBIOLOGÍA Y AFINES', 'BIBLIOTECOLOGÍA',
        '(NO REGISTRA)', 'FÍSICA',
        'DEPORTES, EDUCACIÓN FÍSICA Y RECREACIÓN', 'ZOOTECNIA',
        'OTROS PROGRAMAS DE CIENCIAS NATURALES', 'FORMACIÓN MILITAR',
        'SALUD PÚBLICA', 'ARTES DRAMÁTICAS Y REPRESENTATIVAS',
        'INGENIERÍA BIOMÉDICA Y AFINES',
        'INGENIERÍA AGRÍCOLA, FORESTAL Y AFINES', 'BACTERIOLOGÍA',
        'INGENIERÍA DE MINAS, METALURGIA Y AFINES', 'OPTOMETRÍA',
        'GEOLOGÍA', 'INGENIERÍA AGRONÓMICA, PECUARIA Y AFINES']
    Estado_civil: Literal['CASADO', 'UNION_LIBRE', 'DESCONOCIDO', 'SOLTERO', 'DIVORCIADO',
        'VIUDO']
    Etnia_de_la_persona: Literal['NINGUNA', 'OTRO', 'AFRODESCENDIENTE', 'SIN ETNIA REGISTRADA',
        'INDÍGENA', 'RAIZAL DEL ARCHIPIELAGO DE SAN ANDRES', 'GITANO',
        'PALENQUERO DE SAN BASILO', 'PALENQUERO DE SAN BASILIO']
    Estatura: float = Field(description='Estatura en centimentros',ge=1, le=1000)
    

    # OPCIONAL: Poner el ejemplo para que en la documentación ya puedan de una lanzar la predicción.
    class Config:
        schema_extra = {
            "example": {
                'Área Conocimiento': 'INGENIERÍA, ARQUITECTURA Y AFINES',
                'Sub Area Conocimiento': 'INGENIERÍA EN SISTEMAS',
                'Estado civil': 'CASADO',
                'Etnia de la persona': 'NINGUNA',
                'Estatura_(CM)': "172"
            }
        }


class ModelOutput(PydanticBaseModel):
    '''
    Clase que define las salidas del modelo
    '''
    País: Literal['ESPAÑA', 'VENEZUELA', 'ESTADOS UNIDOS', 'BELGICA', 'CANADA',
        'CHILE', 'SUIZA', 'PANAMA', 'PERU', 'FRANCIA', 'ECUADOR',
        'FEDERACION DE RUSIA', 'AUSTRALIA', 'LIBANO', 'TAILANDIA',
        'MEXICO', 'PORTUGAL', 'COSTA RICA', 'JAPON', 'CURAÇAO', 'BRASIL',
        'GUATEMALA', 'REINO UNIDO', 'ITALIA', 'ARGENTINA', 'ARUBA',
        'REPUBLICA DOMINICANA', 'TURQUIA', 'ALEMANIA', 'ISRAEL',
        'HONG KONG', 'BOLIVIA', 'CUBA', 'PAISES BAJOS', 'KENIA',
        'BOSNIA Y HERZEGOVINA', 'NUEVA ZELANDA', 'HONDURAS', 'POLONIA',
        'PARAGUAY', 'QATAR', 'CHINA', 'AUSTRIA', 'LETONIA', 'SUECIA',
        'ANDORRA', 'EMIRATOS ARABES UNIDOS', 'MARRUECOS', 'BULGARIA',
        'URUGUAY', 'CROACIA', 'LUXEMBURGO', 'ST. MAARTEN', 'BONAIRE',
        'RUSIA', 'NORUEGA', 'EL SALVADOR', 'IRLANDA', 'SURINAM',
        'FILIPINAS', 'INDIA', 'TRINIDAD Y TOBAGO', 'CHIPRE', 'MALTA',
        'HUNGRIA', 'GUYANA FRANCESA', 'VIET NAM', 'DINAMARCA', 'GUADALUPE',
        'NIGERIA', 'COREA, REPUBLICA DE', 'PALESTINA', 'INDONESIA',
        'AFGANISTAN', 'ANTILLAS HOLANDESAS', 'REPUBLICA CHECA',
        'SUDAN DEL SUR', 'JORDANIA', 'SINGAPUR', 'JAMAICA', 'MOZAMBIQUE',
        'GRECIA', 'FINLANDIA', 'ARABIA SAUDITA', 'SUDAFRICA', 'AZERBAIYAN',
        'ANGOLA', 'NIGER', 'UCRANIA', 'RUMANIA', 'BANGLADESH', 'MALASIA',
        'BAHREIN', 'NICARAGUA', 'BENIN', 'ARGELIA', 'EGIPTO', 'LIBERIA',
        'LAO, REPUBLIC DEMOCRATICA POPULAR DE', 'HAITI', 'BAHAMAS',
        'GUINEA ECUATORIAL', 'GABON', 'MOLDOVA, REPUBLICA DE', 'MALAWI',
        'SAINT-MARTIN', 'KUWAIT', 'REPUBLICA DE CHINA-TAIWAN', 'SRI LANKA',
        'BERMUDAS', 'ANTIGUA Y BARBUDA', 'CONGO', 'CAMERUN', 'BIELORRUSIA',
        'ISLANDIA', 'ESLOVAQUIA', 'OMAN', 'LITUANIA',
        'CONGO, REPUBLICA DEMOCRATICA DE', 'ESTONIA', 'GHANA', 'TUNEZ',
        'IRAN, REPUBLICA ISLAMICA DE', 'DESCONOCIDO', 'ESLOVENIA',
        'MYANMAR', 'SAN MARINO', 'CAMBOYA', 'RUANDA', 'MONACO', 'SENEGAL',
        'SIERRA LEONA', 'ALBANIA', 'CABO VERDE', 'IRAK', 'MALI', 'SERBIA',
        'MACEDONIA, EX REPUBLICA YUGOSLAVA DE', 'KOSOVO',
        'TANZANIA, REPUBLICA UNIDA DE', 'SUAZILANDIA', 'PAKISTAN',
        'UGANDA', 'ETIOPIA', 'MONGOLIA', 'BARBADOS', 'BELICE', 'GUYANA',
        'GUINEA', 'GEORGIA', 'VIETNAM', 'UZBEKISTAN', 'MARTINICA',
        'VANUATU', 'MADAGASCAR', 'ARMENIA', 'KAZAJSTAN', 'BOTSUANA',
        'MAURICIO', 'COSTA DE MARFIL', 'BRUNEI DARUSSALAM',
        'REPUBLICA ARABE SIRIA', 'MACAO', 'SANTO TOME Y PRINCIPE',
        'LIECHTENSTEIN', 'YEMEN', 'GUINEA-BISSAU', 'SIRIA',
        'CHINA, REPÚBLICA POPULAR', 'SUDAN', 'KIRGUISTAN',
        'COREA, REPUBLICA DEMOCRATICA POPULAR DE', 'DOMINICA',
        'ISLAS COMOROS', 'MONTENEGRO', 'NUEVA CALEDONIA',
        'ISLAS VIRGENES BRITANICAS', 'SANTA LUCIA', 'PAPUA NUEVA GUINEA',
        'GRANADA', 'NAMIBIA', 'GROENLANDIA', 'MALDIVAS',
        'SAINT KITTS Y NEVIS', 'POLINESIA FRANCESA', 'BURKINA FASO',
        'ZAMBIA', 'BURUNDI']

    class Config:
        schema_extra = {
            "example": {
                'País': 'ESPAÑA'
            }
        }


class APIModelBackEnd():
    '''
    Esta clase maneja el back end de nuestro modelo de Machine Learning para la API en FastAPI
    '''

    def __init__(self,Area_conocimiento,Sub_Area_Conocimiento,Estado_civil,Etnia_de_la_persona,Estatura):
        '''
        Este método se usa al instanciar las clases

        Aquí, hacemos que pida los mismos parámetros que tenemos en ModelInput.

        '''
        
        self.Area_conocimiento = Area_conocimiento
        self.Sub_Area_Conocimiento = Sub_Area_Conocimiento
        self.Estado_civil = Estado_civil
        self.Etnia_de_la_persona = Etnia_de_la_persona
        self.Estatura = Estatura

    def _load_model(self, model_filename: str = 'model.pkl'):
        '''
        Clase para cargar el modelo. Es una forma exótica de correr joblib.load pero teniendo funcionalidad con la API.
        Este método seguramente no lo van a cambiar, y si lo cambian, cambian el valor por defecto del string
        '''
        # Asignamos a un atributo el nombre del archivo
        self.model_filename = model_filename
        try:
            # Se intenta cargar el modelo
            self.model = joblib.load(self.model_filename)
        except Exception:
            # Si hay un error, se levanda una Exception de HTTP diciendo que no se encontró el modelo
            raise HTTPException(status_code=404, detail=f'Modelo con el nombre {self.model_filename} no fue encontrado')
        # Si todo corre ok, imprimimos que cargamos el modelo
        print(f"El modelo '{self.model_filename}' fue cargado exitosamente")

    def _prepare_data(self):
        '''
        Clase de preparar lo datos.
        Este método convierte las entradas en los datos que tenían en X_train y X_test.

        Miren el orden de las columnas de los datos antes de su modelo.
        Tienen que recrear ese orden, en un dataframe de una fila.

        '''
        # Pueden manejar así las variables categoricas.
        # Revisen los X!!! De eso depende que valores hay aquí.
        # Para ver más o menos que valores pueden ser, en un data frame se le aplico pd.get_dummies, corran algo como:
        # X_test[[col for col in X_test.columns if "nombre de columna" in col]].drop_duplicates()
        
        f2 = ['Área Conocimiento_AGRONOMÍA, VETERINARIA Y AFINES',
        'Área Conocimiento_AGRONOMÍA, VETERINARIA Y ZOOTECNIA',
        'Área Conocimiento_AVIACIÓN', 'Área Conocimiento_BELLAS ARTES',
        'Área Conocimiento_CIENCIAS DE LA EDUCACIÓN',
        'Área Conocimiento_CIENCIAS DE LA SALUD',
        'Área Conocimiento_CIENCIAS SOCIALES Y HUMANAS',
        'Área Conocimiento_COCINA Y CULINARIA',
        'Área Conocimiento_ECONOMÍA, ADMINISTRACIÓN CONTADURIA Y AFINES',
        'Área Conocimiento_INGENIERÍA, ARQUITECTURA Y AFINES',
        'Área Conocimiento_MATEMÁTICAS Y CIENCIAS NATURALES',
        'Área Conocimiento_NINGUNA', 'Área Conocimiento_NO INDICA',
        'Sub Area Conocimiento_ADMINISTRACIÓN',
        'Sub Area Conocimiento_AGRONOMÍA',
        'Sub Area Conocimiento_ANTROPOLOGÍA O ARTES LIBERALES',
        'Sub Area Conocimiento_ARQUITECTURA',
        'Sub Area Conocimiento_ARTES DRAMÁTICAS Y REPRESENTATIVAS',
        'Sub Area Conocimiento_ARTES PLÁSTICAS, VISUALES Y AFINES',
        'Sub Area Conocimiento_AVIACIÓN', 'Sub Area Conocimiento_BACTERIOLOGÍA',
        'Sub Area Conocimiento_BIBLIOTECOLOGÍA',
        'Sub Area Conocimiento_BIOLOGÍA, MICROBIOLOGÍA Y AFINES',
        'Sub Area Conocimiento_CIENCIA POLÍTICA Y/O RELACIONES INTERNACIONALES',
        'Sub Area Conocimiento_COCINA Y CULINARIA',
        'Sub Area Conocimiento_CONTADURÍA PÚBLICA',
        'Sub Area Conocimiento_DEPORTES, EDUCACIÓN FÍSICA Y RECREACIÓN',
        'Sub Area Conocimiento_DERECHO Y AFINES',
        'Sub Area Conocimiento_DISEÑO', 'Sub Area Conocimiento_ECONOMÍA',
        'Sub Area Conocimiento_EDUCACIÓN', 'Sub Area Conocimiento_ENFERMERÍA',
        'Sub Area Conocimiento_FILOSOFÍA, TEOLOGÍA Y AFINES',
        'Sub Area Conocimiento_FORMACIÓN MILITAR',
        'Sub Area Conocimiento_FÍSICA',
        'Sub Area Conocimiento_GEOGRAFÍA O HISTORIA',
        'Sub Area Conocimiento_GEOLOGÍA',
        'Sub Area Conocimiento_INGENIERÍA ADMINISTRATIVA Y AFINES',
        'Sub Area Conocimiento_INGENIERÍA AGROINDUSTRIAL, ALIMENTOS Y AFINES',
        'Sub Area Conocimiento_INGENIERÍA AGRONÓMICA, PECUARIA Y AFINES',
        'Sub Area Conocimiento_INGENIERÍA AGRÍCOLA, FORESTAL Y AFINES',
        'Sub Area Conocimiento_INGENIERÍA AMBIENTAL, SANITARIA Y AFINES',
        'Sub Area Conocimiento_INGENIERÍA BIOMÉDICA Y AFINES',
        'Sub Area Conocimiento_INGENIERÍA CIVIL Y AFINES',
        'Sub Area Conocimiento_INGENIERÍA DE MINAS, METALURGIA Y AFINES',
        'Sub Area Conocimiento_INGENIERÍA DE PETRÓLEOS',
        'Sub Area Conocimiento_INGENIERÍA ELECTRÓNICA, TELECOMUNICACIONES Y AFINES',
        'Sub Area Conocimiento_INGENIERÍA ELÉCTRICA Y AFINES',
        'Sub Area Conocimiento_INGENIERÍA EN SISTEMAS, TELEMÁTICA Y AFINES',
        'Sub Area Conocimiento_INGENIERÍA INDUSTRIAL Y AFINES',
        'Sub Area Conocimiento_INGENIERÍA MECÁNICA Y AFINES',
        'Sub Area Conocimiento_INGENIERÍA QUÍMICA Y AFINES',
        'Sub Area Conocimiento_INSTRUMENTACIÓN QUIRÚRGICA',
        'Sub Area Conocimiento_LENGUAS MODERNAS, FILOLOGÍA, LINGÜÍSTICA Y AFINES',
        'Sub Area Conocimiento_MATEMÁTICAS, ESTADÍSTICA Y AFINES',
        'Sub Area Conocimiento_MEDICINA',
        'Sub Area Conocimiento_MEDICINA VETERINARIA',
        'Sub Area Conocimiento_MÚSICA', 'Sub Area Conocimiento_NINGUNA',
        'Sub Area Conocimiento_NO INDICA',
        'Sub Area Conocimiento_NUTRICIÓN Y DIETÉTICA',
        'Sub Area Conocimiento_ODONTOLOGÍA', 'Sub Area Conocimiento_OPTOMETRÍA',
        'Sub Area Conocimiento_OTRAS INGENIERÍAS',
        'Sub Area Conocimiento_OTRO PROGRAMA DE BELLAS ARTES',
        'Sub Area Conocimiento_OTRO PROGRAMA DE SALUD',
        'Sub Area Conocimiento_OTROS ESTUDIOS EN CIENCIAS SOCIALES Y HUMANAS',
        'Sub Area Conocimiento_OTROS PROGRAMAS DE CIENCIAS NATURALES',
        'Sub Area Conocimiento_PERIODISMO, COMUNICACIÓN SOCIAL Y AFINES',
        'Sub Area Conocimiento_PSICOLOGÍA Y AFINES',
        'Sub Area Conocimiento_PUBLICIDAD Y AFINES',
        'Sub Area Conocimiento_QUÍMICA Y AFINES',
        'Sub Area Conocimiento_SALUD OCUPACIONAL (HSEQ)',
        'Sub Area Conocimiento_SALUD PÚBLICA',
        'Sub Area Conocimiento_SOCIOLOGÍA, TRABAJO SOCIAL Y AFINES',
        'Sub Area Conocimiento_TERAPIAS', 'Sub Area Conocimiento_ZOOTECNIA',
        'Estado civil_DESCONOCIDO', 'Estado civil_DIVORCIADO',
        'Estado civil_SOLTERO', 'Estado civil_UNION_LIBRE',
        'Estado civil_VIUDO', 'Etnia de la persona_GITANO',
        'Etnia de la persona_INDÍGENA', 'Etnia de la persona_NINGUNA',
        'Etnia de la persona_OTRO',
        'Etnia de la persona_PALENQUERO DE SAN BASILIO',
        'Etnia de la persona_PALENQUERO DE SAN BASILO',
        'Etnia de la persona_RAIZAL DEL ARCHIPIELAGO DE SAN ANDRES',
        'Etnia de la persona_SIN ETNIA REGISTRADA','Estatura_(CM)']
        
        
        df2 = pd.DataFrame(columns=f2,data=[[*[0]*len(f2)]])

        
        columA = [x for x in df2.columns if "Área Conocimiento_" in x and str(self.Area_conocimiento) == x.split('_')[-1]]
        df2[columA] = 1
        columS = [x for x in df2.columns if "Sub Area Conocimiento_" in x and str(self.Sub_Area_Conocimiento) == x.split('_')[-1]]
        df2[columS] = 1
        columE = [x for x in df2.columns if "Estado civil_" in x and str(self.Estado_civil) == x.split('_')[-1]]
        df2[columE] = 1
        columET = [x for x in df2.columns if "Etnia de la persona_" in x and str(self.Etnia_de_la_persona) == x.split('_')[-1]]
        df2[columET] = 1
        df2['Estatura (CM)'] = self.Estatura
        
        return df2

    def predict(self, y_name: str = 'País'):
        '''
        Clase para predecir.
        Carga el modelo, prepara los datos y predice.

        prediction = pd.DataFrame(self.model.predict(X)).rename(columns={0:y_name})

        '''
        self._load_model()
        X = self._prepare_data()
        prediction = pd.DataFrame(self.model.predict(X)).rename(columns={0: y_name})
        return prediction.to_dict(orient='records')