Create or Update File Contents
===============
Creates a new file or replaces an existing file in a repository.


Inputs
~~~~~~~~~~~~


*Path Parameters**                    (*object*)  

  *Owner**                    (*string*)

    :Description: The account owner of the repository. The name is not case sensitive.

    ..  

  *Repo**                    (*string*)

    :Description: The name of the repository without the .git extension. The name is not case sensitive.

    ..  

  *Path**                    (*string*)

    :Description: Path from root to the file to be created or updated.

    ..

*Headers**                    (*object*)  

  *Accept**                    (*string*)  

  *X-Git Hub-Api-Version**                    (*string*)

*JSON Body**                    (*object*)  

  *Message**                    (*string*)

    :Description: The commit message.

    ..  

  *Content**                    (*string*)

    :Description: The file content, using Base64 encoding.

    ..  

  *SHA*                    (*string*)

    :Description: Required if you are updating a file. The blob SHA of the file being replaced.

    ..  

  *Branch*                    (*string*)

    :Description: The branch name. Default - the repository’s default branch.

    ..  

  *Committer*                    (*object*)

    :Description: The person that committed the file. Default - the authenticated user.

    ..    

    *Name*                    (*string*)

      :Description: The name of the committer of the commit. You'll receive a 422 status code if name is omitted.

      ..    

    *Email*                    (*string*)

      :Description: The email of the committer of the commit. You'll receive a 422 status code if email is omitted.

      ..    

    *Date*                    (*string*)  

  *Author*                    (*object*)    

    *Name*                    (*string*)

      :Description: The name of the author of the commit. You'll receive a 422 status code if name is omitted.

      ..    

    *Email*                    (*string*)

      :Description: The email of the author of the commit. You'll receive a 422 status code if email is omitted.

      ..    

    *Date*                    (*string*)
Outputs
~~~~~~~~~~~~


*Status Code*                    (*number*)

  :Example: 200

  ..

*Response Headers*                    (*object*)  

  *Server*                    (*string*)

    :Example: GitHub.com

    ..  

  *Date*                    (*string*)

    :Example: Sun, 10 Sep 2023 08:29:41 GMT

    ..  

  *Content-Type*                    (*string*)

    :Example: application/json; charset=utf-8

    ..  

  *Transfer-Encoding*                    (*string*)

    :Example: chunked

    ..  

  *Cache-Control*                    (*string*)

    :Example: private, max-age=60, s-maxage=60

    ..  

  *Vary*                    (*string*)

    :Example: Accept, Authorization, Cookie, X-GitHub-OTP, Accept-Encoding, Accept, X-Requested-With

    ..  

  *ETag*                    (*string*)

    :Example: W/"911292a7951b39bdc0d53e0b0ed712f92385469a64c500a2fc0e186c6d1498ec"

    ..  

  *X-OAuth-Scopes*                    (*string*)

    :Example: admin:enterprise, admin:gpg_key, admin:org, admin:org_hook, admin:repo_hook, admin:ssh_signing_key, audit_log, codespace, copilot, delete:packages, delete_repo, gist, notifications, project, repo, user, workflow, write:discussion, write:packages

    ..  

  *X-Accepted-OAuth-Scopes*                    (*string*)

    :Example: 

    ..  

  *Github Authentication Token Expiration*                    (*string*)

    :Example: 2023-09-17 08:10:24 UTC

    ..  

  *X-Git Hub-Media-Type*                    (*string*)

    :Example: github.v3; format=json

    ..  

  *X Github Api Version Selected*                    (*string*)

    :Example: 2022-11-28

    ..  

  *X-Rate Limit-Limit*                    (*string*)

    :Example: 5000

    ..  

  *X-Rate Limit-Remaining*                    (*string*)

    :Example: 4997

    ..  

  *X-Rate Limit-Reset*                    (*string*)

    :Example: 1694337529

    ..  

  *X-Rate Limit-Used*                    (*string*)

    :Example: 3

    ..  

  *X-Rate Limit-Resource*                    (*string*)

    :Example: core

    ..  

  *Access-Control-Expose-Headers*                    (*string*)

    :Example: ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset

    ..  

  *Access-Control-Allow-Origin*                    (*string*)

    :Example: *

    ..  

  *Strict-Transport-Security*                    (*string*)

    :Example: max-age=31536000; includeSubdomains; preload

    ..  

  *X-Frame-Options*                    (*string*)

    :Example: deny

    ..  

  *X-Content-Type-Options*                    (*string*)

    :Example: nosniff

    ..  

  *X-XSS-Protection*                    (*string*)

    :Example: 0

    ..  

  *Referrer-Policy*                    (*string*)

    :Example: origin-when-cross-origin, strict-origin-when-cross-origin

    ..  

  *Content-Security-Policy*                    (*string*)

    :Example: default-src 'none'

    ..  

  *Content-Encoding*                    (*string*)

    :Example: gzip

    ..  

  *X-Git Hub-Request-Id*                    (*string*)

    :Example: 9C11:3F8C1E:5FD5E3:6AE11F:64FD7E74

    ..

