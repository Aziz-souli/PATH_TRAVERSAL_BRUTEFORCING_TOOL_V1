
from urllib.parse import urlencode, urlparse, parse_qs, urlunparse
def get_domain(url):
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{parsed_url.netloc}"

def SET_QUERY( new_filename ,url = "/images/image?filename=38.jpg"):  
    # Parse the URL
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    # Update the filename query parameter
    query_params['filename'] = [new_filename]

    # Reconstruct the URL
    updated_query = urlencode(query_params, doseq=True)
    updated_url = urlunparse(parsed_url._replace(query=updated_query))
    return updated_url
    
