# CSV -> XLS

A versão atual pega os valores das primeiras duas colunas da UI do Cost Explorer e passa para uma tabela em Excel. 

## Workflow

- garanta que python3 esteja instalado na máquina. caso contrário, baixe a versão correta para seu OS em https://www.python.org/downloads/

- ative o venv para o código com ```source venv/bin/activate``` (linux) ou ```venv\Scripts\activate``` (windows)

- ```pip install -r requirements.txt```

- Baixe o arquivo para dentro da pasta do código com o nome ```costs.csv```

- abra o terminal e ```cd``` para o diretório do repositório

- rode o código com ```python3 main.py```

- recolha os dados de ```structured_costs.xls```

- feche o arquivo ```structured_costs.xls``` após uso, para possibilitar a próxima conversão de CSV para XLS

## Limitações

- Atualmente o arquivo structured_costs.xls precisa ser excluído para funcionar

- Os valores estão sendo passados 
