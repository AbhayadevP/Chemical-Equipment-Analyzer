from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import io


@api_view(['POST'])
def analyze_csv(request):
    """
    This function receives a CSV file, processes it, and returns statistics.
    
    Flow:
    1. Check if file exists in request
    2. Read CSV using Pandas
    3. Calculate statistics
    4. Return JSON response
    """
    
    # Step 1: Check if file was uploaded
    if 'file' not in request.FILES:
        return Response(
            {'error': 'No file provided'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    csv_file = request.FILES['file']
    
    # Step 2: Read CSV file using Pandas
    try:
        # Read the file content
        file_content = csv_file.read().decode('utf-8')
        
        # Convert to Pandas DataFrame
        df = pd.read_csv(io.StringIO(file_content))
        
        # Step 3: Validate required columns exist
        required_columns = ['equipment_name', 'equipment_type', 'flowrate', 'pressure', 'temperature']
        
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            return Response(
                {'error': f'Missing columns: {", ".join(missing_columns)}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Step 4: Calculate statistics
        total_equipment = len(df)
        avg_flowrate = df['flowrate'].mean()
        avg_pressure = df['pressure'].mean()
        avg_temperature = df['temperature'].mean()
        
        # Count equipment per type
        equipment_counts = df['equipment_type'].value_counts().to_dict()
        
        # Step 5: Prepare response data
        response_data = {
            'total_equipment': total_equipment,
            'average_flowrate': round(avg_flowrate, 2),
            'average_pressure': round(avg_pressure, 2),
            'average_temperature': round(avg_temperature, 2),
            'equipment_by_type': equipment_counts
        }
        
        # Step 6: Return JSON response
        return Response(response_data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response(
            {'error': f'Error processing file: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )