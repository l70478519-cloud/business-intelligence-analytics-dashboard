import sys
sys.path.insert(0,'.')
from fastapi.testclient import TestClient
from app.main import app
def test_health_and_create():
 c=TestClient(app); assert c.get('/health').status_code==200
 assert c.post('/api/metrics',json={"label":"Synthetic demo","value":"100"}).status_code==201
