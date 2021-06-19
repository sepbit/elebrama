# Elebrama

> ELEição no BRAsil para MAstodon

Resultado da eleição no Brasil para Mastodon

Fonte: [TSE](https://www.tse.jus.br/eleicoes/eleicoes-2020/eleicoes-2020/interessados-na-divulgacao-de-resultados)

Esse pacote é compatível com [Pylint](https://www.pylint.org).

# Instalação

``` bash
# apt install -y python3 python3-pip python3-setuptools python3-wheel python3-venv python3-dev
```

``` bash
$ python3 -m venv env
$ source ./env/bin/activate
$ pip install -r requirements.txt
$ python3 -m pip install .
```

# Configuração

Em sua instância [Mastodon](https://joinmastodon.org), crie um aplicativo com a permissão `write:statuses`

Defina as variáveis do ambiente `INSTANCE` e `TOKEN`, veja o arquivo [.env](.env)

``` bash
$ export INSTANCE="foo bar"
$ export TOKEN="bar foo"
```

## Execução

Se você não receber mensagem, deu tudo certo!

``` bash
$ ./env/bin/elebrama ms 9054
```

## Testes

Execução de testes e verificar a cobertura de código

``` bash
$ ./env/bin/tox 
```

## Registro de alterações

Por favor veja o arquivo [CHANGELOG](CHANGELOG.md) para mais informações.

## Contribuição

Pull Requests não serão aceitos.

## Segurança

Se você descobrir algum problema relacionado à segurança, envie um e-mail para `contato@sepbit.com` em vez de usar o issue.

## Licença

GPL-3.0-or-later, por favor veja o arquivo [COPYING](COPYING) para mais informações.
