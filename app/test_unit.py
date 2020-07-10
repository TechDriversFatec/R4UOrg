import pytest
import server

def test ():
  response = server.getFilmeByGrupo(7)
  assert response == 'filme'
