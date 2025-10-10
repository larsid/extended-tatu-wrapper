# extended-tatu-wrapper

O protocolo **TATU (The Accessible Thing Universe)** tem como objetivo controlar as requisições e respostas em um ambiente da Internet das Coisas (Internet of Things, IoT). Este repositório oferece implementação de wrappers para construir ou tratar mensagens baseadas no protocolo TATU em diferentes sistemas, serviços e ou dispositivos da IoT. Um wrapper é um módulo que permite criar mensagens ou interpretar respostas recebidas, encapsulando primitivas ou comandos (FLOW, GET, CONNECT, etc.) sobre diferentes subsistemas de comunicação (Websockets, MQTT, etc.). A proposta do repositório é reunir wrappers do protocolo TATU que incrementam novas primitivas em diferentes linguagens, oferecendo uma base de teste para integração de dispositivos e serviços voltados a IoT.

## Objetivos do projeto

- Fornecer um ponto para estudo e evolução do protoclo TATU em diferentes linguagens.
- Fornecer uma base para a experimentação de novas funcionalidades que facilitem o teste do protocolo.
- Padronizar práticas de versionamento, empacotamento e publicação para cada implementação.
- Facilitar contribuições, destacando onde e como cada implementação é utilizada.

## Estrutura do repositório

- `java-version/`: implementação Java baseada em Maven do wrapper.
- `python-version/`: espaço reservado para a implementação Python do wrapper.
O repositório está organizado por linguagem. Cada implementação mantém seu próprio histórico, ferramentas e dependências.

| Diretório | Linguagem | Descrição |
|-----------|-----------|-----------|
| [`java-version/`](java-version/) | [README da versão Java](java-version/README.md) | Wrapper escrito em Java com build via Maven, exemplos de uso e documentação específica. |
| [`python-version/`](python-version/) | [README da versão Python](python-version/README.md) | Wrapper escrito em Python, incluindo scripts de execução e instruções de ambiente virtual. |

> **Dica:** consulte o `README` existente dentro de cada diretório para detalhes de configuração, dependências e fluxos de execução próprios da linguagem.

## Como utilizar

## Estratégia de versionamento
1. **Escolha a linguagem desejada:** navegue até o diretório correspondente (`java-version/` ou `python-version/`).
2. **Leia a documentação local:** cada implementação possui instruções passo a passo para instalação de dependências, execução de exemplos e execução de testes.
3. **Execute o wrapper:** siga os comandos indicados no README específico da linguagem para iniciar o wrapper, conectar-se ao broker ou interagir com os dispositivos TATU.
4. **Contribua:** abra issues ou pull requests indicando a linguagem impactada. Mantenha as implementações independentes e sincronize funcionalidades quando fizer sentido para o ecossistema como um todo.

## Versionamento

Utilizamos tags específicas por tecnologia para identificar lançamentos independentes:

- `vMAJOR.MINOR.PATCH-java` identifica uma release da versão Java.
- `vMAJOR.MINOR.PATCH-python` identifica uma release da versão Python.

Os históricos de cada implementação evoluem de forma independente, permitindo que correções ou features sejam entregues sem interferir na outra linguagem. Quando necessário publicar atualizações simultâneas, crie as duas tags correspondentes no mesmo commit.
Os históricos de cada implementação evoluem de forma independente, permitindo que correções ou funcionalidades sejam entregues sem interferir na outra linguagem. Quando necessário publicar atualizações simultâneas, crie as duas tags correspondentes no mesmo commit.

## Recursos adicionais

- Consulte a documentação oficial do protocolo TATU para entender o fluxo de mensagens, autenticação e requisitos de interoperabilidade a partir dos seguintes repositórios:
  
| Author | Linguagem | Descrição |
|-----------|-----------|-----------|
| [`WiserUFBA`] | [Java](https://github.com/WiserUFBA/TATU) | Protocolo TATU oficial na versão Java, desenvolvido pelo grupo de pesquisa Wiser da UFBA. |
| [`WiserUFBA`] | [Python](https://github.com/WiserUFBA/soft-iot-tatu-python) | Protocolo TATU na versão Python, atualmente em desenvolvimento. |

- Utilize os exemplos existentes em cada implementação para acelerar a criação de protótipos e integrações com seu ambiente.
