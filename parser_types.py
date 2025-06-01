import re
from typing import Any, List, Literal, Optional

from pydantic import BaseModel, field_validator


#pylint: disable=E1133,E0213,C0209
class ApiScheme(BaseModel):
    objects: List["ApiObject"]
    methods: List["ApiMethod"]


    def to_code_objects(self) -> str:
        return '\n\n'.join(el.to_code() for el in self.objects)
    
    def to_code_methods(self) -> str:
        return """class ApiWrapper:
    def __init__(self, token: str, *, api_url: str = "https://api.telegram.org/"):
        self.token = token
        self.api_url = api_url
        self.client = AsyncClient(
            base_url=api_url + "bot" + token + '/'
        )

    async def exec_request(
            self,
            method: str,
            json: Dict,
            return_type: Type[T]
    ) -> T:
        result = await self.client.post(
            method,
            json=json
        )
        mdl = ApiResponse[return_type]# type: ignore
        response = mdl.model_validate(result.json())
        return response.result

    {methods}
""".format(
    methods='\n\n    '.join(el.to_function() for el in self.methods)
) 
        



PythonReservedNames = {
    "from": "from_",
    "format": "format_",
    "type": "type_",
}

ApiObjectTypes = Literal[
    "properties", 
    "reference", 
    "any_of", 
    "unknown",
    "integer",
    "string",
    "bool",
    "array",
    "float"
]

JsonToPythonTypes = {
    "integer": "int",
    "string": "str",
    "bool": "bool",
    "float": "float"
}

class ApiTypeInfo(BaseModel):
    type: ApiObjectTypes
    enumeration: Optional[List] = None
    reference: Optional[str] = None
    default: Optional[Any] = None
    array: Optional["ApiTypeInfo"] = None
    any_of: Optional[List["ApiTypeInfo"]] = None

    def to_typehint(self, *, ref_str: bool = True) -> str:
        typehint = ""
        if self.type == "any_of" and self.any_of:
            typehint = f"Union[{', '.join(el.to_typehint(ref_str=ref_str) for el in self.any_of)}]"
        elif self.type == "array" and self.array:
            typehint = f"List[{self.array.to_typehint(ref_str=ref_str)}]"
        elif self.type == "unknown":
            ...
        elif self.type == "reference" and self.reference:
            if ref_str:
                typehint = f"\"{self.reference}\""
            else:
                typehint = f"objects.{self.reference}"
        else: 
            typehint = JsonToPythonTypes[self.type]

        return typehint

# Methods
class ApiMethod(BaseModel):
    name: str
    description: str
    arguments: List["ApiProperty"]
    maybe_multipart: bool
    return_type: ApiTypeInfo
    @field_validator("description")
    def validate_description(cls, value: str, _):
        # replace "
        value = value.replace("\"", "'")
        # replace \_
        value = value.replace("\\", "")
        return value
    
    def to_function(self) -> str:
        args = []
        args_opt = []
        json_params = []
        
        for el in self.arguments:
            if el.required:
                args.append(el.to_typehint(ref_str=False))
            else:
                args_opt.append(el.to_typehint(ref_str=False))
            json_params.append(f"\"{el.name[:-1] if el.name.endswith('_') else el.name}\": {el.name}")

        if args_opt:
            args.append('*')
            args += args_opt
        snake_case_name = re.sub(r'(?<!^)(?=[A-Z])', '_', self.name).lower()
        return '''async def {snake_case_name}(self{first_comma}{args}) -> {return_typehint}:
        """{description}

        Args:
            {doc_args}
        """
        response_api: {return_typehint} = await self.exec_request(
            "{name}",
            json={json_params},
            return_type={return_typehint} # type: ignore

        )
        return response_api
'''.format(
    snake_case_name=snake_case_name,
    description=self.description,
    name=self.name,
    json_params='{' + ',\n                '.join(json_params) + '}',
    first_comma=', ' if args else '',
    args=', '.join(args),
    return_typehint=self.return_type.to_typehint(ref_str=False),
    doc_args='\n            '.join([el.to_doc_line() for el in self.arguments]),


)

# Objects
class ApiProperty(BaseModel):
    name: str
    description: str
    required: bool
    type_info: ApiTypeInfo

    @field_validator("name")
    def validate_name(cls, value, _):
        formated_name = PythonReservedNames.get(value)
        return formated_name or value
    
    @field_validator("description")
    def validate_description(cls, value: str, _):
        # replace "
        value = value.replace("\"", "'")
        # replace \_
        value = value.replace("\\", "")
        return value

    def to_typehint(self, *, ref_str: bool = True) -> str:

        default_value = self.type_info.default or None

        if default_value and self.type_info.type == "string":
            default_value = f"\"{default_value}\""
        if not self.required:
            return f"{self.name}: Optional[{self.type_info.to_typehint(ref_str=ref_str)}] = {default_value}"

        return f"{self.name}: {self.type_info.to_typehint(ref_str=ref_str)}{' = ' + str(default_value) if default_value else ''}" 
    
    def to_obj_var(self) -> str:
        return f"self.{self.name} = {self.name}"
    
    def to_doc_line(self) -> str:
        return f"{self.name} ({self.type_info.to_typehint()}): {self.description}"



class ApiObject(BaseModel):
    name: str
    description: str
    type: ApiObjectTypes
    documentation_link: str
    properties: Optional[List[ApiProperty]] = None
    any_of: Optional[List[ApiTypeInfo]] = None

    @field_validator("description")
    def validate_description(cls, value: str, _):
        # replace "
        value = value.replace("\"", "'")
        # replace \_
        value = value.replace("\\", "")
        return value

    def __to_code_properties(self) -> str:
        if not self.properties:
            raise ValueError("can not parse properties")
        
        typehints = []
        typehints_optional = []
        vars_init = []
        doc_lines = []
        for el in self.properties:
            if el.required and not el.type_info.default:
                typehints.append(el.to_typehint())
            else:
                typehints_optional.append(el.to_typehint())
            doc_lines.append(el.to_doc_line())
            vars_init.append(el.to_obj_var())

        if typehints_optional:
            # typehints.append('*')
            typehints += typehints_optional
        return """class {name}(BaseModel):
    \"\"\"{description}

    {documentation_link}
    \"\"\"
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=lambda x: x[:-1] if x in reserved_python else x,
    )
    {properties} 
    
""".format(
    name=self.name,
    description=self.description,
    documentation_link=self.documentation_link,
    properties='\n    '.join([f"{el.to_typehint()}\n    \"\"\"{el.to_doc_line()}\"\"\"" for el in self.properties])
)
    
    def __to_code_any_of(self) -> str:
        if not self.any_of:
            raise ValueError("can not parse any_of")
        return f"{self.name} = Union[{', '.join(el.to_typehint() for el in self.any_of)}]\n\"\"\"{self.description}\"\"\""

    def __to_code_unknown(self) -> str:
        return f"{self.name} = Any\n\"\"\"{self.description}\"\"\""

    def to_code(self) -> str:
        if self.type == "properties":
            return self.__to_code_properties()
        elif self.type == "any_of":
            return self.__to_code_any_of()
        elif self.type == "unknown":
            return self.__to_code_unknown()
        print(self.name, "can not be parsed!")
        return ""
        
