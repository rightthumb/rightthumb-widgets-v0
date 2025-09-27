# fetch_advanced, Usage examples

___

## **1. Basic GET (default Win11 Chrome agent)**

~~~python
from my_http_lib import fetch_advanced

text = fetch_advanced("https://example.com")
print(text)
~~~

___

## **2. Basic POST with form data (`application/x-www-form-urlencoded`)**

~~~python
form_data = {"username": "scott", "password": "secret123"}

result = fetch_advanced(
    "https://httpbin.org/post",
    data=form_data,
    return_type="json"
)
print(result)
~~~

___

## **3. Basic POST with JSON body (`application/json`)**

~~~python
json_data = {"name": "Scott", "project": "AI"}

result = fetch_advanced(
    "https://httpbin.org/post",
    json=json_data,
    return_type="json"
)
print(result)
~~~

___

## **4. Passing query parameters (`params`)**

~~~python
result = fetch_advanced(
    "https://httpbin.org/get",
    params={"page": 2, "filter": "active"},
    return_type="json"
)
print(result)
~~~

___

## **5. Forcing GET or POST manually**

~~~python
# Force GET even if you pass `data`
result = fetch_advanced(
    "https://httpbin.org/get",
    data={"ignored": "because GET"},
    method="GET"
)
print(result)
~~~

___

## **6. Using a different agent profile**

~~~python
result = fetch_advanced(
    "https://example.com",
    agent="android_chrome"
)
print(result)
~~~

___

## **7. Adding an API key in the header**

~~~python
result = fetch_advanced(
    "https://api.example.com/data",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    return_type="json"
)
print(result)
~~~

___

## **8. Adding an API key as a query parameter**

~~~python
result = fetch_advanced(
    "https://api.example.com/data",
    params={"api_key": "YOUR_API_KEY"},
    return_type="json"
)
print(result)
~~~

___

## **9. Using cookies**

~~~python
result = fetch_advanced(
    "https://httpbin.org/cookies",
    cookies={"session_id": "abc123"},
    return_type="json"
)
print(result)
~~~

___

## **10. Using a proxy**

~~~python
result = fetch_advanced(
    "https://httpbin.org/ip",
    proxies={"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"},
    return_type="json"
)
print(result)
~~~

___

## **11. Disabling SSL verification**

~~~python
result = fetch_advanced(
    "https://self-signed.badssl.com/",
    verify=False
)
print(result)
~~~

___

## **12. Forcing text output without HTML parsing**

~~~python
html_raw = fetch_advanced(
    "https://example.com",
    text_mode="plain",
    return_type="text"
)
print(html_raw)
~~~

___

## **13. Forcing BeautifulSoup HTML parsing**

~~~python
html_clean = fetch_advanced(
    "https://example.com",
    text_mode="html",
    return_type="text"
)
print(html_clean)
~~~

___

## **14. Forcing bytes output (e.g., file download)**

~~~python
image_bytes = fetch_advanced(
    "https://httpbin.org/image/png",
    return_type="bytes"
)
with open("test.png", "wb") as f:
    f.write(image_bytes)
~~~

___

## **15. Retrying on transient errors with backoff**

~~~python
result = fetch_advanced(
    "https://httpbin.org/status/503",
    retries=3,
    backoff=1.0,
    return_type="text"
)
print(result)
~~~

___

## **16. Overriding encoding**

~~~python
result = fetch_advanced(
    "https://example.com",
    encoding="utf-8"
)
print(result)
~~~

___

## **17. Custom retry-on status codes**

~~~python
result = fetch_advanced(
    "https://httpbin.org/status/418",
    retries=2,
    retry_on=(418,),  # Retry on "I'm a teapot" just for fun
    return_type="text"
)
print(result)
~~~

___

## **18a. POST multipart form-data (file upload)**

~~~python
files = {"file": open("myfile.txt", "rb")}

result = fetch_advanced(
    "https://httpbin.org/post",
    data={"description": "Test file"},
    files=files,                        # <___ actually pass files
    headers={"Content-Type": None},     # Let requests auto-set multipart boundary
    method="POST",
    return_type="json"
)

print(result)

# Always close files when done
files["file"].close()

~~~

___

## **18b. POST multipart form-data (multiple file upload)**

~~~python
files = [
    ("file1", ("first.txt", open("first.txt", "rb"), "text/plain")),
    ("file2", ("second.jpg", open("second.jpg", "rb"), "image/jpeg")),
]

result = fetch_advanced(
    "https://httpbin.org/post",
    data={"description": "Two files uploaded"},
    files=files,
    method="POST",
    return_type="json",
)

print(result)

# Close all file handles (no underscores)
for field_name, file_tuple in files:
    file_name, file_obj, mime_type = file_tuple
    file_obj.close()

~~~

___

## **19. Adding API key to both headers and params**

~~~python
result = fetch_advanced(
    "https://api.example.com/data",
    params={"api_key": "param_key"},
    headers={"X-API-Key": "header_key"},
    return_type="json"
)
print(result)
~~~

___

## **20. Using a completely custom agent profile**

~~~python
custom_profiles = {
    "custom_agent": {
        "User-Agent": "MyCustomAgent/1.0",
        "Accept": "*/*"
    }
}

result = fetch_advanced(
    "https://example.com",
    agent="custom_agent",
    profiles=custom_profiles
)
print(result)
~~~
