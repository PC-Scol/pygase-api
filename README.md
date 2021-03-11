## Prérequis

- IDE pour développement Python
- Python >= 3.8 installé sur la machine

## Prise en main APIs Swagger :

- Visiter https://ref.rdd.pc-scol.fr/swagger-ui.html
- Récupération token via curl : `curl -d "username=svc-api&password=???&token=true" -H "Content-Type: application/x-www-form-urlencoded" -X POST https://authn-app.rdd.pc-scol.fr/cas/v1/tickets`
- Appel du endpoint "lecture d'un établissement par code pegase"
- (Optionnel) Appel du endpoint "création d'un nouvel établissement"
- (Optionnel) Exploration des autres APIs

## Prise en main de l'outil de génération de code OpenApiGenerator :

- Visiter https://github.com/OpenAPITools/openapi-generator/blob/master/README.md
- Télécharger : `wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/5.0.0/openapi-generator-cli-5.0.0.jar -O openapi-generator-cli.jar`
- Créer alias : `alias open-api-generator="java -jar $PWD/openapi-generator-cli.jar"`
- Explorer l'outil : 
    - `open-api-generator --help`
    - `open-api-generator help generate`
    - `open-api-generator list` (https://github.com/OpenAPITools/openapi-generator/blob/v5.0.0/docs/generators)
    - `open-api-generator config-help -g python` (https://github.com/OpenAPITools/openapi-generator/blob/v5.0.0/docs/generators/python.md)
- Générer un client Python : `open-api-generator generate -g python -i ./apis/ref-api-1.3.0.yml -c python-gen-config.json -o generated`

## Installer le client et les dépendances pour l'exercice

```
> python3 -m venv .env
> source .env/bin/activate
> pip install -r requirements.txt
```

## Utilisation

Dans le fichier `api.py`, renseigner le nom de votre environnement au niveau de la variable globale `ENV`, idéalement `bas-$etab.pc-scol.fr`. Tests possibles en éxécutant le fichier `api.py` ou en utilisant la CLI `structure` une fois l'identifiant et mot de passe du compte de service saisi dans les deux fichiers pour créer le client.

```
> source .env/bin/activate
> ./structure --help
