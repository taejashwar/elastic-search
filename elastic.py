from ast import main
from pydoc import doc
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host':'localhost','port':'9200'}])

data = {
        "Name":"Graeme Smith",
        "Age": "42",
        "Country":"South Africa",
        "Profession":"Cricketer",
        "Role":"Batsman",
        "Status":"Retired"
    }

# Creating an index
def create_index(_index):
    es.indices.create(index=_index,ignore=400)

def insert_data(_index,_doctype,_id,_data):
    res = es.index(index=_index, doc_type=_doctype,id=_id,body=_data)
    print(res)
  
# Reading the index
def search_index(_index):
    query = {
        "query":{
            "match_all":{}
        }
    }
    res = es.search(index=_index,body=query)
    print(res)

# Updating the index
def update_index(_index,_doctype,_id,_update_data):
    res = es.update(index=_index,doc_type=_doctype,id=_id,body=_update_data)
    print(res)

# Deleting the index
def delete_index(_index):
    es.indices.delete(index=_index,ignore=400)

if __name__ == "__main__":
    id = 1
    index = "sports"
    doctype = "cricketers"
    update_data = {
        "doc":{"Age":"55"}
    }
    create_index(index)
    insert_data(index,doctype,id,data)
    # search_index(index)
    update_index(index,doctype,id,update_data)
    search_index(index)
    delete_index(index)
    