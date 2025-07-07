# Run command

**Description**: Run command

## Endpoint

- **URL:** `api/open/cli`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **cmd** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 204,
    "response_headers": {
      "Server": "nginx/1.23.3",
      "Date": "Fri, 30 Dec 2022 21:53:39 GMT",
      "Connection": "keep-alive",
      "Cache-Control": "no-cache",
      "Set-Cookie": "XSRF-TOKEN-a2f51e93-1b6e-42fc-ae3e-55663a662c99=HIEHdNYa3JeXj%2FTKSH9glAnh7f6ZiWbB3rF8abllKfHuDc7Ka8hPtFWcBPaLOTG%2BeILn8BCUuOmQUJ5gfg7XvQ%3D%3D; path=/; secure; SameSite=None, _n2os-webconsole_session-985532b601d345865256f4fa4c80c7df2413f44aaf69643b0782f32776518980=40a6199934ff1bfd18b17f54b6ce2927; path=/; HttpOnly; secure; SameSite=None",
      "X-Request-Id": "92e0d3a3-a2d8-4362-b2e2-821fb45203d5",
      "Content-Security-Policy": "default-src 'none'; block-all-mixed-content; connect-src 'self'; font-src 'self'; form-action 'self'; img-src 'self' data:; script-src 'self' 'unsafe-eval' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; upgrade-insecure-requests",
      "Strict-Transport-Security": "max-age=63072000; includeSubdomains;",
      "X-Frame-Options": "DENY",
      "X-Content-Type-Options": "nosniff",
      "X-XSS-Protection": "0",
      "Cross-Origin-Embedder-Policy": "require-corp",
      "Cross-Origin-Resource-Policy": "same-origin",
      "X-Download-Options": "noopen",
      "X-Permitted-Cross-Domain-Policies": "none",
      "Referrer-Policy": "origin-when-cross-origin, strict-origin-when-cross-origin",
      "Feature-Policy": "geolocation none;midi none;notifications none;push none;microphone none;camera none;magnetometer none;gyroscope none;speaker self;vibrate none;fullscreen self;payment none;"
    },
    "reason": "No Content",
    "response_text": ""
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **response_text** (string)
## Response Headers

| Header | Type |
|--------|------|
| Server | string |
| Date | string |
| Connection | string |
| Cache-Control | string |
| Set-Cookie | string |
| X-Request-Id | string |
| Content-Security-Policy | string |
| Strict-Transport-Security | string |
| X-Frame-Options | string |
| X-Content-Type-Options | string |
| X-XSS-Protection | string |
| Cross-Origin-Embedder-Policy | string |
| Cross-Origin-Resource-Policy | string |
| X-Download-Options | string |
| X-Permitted-Cross-Domain-Policies | string |
| Referrer-Policy | string |
| Feature-Policy | string |