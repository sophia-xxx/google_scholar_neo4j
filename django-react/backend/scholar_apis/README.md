**You will need python 3 installed.**

## Requirements
pip install django <br />
pip install djangorestframework <br />
pip install django-cors-headers <br />

## How to run
go to cs411/django-react/backend/scholar_apis/<br />
run `manage.py runserver` <br />
server has been started at http://127.0.0.1:8000/ <br />

## Testing:
* you can always command line to get/post/put/delete to api and get results
* for get requests, you can also go to api url in any browser to see results

## APIS - READ BEFOREHAND:
* all apis require a certain type of request -> `[GET, POST, PUT, DELETE]`
* for any request, if no result is found (but parameters are formatted correctly), these return an empty repsonse
* any time an author is returned, their `[name,affiliation]` will be returned (those are the only fields in DB)
  * mandatory author fields: `[name, affiliation]`
* any time an article is returned, `[name, affiliation, pub_title]` are guaranteed to be returned. other fields are only returned if their values are non-null
  * in other words, all other article articles fields are optional
    * optional article fields: `['pub_year', 'pub_url', 'citations', 'citedby', 'journal','pub_author']`
    * mandatory article fields: `[name, affiliation, pub_title]`
* for CREATE, UPDATE, and DELETE, the data **MUST** include mandatory field information!! otherwise you **will** get an error.
* for CREATE, UPDATE, and DELETE, the apis only returns an error if the data is incorrectly formatted. Otherwise, they attempt to change DB, and return ok.
* for CREATE, UPDATE, and DELETE you cannot specify id, it is not supported (because it makes no sense)
* for all requests: to specify a field that contains spaces, **replace all ' ' with '+'**
* **ALL APIS RETURN 400 IF DATA IS NOT FORMATTED CORRECTLY OR DOES NOT CONTAIN THE MINIMUM AMOUNT OF FIELDS**

## APIS - Read
**all these require that you GET to url**

#### Authors

`127.0.0.1:8000/api/authors/all`<br />
lists all authors (no pagination, use at your own risk) <br />

`127.0.0.1:8000/api/authors/id=<int:ID>` <br />
finds author by id (only to be used for debugging, etc.) <br />

`127.0.0.1:8000/api/authors/name=<str:name>` <br />
finds author(s) by name <br />

`127.0.0.1:8000/api/authors/name=<str:name>/affiliation=<str:affiliation>` <br />
finds author(s) by name and affiliation <br />

#### Articles
`127.0.0.1:8000/api/articles/all` <br />
lists all articles (no pagination, use at your own risk) <br />

`127.0.0.1:8000/api/articles/id=<int:ID>` <br />
finds articles by id (only to be used for debugging, etc.) <br />

`127.0.0.1:8000/api/articles/name=<str:name>` <br />
finds article(s) by name <br />

`127.0.0.1:8000/api/articles/name=<str:name>/affiliation=<str:affiliation>` <br />
finds article(s) by name and affiliation <br />

`127.0.0.1:8000/api/articles/journal=<str:journal` <br />
finds article(s) by journal <br />

#### Topics
`127.0.0.1:8000/api/topics/topic=<str:topic>` <br />
join topics and articles tables and finds all the articles in same topic  <br />

## APIS - Create
**these require that you POST to url**

#### Authors
`127.0.0.1:8000/api/authors/add` <br />
attempts to add author to DB <br />
**there is a problem in the Authors table in the DB, avoid using this API(or roll back DB changes whenever you do use it)** <br />
all author information should be in the data field, format: `name=abc+def&affiliation=UIUC` (order of fields doesn't matter) <br />

#### Articles
`127.0.0.1:8000/api/articles/add` <br /> 
attempts to add article to DB (DB will auto-assign id)
all article information should be in data field, format: `name=Jane+Doe&affiliation=UIC&pub_title=COVID-19&...`.  <br />
only mandatory fields must to be specified, optional fields can also be specified <br />


## APIS - Update
**these require that you PUT to url**

#### Authors
There is no API to update an author! You can delete and create if neccesary. <br />

#### Articles
`127.0.0.1:8000/api/articles/update` <br />
attempts to update optional fields of an article <br />
data format: `name=Jane+Doe&affiliation=UIC&pub_title=COVID-19&...` <br />
if you need to update mandatory fields, delete and create a new article


## APIS - Delete
**all of these will require that you DELETE to url**

#### Authors
`127.0.0.1:8000/api/articles/delete` <br />
attempts to delete an author <br />
data must include author mandatory fields, format (same as update/create): `name=abc&affiliation=UIUC`

#### Articles
`127.0.0.1:8000/api/articles/delete` <br />
attempts to delete an article <br />
data must include article mandatory fields, format (same as update/create): `name=Jane+Doe&affiliation=UIC&pub_title=COVID-19&...`

## Things to do/consider
* fancy SQL statements (join, etc.) <br />
* if you attempt to update/delete a document that exists, no error code returns- but maybe it should? <br />
* no interaction with interests/topics table yet (CRUD operations for those?) <br />
* create author is not able to auto-generate an id for an author due to db issues (see slack):
  * author ids should be unique, but there are two different authors with same id in DB
* update for article only allows update on *optional* author fields, is this sufficient? <br />
* no update for author, is this sufficient? <br />
* do we need pagination? <br />
* should we required all new inserted articles have their corresponding author in authors table? (i think yes)
  ** this is not currently implemented
* username/password authentication for CREATE/UPDATE/DELETE queries?

## SQLite data migrate to neo4j
* pip install py2neo <br />
* open neo4j, then set username and password <br />
* modify the conneciton username and password in migrate_data.py </br>
* in project file, run command >python3 migrate_data.py <br />
