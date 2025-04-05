from Entities.Response import Response
from Utils.logger import LocalLogger
from Services.validate_service import is_number, is_string




async def hello_world_method(logger: LocalLogger):
    response = Response(False, 500, None)
    try:
        # value
        message = "Hello world"
        
        # Create response to client
        response.message = message
        response.status_code = 200
        response.success = True
        logger.info(f'hello_world_method was completed successfully, status: {response.success}')
        return response

    except Exception as e:
        logger.error(f'Error in hello_world_method: {e}')
        response['message'] = f"Error in hello_world_method: {e}"
        return response



async def env_var_method(logger: LocalLogger, var1, var2, var3):
    response = Response(False, 500, None)
    try:
        variables = "variables: " + var1 + ", " + var2 + ", " + var3
        
        # Create response to client
        response.message = variables
        response.status_code = 200
        response.success = True
        logger.info(f'env_var_method was completed successfully, status: {response.success}')
        return response

    except Exception as e:
        logger.error(f'Error in env_var_method: {e}')
        response['message'] = f"Error in env_var_method: {e}"
        return response
    


async def validate_method(logger: LocalLogger, query):
    response = Response(False, 500, None)
    try:
        message = ""
        # Validate query
        if is_number(query):
            message = "The input is a number."
        elif is_string(query):
            message = "The input is a string."
        else:
            message = "The input is neither a number nor a string."

        
        # Create response to client
        response.message = message
        response.status_code = 200
        response.success = True
        logger.info(f'validate_method was completed successfully, status: {response.success}')
        return response

    except Exception as e:
        logger.error(f'Error in validate_method: {e}')
        response['message'] = f"Error in validate_method: {e}"
        return response
