# 1. Projeto mvpPADOCA

Este projeto é um MVP (produto viável mínimo) que tem por objetivo demonstrar a utilização das seguintes tecnologias com o intuito de disponibilizar uma API para um resolvedor de problemas de otimização (PLIs) que possa ser acessada por diferentes sistemas. 

- Flask
- Flask Restful
- LocalSolver

No caso específico deste MVP o problema resolvido é descrito em [2] e sua utilização é descrita em [4]. O passo-a-passo para a execução do projeto são listados em [3].

# 2. Problema: PADOCA

## Descrição

No Problema PADOCA (Problema da Alocação de Demandas Orientadas de Clientes em Abastecedores), uma quantidade _C_ de clientes possuem demandas que devem ser atendidas por _A_ abastecedores. 

Para cada combinação _cliente_ x _abastecedor_ existe um custo de alocação da demanda do cliente _ci_ no abastecedor _ai_.

Por exemplo, para um cliente _ci=2_, existe os custos _c2f1=7_ indicando que o abastecedor 1 atende a demanda do cliente 2 com custo 7.

Além do custo de alocação da demanda, cada abastecedor também possui um custo de _ai_ de ativação. Para que o abastecedor 1 possa atender o cliente 2, por exemplo, um custo _a1=100_ deve ser pago uma vez nessa alocação de demandas. Caso o custo de ativação de um abastecedor esteja pago, ele pode ser usado para atender quaisquer clientes. 



## Modelo Matemático

### Constantes

- _kc_: quantidade de clientes
- _ka_: quantidade de abastecedor
- _cia_: custo de alocação da demanda do cliente _i_ no abastecedor _a_, _0_ <= _i_ <= _kc_, _0_ <= _a_ <= _ka_.
- _va_: custo de ativação do Fornecedor _0_ <= _a_ < _ka_

### Variáveis

- _xij_: é 1 se o Cliente _i_ tem demanda atendida pelo Abastecedor j e 0 caso contrário.  _0_ <= _i_ <= _kc_, _0_ <= _j_ <= _ka_.
- _yj_: é 1 se o Abastecedor _j_ foi ativado e 0 caso contrário. _0_ <= _j_ < _kf_

### Objetivo

- _min_ SUM(SUM(_xij_ * _cia_)) +  SUM(_yj_ * _vj_) 


### Modelagem

_min_ SUM(SUM(_xij_ * _cif_)) +  SUM(_yj_ * _aj_) 

1. SUM(_xij_) >= 1  , Para todo _j_, _0_ <= _j_ < _ka_

1. _yj_ >= _xij_    , Para todo _j_, _0_ <= _j_ < _ka_, Para todo _0_ <= _i_ <= _kc_

1. _xij_ in {0,1}

1. _yj_ in {0,1}


# 3. Instanciação e Execução do Projeto

Clonar o projeto

    git clone git@github.com:Borghezane/mvpPLPython.git

Acessar o diretório

    cd mvpPLPython

Criar um diretório venv

    python3 -m venv venv

Ativar o _environment_

    . venv/bin/activate

Instalar dependências:

    pip install Flask
    pip install flask-restful
    pip install flask_httpauth
    pip install localsolver -i https://pip.localsolver.com

Executar o arquivo api.py:

    python3 api.py

Fazer requisições:

    curl http://localhost:5000/todo1 -d "data=Tirar o lixo" -X PUT


# 4. Utilização

A API oferece duas operações:

- **init**
- **getSol**

## Init

**Entrada:**


        curl --header "Content-Type: application/json"   --request POST  --data '{"nAbastecedores": "3", "nClients": "5", "custoAbastecedorCliente":[["1","2","3"],["5","7","5"],["3","9","2"],["9","1","4"],["1","154","13"]],"custoAbastecedor": ["10","2","7"]}'   http://localhost:5000/api/v1/init

Dados do Problema

- nAbastecedores: inteiro que indica a quantidade de Abastecedores
- nClientes: inteiro que indica a quantidade de Clientes
- custoAbastecedorCliente: um vetor custos para cada cliente _i_. Dentro de cada i-ésimo vetor, cada posição _j_ indica o custo de alocação da demanda do Cliente _i_ no Abastecedor _j_.
- custoAbastecedor: vetor com o custo de ativação de cada Abastecedor _j_.

Segue o exemplo de chamada:

	 {
	     nAbastecedores: "3",
	     nClients: "5",
	     custoAbastecedorCliente: [
		 ["1","2","3"],
		 ["5","7","5"],
		 ["3","9","2"],
		 ["9","1","4"],
		 ["1","154","13"]
	     ],
	     custoAbastecedor: ["10","2","7"]
	 }

	


**Saída:**

- ID de execução e Senha para autenticação

Segue o exemplo:

     {
 	     id:"8075662",
	     password: "eTr#21@!!lop"
	 }


## getSol

**Entrada:**

Uma requisição com os dados de autenticação equivalentes aos recebidos como saída da operação `init`.

curl --user admin:admin http://localhost:5000/api/v1/private

**Saída:**

Caso a instância ainda não esteja resolvida, retorna um JSON indicando que ainda não foi encerrado:
	

	 {
	     custo:"-inf",
	     solucao: ["-1","-1","-1","-1","-1"]
	     encerrado: "false"
	 }

Caso contrário, retorna o resultado da função objetivo (soma dos custos) e um vetor solução indicando em qual fornecedor cada cliente teve a sua demanda alocada. Neste caso, `encerrado-true`.

 	 {
	     custo:"107",
	     solucao: ["0","1","1","0","1"]
	     encerrado: "true"
	 }



