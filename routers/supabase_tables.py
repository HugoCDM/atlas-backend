from fastapi import APIRouter, status, HTTPException
from supabase_client import supabase_client
import asyncio
from functools import partial

router = APIRouter(prefix='/api', tags=['api'])


def fetch_table_sync(table_name, columns):
    return supabase_client.table(table_name).select(columns).execute()


@router.get('/get-all-data')
async def get_all_data():
    try:
        loop = asyncio.get_event_loop()
    
        tables = {
            'train_stations': ('estacoes-trem', 'nome, rua, presencaRamais, latitude, longitude'),
            'metro_stations': ('estacoes-metro', 'nome, latitude, longitude'),
            'federal_schools': ('escolas-federais', 'unidade, endereco, zona, telefone, latitude, longitude'),
            'state_schools': ('escolas-estaduais', 'unidade, endereco, zona, telefone, latitude, longitude'),
            'municipal_schools': ('escolas-municipais', 'nome, tipo, latitude, longitude'),
            'squares': ('pracas', 'nomeCompleto, endereco, ap, latitude, longitude'),
            'hospitals': ('unidades-saude-municipais', 'NOME, ENDERECO, BAIRRO, TIPO_UNIDADE, CNES, HORARIO_SEMANA, TELEFONE, latitude, longitude'),
            'equipments': ('gestao-equipamento-smas2023', 'nome_equip, endereco, bairro, bairros_at, hierarquia, telefone, latitude, longitude'),
            'vlt': ('vlt-paradas', 'nome, latitude, longitude'),
            'brt': ('estacoes-brt', 'nome, corredor, latitude, longitude'),
            'supermarkets': ('supermercados', 'nome, latitude, longitude'),
        }
        keys = list(tables.keys())
        tasks = [
            loop.run_in_executor(None, fetch_table_sync, tables[key][0], tables[key][1]) for key in keys]

        results = await asyncio.gather(*tasks.values())

        data = {keys[i]: results[i].data for i in range(len(keys))}

        return {
                'success': True,
                'data': data
            }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"success": False, "error": str(e)}
        )


# @router.get('/locations')
# async def get_mcmv_database():
#     """Buscar dados Minha Casa Minha Vida"""
#     try:
#         response = supabase_client.table('mcmv-database').select('*').execute()
#         return response
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail={
#                 'success': False,
#                 'error': 'table invalid or not found'
#             }
#         )
    
# @router.get('/train-stations')
# async def get_train_stations():
#     """Buscar dados das estações de trem"""
#     try:
#         response = supabase_client.table('estacoes-trem').select('*').execute()
#         return response
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail={
#                 'success': False,
#                 'error': 'table invalid or not found'
#             }
#         )

# @router.get('/metro-stations')
# async def get_metro_stations():
#     """Buscar dados das estações de metrô"""
#     try:
#         response = supabase_client.table('estacoes-metro').select('*').execute()
#         return response
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail={
#                 'success': False,
#                 'error': 'table invalid or not found'
#             }
#         )

# @router.get('/state-schools')
# async def get_state_schools():
#     """Buscar dados das Escolas Estaduais"""
#     try:
#         response = supabase_client.table('escolas-estaduais').select('*').execute()
#         return response
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail={
#                 'success': False,
#                 'error': 'table invalid or not found'
#             }
#         )

# @router.get('/municipal-schools')
# async def get_municipal_schools():
#     """Buscar dados das Escolas Municipais"""
#     try:
#         response = supabase_client.table('escolas-municipais').select('*').execute()
#         return response
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail={
#                 'success': False,
#                 'error': 'table invalid or not found'
#             }
#         )

# @router.get('/federal-schools')
# async def get_federal_schools():
#     """Buscar dados das Escolas Federais"""
#     try:
#         response = supabase_client.table('escolas-federais').select('*').execute()
#         return response
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail={
#                 'success': False,
#                 'error': 'table invalid or not found'
#             }
#         )

# @router.get('/brt-stations')
# async def get_brt_station():
#     """Buscar dados das paradas do BRT"""
#     try:
#         response = supabase_client.table('estacoes-brt').select('*').execute()
#         return response
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail={
#                 'success': False,
#                 'error': 'table invalid or not found'
#             }
#         )

# @router.get('/vlt-stations')
# async def get_vlt_stations():
#     """Buscar dados das paradas do VLT"""
#     try:
#         response = supabase_client.table('vlt-paradas').select('*').execute()
#         return response
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail={
#                 'success': False,
#                 'error': 'table invalid or not found'
#             }
#         )

# @router.get('/equipments')
# async def get_equipments():
#     """Buscar dados de equipamentos"""
#     try:
#         response = supabase_client.table('gestao-equipamento-smas2023').select('*').execute()
#         return response
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail={
#                 'success': False,
#                 'error': 'table invalid or not found'
#             }
#         )

# @router.get('/squares')
# async def get_squares():
#     """Buscar dados das Praças"""
#     try:
#         response = supabase_client.table('pracas').select('*').execute()
#         return response
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail={
#                 'success': False,
#                 'error': 'table invalid or not found'
#             }
#         )

# @router.get('/municipal-health-units')
# async def get_municipal_health_units():
#     """Buscar dados Unidades de Saúde Municipais"""
#     try:
#         response = supabase_client.table('unidades-saude-municipais').select('*').execute()
#         return response
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail={
#                 'success': False,
#                 'error': 'table invalid or not found'
#             }
#         )


# @router.get('/supermarkets')
# async def get_supermarkets():
#     try:
#         response = supabase_client.table('supermercados').select('*').execute()
#         return response
#     except Exception:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail={
#                 'success': False,
#                 'error': 'table invalid or not found'
#             }
#         )
    



