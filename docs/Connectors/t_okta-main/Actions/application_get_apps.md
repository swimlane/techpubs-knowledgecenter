# Get Applications

**Description**: Retrieves a paginated list of all applications within the organization, with optional filtering based on expressions or queries.

## Endpoint

- **URL:** `/api/v1/apps`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **q** (string): Searches for apps with name or label properties that starts with the q value using the startsWith operation.
  - **after** (string): Specifies the pagination cursor for the next page of results. Treat this as an opaque value obtained through the next link relationship.
  - **useOptimization** (boolean): Specifies whether to use query optimization. If you specify useOptimization=true in the request query, the response contains a subset of app instance properties.
  - **limit** (number): It should be integer <int32> <= 200. Specifies the number of results per page.
  - **filter** (string): Filters apps by status, user.id, group.id, credentials.signing.kid or name expression that supports the eq operator. Filter for active apps:
  filter=status eq "ACTIVE"
Filter for apps with `okta_org2org` name:
  filter=name eq "okta_org2org"
Filter for apps using a specific key:
  filter=credentials.signing.kid eq "SIMcCQNY3uwXoW3y0vf6VxiBb5n9pf8L2fK8d-F1bm4"
  - **expand** (string): An optional parameter used for link expansion to embed more resources in the response. Only supports expand=user/{userId} and must be used with the user.id eq "{userId}" filter query for the same user. Returns the assigned Application User in the _embedded property.
  - **includeNonDeleted** (boolean): Specifies whether to include non-active, but not deleted apps in the results.
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
    "response": [
      {
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
            "idpIssuer": "http://www.okta.com/${org.externalKey}",
            "audience": "https://example.com/tenant/123",
            "recipient": "http://recipient.okta.com",
            "destination": "http://destination.okta.com",
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
              "spIssuer": "https://testorgone.okta.com",
              "logoutUrl": "https://testorgone.okta.com/logout"
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
                "id": "${inlineHookId}",
                "_links": {
                  "self": {
                    "href": "https://{yourOktaDomain}/api/v1/inlineHooks/${inlineHookId}",
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
              "href": "http://testorgone.okta.com/assets/img/logos/default.6770228fb0dab49a1695ef440a5279bb.png",
              "type": "image/png"
            }
          ],
          "appLinks": [
            {
              "name": "testorgone_customsaml20app_1_link",
              "href": "http://testorgone.okta.com/home/testorgone_customsaml20app_1/0oa1gjh63g214q0Hq0g4/aln1gofChJaerOVfY0g4",
              "type": "text/html"
            }
          ],
          "help": {
            "href": "http://testorgone-admin.okta.com/app/testorgone_customsaml20app_1/0oa1gjh63g214q0Hq0g4/setup/help/SAML_2_0/instructions",
            "type": "text/html"
          },
          "users": {
            "href": "http://testorgone.okta.com/api/v1/apps/0oa1gjh63g214q0Hq0g4/users"
          },
          "deactivate": {
            "href": "http://testorgone.okta.com/api/v1/apps/0oa1gjh63g214q0Hq0g4/lifecycle/deactivate"
          },
          "groups": {
            "href": "http://testorgone.okta.com/api/v1/apps/0oa1gjh63g214q0Hq0g4/groups"
          },
          "metadata": {
            "href": "http://testorgone.okta.com:/api/v1/apps/0oa1gjh63g214q0Hq0g4/sso/saml/metadata",
            "type": "application/xml"
          }
        }
      },
      {
        "id": "0oabkvBLDEKCNXBGYUAS",
        "name": "template_swa",
        "label": "Sample Plugin App",
        "status": "ACTIVE",
        "lastUpdated": "2013-09-11T17:58:54.000Z",
        "created": "2013-09-11T17:46:08.000Z",
        "accessibility": {
          "selfService": false,
          "errorRedirectUrl": null
        },
        "visibility": {
          "autoSubmitToolbar": false,
          "hide": {
            "iOS": false,
            "web": false
          },
          "appLinks": {
            "login": true
          }
        },
        "features": [],
        "signOnMode": "BROWSER_PLUGIN",
        "credentials": {
          "scheme": "EDIT_USERNAME_AND_PASSWORD",
          "userNameTemplate": {
            "template": "${source.login}",
            "type": "BUILT_IN"
          }
        },
        "settings": {
          "app": {
            "buttonField": "btn-login",
            "passwordField": "txtbox-password",
            "usernameField": "txtbox-username",
            "url": "https://example.com/login.html"
          }
        },
        "_links": {
          "logo": [
            {
              "href": "https:/example.okta.com/img/logos/logo_1.png",
              "name": "medium",
              "type": "image/png"
            }
          ],
          "users": {
            "href": "https://{yourOktaDomain}/api/v1/apps/0oabkvBLDEKCNXBGYUAS/users"
          },
          "groups": {
            "href": "https://{yourOktaDomain}/api/v1/apps/0oabkvBLDEKCNXBGYUAS/groups"
          },
          "self": {
            "href": "https://{yourOktaDomain}/api/v1/apps/0oabkvBLDEKCNXBGYUAS"
          },
          "deactivate": {
            "href": "https://{yourOktaDomain}/api/v1/apps/0oabkvBLDEKCNXBGYUAS/lifecycle/deactivate"
          }
        }
      }
    ]
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
- **response** (array)
  - **id** (string)
  - **name** (string)
  - **label** (string)
  - **status** (string)
  - **lastUpdated** (string)
  - **created** (string)
  - **accessibility** (object)
    - **selfService** (boolean)
    - **errorRedirectUrl** (object)
  - **visibility** (object)
    - **autoSubmitToolbar** (boolean)
    - **hide** (object)
      - **iOS** (boolean)
      - **web** (boolean)
    - **appLinks** (object)
      - **login** (boolean)
  - **features** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **signOnMode** (string)
  - **credentials** (object)
    - **scheme** (string)
    - **userNameTemplate** (object)
      - **template** (string)
      - **type** (string)
  - **settings** (object)
    - **app** (object)
      - **buttonField** (string)
      - **passwordField** (string)
      - **usernameField** (string)
      - **url** (string)
  - **_links** (object)
    - **logo** (array)
      - **href** (string)
      - **name** (string)
      - **type** (string)
    - **users** (object)
      - **href** (string)
    - **groups** (object)
      - **href** (string)
    - **self** (object)
      - **href** (string)
    - **deactivate** (object)
      - **href** (string)