from fastapi import APIRouter, HTTPException
from app.services.executor import CommandExecutor

router = APIRouter()
executor = CommandExecutor()

@router.post("/execute")
async def execute_command(command: str):
    try:
        output = executor.run_command(command)
        return {"output": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))