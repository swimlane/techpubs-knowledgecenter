# Get URL Threat Match

**Description**: Check a URL against the Google Safe Browsing API for any threat entries that match the Safe Browsing lists

## Endpoint

- **URL:** `/v4/threatMatches:find`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **client** (object) – Required: Client Information
    - **clientId** (string): A client ID that (hopefully) uniquely identifies the client implementation of the Safe Browsing API.
    - **clientVersion** (string): The version of the client implementation.
  - **threatInfo** (object) – Required: Threat Information
    - **threatTypes** (array): The threat types to be checked.
    - **platformTypes** (array): The platform types to be checked.
    - **threatEntryTypes** (array): The entry types to be checked.
    - **threatEntries** (array) – Required: The threat entries to be checked.
      - **hash** (string): A hash prefix, consisting of the most significant 4-32 bytes of a SHA256 hash. This field is in binary format. For JSON requests, hashes are base64-encoded. A base64-encoded string.
      - **url** (string): A URL.
      - **digest** (string): The digest of an executable in SHA256 format. The API supports both binary and hex digests. For JSON requests, digests are base64-encoded. A base64-encoded string.
## Output

### Output Parameters

- **threat_type** (string)