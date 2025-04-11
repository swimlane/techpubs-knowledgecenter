# Forensics Threat

**Description**: Retrieve aggregate forensics data for a specified threat in ProofPoint using the threatId parameter.

## Endpoint

- **URL:** `/v2/forensics`
- **Method:** `GET`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| parameters | object |  | Yes |
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Wed, 18 Oct 2023 13:44:40 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "X-Content-Type-Options": "nosniff",
      "Vary": "Accept-Encoding, User-Agent",
      "Content-Encoding": "gzip",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "generated": "2023-10-18T13:44:39.664Z",
      "reports": [
        {
          "scope": "THREAT",
          "id": "4bae2afd5bde68ade4218e95bbca7d640eb39d9702d383d92d2a5488ed27e2c1",
          "name": "https://t.co/RBOyv9dl3C",
          "threatStatus": "active",
          "forensics": [
            {
              "type": "dns",
              "display": "DNS lookup of host: pixelfy.me",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "pixelfy.me"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: www.googletagmanager.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "www.googletagmanager.com",
                "ips": [
                  "142.250.217.136"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: fonts.googleapis.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "fonts.googleapis.com"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://www.facebook.com/tr/?id=194243278145610&ev=PageView&dl=https%3A%2F%2Fpixelfy.me%2FQxUk5c&rl=https%3A%2F%2Ft.co%2F&if=false&ts=1697294133296&sw=1536&sh=864&v=2.9.134&r=stable&ec=0&o=30&fbp=fb.1.1697294133293.13977260&ler=other&it=1697294132925&co..",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://www.facebook.com/tr/?id=194243278145610&ev=PageView&dl=https%3A%2F%2Fpixelfy.me%2FQxUk5c&rl=https%3A%2F%2Ft.co%2F&if=false&ts=1697294133296&sw=1536&sh=864&v=2.9.134&r=stable&ec=0&o=30&fbp=fb.1.1697294133293.13977260&ler=other&it=1697294132925&coo=false&rqm=GET"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 172.217.12.138:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "172.217.12.138",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://grigomac.com/brita/amx-page/index.php",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://grigomac.com/brita/amx-page/index.php"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 142.250.186.74:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "142.250.186.74",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: www.googletagmanager.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "www.googletagmanager.com",
                "ips": [
                  "172.217.18.104"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: fonts.googleapis.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "fonts.googleapis.com",
                "ips": [
                  "142.250.186.74"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "behavior",
              "display": "PFPT HUNTING LOTS-PROJECT DOMAIN - DNS Request for Twitter Domain -- t .co",
              "engine": "iee",
              "malicious": false,
              "note": "PFPT HUNTING LOTS-PROJECT DOMAIN - DNS Request for Twitter Domain -- t .co",
              "time": 0,
              "what": {
                "rule": "etpro_44683"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "File fbevents.js created",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "564a53ce84ae022b30816d44aa48589ebfe170c226b098d0245c47fe13341c67",
                "size": 203000,
                "path": "fbevents.js"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 104.244.42.69:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "104.244.42.69",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 142.250.217.136:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "142.250.217.136",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "File gr.html created",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "3ef653c2aec0c36f7fa5a6c2df2a35d47675b86a0e79272a96cab7c4f8c26d6b",
                "size": 7556,
                "path": "gr.html"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://connect.facebook.net/signals/config/194243278145610?v=2.9.134&r=stable&domain=pixelfy.me",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://connect.facebook.net/signals/config/194243278145610?v=2.9.134&r=stable&domain=pixelfy.me"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://connect.facebook.net/en_US/fbevents.js",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://connect.facebook.net/en_US/fbevents.js"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: region1.google-analytics.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "region1.google-analytics.com",
                "ips": [
                  "216.239.34.36",
                  "216.239.32.36"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: grigomac.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "grigomac.com"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 172.67.74.184:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "172.67.74.184",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 31.13.70.7:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "31.13.70.7",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: t.co",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "t.co"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "HTTP response would be written to disk: https://pixelfy.me/QxUk5c",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "66001f7eed6229831c412aa9296e09bacec4b1e40e675e039d61b63f7b397001",
                "size": 5554,
                "path": "https://pixelfy.me/QxUk5c"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: www.facebook.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "www.facebook.com",
                "ips": [
                  "31.13.70.36"
                ],
                "cnames": [
                  "star-mini.c10r.facebook.com"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "HTTP response would be written to disk: https://connect.facebook.net/signals/config/194243278145610?v=2.9.134&r=stable&domain=pixelfy.me",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "64ea5f62b58b4ecfb123be34bcb3a49546d4ff0bd96266b441ffdb0005ca368b",
                "size": 134873,
                "path": "https://connect.facebook.net/signals/config/194243278145610?v=2.9.134&r=stable&domain=pixelfy.me"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://www.google-analytics.com/g/collect?v=2&tid=G-1QBJ2GPV5Y&gtm=45je3ab0&_p=1587741629&cid=569024392.1697311258&ul=en-us&sr=1536x864&uaa=&uab=&uafvl=HeadlessChrome%3B%7CNot%253BA%253DBrand%3B8.0.0.0%7CChromium%3B&uamb=0&uam=&uap=Linux&uapv=&uaw=0&_e..",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://www.google-analytics.com/g/collect?v=2&tid=G-1QBJ2GPV5Y&gtm=45je3ab0&_p=1587741629&cid=569024392.1697311258&ul=en-us&sr=1536x864&uaa=&uab=&uafvl=HeadlessChrome%3B%7CNot%253BA%253DBrand%3B8.0.0.0%7CChromium%3B&uamb=0&uam=&uap=Linux&uapv=&uaw=0&_eu=AEA&_s=2&sid=1697311258&sct=1&seg=0&dl=https%3A%2F%2Fpixelfy.me%2FQxUk5c&dr=https%3A%2F%2Ft.co%2F&dt=Pixelfy.me&en=scroll&epn.percent_scrolled=90&_et=7"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "behavior",
              "display": "Malicious content dropped during execution",
              "engine": "iee",
              "malicious": true,
              "note": "Malicious content dropped during execution",
              "time": 0,
              "what": {
                "rule": "behavior_b6b72d3557d48f8d4cf7d87ec993ed24"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "HTTP response would be written to disk: https://t.co/RBOyv9dl3C",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "54a545785b61eccb1d30d27a38f0ff65473015994500d151d47a54861758f189",
                "size": 230,
                "path": "https://t.co/RBOyv9dl3C"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: grigomac.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "grigomac.com",
                "ips": [
                  "188.114.97.3",
                  "188.114.96.3"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "File main.js created",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "bbdfdbb816159c4fff8e14c65680756e6ac3fe79e8bbcb1b91dac9142264b167",
                "size": 7451,
                "path": "main.js"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 188.114.96.3:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "188.114.96.3",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 172.217.12.142:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "172.217.12.142",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: www.facebook.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "www.facebook.com",
                "ips": [
                  "157.240.251.35"
                ],
                "cnames": [
                  "star-mini.c10r.facebook.com"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 216.239.32.36:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "216.239.32.36",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "HTTP response would be written to disk: https://www.googletagmanager.com/gtag/js?id=G-1QBJ2GPV5Y",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "b40f9985c098494b8371b4d0e2698bf89fa6230f5e635d66e761e55a0ab4b21b",
                "size": 242893,
                "path": "https://www.googletagmanager.com/gtag/js?id=G-1QBJ2GPV5Y"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://grigomac.com/cdn-cgi/challenge-platform/h/g/jsd/r/81608cb30b251c20",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://grigomac.com/cdn-cgi/challenge-platform/h/g/jsd/r/81608cb30b251c20"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 104.244.42.197:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "104.244.42.197",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "UDP connection to 1.1.1.1:53",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "1.1.1.1",
                "port": 53,
                "type": "udp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "File QxUk5c created",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "3b0e329f2afb381750edef6e285ee7ed6f092aa89d108a3f498299b01e6692bd",
                "size": 5566,
                "path": "QxUk5c"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "HTTP response would be written to disk: https://grigomac.com/cdn-cgi/challenge-platform/h/g/scripts/jsd/dffb14d6/main.js",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "bc4deac632988d79af92225d5cf552c97c544196342b55a9d47f88f84c523282",
                "size": 7324,
                "path": "https://grigomac.com/cdn-cgi/challenge-platform/h/g/scripts/jsd/dffb14d6/main.js"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://grigomac.com/cdn-cgi/challenge-platform/h/g/jsd/r/81622ed18ed4dbb6",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://grigomac.com/cdn-cgi/challenge-platform/h/g/jsd/r/81622ed18ed4dbb6"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: t.co",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "t.co",
                "ips": [
                  "104.244.42.197",
                  "104.244.42.133",
                  "104.244.42.69",
                  "104.244.42.5"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "File main.js created",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "bc4deac632988d79af92225d5cf552c97c544196342b55a9d47f88f84c523282",
                "size": 7324,
                "path": "main.js"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://www.google-analytics.com/g/collect?v=2&tid=G-1QBJ2GPV5Y&gtm=45je3ab0&_p=1587741629&cid=569024392.1697311258&ul=en-us&sr=1536x864&uaa=&uab=&uafvl=HeadlessChrome%3B%7CNot%253BA%253DBrand%3B8.0.0.0%7CChromium%3B&uamb=0&uam=&uap=Linux&uapv=&uaw=0&_s..",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://www.google-analytics.com/g/collect?v=2&tid=G-1QBJ2GPV5Y&gtm=45je3ab0&_p=1587741629&cid=569024392.1697311258&ul=en-us&sr=1536x864&uaa=&uab=&uafvl=HeadlessChrome%3B%7CNot%253BA%253DBrand%3B8.0.0.0%7CChromium%3B&uamb=0&uam=&uap=Linux&uapv=&uaw=0&_s=3&sid=1697311258&sct=1&seg=0&dl=https%3A%2F%2Fpixelfy.me%2FQxUk5c&dr=https%3A%2F%2Ft.co%2F&dt=Pixelfy.me&en=user_engagement&_et=1307"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: t.co",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "t.co",
                "ips": [
                  "104.244.42.197"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "HTTP response would be written to disk: https://grigomac.com/brt/gr.html",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "3ef653c2aec0c36f7fa5a6c2df2a35d47675b86a0e79272a96cab7c4f8c26d6b",
                "size": 7556,
                "path": "https://grigomac.com/brt/gr.html"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "HTTP response would be written to disk: https://grigomac.com/cdn-cgi/challenge-platform/h/g/scripts/jsd/dffb14d6/main.js",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "bbdfdbb816159c4fff8e14c65680756e6ac3fe79e8bbcb1b91dac9142264b167",
                "size": 7451,
                "path": "https://grigomac.com/cdn-cgi/challenge-platform/h/g/scripts/jsd/dffb14d6/main.js"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "HTTP response would be written to disk: https://fonts.googleapis.com/css?family=Ubuntu:400,500",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "6d58c1e726f9c0c33808d6bd8a03711b904f093fd0e0121391b5a73d60c5d284",
                "size": 3492,
                "path": "https://fonts.googleapis.com/css?family=Ubuntu:400,500"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://fonts.googleapis.com/css?family=Ubuntu:400,500",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://fonts.googleapis.com/css?family=Ubuntu:400,500"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "behavior",
              "display": "ETPRO Suricata IDS Alerts",
              "engine": "iee",
              "malicious": false,
              "note": "ETPRO Suricata IDS Alerts",
              "time": 0,
              "what": {
                "rule": "behavior_288b6c09e0dc5b5fc7664b918c773caa"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 157.240.0.6:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "157.240.0.6",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "HTTP response would be written to disk: https://grigomac.com/brt/gr.html",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "263a4774bc45f481a70312827a54d1834edf1c00eff8426e50bbfdb219cdaa0b",
                "size": 1348,
                "path": "https://grigomac.com/brt/gr.html"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://t.co/RBOyv9dl3C",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://t.co/RBOyv9dl3C"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "File js created",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "b40f9985c098494b8371b4d0e2698bf89fa6230f5e635d66e761e55a0ab4b21b",
                "size": 242893,
                "path": "js"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 104.21.76.224:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "104.21.76.224",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://region1.google-analytics.com/g/collect?v=2&tid=G-1QBJ2GPV5Y&gtm=45je3ab0&_p=687611364&cid=109704680.1697294133&ul=en-us&sr=1536x864&uaa=&uab=&uafvl=HeadlessChrome%3B%7CNot%253BA%253DBrand%3B8.0.0.0%7CChromium%3B&uamb=0&uam=&uap=Linux&uapv=&uaw=0..",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://region1.google-analytics.com/g/collect?v=2&tid=G-1QBJ2GPV5Y&gtm=45je3ab0&_p=687611364&cid=109704680.1697294133&ul=en-us&sr=1536x864&uaa=&uab=&uafvl=HeadlessChrome%3B%7CNot%253BA%253DBrand%3B8.0.0.0%7CChromium%3B&uamb=0&uam=&uap=Linux&uapv=&uaw=0&_s=1&sid=1697294132&sct=1&seg=0&dl=https%3A%2F%2Fpixelfy.me%2FQxUk5c&dr=https%3A%2F%2Ft.co%2F&dt=Pixelfy.me&en=page_view&_fv=1&_nsi=1&_ss=1&_ee=1"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 31.13.70.36:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "31.13.70.36",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://grigomac.com/cdn-cgi/challenge-platform/h/g/jsd/r/81622ec97ea3dbb6",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://grigomac.com/cdn-cgi/challenge-platform/h/g/jsd/r/81622ec97ea3dbb6"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://www.googletagmanager.com/gtag/js?id=G-1QBJ2GPV5Y",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://www.googletagmanager.com/gtag/js?id=G-1QBJ2GPV5Y"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "HTTP response would be written to disk: https://www.googletagmanager.com/gtag/js?id=G-1QBJ2GPV5Y",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "e8fdde1d979b12690fb9efd88337f4c6057c73f669e2fe257ccacf3136578ac3",
                "size": 242931,
                "path": "https://www.googletagmanager.com/gtag/js?id=G-1QBJ2GPV5Y"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://region1.google-analytics.com/g/collect?v=2&tid=G-1QBJ2GPV5Y&gtm=45je3ab0&_p=687611364&cid=109704680.1697294133&ul=en-us&sr=1536x864&uaa=&uab=&uafvl=HeadlessChrome%3B%7CNot%253BA%253DBrand%3B8.0.0.0%7CChromium%3B&uamb=0&uam=&uap=Linux&uapv=&uaw=0..",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://region1.google-analytics.com/g/collect?v=2&tid=G-1QBJ2GPV5Y&gtm=45je3ab0&_p=687611364&cid=109704680.1697294133&ul=en-us&sr=1536x864&uaa=&uab=&uafvl=HeadlessChrome%3B%7CNot%253BA%253DBrand%3B8.0.0.0%7CChromium%3B&uamb=0&uam=&uap=Linux&uapv=&uaw=0&_eu=AEA&_s=2&sid=1697294132&sct=1&seg=0&dl=https%3A%2F%2Fpixelfy.me%2FQxUk5c&dr=https%3A%2F%2Ft.co%2F&dt=Pixelfy.me&en=scroll&epn.percent_scrolled=90&_et=69"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 157.240.251.35:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "157.240.251.35",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "HTTP response would be written to disk: https://connect.facebook.net/en_US/fbevents.js",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "564a53ce84ae022b30816d44aa48589ebfe170c226b098d0245c47fe13341c67",
                "size": 203000,
                "path": "https://connect.facebook.net/en_US/fbevents.js"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 104.26.11.17:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "104.26.11.17",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://pixelfy.me/QxUk5c",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://pixelfy.me/QxUk5c"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://grigomac.com/brt/gr.html",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://grigomac.com/brt/gr.html"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: www.google-analytics.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "www.google-analytics.com",
                "ips": [
                  "172.217.12.142"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "File js created",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "e8fdde1d979b12690fb9efd88337f4c6057c73f669e2fe257ccacf3136578ac3",
                "size": 242931,
                "path": "js"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: connect.facebook.net",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "connect.facebook.net",
                "ips": [
                  "31.13.70.7"
                ],
                "cnames": [
                  "scontent.xx.fbcdn.net"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: fonts.googleapis.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "fonts.googleapis.com",
                "ips": [
                  "172.217.12.138"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "TCP connection to 172.217.18.104:443",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "172.217.18.104",
                "port": 443,
                "type": "tcp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "Malicious attachment with url: https://t.co/RBOyv9dl3C",
              "engine": "iee",
              "malicious": true,
              "time": 0,
              "what": {
                "url": "https://t.co/RBOyv9dl3C"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "File QxUk5c created",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "66001f7eed6229831c412aa9296e09bacec4b1e40e675e039d61b63f7b397001",
                "size": 5554,
                "path": "QxUk5c"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "File RBOyv9dl3C created",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "54a545785b61eccb1d30d27a38f0ff65473015994500d151d47a54861758f189",
                "size": 230,
                "path": "RBOyv9dl3C"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: pixelfy.me",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "pixelfy.me",
                "ips": [
                  "172.67.74.184",
                  "104.26.11.17",
                  "104.26.10.17"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "HTTP response would be written to disk: https://grigomac.com/brita/amx-page/index.php",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "2221adbdf86738989c59a873e86e3499ab1f9a7bd9f8cea82a261e999b2551b0",
                "size": 8079,
                "path": "https://grigomac.com/brita/amx-page/index.php"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://grigomac.com/cdn-cgi/challenge-platform/h/g/scripts/jsd/dffb14d6/main.js",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://grigomac.com/cdn-cgi/challenge-platform/h/g/scripts/jsd/dffb14d6/main.js"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: region1.google-analytics.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "region1.google-analytics.com"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "File 194243278145610 created",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "64ea5f62b58b4ecfb123be34bcb3a49546d4ff0bd96266b441ffdb0005ca368b",
                "size": 134873,
                "path": "194243278145610"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "HTTP response would be written to disk: https://grigomac.com/brita/amx-page/index.php",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "5222579ba7e03b694b6b5bd7adc8e2083add7d00ab984591b45d943f5b97586d",
                "size": 1348,
                "path": "https://grigomac.com/brita/amx-page/index.php"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "network",
              "display": "UDP connection to 1.0.0.1:53",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "action": "connect",
                "ip": "1.0.0.1",
                "port": 53,
                "type": "udp"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://www.facebook.com/tr/?id=194243278145610&ev=PageView&dl=https%3A%2F%2Fpixelfy.me%2FQxUk5c&rl=https%3A%2F%2Ft.co%2F&if=false&ts=1697311258687&sw=1536&sh=864&v=2.9.134&r=stable&ec=0&o=30&fbp=fb.1.1697311258685.1456490579&ler=other&it=1697311258277&..",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://www.facebook.com/tr/?id=194243278145610&ev=PageView&dl=https%3A%2F%2Fpixelfy.me%2FQxUk5c&rl=https%3A%2F%2Ft.co%2F&if=false&ts=1697311258687&sw=1536&sh=864&v=2.9.134&r=stable&ec=0&o=30&fbp=fb.1.1697311258685.1456490579&ler=other&it=1697311258277&coo=false&rqm=GET"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "File index.php created",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "5222579ba7e03b694b6b5bd7adc8e2083add7d00ab984591b45d943f5b97586d",
                "size": 1348,
                "path": "index.php"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "File css created",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "6d58c1e726f9c0c33808d6bd8a03711b904f093fd0e0121391b5a73d60c5d284",
                "size": 3492,
                "path": "css"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: connect.facebook.net",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "connect.facebook.net",
                "ips": [
                  "157.240.0.6"
                ],
                "cnames": [
                  "scontent.xx.fbcdn.net"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: www.facebook.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "www.facebook.com",
                "cnames": [
                  "star-mini.c10r.facebook.com"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: www.google-analytics.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "www.google-analytics.com"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "file",
              "display": "HTTP response would be written to disk: https://pixelfy.me/QxUk5c",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "sha256": "3b0e329f2afb381750edef6e285ee7ed6f092aa89d108a3f498299b01e6692bd",
                "size": 5566,
                "path": "https://pixelfy.me/QxUk5c"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://www.google-analytics.com/g/collect?v=2&tid=G-1QBJ2GPV5Y&gtm=45je3ab0&_p=1587741629&cid=569024392.1697311258&ul=en-us&sr=1536x864&uaa=&uab=&uafvl=HeadlessChrome%3B%7CNot%253BA%253DBrand%3B8.0.0.0%7CChromium%3B&uamb=0&uam=&uap=Linux&uapv=&uaw=0&_s..",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://www.google-analytics.com/g/collect?v=2&tid=G-1QBJ2GPV5Y&gtm=45je3ab0&_p=1587741629&cid=569024392.1697311258&ul=en-us&sr=1536x864&uaa=&uab=&uafvl=HeadlessChrome%3B%7CNot%253BA%253DBrand%3B8.0.0.0%7CChromium%3B&uamb=0&uam=&uap=Linux&uapv=&uaw=0&_s=1&sid=1697311258&sct=1&seg=0&dl=https%3A%2F%2Fpixelfy.me%2FQxUk5c&dr=https%3A%2F%2Ft.co%2F&dt=Pixelfy.me&en=page_view&_fv=1&_nsi=1&_ss=1&_ee=1"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: www.googletagmanager.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "www.googletagmanager.com"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: connect.facebook.net",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "connect.facebook.net",
                "cnames": [
                  "scontent.xx.fbcdn.net"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "dns",
              "display": "DNS lookup of host: grigomac.com",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "host": "grigomac.com",
                "ips": [
                  "172.67.201.233",
                  "104.21.76.224"
                ]
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            },
            {
              "type": "url",
              "display": "URL: https://grigomac.com/cdn-cgi/challenge-platform/scripts/jsd/main.js",
              "engine": "iee",
              "malicious": false,
              "time": 0,
              "what": {
                "url": "https://grigomac.com/cdn-cgi/challenge-platform/scripts/jsd/main.js"
              },
              "platforms": [
                {
                  "name": "Win10",
                  "os": "win",
                  "version": "win10"
                }
              ]
            }
          ]
        }
      ]
    }
  }
]
```
### Output Parameters

| Name | Type | Description |
|------|------|-------------|
| status_code | number |  |
| reason | string |  |
| json_body | object |  |
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Date | string |  |
| Content-Type | string |  |
| Transfer-Encoding | string |  |
| Connection | string |  |
| X-Content-Type-Options | string |  |
| Vary | string |  |
| Content-Encoding | string |  |
| Strict-Transport-Security | string |  |