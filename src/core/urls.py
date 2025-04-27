__protocol = "http"
__host = "localhost"
__port = "8000"

def make_url(endpoint: str):
    url = f"{__protocol}://{__host}:{__port}{endpoint}" if __port \
        else f"{__protocol}://{__host}{endpoint}"
    return url
