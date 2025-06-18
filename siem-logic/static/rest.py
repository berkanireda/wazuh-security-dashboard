import numpy as np
import pandas as pd
import re
import sys



def Structuration():
    
    if len(sys.argv) < 2:
        print("Usage: python script.py <parameter> - Saisissez le nom du fichier")
        return

    file_name = sys.argv[1]
    
    columns = ['v013xxxxdate', 'time', 'log_id', 'msg_id', 'device_id', 'vd', 'timezone', 'timezone_dayst', 'type', 'pri', 'main_type',
          'sub_type', 'trigger_policy', 'severity_level', 'proto', 'service', 'backend_service', 'action', 'policy', 'src', 'src_port',
          'dst', 'dst_port', 'http_method', 'http_url', 'http_host', 'http_agent', 'http_session_id', 'msg', 'signature_subclass',
          'signature_id', 'signature_cve_id', 'srccountry', 'content_switch_name', 'server_pool_name', 'false_positive_mitigation',
          'user_name', 'monitor_status', 'http_refer', 'http_version', 'dev_id', 'es', 'threat_weight', 'history_threat_weight',
          'threat_level', 'ftp_mode', 'ftp_cmd', 'cipher_suite', 'ml_log_hmm_probability', 'ml_log_sample_prob_mean',
          'ml_log_sample_arglen_mean', 'ml_log_arglen', 'ml_svm_log_main_types', 'ml_svm_log_match_types', 'ml_svm_accuracy',
          'ml_domain_index', 'ml_url_dbid', 'ml_arg_dbid', 'ml_allow_method', 'owasp_top10', 'bot_info', 'client_level', 'x509_cert_subject', 'owasp_api_top10']
    df = pd.read_csv(file_name, encoding = "ISO-8859-1", sep=';',  names=columns)
   
    # df['date'] = pd.to_datetime(df['v013xxxxdate'])
    
    df['data'] = df['v013xxxxdate'] + df['time'].fillna('') + df['log_id'].fillna('') + df['msg_id'].fillna('') + df['device_id'].fillna('') + df['vd'].fillna('') + df['timezone'].fillna('') + df['timezone_dayst'].fillna('') + df['type'].fillna('') + df['pri'].fillna('') + df['main_type'].fillna('') + df['sub_type'].fillna('') + df['trigger_policy'].fillna('') + df['severity_level'].fillna('')+ df['proto'].fillna('') + df['service'].fillna('') + df['backend_service'].fillna('') + df['action'].fillna('') + df['policy'].fillna('') + df['src'].fillna('')
    default_value = []
    df_dict = {key: default_value for key in columns}

    real_data = pd.DataFrame(df_dict)

    i = 1
    j = 1
        
    PATTERN = re.compile(r'''((?:[^,"']|"[^"]*"|'[^']*')+)''')
    PATTERN2 = re.compile(r'''((?:[^="']|"[^"]*"|'[^']*')+)''')
    keys = []
    values = []

    data = df['data']

    for row in data:
        
        if type(row) != type('a'):
                row = str(row)
            
        row_pairs = []
        for p in PATTERN.split(row)[1::2]:
                if p[0] == '"':
                    p = p[1:-1]
                row_pairs.append(PATTERN2.split(p)[1::2])
        try:    
                d = dict(row_pairs)
        except:
                pass
        d1 = pd.DataFrame(d, index=[0])
        real_data =  pd.concat([real_data, d1]) 
        
    real_data.to_csv('logdata9.csv', index=False)
    
    
Structuration()