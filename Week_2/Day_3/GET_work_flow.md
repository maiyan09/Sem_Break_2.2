# GET Request Workflow

1. Import `requests`

   ```python
   import requests
   ```

2. Define the API URL

   ```python
   url = "https://api.example.com/data"
   ```

3. Send a GET request

   ```python
   response = requests.get(url)
   ```

4. Check for HTTP errors

   ```python
   response.raise_for_status()
   ```

   * Raises an exception for 4xx and 5xx status codes.

5. Convert the response to Python data

   ```python
   data = response.json()
   ```

6. Access the required data

   ```python
   print(data)
   ```

### Short Version

```text
Import requests
↓
Define URL
↓
requests.get(url)
↓
response.raise_for_status()
↓
response.json()
↓
Use / Print data
```
