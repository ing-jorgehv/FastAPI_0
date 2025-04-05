import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, Request
from tenacity import retry, wait_random_exponential, stop_after_attempt
from Business.api_business import hello_world_method, validate_method, env_var_method
from Utils.logger import LocalLogger
from Utils.error_handle import ApiControllerError





# Load environment variables
load_dotenv()



# Environment variables
ENVIRONMENT_VARIABLE_0 = os.environ.get("ENVIRONMENT_VARIABLE_0")
ENVIRONMENT_VARIABLE_1 = os.environ.get("ENVIRONMENT_VARIABLE_1")
ENVIRONMENT_VARIABLE_2 = os.environ.get("ENVIRONMENT_VARIABLE_2")



router = APIRouter()



# Create log file
root_path = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(root_path)
logger_file_path = os.path.join(parent_path, 'logs_file.txt')
logger = LocalLogger(logger_file_path, 'Logs local file created!')





@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(5))
@router.get("/hello_world")
async def hello_world():
    try:
        # Start main process
        response = await hello_world_method(logger)
        logger.info(f'The response is:\n {response.success} and its status code is {response.status_code} and its message is {response.message}')

        return response.to_dict()
    
    except Exception as e:
        logger.error(f'Error in hello_world: {e}')
        raise ApiControllerError(f"Error in hello_world: {e}")


@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(5))
@router.get("/env_var")
async def env_var():
    try:
        # Get environment variables
        var0 = ENVIRONMENT_VARIABLE_0 if ENVIRONMENT_VARIABLE_0 else ""
        var1 = ENVIRONMENT_VARIABLE_1 if ENVIRONMENT_VARIABLE_1 else ""
        var2 = ENVIRONMENT_VARIABLE_2 if ENVIRONMENT_VARIABLE_2 else ""

        # Start main process
        response = await env_var_method(logger, var0, var1, var2)
        logger.info(f'The response is:\n {response.success} and its status code is {response.status_code} and its message is {response.message}')

        return response.to_dict()
    
    except Exception as e:
        logger.error(f'Error in env_var_method: {e}')
        raise ApiControllerError(f"Error in env_var_method: {e}")
    

@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(5))
@router.post("/validate")
async def validate(request: Request):
    try:
        # Get query
        data = await request.json()
        param1 = data.get('param1', '')
        param2 = data.get('param2', '')

        if not param1:
            raise HTTPException(status_code=400, detail="param1 is missing!")

        # Send query to business logic
        response = await validate_method(logger, param1)
        logger.info(f'The response is:\n {response.success} and its status code is {response.status_code} and its message is {response.message}')

        return response.to_dict()
    
    except Exception as e:
        logger.error(f'Error in validate: {e}')
        raise ApiControllerError(f"Error in validate: {e}")