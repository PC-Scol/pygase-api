# pygase-api

Exemple de création d'un client API Pégase en Python

## Prérequis

- IDE pour développement Python
- Python >= 3.8 installé sur la machine
- Le nom de l'environnement Pégase sur lequel vous souhaitez travailler. Dans ce document, l'environnement est `bas-esup`. Il faudra changer cette valeur pour la faire correspondre à votre environnement.

## Prise en main APIs Swagger :

- Visiter https://pegase-swagger-ui.bas-esup.pc-scol.fr
- Récupération token via curl : 

```bash
curl -d "username=svc-api&password=???&token=true" \
-H "Content-Type: application/x-www-form-urlencoded" \
-X POST https://authn-app.bas-esup.pc-scol.fr/cas/v1/tickets
```

- Appel du endpoint "lecture d'un établissement par code pegase"
- (Optionnel) Appel du endpoint "création d'un nouvel établissement"
- (Optionnel) Exploration des autres APIs

## Prise en main de l'outil de génération de code OpenApiGenerator :

- Explorer [la page Github de l'outil](https://github.com/OpenAPITools/openapi-generator/blob/master/README.md)
- Identifier [la dernière version publiée de l'outil](https://github.com/OpenAPITools/openapi-generator/blob/master/README.md#11---compatibility) et modifier la version utilisée dans le document si besoin.
- Télécharger :

```bash
wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/5.3.0/openapi-generator-cli-5.3.0.jar -O openapi-generator-cli.jar
```

- Créer un alias pour faciliter l'appel de la commande : 
```bash
alias open-api-generator="java -jar $PWD/openapi-generator-cli.jar"
```

- Explorer l'outil : 
    - `open-api-generator --help`
    - `open-api-generator help generate`
    - `open-api-generator list` − [voir la documentation des générateurs disponibles](https://github.com/OpenAPITools/openapi-generator/blob/v5.3.0/docs/generators)
    - `open-api-generator config-help -g python` − [voir la documentation des paramètres spécifiques à Python](https://github.com/OpenAPITools/openapi-generator/blob/v5.3.0/docs/generators/python.md)

- Créer un alias pour faciliter la génération de clients Python

```bash
alias python-client-generator="open-api-generator generate -g python -c python-gen-config.json"
```

- Générer un client Python pour REF :

Vérifier au préalable de récupérer la dernière version de fichier open-api en consultant [pegase-swagger-ui](https://pegase-swagger-ui.bas-esup.pc-scol.fr/)

```bash
python-client-generator -i https://pegase-swagger-ui.bas-esup.pc-scol.fr/fr.pcscol/ref-api/ref-api-2.2.0.yml -o generated/ref --package-name ref-client
```

- Générer un client Python pour MOF :

Vérifier au préalable de récupérer la dernière version de fichier open-api en consultant [pegase-swagger-ui](https://pegase-swagger-ui.bas-esup.pc-scol.fr/)

```bash
python-client-generator -i https://pegase-swagger-ui.bas-esup.pc-scol.fr/fr.pcscol.mof-api/mof-application-api-v1/mof-application-api-v1-2.2.0.yml -c python-gen-config.json -o generated/mof --package-name mof-client --skip-validate-spec
```

## Installer les clients et les dépendances pour l'exercice

```
> python3 -m venv .env
> source .env/bin/activate
> pip install -r requirements.txt
```

## Configuration

Dans le fichier  `conf.ini` à la racine du dépôt, ajuster les variables :

- `username` avec le nom du compte applicatif que vous souatez utiliser
- `password` avec le mot de passe correspondant au compte applicatif mentionné ci-dessus
- `name` avec le nom de votre environnement

Si nécessaire, ajuster les valeurs pour `domain` et `scheme`.

## Utilisation

```bash
> source .env/bin/activate
> ./pegase --help
Usage: pegase [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  extractions
  structure

> ./pegase structure --help
Usage: pegase structure [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  lire
  liste

> ./pegase structure liste
```