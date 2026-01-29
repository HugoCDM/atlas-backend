from fastapi import APIRouter, status, HTTPException
from supabase_client import supabase_client
import asyncio
from concurrent.futures import ThreadPoolExecutor

router = APIRouter(prefix='/api', tags=['api'])

# Pool de threads para queries síncronas do Supabase
executor = ThreadPoolExecutor(max_workers=12)


def fetch_table(table_name: str, columns: str):
    """Fetch síncrono de uma tabela - simples e direto"""
    try:
        result = supabase_client.table(table_name).select(columns).execute()
        return result.data if result.data else []
    except Exception as e:
        print(f"❌ Erro ao buscar {table_name}: {e}")
        return []


@router.get('/health')
async def health():
    return {'status': 'ok'}


@router.get('/get-all-data')
async def get_all_data():
    
    try:
        loop = asyncio.get_event_loop()
        
        tasks = [
            loop.run_in_executor(executor, fetch_table, 'estacoes-trem', 'nome, rua, presencaRamais, latitude, longitude'),
            loop.run_in_executor(executor, fetch_table, 'estacoes-metro', 'nome, latitude, longitude'),
            loop.run_in_executor(executor, fetch_table, 'escolas-federais', 'unidade, endereco, zona, telefone, latitude, longitude'),
            loop.run_in_executor(executor, fetch_table, 'escolas-estaduais', 'unidade, endereco, zona, telefone, latitude, longitude'),
            loop.run_in_executor(executor, fetch_table, 'escolas-municipais', 'nome, tipo, latitude, longitude'),
            loop.run_in_executor(executor, fetch_table, 'pracas', 'nomeCompleto, endereco, ap, latitude, longitude'),
            loop.run_in_executor(executor, fetch_table, 'unidades-saude-municipais', 'NOME, ENDERECO, BAIRRO, TIPO_UNIDADE, CNES, HORARIO_SEMANA, TELEFONE, latitude, longitude'),
            loop.run_in_executor(executor, fetch_table, 'gestao-equipamento-smas2023', 'nome_equip, endereco, bairro, bairros_at, hierarquia, telefone, latitude, longitude'),
            loop.run_in_executor(executor, fetch_table, 'vlt-paradas', 'nome, latitude, longitude'),
            loop.run_in_executor(executor, fetch_table, 'estacoes-brt', 'nome, corredor, latitude, longitude'),
            loop.run_in_executor(executor, fetch_table, 'supermercados', 'nome, latitude, longitude'),
            loop.run_in_executor(executor, fetch_table, 'hospitais-estaduais', 'nome, latitude, longitude'),
            loop.run_in_executor(executor, fetch_table, 'hospitais-federais', 'nome, latitude, longitude'),
        ]

        results = await asyncio.gather(*tasks)
        
        train_stations, metro_stations, federal_schools, state_schools, municipal_schools, squares, hospitals, equipments, vlt, brt, supermarkets, federal_hospitals, state_hospitals = results
        
        total_items = sum(len(r) for r in results)
        print(f"Total de itens carregados: {total_items}")
        
        data = {
            'train_stations': train_stations,
            'metro_stations': metro_stations,
            'federal_schools': federal_schools,
            'state_schools': state_schools,
            'municipal_schools': municipal_schools,
            'squares': squares,
            'municipal_hospitals': hospitals,
            'equipments': equipments,
            'vlt': vlt,
            'brt': brt,
            'supermarkets': supermarkets,
            'federal_hospitals': federal_hospitals,
            'state_hospitals': state_hospitals
        }

        return {
            'success': True,
            'data': data
        }
    
    except Exception as e:
        print(f"❌ Erro geral: {e}")
        raise HTTPException(
            status_code=500,
            detail={"success": False, "error": str(e)}
        )

