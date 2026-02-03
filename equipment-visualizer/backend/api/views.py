import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def upload_csv(request):
    """
    API endpoint to receive CSV file and return calculated statistics.
    
    Expected CSV columns:
    - equipment_name
    - equipment_type
    - flowrate
    - pressure
    - temperature
    """
    if 'file' not in request.FILES:
        return Response(
            {'error': 'No file provided'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    csv_file = request.FILES['file']
    
    try:
        # Read CSV file using Pandas
        df = pd.read_csv(csv_file)
        
        # Check for required columns (case-insensitive)
        required_columns = ['equipment_name', 'equipment_type', 'flowrate', 'pressure', 'temperature']
        df_columns_lower = [col.lower().strip() for col in df.columns]
        
        # Map column names (case-insensitive)
        column_mapping = {}
        for req_col in required_columns:
            found = False
            for df_col in df.columns:
                if df_col.lower().strip() == req_col:
                    column_mapping[req_col] = df_col
                    found = True
                    break
            if not found:
                return Response(
                    {'error': f'Missing required column: {req_col}'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        # Rename columns to standardize
        df_renamed = df.rename(columns={v: k for k, v in column_mapping.items()})
        
        # Calculate statistics
        total_equipment = len(df_renamed)
        
        # Calculate averages (handle missing values)
        avg_flowrate = df_renamed['flowrate'].mean() if 'flowrate' in df_renamed.columns else None
        avg_pressure = df_renamed['pressure'].mean() if 'pressure' in df_renamed.columns else None
        avg_temperature = df_renamed['temperature'].mean() if 'temperature' in df_renamed.columns else None
        
        # Count equipment per type
        equipment_per_type = df_renamed['equipment_type'].value_counts().to_dict()
        
        # Prepare response
        response_data = {
            'total_equipment': total_equipment,
            'average_flowrate': float(avg_flowrate) if avg_flowrate is not None and not pd.isna(avg_flowrate) else None,
            'average_pressure': float(avg_pressure) if avg_pressure is not None and not pd.isna(avg_pressure) else None,
            'average_temperature': float(avg_temperature) if avg_temperature is not None and not pd.isna(avg_temperature) else None,
            'equipment_per_type': equipment_per_type,
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
        
    except pd.errors.EmptyDataError:
        return Response(
            {'error': 'CSV file is empty'},
            status=status.HTTP_400_BAD_REQUEST
        )
    except pd.errors.ParserError as e:
        return Response(
            {'error': f'Invalid CSV format: {str(e)}'},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return Response(
            {'error': f'Error processing file: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
