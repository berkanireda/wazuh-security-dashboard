from django.shortcuts import render
import pandas as pd
# Create your views here.
from django.http import JsonResponse
import json
import math

def dashboard(request):
    try:
        # Read log data from a CSV file
        df = pd.read_csv(f'siem/static/logdata9.csv', encoding="ISO-8859-1")

        # Calculate the total number of attacks
        nb_attaques = df.shape[0]
        
        # Convert 'v013xxxxdate' column to datetime format
        df['date'] = pd.to_datetime(df['v013xxxxdate'])
        
        # Extract the day of the week from the date
        df['day_of_week'] = df['date'].dt.date.astype(str)
        print('these are known exploits :',df[df['sub_type'] == '"Line Comments"'])
        
        # Group data by day of the week and sub_type, count occurrences
        result_df = df.groupby(['day_of_week', 'sub_type']).size().reset_index(name='count')
        print(result_df)

        # Count occurrences of each threat level
        threat_level_counts = df['threat_level'].value_counts().to_dict()

        # Count occurrences of each server pool and create data for a pie chart
        server_pool_data = df['server_pool_name'].value_counts().to_dict()
        server_pool_list = []
        server_pool_categories = list(df['server_pool_name'].unique())
        for cat in server_pool_categories:
            
            cat = str(cat)
            if cat != 'nan':
                server_pool_list.append(server_pool_data[cat])
        print(server_pool_list)
        cleaned_server_pool_categories = [value for value in server_pool_categories if type(value) == type('a')]
        print("cleaned list",cleaned_server_pool_categories)
        print(server_pool_categories)
        # server_pool_list = [server_pool_data['"pool_salesreport"'], server_pool_data['"pool_tms"'],
        #                server_pool_data['"pool_kelio"'], server_pool_data['"pool_cevicloud"'],
        #                server_pool_data['"pool_mail"']]
        server_pool = {
            'labels': cleaned_server_pool_categories,
            'values': server_pool_list,
            'colors': ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#448040', '#022A4F'],
        }

        # Organize data for bar chart: day_of_week -> sub_type -> count
        data = {}
        sub_types = []
        for _, row in result_df.iterrows():
            day_of_week = row['day_of_week']
            feature = row['sub_type']
            if feature not in sub_types:
                sub_types.append(feature)
            count = row['count']
            if day_of_week not in data:
                data[day_of_week] = {}
            data[day_of_week][feature] = count

        # Group data by day of the week and threat level, count occurrences
        result_df2 = df.groupby(['day_of_week', 'threat_level']).size().reset_index(name='count')
        data2 = {}

        # Organize data for bar chart: day_of_week -> threat_level -> count
        for _, row in result_df2.iterrows():
            day_of_week = row['day_of_week']
            feature = row['threat_level']
            count = row['count']
            if day_of_week not in data2:
                data2[day_of_week] = {}
            data2[day_of_week][feature] = count

        # Count specific attack occurrences
        specific_attack_counts = (df[df['sub_type'] == '"Known Exploits"'].shape[0] +
                                  df[df['sub_type'] == '"Generic Attacks"'].shape[0] +
                                  df[df['sub_type'] == '"SQL Injection"'].shape[0] +
                                  df[df['sub_type'] == '"Embedded Queries SQL Injection"'].shape[0] +
                                  df[df['sub_type'] == '"Stacked Queries SQL Injection"'].shape[0] +
                                  df[df['sub_type'] == '"SQL Function Based Boolean Injection"'].shape[0] +
                                  df[df['sub_type'] == '"Cross Site Scripting"'].shape[0])

        # Render the 'dashboard.html' template with data to display
        return render(request, 'dashboard.html', {'nb_attaques': nb_attaques,
                                                   'bar_data': data,
                                                   'threat_level': threat_level_counts,
                                                   'server_pool': server_pool,
                                                   'chart_data': data2,
                                                   'test': result_df.to_dict(),
                                                   'sub_types' : sub_types,
                                                   'specific_attacks_count': specific_attack_counts})
    except FileNotFoundError:
        # Return an error message as JSON if the CSV file is not found
        return JsonResponse({'error': 'CSV file not found.'})

      


