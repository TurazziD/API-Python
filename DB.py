import psycopg2

class DB():

    def executarInsert(self, query):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="asd123$%",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Teste")
            cursor = connection.cursor()

            cursor.execute(query)
            connection.commit()
            print("Query executada com sucesso ")
        except (Exception, psycopg2.DatabaseError) as error:
            print ("Ocorreu um erro na Query", error)

    def executarSelect(self, query):
        try:
            print (query)
            connection = psycopg2.connect(user="postgres",
                                          password="asd123$%",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="Teste")
            cursor = connection.cursor()

            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print ("Ocorreu um erro na Query", error)
