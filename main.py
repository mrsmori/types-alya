import logging
import requests

import autopep8# type: ignore

from parser_types import ApiScheme, PythonReservedNames


logging.basicConfig(level=logging.INFO)

logging.info("Fetching v2 api")
# Using .json parsed api from https://github.com/ark0f/tg-bot-api
data = requests.get("https://ark0f.github.io/tg-bot-api/custom_v2.json", timeout=15).json()

logging.info("Parsing models...")
parsed = ApiScheme.model_validate(data)

logging.info("Generate api objects...")
with open("alya_types/objects.py", "w", encoding="utf-8") as f:
    f.write(f"""
from typing import Union, Optional, Any, List
            
from pydantic import BaseModel, ConfigDict
            
reserved_python = ({', '.join([f'"{el}"' for el in PythonReservedNames.values()])})

# pylint: disable=C0301,C0302,W0611

{autopep8.fix_code(parsed.to_code_objects())}""")
    
logging.info("Generate api wrapper...")
with open("alya_types/api_wrapper.py", "w", encoding="utf-8") as f:
    f.write(f"""
from typing import Dict, Union, Optional, List, TypeVar, Generic, Type

from httpx import AsyncClient    
from pydantic import BaseModel
            
from alya_types import objects
            

# pylint: disable=C0301,C0302
T = TypeVar('T')
            

class ApiResponse(BaseModel, Generic[T]):
    ok: bool
    result: T

{autopep8.fix_code(parsed.to_code_methods())}""")
    
logging.info("Work done!")
