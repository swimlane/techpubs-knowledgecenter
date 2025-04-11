# Get Attachment

**Description**: Retrieves a specific attachment from a ServiceNow table using the provided unique sys_id.

## Endpoint

- **URL:** `api/now/attachment/{{sys_id}}/file`
- **Method:** `GET`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| path_parameters | object |  | Yes |
## Output

### Example

```json
[
    {
        "status_code": 200,
        "response_headers": {
            "Server-Timing": "sem_wait;dur=0, sesh_wait;dur=0",
            "Content-Encoding": "gzip",
            "X-Is-Logged-In": "true",
            "X-Transaction-ID": "1dd293709703",
            "Content-Disposition": "attachment;filename=\"test\";filename*=UTF-8''test",
            "X-Content-Type-Options": "nosniff",
            "x-attachment-metadata": "{  \"size_bytes\" : \"5881\",  \"file_name\" : \"test\",  \"sys_mod_count\" : \"1\",  \"average_image_color\" : \"\",  \"image_width\" : \"\",  \"sys_updated_on\" : \"2022-11-05 00:53:44\",  \"sys_tags\" : \"\",  \"table_name\" : \"incident\",  \"sys_id\" : \"41f9dad09783111084d57e121153af94\",  \"image_height\" : \"\",  \"sys_updated_by\" : \"system\",  \"content_type\" : \"application/json\",  \"sys_created_on\" : \"2022-11-05 00:53:43\",  \"size_compressed\" : \"4343\",  \"compressed\" : \"true\",  \"state\" : \"available\",  \"table_sys_id\" : \"1c741bd70b2322007518478d83673af3\",  \"chunk_size_bytes\" : \"700000\",  \"hash\" : \"8671fa6613cd1c6e82c0e1d6b940ae0771d1d8b3f56019f8274ed501407ffc2a\",  \"sys_created_by\" : \"admin\"}",
            "x-edge-enc-proxy-static": "true",
            "Content-Type": "application/json;charset=UTF-8",
            "Transfer-Encoding": "chunked",
            "Date": "Sun, 06 Nov 2022 18:19:10 GMT",
            "Keep-Alive": "timeout=20",
            "Connection": "keep-alive",
            "Server": "ServiceNow",
            "Set-Cookie": "glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_session=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_route=glide.f6d1c4085a807931391acf9b7192b09e; Max-Age=2147483647; Expires=Fri, 24-Nov-2090 21:33:17 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_session_store=91D21B709703111084D57E121153AF51; Max-Age=1800; Expires=Sun, 06-Nov-2022 18:49:10 GMT; Path=/; HttpOnly; SameSite=None; Secure",
            "Strict-Transport-Security": "max-age=63072000; includeSubDomains"
        },
        "reason": "OK",
        "response_text": "file=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAFYAAABWCAYAAABVVmH3AAAPvklEQVR4nO1de3RU1fX%2Bzp1H5pHJ5E0SAglCIISnIEWF8BK6iFqMwdLWVsuytKL%2BeGldpCygiEuruFrEZ1ACSlddgBKwWqBQlJcikAhNavgFQsIzJQkhmUwew7xO%2F4AJd%2B7zzGQmmXb5rXVXZvY9e%2B%2Fv7HvuPfvse%2B%2BEeL1eSggBpRSEEAAApRQ%2B%2BGRycp%2Bebx%2B%2FvXC%2FlH05W3J2hFyk2gXCg4W7nH2lmHEIEEJHwu%2FB2Ogpv%2BHgIQfVwApHFwuEOvzv1O0OykYwUOIRrA1WHdXAhnJ0tZaW4uSMaXDb7QHbCAa9eXb1yIgFgNajR3H610%2FA1dKCskkTUD47H876qyH1q2ajJ0cs8Xq93e%2BBEghBRf4sdF44L7lb36cP7tyzLySBjCRwwO3hTgiRPH34cmFboY5QXv7Qg3BcvCBr31lfj%2BNjRsH%2BzVFF%2B1JbIDyC4S7HgylmgaZbSumQVHt64wb%2B9fOfoaP6LDiNRmSfr2MYMADD%2FrIFXFQU07WNlUcw3OXsy9kSxiysgeXrOBsbcfKH00AIJ5%2FHAtCYzbjr8Neizkjh%2B8DydNqrqlDxyMMgWq3IB7%2FtuG9OgIuKEnVKreMRFVhF9mHC2SWL0HzgS0DulKcUY%2FYfgDY%2BvmeJhQgBj1ihvDtLWkIISieMh7fTId2WUozY8SmMmQO%2BX9IGYoNSirFHvkHynJ%2FKNURFQT6qC5eq8ggG3eGuhoADG46kO7PwdzBmDZZt37RnF1wNDd32q8YjlHoRU4QZvmUbEh94ENTrFbfnOJzMmyF7iQoWrDYopbDZbFi4YAHi4%2BLhuHXpUkKPF2HkQAjBHS%2B%2BhBElOwFKb%2BbAvA0UqH1xVUB8unN2UUrR2dmJ3y55FklJyUhKScE7772H1o52Jt1eywqU4LhwAeUPz5Lcl%2FPBZkSPHBU23263G%2Fv27sXihYtw%2FspleKXqHtebYTQZFe0EvKQVyvn6wvYsyz8pW4aMDGS%2FUyRpp3Lu42g5dFDRXyA8fJ%2BPHDqM0SNGwmK1YlZBAWpvBVXJvlLMIuYaK4T1nnuRPGeOpO6ZRQuY67pKOHXyJH7x6KOIiY3F1B%2FOQGX1WXi8XmV%2BjJeTgAPbk8hcukx2Mqvb%2BH7QdhsaGjB10iRMnjIFW7ZvR0dnJ5OehuMwsH8GtDqtatuIDiwIweg9%2ByA1Rq4UFQEBjNqG%2BgZMnzoNfVPTkN6%2FPw4fO4aOGzdUzx6OEGSm9cW8x3%2BJ5qYmVFWfhU6nU6eutvK62T%2B2m32%2BtqFcxVFK4bXbUTp5ooi8oX8GRn36mSwPl8uF1%2F%2F0J7y6Zg1s7e0BZQVxFgse%2F8VjeHnNq9DrdKo1E6FtLV8o59jvnhVjW6n9gdjnf%2BYsFsTm5qLl8GE%2FPcfFC%2FC0t4MzmbpkhBBs2lCM5557Dg63C84ARnWM2YxHCgqwZMmzGDosR5YX%2F7tcn3q8uiVFlOWMAKU4Pna0SF%2BflIQ79%2B7H%2BdpaPJCXh9rLl%2BF0uZhrBTqtFjmDsvCXrVuQnZ0tqSMES3UrIpa0TDoAKBVPZFfq6zHp3gkYOWo0qmpr4XS5mOxpNBrckZ6O4vXrUXrqJIYMGcLGg5G7%2BvQmAP8a6PveXRusOv0WLsblN9%2BAFsBb7Q582tQEW1ubX06pZFfDcTDo9Fi9%2BgUsXLSoSx4IF1buAQe2N1F0tgZFl%2BrQYrd3rYjUDiylFDEmExYvWoTCZcugE0xE4UJELml9IITg6Ndf4%2FcrVuLIN0eZJyJCCGItFmRnDcbWj7chNS0tzEzF0PqI9EahW86W2%2B3GnILZ2PvFF3C4nIqTH18WpdMhe1AWSnbuRP%2BM%2Fkw8wlXojpgRSwjBuepq%2FHnzZrz9bhFa7K0BXfs0HIe%2F%2FfUz3Df9vjCyZEevj1iXy4U%2FvvYa1r6%2BDs32Vj8dqVRPzqbH60X12bNdgWXlEa4R2ytFGLfbjTfWrcO4sWMRGx%2BPFatXo5lhhBJC0C8lFQvmz0dSXLxoX1HRuwHxCFcBCWDICuSS5GB0TpZ9i6eefBLlpytFE5FwJcMfGXqtFsOzs7H%2FwAGYzWYAgMloxKtr1%2FodjKpz5xR5BJtzB9X%2FcF5jCSEoP3UK8341D9U1NbB3djB3Tq%2FXY2R2Nt7bUIycYTnQ3HqKxoeG%2BnqkZ2aKTsHGq1dhtVpD2o%2Bg4PV6KaWU%2Bv76Pvs2PqTkfH3f57a2NrpowQIaa42l2qgoqo2Kohq93u8zf%2FPJooxGmtInhb6x9nXq8XhEvvlwu93UYDJ12fTZOHjgoKitkKcSdyWfwrZKMQNf0N3N7XbTp379GxoXG%2BsXMJYtJTmZFr%2B%2FgTqdTmZ%2FCQkJIjtLf%2Ft8yPrTnS3gESts63Q66a5du2hqnxS%2FUSkcqcIRq9XrqTk6ms5%2BKF%2FRvhL6p%2FcT%2BRs5bDjziJUahVI6LLaEMQuq0E0IweFDhzB40CCYY2Lwo%2Fx8NDRfV9WjlEKv0WL6pEmo%2F%2Fe%2F0Wa34%2BMdJcFQAADk5c0UyewMT4v3BJhvf1NK8cX%2B%2Fbh%2F5kyYoqMxZcYM1Fy6BK%2Fg1gmlvFvWtxCl0yEjLQ37du9Ge3sb9uzbh7i4OMWJTGmfD5MnT%2FbzRynFdZtN1gaLzWB4SOkwFbp%2F8siPsXvvXnTcuP2ggloCwnEcUuIT8Obbb%2BGh%2FHzmArjcZyn069dPJHO5XX5Jv5q%2FYOVqMWOqbu36%2Bx50Op0sTcFxHKzRFjw9%2F0ksW74cer0%2BqKPOgvjERJHM6XaHzV8gYF7SytVhfbK4mBjMe%2BIJvPzKKwHfH2K9pya0m5ycLF4JQnp1JMcjXEtappWXUNH3PT2pDzZt%2FgATc3OhvfUgsdptGH4bNb98G0pLaT9bMvUFOR5qkOLBwp3jOxROOmq43FiPGXl5sMbFYtiQoagor%2FAzLnUwlOR8LsL2UpsUCE%2BXhYeSPyW5WsyYHjHi%2F%2BXLfTKX24MzF2ox5gfjkJiYiOFDc3C%2Btlak69NRsiXVVm5rrK8HeJUw4cgSyuVsq%2Bmw2BL2hymPjY22MI9kW1sbqmprMHLUaDz26M8l24Qi7aGUornFBio4m3Va9rtN4Uy%2FmAJ7se4K2mw2PPaTnyLGqPyUHXDziDlcTmwp2Q690Yi%2BqalY%2BMwzXadNKMp1hBDUXbkCIkj8dFotc%2BfDWTZkCiwhBAaDARs%2F%2FADXW1rQ3HgND%2BXdjyidTvW6TClFQ3Mz3i0uht5gRGb%2FDOzetSuoTgnx1ddfiWQxFku37YYE3S02lJWW0WmTp1CTOZq54KLR66nRZKJZdwykRw4fFq21Wbc7MgaI7I7Iyen1AkxQRRihnK9%2F6OBBmp6aRqMtFtUiDH8zR5vpAzPzqNPpFHER%2BuEjKTFRVIQpfP555iIMX8bqk99WtQhDGVMTKTlff2JuLqprzuFvf%2F0MI7Kzu3JbJfsA4HC68Pcvv0BaahqmT52GM2fOSPrmf6eUosPhEMkm5uZKtpXjwecjpyMVA7WYhaXQ7YPD4aC%2FX7GSJiYk0iijUbZGK1UMT07uQ198YbXsKG5paRGVKTV6PW1oaIiIEdvteqyUQykdh8NBVy5fQZMTk6jWYFAMLP%2Bv0WymSYmJ9JWXXvazu3rVKlFgDUaTKo9guLPYCjiwckdYiZySQ6%2FXSyu%2F%2B47eN3kKTUhICOguQ2xsHH3il3PpwYMHaVpKimh%2FdlYWMw%2FWwAYy%2Bvlbrz%2BwUfldJZ6ePx%2Bl%2FzyFG4wVNOBmFc0rqAW%2F9vIfsPjZJaGmGBR69V1avi2v14v3ioqwceMmVFRWwuVxyz6wwbfRtbQEcOXSJSTeKiVGxAMbVGWGU5ILjfLbC%2FdL2eF34MmnnsLx0hPYsL4IyXFxos5IcemSAcjOysL7Reu7Os3Cg4W7nF%2BlmPXY5BVohkEppR6Ph%2F64oID2SUymOoNBlAHI3bw0mkx0yKAsumN7SUi4s%2FRJ2J%2F%2FmkflbTYbJoy%2FG2cuXoDX45HkJ%2BRB6c1H4UcOzUHJzh3om54eFHchpHgK%2BxMx79Kq2bBarfjytVdxNDsLmwZnISMpGRqOUz1VXW43yirKkTFwIKxWK6ZPmYqG%2BgZmTsFy7%2FWsIBAcHz0C4G6PBQMhWN%2FRiY%2BvNcPWZr%2F1noJ6dyilsBhNWFZYiPnPPA1LGAo3kf0CnRCcP10HpZjXJxmn%2F%2F80lhcWIj4mhqlqRghBm6MTK15YhczMTCxbWggX40shrIiYdEuurQ81q1%2FAtZ23H%2B7w2Rjzjy%2BhS0joktfV1SH%2FwR%2FhdPVZOHh5sRwPn0yr0SAzrS%2F%2B%2FNFHGPeDcX77hf3xce7WNVYIpZt6wdpQg6fNjsYd20VyXUKCX1ABIDU1FcfKSmFvbcW5qiqMGT4ceoZXNN0eD85dvoR7cifCYDZjeE4OSk%2BUBs094i8F7uZmfDtD%2BvH30Z%2FvVtTtn5GBY6WlaG1pwfq33kKsOVr1DgMhBB6PB1U1NbgndyLi4uLxq7lzUV5eHhDviJ68CCE4PmaUZCCSC2Yjc%2FnKoOxu3FCMVatWob6pCV6Jl%2FLkYIoy4OFZs7Bp84eqIzeiX1K%2B%2BuEHuLhurQRtinEnToJoNEHzaG9vx4rly1HyyXbUXWsU1R3kQDgOtmtNMJlNyjGL1BHrOF%2BLioJ88Sv1lGLA8pVImv1IyHxdv34dy5YWYtsnn8De2eF3cKXA8tMlEZkVuFtbUTZpAggvvfLtG7zuTcTmTlL0FwgPIfeysjL8cc0afLZ7Nzolfs%2BAUorW682KIzYiswK3zSYKqg8xd98N68TcoP2y8Bg7diw%2B2roV9tZW7P78cwweMACcygiWQsQsaSmluLK%2BCGVTcgGZ6tSQt4sCCmh3l9bTp0%2FHvyor0dLUhJKt2zAwI0P0komc34i4xhJCUPV%2FT6PlqyOybYZ9tAXm7KE9yEoa9lY7oi3RqgdY9TFO336fPBxZQf32jxWDaho4EObsoSEtRMvpqMljrDFs80ZvjlhCCP6ZPwsOmd%2FvJoRgyLvrYR1%2Fd1CXpN5EwO%2FShqoeW7exGJfWrQU4TvqMADC0eBMsd46RtMtv3x0eLDpyfpVi1uM%2FBOFsbMCp%2B2fe%2FEEyiZkfAEApRu%2FZB31KSs%2BSCyF67F1aT1sbKubMhvOq%2BH8f%2BJ3mHIdxx0r9fmo6WAh5BF20DqL%2Fquy7m6cSQlD7h5fQuP0T4NbP28lNjrr4BAzbsg1Eqw1Lnqq2omKxwaoT1smL3riBE%2BPvkj%2Flb7dEv8XPIvXxueGi0uMI%2B5LW3WrDt5NzQQU6PnA6He46ehxEo1GdYKS4hHpJq%2BRTaL9Xl7QaSwzGHvoKHK%2FYTAgBZzBgyDtFuOtYKQjDaiYUS2k1m6HU6bHb3wBw4t7xIJRiRMmnfjM%2BywJECpGcbvXocwWeVhs00Zau017o438psD1ahNFaY5lO%2B2D9svLojg1WnYgownyP78GM%2FwC8ldCT9gRg9wAAAABJRU5ErkJggg%3D%3D"
    }
]
```
### Output Parameters

