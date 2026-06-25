# POST Request Workflow

1. Import `requests`

   ```python
   import requests
   ```

2. Define the API URL

   ```python
   url = "https://api.example.com/posts"
   ```

3. Create the data to send

   ```python
   payload = {
       "title": "My Post",
       "body": "Hello World"
   }
   ```

4. Send a POST request

   ```python
   response = requests.post(url, json=payload)
   ```

5. Check for HTTP errors

   ```python
   response.raise_for_status()
   ```

   * Raises an exception for 4xx and 5xx status codes.

6. Convert the response to Python data

   ```python
   data = response.json()
   ```

7. Use or print the response data

   ```python
   print(data)
   ```

### Short Version

```text id="u3ql1i"
Import requests
↓
Define URL
↓
Create payload (data)
↓
requests.post(url, json=payload)
↓
response.raise_for_status()
↓
response.json()
↓
Use / Print data
```
