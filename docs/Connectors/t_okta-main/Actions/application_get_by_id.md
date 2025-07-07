# Get Application By ID

**Description**: Retrieve details of a specific application in Okta Identity Management using the provided application ID.

## Endpoint

- **URL:** `/api/v1/apps/{{appId}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **appId** (string) – Required: Application ID.
- **parameters** (object): Parameters
  - **expand** (string): An optional query parameter to return the specified Application User in the _embedded property. Valid value: expand=user/{userId}.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "reason": "Ok",
    "headers": {
      "content-type": "application/json; charset=utf-8",
      "content-length": "0",
      "connection": "close",
      "date": "Tue, 10 Mar 2020 15:00:00 GMT",
      "server": "nginx",
      "x-request-id": "a1b2c3d4e5f6g7h8i9j0",
      "x-runtime": "0.000000",
      "x-powered-by": "Phusion Passenger 5.3.7",
      "x-frame-options": "SAMEORIGIN",
      "x-xss-protection": "1; mode=block",
      "x-content-type-options": "nosniff",
      "x-download-options": "noopen",
      "x-permitted-cross-domain-policies": "none",
      "referrer-policy": "strict-origin-when-cross-origin",
      "strict-transport-security": "max-age=31536000; includeSubDomains",
      "x-content-security-policy": "default-src 'self' https://*.googleapis.com https://*.gstatic.com https://*.google.com https://*.google-analytics.com https://*.googleadservices.com https://*.googletagmanager.com https://*.googleusercontent.com https://*.gvt1.com https://*.gvt2.com https://*.gvt3.com https://*.gvt4.com https://*.gvt5.com https://*.gvt6.com https://*.gvt7.com https://*.gvt8.com https://*.gvt9.com https://*.gvt10.com https://*.gvt11.com https://*.gvt12.com https://*.gvt13.com https://*.gvt14.com https://*.gvt15.com https://*.gvt16.com https://*.gvt17.com https://*.gvt18.com https://*.gvt19.com https://*.gvt20.com https://*.gvt21.com https://*.gvt22.com https://*.gvt23.com https://*.gvt24.com https://*.gvt25.com https://*.gvt26.com https://*.gvt27.com https://*.gvt28.com https://*.gvt29.com https://*.gvt30.com https://*.gvt31.com https://*.gvt32.com https://*.gvt33.com https://*.gvt"
    },
    "response": {
      "id": "0oa1gjh63g214q0Hq0g4",
      "name": "testorgone_customsaml20app_1",
      "label": "Custom Saml 2.0 App",
      "status": "ACTIVE",
      "lastUpdated": "2016-08-09T20:12:19.000Z",
      "created": "2016-08-09T20:12:19.000Z",
      "accessibility": {
        "selfService": false,
        "errorRedirectUrl": null,
        "loginRedirectUrl": null
      },
      "visibility": {
        "autoSubmitToolbar": false,
        "hide": {
          "iOS": false,
          "web": false
        },
        "appLinks": {
          "testorgone_customsaml20app_1_link": true
        }
      },
      "features": [],
      "signOnMode": "SAML_2_0",
      "credentials": {
        "userNameTemplate": {
          "template": "${fn:substringBefore(source.login, \"@\")}",
          "type": "BUILT_IN"
        },
        "signing": {}
      },
      "settings": {
        "app": {},
        "notifications": {
          "vpn": {
            "network": {
              "connection": "DISABLED"
            },
            "message": null,
            "helpUrl": null
          }
        },
        "signOn": {
          "defaultRelayState": "",
          "ssoAcsUrl": "https://{yourOktaDomain}",
          "idpIssuer": "https://www.okta.com/${org.externalKey}",
          "audience": "https://example.com/tenant/123",
          "recipient": "https://recipient.okta.com",
          "destination": "https://destination.okta.com",
          "subjectNameIdTemplate": "${user.userName}",
          "subjectNameIdFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
          "responseSigned": true,
          "assertionSigned": true,
          "signatureAlgorithm": "RSA_SHA256",
          "digestAlgorithm": "SHA256",
          "honorForceAuthn": true,
          "authnContextClassRef": "urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport",
          "slo": {
            "enabled": true,
            "spIssuer": "http://testorgone.okta.com",
            "logoutUrl": "http://testorgone.okta.com/logout"
          },
          "spCertificate": {
            "x5c": [
              "MIIFnDCCA4QCCQDBSLbiON2T1zANBgkqhkiG9w0BAQsFADCBjzELMAkGA1UEBhMCVVMxDjAMBgNV\r\nBAgMBU1haW5lMRAwDgYDVQQHDAdDYXJpYm91MRcwFQYDVQQKDA5Tbm93bWFrZXJzIEluYzEUMBIG\r\nA1UECwwLRW5naW5lZXJpbmcxDTALBgNVBAMMBFNub3cxIDAeBgkqhkiG9w0BCQEWEWVtYWlsQGV4\r\nYW1wbGUuY29tMB4XDTIwMTIwMzIyNDY0M1oXDTMwMTIwMTIyNDY0M1owgY8xCzAJBgNVBAYTAlVT\r\nMQ4wDAYDVQQIDAVNYWluZTEQMA4GA1UEBwwHQ2FyaWJvdTEXMBUGA1UECgwOU25vd21ha2VycyBJ\r\nbmMxFDASBgNVBAsMC0VuZ2luZWVyaW5nMQ0wCwYDVQQDDARTbm93MSAwHgYJKoZIhvcNAQkBFhFl\r\nbWFpbEBleGFtcGxlLmNvbTCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBANMmWDjXPdoa\r\nPyzIENqeY9njLan2FqCbQPSestWUUcb6NhDsJVGSQ7XR+ozQA5TaJzbP7cAJUj8vCcbqMZsgOQAu\r\nO/pzYyQEKptLmrGvPn7xkJ1A1xLkp2NY18cpDTeUPueJUoidZ9EJwEuyUZIktzxNNU1pA1lGijiu\r\n2XNxs9d9JR/hm3tCu9Im8qLVB4JtX80YUa6QtlRjWR/H8a373AYCOASdoB3c57fIPD8ATDNy2w/c\r\nfCVGiyKDMFB+GA/WTsZpOP3iohRp8ltAncSuzypcztb2iE+jijtTsiC9kUA2abAJqqpoCJubNShi\r\nVff4822czpziS44MV2guC9wANi8u3Uyl5MKsU95j01jzadKRP5S+2f0K+n8n4UoV9fnqZFyuGAKd\r\nCJi9K6NlSAP+TgPe/JP9FOSuxQOHWJfmdLHdJD+evoKi9E55sr5lRFK0xU1Fj5Ld7zjC0pXPhtJf\r\nsgjEZzD433AsHnRzvRT1KSNCPkLYomznZo5n9rWYgCQ8HcytlQDTesmKE+s05E/VSWNtH84XdDrt\r\nieXwfwhHfaABSu+WjZYxi9CXdFCSvXhsgufUcK4FbYAHl/ga/cJxZc52yFC7Pcq0u9O2BSCjYPdQ\r\nDAHs9dhT1RhwVLM8RmoAzgxyyzau0gxnAlgSBD9FMW6dXqIHIp8yAAg9cRXhYRTNAgMBAAEwDQYJ\r\nKoZIhvcNAQELBQADggIBADofEC1SvG8qa7pmKCjB/E9Sxhk3mvUO9Gq43xzwVb721Ng3VYf4vGU3\r\nwLUwJeLt0wggnj26NJweN5T3q9T8UMxZhHSWvttEU3+S1nArRB0beti716HSlOCDx4wTmBu/D1MG\r\nt/kZYFJw+zuzvAcbYct2pK69AQhD8xAIbQvqADJI7cCK3yRry+aWtppc58P81KYabUlCfFXfhJ9E\r\nP72ffN4jVHpX3lxxYh7FKAdiKbY2FYzjsc7RdgKI1R3iAAZUCGBTvezNzaetGzTUjjl/g1tcVYij\r\nltH9ZOQBPlUMI88lxUxqgRTerpPmAJH00CACx4JFiZrweLM1trZyy06wNDQgLrqHr3EOagBF/O2h\r\nhfTehNdVr6iq3YhKWBo4/+RL0RCzHMh4u86VbDDnDn4Y6HzLuyIAtBFoikoKM6UHTOa0Pqv2bBr5\r\nwbkRkVUxl9yJJw/HmTCdfnsM9dTOJUKzEglnGF2184Gg+qJDZB6fSf0EAO1F6sTqiSswl+uHQZiy\r\nDaZzyU7Gg5seKOZ20zTRaX3Ihj9Zij/ORnrARE7eM/usKMECp+7syUwAUKxDCZkGiUdskmOhhBGL\r\nJtbyK3F2UvoJoLsm3pIcvMak9KwMjSTGJB47ABUP1+w+zGcNk0D5Co3IJ6QekiLfWJyQ+kKsWLKt\r\nzOYQQatrnBagM7MI2/T4\r\n"
            ]
          },
          "requestCompressed": false,
          "allowMultipleAcsEndpoints": false,
          "acsEndpoints": [],
          "attributeStatements": [],
          "inlineHooks": [
            {
              "id": "cal3ughy17pylLxQB357",
              "_links": {
                "self": {
                  "href": "https://{yourOktaDomain}/api/v1/inlineHooks/cal3ughy17pylLxQB357",
                  "hints": {
                    "allow": [
                      "GET",
                      "PUT",
                      "DELETE"
                    ]
                  }
                }
              }
            }
          ]
        }
      },
      "_links": {
        "logo": [
          {
            "name": "medium",
            "href": "https://testorgone.okta.com/assets/img/logos/default.6770228fb0dab49a1695ef440a5279bb.png",
            "type": "image/png"
          }
        ],
        "appLinks": [
          {
            "name": "testorgone_customsaml20app_1_link",
            "href": "https://testorgone.okta.com/home/testorgone_customsaml20app_1/0oa1gjh63g214q0Hq0g4/aln1gofChJaerOVfY0g4",
            "type": "text/html"
          }
        ],
        "help": {
          "href": "https://testorgone-admin.okta.com/app/testorgone_customsaml20app_1/0oa1gjh63g214q0Hq0g4/setup/help/SAML_2_0/instructions",
          "type": "text/html"
        },
        "users": {
          "href": "https://testorgone.okta.com/api/v1/apps/0oa1gjh63g214q0Hq0g4/users"
        },
        "deactivate": {
          "href": "https://testorgone.okta.com/api/v1/apps/0oa1gjh63g214q0Hq0g4/lifecycle/deactivate"
        },
        "groups": {
          "href": "https://testorgone.okta.com/api/v1/apps/0oa1gjh63g214q0Hq0g4/groups"
        },
        "metadata": {
          "href": "https://testorgone.okta.com/api/v1/apps/0oa1gjh63g214q0Hq0g4/sso/saml/metadata",
          "type": "application/xml"
        }
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **headers** (object)
  - **content-type** (string)
  - **content-length** (string)
  - **connection** (string)
  - **date** (string)
  - **server** (string)
  - **x-request-id** (string)
  - **x-runtime** (string)
  - **x-powered-by** (string)
  - **x-frame-options** (string)
  - **x-xss-protection** (string)
  - **x-content-type-options** (string)
  - **x-download-options** (string)
  - **x-permitted-cross-domain-policies** (string)
  - **referrer-policy** (string)
  - **strict-transport-security** (string)
  - **x-content-security-policy** (string)
- **response** (object)
  - **id** (string)
  - **name** (string)
  - **label** (string)
  - **status** (string)
  - **lastUpdated** (string)
  - **created** (string)
  - **accessibility** (object)
    - **selfService** (boolean)
    - **errorRedirectUrl** (object)
    - **loginRedirectUrl** (object)
  - **visibility** (object)
    - **autoSubmitToolbar** (boolean)
    - **hide** (object)
      - **iOS** (boolean)
      - **web** (boolean)
    - **appLinks** (object)
      - **testorgone_customsaml20app_1_link** (boolean)
  - **features** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **signOnMode** (string)
  - **credentials** (object)
    - **userNameTemplate** (object)
      - **template** (string)
      - **type** (string)
    - **signing** (object)
  - **settings** (object)
    - **app** (object)
    - **notifications** (object)
      - **vpn** (object)
        - **network** (object)
          - **connection** (string)
        - **message** (object)
        - **helpUrl** (object)
    - **signOn** (object)
      - **defaultRelayState** (string)
      - **ssoAcsUrl** (string)
      - **idpIssuer** (string)
      - **audience** (string)
      - **recipient** (string)
      - **destination** (string)
      - **subjectNameIdTemplate** (string)
      - **subjectNameIdFormat** (string)
      - **responseSigned** (boolean)
      - **assertionSigned** (boolean)
      - **signatureAlgorithm** (string)
      - **digestAlgorithm** (string)
      - **honorForceAuthn** (boolean)
      - **authnContextClassRef** (string)
      - **slo** (object)
        - **enabled** (boolean)
        - **spIssuer** (string)
        - **logoutUrl** (string)
      - **spCertificate** (object)
        - **x5c** (array)
      - **requestCompressed** (boolean)
      - **allowMultipleAcsEndpoints** (boolean)
      - **acsEndpoints** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **attributeStatements** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **inlineHooks** (array)
        - **id** (string)
        - **_links** (object)
          - **self** (object)
            - **href** (string)
            - **hints** (object)
              - **allow** (array)
  - **_links** (object)
    - **logo** (array)
      - **name** (string)
      - **href** (string)
      - **type** (string)
    - **appLinks** (array)
      - **name** (string)
      - **href** (string)
      - **type** (string)
    - **help** (object)
      - **href** (string)
      - **type** (string)
    - **users** (object)
      - **href** (string)
    - **deactivate** (object)
      - **href** (string)
    - **groups** (object)
      - **href** (string)
    - **metadata** (object)
      - **href** (string)
      - **type** (string)