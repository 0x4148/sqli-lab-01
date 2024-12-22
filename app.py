from flask import Flask, request
import pymysql
from pygments import highlight
from pygments.lexers import SqlLexer
from pygments.formatters import HtmlFormatter

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host='mysql',
        user='cyard_01',
        password='cyardP@ss',
        database='dummy_org',
        cursorclass=pymysql.cursors.DictCursor
    )

def book_db_connection():
    return pymysql.connect(
        host='mysql',
        user='cyard_01',
        password='cyardP@ss',
        database='BooksLibrary',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/playground')
def get_news():
    news_id = request.args.get('news_id')
    query_format = request.args.get('query_format')
    if not query_format:
        query_format = 1
    
    if not news_id:
        return "<h1>news_id parameter is required, try /playground?news_id=1&query_format=1</h1>", 400

    connection = get_db_connection()
    if query_format == '1':
        query = f"SELECT title, details, date FROM news WHERE id = {news_id}"
    elif query_format == '2':
        query = f"SELECT title, details, date FROM news WHERE id = '{news_id}'"
    elif query_format == '3':
        query = f'SELECT title, details, date FROM news WHERE id = "{news_id}"'
    elif query_format == '4':
        query = f"SELECT title, details, date FROM news WHERE id = ({news_id})"
    elif query_format == '5':
        query = f"SELECT title, details, date FROM news WHERE id = ('{news_id}')"
    elif query_format == '6':
        query = f'SELECT title, details, date FROM news WHERE id = ("{news_id}")'
    else:
        return "<h1>Invalid query_format, try any value from 1 to 6</h1>", 400
    formatter = HtmlFormatter(style='colorful')
    highlighted_query = highlight(query, SqlLexer(), formatter)
    style = f"<style>{formatter.get_style_defs()}</style>"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
    except pymysql.MySQLError as e:
        connection.close()
        error_message = f"<!-- {query} -->"  # Plain text query as HTML comment
        error_message += f"<h1>SQL Error</h1><p>{e}</p><br><br>{style}<div>{highlighted_query}</div>"
        return error_message, 500
    connection.close()
    if result:
        response = f"<!-- {query} -->"  # Plain text query as HTML comment
        response += f"<h1>Title : {result['title']}</h1><p>Details : {result['details']}</p><p>Date : {result['date']}</p>"
        response += f"<br><br>{style}<div>{highlighted_query}</div>"
        return response
    else:
        response = f"<!-- {query} -->"  # Plain text query as HTML comment
        response += f"<h1>News not found</h1><br><br>{style}<div>{highlighted_query}</div>"
        return response, 404


@app.route('/books')
def get_books():
    '''CREATE TABLE Books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    year INT,
    sales INT
    );
    INSERT INTO Books (title, author, year, sales) VALUES ('The Amazing Journey', 'John Smith', 2005, 1200);
    '''
    connection = book_db_connection()
    results_count = request.args.get('results_count')
    if not results_count:
        results_count = 1
    author_name = request.args.get('author_name')
    if not author_name:
        return "<h1>book_id parameter is required, try /books?author_name=John Smith</h1>", 400
    query = f"SELECT title, author, year, sales FROM Books WHERE author = '{author_name}'"
    formatter = HtmlFormatter(style='colorful')
    #check if show_query variable is present in the request
    highlighted_query = 'Use show_query=1 to see the query'
    try:
        show_query = request.args.get('show_query')
        if show_query == '1':
            highlighted_query = highlight(query, SqlLexer(), formatter)
    except:
        pass
    style = f"<style>{formatter.get_style_defs()}</style>"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
    except pymysql.MySQLError as e:
        connection.close()
        error_message = f"<!-- {query} -->"
        error_message += f"<h1>SQL Error</h1><p>{e}</p><br><br>{style}<div>{highlighted_query}</div>"
        return error_message, 500
    connection.close()
    if result:
        response = f"<!-- {query} -->"
        response += f"<h1>Title : {result['title']}</h1><p>Author : {result['author']}</p><p>Year : {result['year']}</p><p>Sales : {result['sales']}</p>"
        response += f"<br><br>{style}<div>{highlighted_query}</div>"
        return response
    else:
        response = f"<!-- {query} -->"
        response += f"<h1>Book not found</h1><br><br>{style}<div>{highlighted_query}</div>"
        return response, 404


@app.route('/books_no_errors')
def get_books_no_errors():
    '''CREATE TABLE Books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    year INT,
    sales INT
    );
    INSERT INTO Books (title, author, year, sales) VALUES ('The Amazing Journey', 'John Smith', 2005, 1200);
    '''
    connection = book_db_connection()
    results_count = request.args.get('results_count')
    if not results_count:
        results_count = 1
    author_name = request.args.get('author_name')
    if not author_name:
        return "<h1>book_id parameter is required, try /books?author_name=John Smith</h1>", 400
    query = f"SELECT title, author, year, sales FROM Books WHERE author = '{author_name}'"
    formatter = HtmlFormatter(style='colorful')
    highlighted_query = 'Use show_query=1 to see the query'
    try:
        show_query = request.args.get('show_query')
        if show_query == '1':
            highlighted_query = highlight(query, SqlLexer(), formatter)
    except:
        pass
    style = f"<style>{formatter.get_style_defs()}</style>"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
    except pymysql.MySQLError as e:
        connection.close()
        response = f"<!-- {query} -->"
        response += f"<h1>Book not found</h1><br><br>{style}<div>{highlighted_query}</div>"
        return response, 404
    
    connection.close()
    if result:
        response = f"<!-- {query} -->"
        response += f"<h1>Title : {result['title']}</h1><p>Author : {result['author']}</p><p>Year : {result['year']}</p><p>Sales : {result['sales']}</p>"
        response += f"<br><br>{style}<div>{highlighted_query}</div>"
        return response
    else:
        response = f"<!-- {query} -->"
        response += f"<h1>Book not found</h1><br><br>{style}<div>{highlighted_query}</div>"
        return response, 404
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8070)
