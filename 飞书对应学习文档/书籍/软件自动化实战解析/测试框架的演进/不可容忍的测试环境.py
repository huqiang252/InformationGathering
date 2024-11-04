import requests
import time
import logging


class QaRestClient:
    MAX_RETRIES = 3
    RETRY_INTERVAL_SECONDS = 5

    retry_status_codes = {
        408: "Request Timeout",
        429: "Too Many Requests",
        509: "Bandwidth Limit Exceeded",
        598: "Network read timeout error",
        599: "Network connection timeout error"
    }

    @classmethod
    def request(cls, method, url, max_retries=None, **kwargs):
        if max_retries is None:
            max_retries = cls.MAX_RETRIES

        for attempt in range( max_retries ):
            response = requests.request( method, url, **kwargs )
            if response.status_code not in cls.retry_status_codes:
                return response

            logging.warning( f"Request failed with status {response.status_code}: "
                             f"{cls.retry_status_codes.get( response.status_code, '' )}. "
                             f"Retrying {attempt + 1}/{max_retries}..." )
            time.sleep( cls.RETRY_INTERVAL_SECONDS )

        return response

    @classmethod
    def get(cls, url, **kwargs):
        return cls.request( 'GET', url, **kwargs )

    @classmethod
    def post(cls, url, **kwargs):
        return cls.request( 'POST', url, **kwargs )

    @classmethod
    def put(cls, url, **kwargs):
        return cls.request( 'PUT', url, **kwargs )

    @classmethod
    def delete(cls, url, **kwargs):
        return cls.request( 'DELETE', url, **kwargs )

    @classmethod
    def patch(cls, url, **kwargs):
        return cls.request( 'PATCH', url, **kwargs )


# Example usage:
if __name__ == "__main__":
    logging.basicConfig( level=logging.INFO )
    client = QaRestClient()

    response = client.get( 'https://jsonplaceholder.typicode.com/posts/dsf' )
    print( response.json() )

    response = client.post( 'https://jsonplaceholder.typicode.com/posts',
                            json={"title": "foo", "body": "bar", "userId": 1} )
    print( response.json() )

    response = client.put( 'https://jsonplaceholder.typicode.com/posts/1',
                           json={"id": 1, "title": "foo", "body": "bar", "userId": 1} )
    print( response.json() )

    response = client.delete( 'https://jsonplaceholder.typicode.com/posts/1' )
    print( response.status_code )

    response = client.patch( 'https://jsonplaceholder.typicode.com/posts/1',
                             json={"title": "foobar"} )
    print( response.json() )