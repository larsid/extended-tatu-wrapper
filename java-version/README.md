# Wrapper TATU em Java

Este módulo oferece utilitários para construir mensagens e tópicos do protocolo **TATU** utilizando Java.
Ele foi pensado para quem já integra dispositivos ao ecossistema TATU e precisa gerar comandos
(`FLOW`, `GET`, `CONNECT`, etc.) ou interpretar respostas recebidas do broker.

## Pré-requisitos

- **Java 8** ou superior instalado (`java -version`).
- **Apache Maven 3.6+** para gerenciar dependências e empacotar o projeto.

## Estrutura do projeto

```
java-version/
├── pom.xml                     # Configuração Maven, gera JAR com dependências
└── src/main/java/extended/tatu/
    ├── wrapper/model/          # Entidades de domínio (Device, Sensor, TATUMessage)
    ├── wrapper/util/           # Builders utilitários (ExtendedTATUWrapper, TATUWrapper, DeviceWrapper, SensorWrapper)
    └── wrapper/enums/          # Enumerações de suporte (por exemplo, ExtendedTATUMethods)
```

Os utilitários principais se concentram em `ExtendedTATUWrapper` e `TATUWrapper`, que criam
payloads JSON prontos para publicar no broker.

## Instalação e build

1. Navegue até este diretório:
   ```bash
   cd java-version
   ```
2. Baixe as dependências e gere o artefato empacotado:
   ```bash
   mvn clean package
   ```
   O Maven produzirá `target/extended-tatu-wrapper-1.0-SNAPSHOT-jar-with-dependencies.jar`,
   que pode ser referenciado em outro projeto ou publicado em um repositório interno.
3. (Opcional) Instale o artefato no repositório local do Maven para reutilizá-lo em outros
   projetos Java:
   ```bash
   mvn clean install
   ```

> Não há testes automatizados neste módulo; `mvn test` executa rapidamente porque não existem
> classes de teste configuradas.

## Uso básico

Após empacotar o projeto, adicione o JAR gerado ao classpath da sua aplicação ou declare o módulo
como dependência (caso tenha feito `mvn install`). A seguir um exemplo de criação de dispositivo,
sensor e mensagens TATU:

```java
import extended.tatu.wrapper.model.Device;
import extended.tatu.wrapper.model.Sensor;
import extended.tatu.wrapper.util.ExtendedTATUWrapper;
import extended.tatu.wrapper.util.TATUWrapper;

import java.util.Arrays;

public class Sample {
    public static void main(String[] args) {
        Sensor temperature = new Sensor("temperatureSensor", "temperature", 5, 5);
        Device device = new Device(
            "device-01",
            -12.973,
            -38.512,
            Arrays.asList(temperature)
        );

        String connectMessage = ExtendedTATUWrapper.buildConnectMessage(device, "192.168.0.10", 30.0);
        String flowCommand = TATUWrapper.buildTATUFlowInfoMessage(temperature.getId(), 5, 5);

        System.out.println(connectMessage);
        System.out.println(flowCommand);
    }
}
```

Outras operações disponibilizadas:

- `ExtendedTATUWrapper.getConnectionTopic()` / `getConnectionTopicResponse()` para nomes de tópicos padrão.
- `TATUWrapper.buildGetMessageResponse(...)` e `buildFlowMessageResponse(...)` para formatar respostas de broker.
- `DeviceWrapper` e `SensorWrapper` para converter objetos Java em JSON e vice-versa.

## Próximos passos sugeridos

- Adicionar testes unitários cobrindo os builders de mensagens.
- Implementar exemplos de integração com um broker MQTT para demonstrar o uso do wrapper em produção.
- Sempre atualizar a documentação quando introduzir novos métodos ou alterar a estrutura dos modelos.