*Reason*                    (*string*)

  :Example: OK

  ..

*JSON Body*                    (*object*)  

  *Content*                    (*object*)    

    *Name*                    (*string*)

      :Example: README.md

      ..    

    *Path*                    (*string*)

      :Example: README.md

      ..    

    *Sha*                    (*string*)

      :Example: 7d71b040dbc5ed0cee2775d7bc31bf9962bb65b3

      ..    

    *Size*                    (*number*)

      :Example: 40

      ..    

    *URL*                    (*string*)

      :Example: https://api.github.com/repos/swimlane-connectors/github-test/contents/README.md?ref=main

      ..    

    *HTML URL*                    (*string*)

      :Example: https://github.com/swimlane-connectors/github-test/blob/main/README.md

      ..    

    *Git URL*                    (*string*)

      :Example: https://api.github.com/repos/swimlane-connectors/github-test/git/blobs/7d71b040dbc5ed0cee2775d7bc31bf9962bb65b3

      ..    

    *Download URL*                    (*string*)

      :Example: https://raw.githubusercontent.com/swimlane-connectors/github-test/main/README.md?token=A5CRVS4CTRB6FBDXTU7L2P3E7V7LC

      ..    

    *Type*                    (*string*)

      :Example: file

      ..    

    *Links*                    (*object*)      

      *Self*                    (*string*)

        :Example: https://api.github.com/repos/swimlane-connectors/github-test/contents/README.md?ref=main

        ..      

      *Git*                    (*string*)

        :Example: https://api.github.com/repos/swimlane-connectors/github-test/git/blobs/7d71b040dbc5ed0cee2775d7bc31bf9962bb65b3

        ..      

      *HTML*                    (*string*)

        :Example: https://github.com/swimlane-connectors/github-test/blob/main/README.md

        ..  

  *Commit*                    (*object*)    

    *Sha*                    (*string*)

      :Example: 61c19c8fc77eec9f2c52ada1bcaa04b3fe55cf72

      ..    

    *Node ID*                    (*string*)

      :Example: MI_kwD

      ..    

    *URL*                    (*string*)

      :Example: https://api.github.com/repos/swimlane-connectors/github-test/git/commits/61c19c8fc77eec9f2c52ada1bcaa04b3fe55cf72

      ..    

    *HTML URL*                    (*string*)

      :Example: https://github.com/swimlane-connectors/github-test/commit/61c19c8fc77eec9f2c52ada1bcaa04b3fe55cf72

      ..    

    *Author*                    (*object*)      

      *Name*                    (*string*)

        :Example: Swimlane

        ..      

      *Email*                    (*string*)

        :Example: 121969355+Swimlane@users.noreply.github.com

        ..      

      *Date*                    (*string*)

        :Example: 2023-09-10T08:29:40Z

        ..    

    *Committer*                    (*object*)      

      *Name*                    (*string*)

        :Example: Swimlane

        ..      

      *Email*                    (*string*)

        :Example: 121969355+Swimlane@users.noreply.github.com

        ..      

      *Date*                    (*string*)

        :Example: 2023-09-10T08:29:40Z

        ..    

    *Tree*                    (*object*)      

      *Sha*                    (*string*)

        :Example: 73657c37901a6a09d6f88cb94b14cc2fb66d1817

        ..      

      *URL*                    (*string*)

        :Example: https://api.github.com/repos/swimlane-connectors/github-test/git/trees/73657c37901a6a09d6f88cb94b14cc2fb66d1817

        ..    

    *Message*                    (*string*)

      :Example: test commit message

      ..    

    *Parents*                    (*array*)

      :Example: [{'sha': '1eeb5ab638b7923546889000df375b178b29b603', 'url': 'https://api.github.com/repos/swimlane-connectors/github-test/git/commits/1eeb5ab638b7923546889000df375b178b29b603', 'html_url': 'https://github.com/swimlane-connectors/github-test/commit/1eeb5ab638b7923546889000df375b178b29b603'}]

      ..    

    *Verification*                    (*object*)      

      *Verified*                    (*boolean*)

        :Example: False

        ..      

      *Reason*                    (*string*)

        :Example: unsigned

        ..      

      *Signature*                    (*object*)      

      *Payload*                    (*object*)