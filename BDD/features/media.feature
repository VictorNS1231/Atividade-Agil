# BDD = Exemplificar com testes casos de uso (features) do sistema/classes e assim colaborar com um time utilizando uma linguagem humana. 
# Pode ser lido por Stakeholder/PO/Scrum Master 

Feature: Média de dois números 
  Scenario: Realizar a média simples entre dois números 
    Given eu tenho dois números flutuantes: 5 e 7 
    When eu somo os dois números flutuantes e divido por dois 
    Then o resultado deve ser 6 
  
    Given eu tenho dois números flutuantes: 3 e 4
    When eu somo os dois números flutuantes e divido por dois 
    Then o resultado deve ser 3,5                                                                            