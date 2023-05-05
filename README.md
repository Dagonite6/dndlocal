# dndlocal

## Auth endpoints:
```
localhost/auth/register/
localhost/auth/login
localhost/auth/logout
```

<br>

## Character endpoints:
Create character (POST Request):
```
localhost/character/create
```
List of characters (GET request):
```
localhost/character/
```
Details of a character (GET request):
```
localhost/character/<ID>
```
Update character (PUT/PATCH requests):
```
localhost/character/<ID>
```
Delete character (DELETE request):
```
localhost/character<ID>
``` 

## ElasticSearch indexes:
```
/equipment/<NUMERIC_ID>
/spells/<NUMERIC_ID>
```


**TODO:** <br>
1. ~~Connect Postgres.~~
2. ~~Declare character model in the database.~~
2. ~~Make User serializers.~~
3. ~~Setup DRF for user cretation and auth.~~
3. ~~Make Character serializers.~~
4. ~~Setup DRF for character creation, list, update, delete.~~
4. ~~Install Elasticsearch.~~
4. ~~Procces spells into our JSON format.~~
5. ~~Map spells.~~
5. ~~Index spells.~~
6. ~~Parse Class tags for Spells.~~
7. ~~Apply class tags to spells index.~~
4. ~~Procces equipment into JSON.~~
5. ~~Map equipment.~~
4. ~~Index equipment.~~
6. Map Class abilities.
7. Map Race abilities.
5. Procces class and race abilities into JSON.
5. Index class and race abilities.
5. Setup React.
5. Connect React with DRF.
5. React authentication.

# elastic 
