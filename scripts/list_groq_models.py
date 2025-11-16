import os, json
from dotenv import load_dotenv
load_dotenv()
from groq import Groq
client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

try:
    models_resp = None
    if hasattr(client, 'models') and hasattr(client.models, 'list'):
        models_resp = client.models.list()
    elif hasattr(client, 'list_models'):
        models_resp = client.list_models()
    else:
        models_resp = None
    names = []
    if models_resp is None:
        print('NO_LIST_METHOD')
    else:
        if hasattr(models_resp, 'data'):
            items = models_resp.data
        elif isinstance(models_resp, dict):
            items = models_resp.get('data') or models_resp.get('models') or models_resp.get('items') or []
        else:
            try:
                items = list(models_resp)
            except Exception:
                items = [models_resp]
        for m in items:
            if isinstance(m, dict):
                names.append(m.get('name') or m.get('id') or str(m))
            else:
                n = getattr(m, 'name', None) or getattr(m, 'id', None) or str(m)
                names.append(n)
        print('MODELS_JSON:'+json.dumps(names))
except Exception as e:
    print('ERROR:'+str(e))
