.. _asset_1_apikey:

VirusTotal API Key Authentication
=================================

Authenticates using an API Key.

Inputs
------

.. list-table:: 
   :header-rows: 1

   * - Property
     - Title
     - Description
     - Type
     - Default / Format
   * - **url**
     - URL
     - A URL to the target host.
     - string
     - `https://www.virustotal.com`
   * - **x-apikey**
     - API Key
     - API key
     - string
     - password
   * - **verify_ssl**
     - Verify SSL Certificates
     - Verify SSL certificate.
     - boolean
     - 
   * - **http_proxy**
     - HTTP(s) Proxy
     - A proxy to route requests through.
     - string
     - 

Required
--------

.. list-table:: 
   :header-rows: 1

   * - Property
   * - url
   * - x-apikey

Meta
----

.. list-table:: 
   :header-rows: 1

   * - Property
     - Value
   * - **asset_url_key**
     - url
   * - **security**
     - 
       - **Type**: apiKey
       - **Name**: x-apikey
       - **In**: header