| Name | Type | Description |
|------|------|-------------|
| status_code | number |  |
| reason | string |  |
| file | array |  |
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Server-Timing | string |  |
| Content-Encoding | string |  |
| X-Is-Logged-In | string |  |
| X-Transaction-ID | string |  |
| Content-Disposition | string |  |
| X-Content-Type-Options | string |  |
| x-attachment-metadata | string |  |
| x-edge-enc-proxy-static | string |  |
| Content-Type | string |  |
| Transfer-Encoding | string |  |
| Date | string |  |
| Keep-Alive | string |  |
| Connection | string |  |
| Server | string |  |
| Set-Cookie | string |  |
| Strict-Transport-Security | string |  |
## Error Handling

### Common Error Responses

| Status Code | Message | Description | Example |
|-------------|---------|-------------|---------|
| 400 | Bad Request | The request was invalid or cannot be processed. | Invalid search ID or parameters. |
| 401 | Unauthorized | Missing or incorrect authentication. | Invalid API token. |
| 403 | Forbidden | Access to the resource is denied. | No permissions for search. |
| 404 | Not Found | The requested item does not exist. | Search ID not found. |
| 500 | Internal Server Error | A server error occurred. | Unexpected failure in Splunk. |

### Error Example

```json
{
  "messages": [
    {
      "type": "ERROR",
      "text": "Search ID not found."
    }
  ],
  "status_code": 404,
  "reason": "Not Found"
}
```