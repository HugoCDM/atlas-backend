from fastapi import APIRouter, status, HTTPException
from supabase_client import supabase_client

router = APIRouter(prefix='/api', tags=['api'])


@router.get('/locations')
async def get_mcmv_database():
    """Buscar dados Minha Casa Minha Vida"""
    try:
        response = supabase_client.table('mcmv-database').select('*').execute()
        return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'success': False,
                'error': 'table invalid or not found'
            }
        )
    
@router.get('/train-stations')
async def get_train_stations():
    """Buscar dados das estações de trem"""
    try:
        response = supabase_client.table('estacoes-trem').select('*').execute()
        return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'success': False,
                'error': 'table invalid or not found'
            }
        )

@router.get('/metro-stations')
async def get_metro_stations():
    """Buscar dados das estações de metrô"""
    try:
        response = supabase_client.table('estacoes-metro').select('*').execute()
        return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'success': False,
                'error': 'table invalid or not found'
            }
        )

@router.get('/state-schools')
async def get_state_schools():
    """Buscar dados das Escolas Estaduais"""
    try:
        response = supabase_client.table('escolas-estaduais').select('*').execute()
        return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'success': False,
                'error': 'table invalid or not found'
            }
        )

@router.get('/municipal-schools')
async def get_municipal_schools():
    """Buscar dados das Escolas Municipais"""
    try:
        response = supabase_client.table('escolas-municipais').select('*').execute()
        return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'success': False,
                'error': 'table invalid or not found'
            }
        )

@router.get('/federal-schools')
async def get_federal_schools():
    """Buscar dados das Escolas Federais"""
    try:
        response = supabase_client.table('escolas-federais').select('*').execute()
        return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'success': False,
                'error': 'table invalid or not found'
            }
        )

@router.get('/brt-stations')
async def get_brt_station():
    """Buscar dados das paradas do BRT"""
    try:
        response = supabase_client.table('estacoes-brt').select('*').execute()
        return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'success': False,
                'error': 'table invalid or not found'
            }
        )

@router.get('/vlt-stations')
async def get_vlt_stations():
    """Buscar dados das paradas do VLT"""
    try:
        response = supabase_client.table('vlt-paradas').select('*').execute()
        return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'success': False,
                'error': 'table invalid or not found'
            }
        )

@router.get('/equipments')
async def get_equipments():
    """Buscar dados de equipamentos"""
    try:
        response = supabase_client.table('gestao-equipamento-smas2023').select('*').execute()
        return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'success': False,
                'error': 'table invalid or not found'
            }
        )

@router.get('/squares')
async def get_squares():
    """Buscar dados das Praças"""
    try:
        response = supabase_client.table('pracas').select('*').execute()
        return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'success': False,
                'error': 'table invalid or not found'
            }
        )

@router.get('/municipal-health-units')
async def get_municipal_health_units():
    """Buscar dados Unidades de Saúde Municipais"""
    try:
        response = supabase_client.table('unidades-saude-municipais').select('*').execute()
        return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'success': False,
                'error': 'table invalid or not found'
            }
        )


@router.get('/supermarkets')
async def get_supermarkets():
    try:
        response = supabase_client.table('supermercados').select('*').execute()
        return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                'success': False,
                'error': 'table invalid or not found'
            }
        )
    
