from fastapi.testclient import TestClient
import pytest
from main import app,mdata
  




# @pytest.fixture()
# def SetUp():
#     mdata.clear()
#     ff = {
#    "A":[[1,2],[3,4]],
#    "B":[[4,4],[5,6]],
#    "i":0,
#    "j":0 
#     }
#     mdata.copy(ff)
    

# def client():
#     return TestClient(app)

client = TestClient(app)

def test_create():
    respon = client.post("/Ko",json={
   "A":[[1,2],[3,4]],
   "B":[[3,4],[5,6]],
   "i":0,
   "j":0 
    })
    assert respon.status_code == 200
    assert respon.json() == ("Answer is :13")
    
