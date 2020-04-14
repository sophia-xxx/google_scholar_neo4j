from py2neo import Graph, Node, Relationship, TransactionError, ClientError
import sqlite3

from urllib3.exceptions import MaxRetryError


# create author node
def create_author_node(graph,conn):
    cursor = conn.execute('select * from authors ')
    authors = cursor.fetchall()
    try:
        for author in authors:
            author_node=Node("Author",id=author[0],name=author[1],affiliation=author[2])
            tx=graph.begin()
            tx.merge(author_node,primary_key='id',primary_label='Author')
            tx.commit()
    except MaxRetryError:
        print("check database connection")
    except RuntimeError:
        print("can't begin transaction")

# create interest node
def create_interest_node(graph,conn):
    cursor = conn.execute('select * from Interests')
    interests = cursor.fetchall()
    try:
        for interest in interests:
            interest_name=interest[1]
            # deal with Null value
            if interest_name is not None:
                interest_node=Node("Interest",author_id=interest[0],interest=interest_name)
                tx = graph.begin()
                tx.merge(interest_node,primary_label='Interest',primary_key='interest')
                tx.commit()
    except MaxRetryError:
        print("check database connection")
    except RuntimeError:
        print("can't begin transaction")

# create article node
def create_article_node(graph,conn):
    cursor = conn.execute('select * from Articles ')
    articles = cursor.fetchall()
    try:
        for article in articles:
            article_node=Node("Article",id=article[0],author_name=article[1],author_affiliation=article[2],
                              pub_title=article[3],pub_url=article[5])
            tx=graph.begin()
            tx.merge(article_node,primary_key='id',primary_label='Article')
            tx.commit()
    except MaxRetryError:
        print("check database connection")
    except RuntimeError:
        print("can't begin transaction")

# create topic node
def create_topic_node(graph,conn):
    cursor = conn.execute('select * from Topics')
    topics = cursor.fetchall()
    try:
        for topic in topics:
            topic_name=topic[1]
            # deal with Null value
            if topic_name is not None:
                topic_node=Node("Topic",article_id=topic[0],topic=topic_name)
                tx = graph.begin()
                tx.merge(topic_node,primary_label='Topic',primary_key='topic')
                tx.commit()
    except MaxRetryError:
        print("check database connection")
    except RuntimeError:
        print("can't begin transaction")

def create_relations(graph):
    # create relations by foreign key
    try:
        graph.run('Match (a:Author),(i:Interest) where a.id=i.author_id merge (a)-[:InterestedIn]->(i)')
        graph.run('Match (a:Article),(t:Topic) where a.id=t.article_id merge (a)-[:About]->(t)')
    except MaxRetryError:
        print("check database connection")
    except AssertionError:
        print("can't begin transaction")



def main():
    # connect with neo4j-- change password
    graph = Graph('http://localhost:7474', username='neo4j', password='1234')
    # connect with sqlite
    conn = sqlite3.connect('custom-google-scholar.db')
    create_article_node(graph,conn)
    create_author_node(graph,conn)
    create_interest_node(graph,conn)
    create_topic_node(graph,conn)
    create_relations(graph)
    print("migration done")
main()
