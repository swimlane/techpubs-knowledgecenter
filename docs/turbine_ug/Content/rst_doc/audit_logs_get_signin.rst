Audit Logs Get SignIn
=====================

Retrieve a specific sign-in event for a Microsoft Entra user by providing the tenant's unique ID.

Inputs
------


**Path Parameters** (*object*) - Required


  **ID** (*string*) - Required

    .. list-table::
       :class: custom-table

       * - Example
         - 66ea54eb-6301-4ee5-be62-ff5a759b0100


**Parameters** (*object*)


  **ID** (*string*) - Required

    .. list-table::
       :class: custom-table

       * - Description
         - OData query parameters to help customize the response.

Outputs
-------


 - **Status Code** (*number*): 200


 - **Response Headers** (*object*): 

 - **Reason** (*string*): OK


 - **JSON Body** (*object*): 

   - **@odata.context** (*string*): https://graph.microsoft.com/v1.0/$metadata#auditLogs/signIns


   - **Value** (*array*): 

     - **ID** (*string*): 66ea54eb-6301-4ee5-be62-ff5a759b0100


     - **Created Date Time** (*string*): 2023-12-01T16:03:24Z


     - **User Display Name** (*string*): Test Contoso


     - **User Principal Name** (*string*): testaccount1@contoso.com


     - **User ID** (*string*): 26be570a-ae82-4189-b4e2-a37c6808512d


     - **App ID** (*string*): de8bc8b5-d9f9-48b1-a8ad-b748da725064


     - **App Display Name** (*string*): Graph explorer


     - **IP Address** (*string*): 131.107.159.37


     - **Client App Used** (*string*): Browser


     - **Correlation ID** (*string*): d79f5bee-5860-4832-928f-3133e22ae912


     - **Conditional Access Status** (*string*): notApplied


     - **Is Interactive** (*boolean*): True


     - **Risk Detail** (*string*): none


     - **Risk Level Aggregated** (*string*): none


     - **Risk Level During Sign In** (*string*): none


     - **Risk State** (*string*): none


     - **Risk Event Types** (*array*): 

       - **file_name** (*string*) - Required


       - **file** (*string*) - Required


     - **Resource Display Name** (*string*): Microsoft Graph


     - **Resource ID** (*string*): 00000003-0000-0000-c000-000000000000


     - **Status** (*object*): 

       - **Error Code** (*number*): 0


       - **Failure Reason** (*object*): 

       - **Additional Details** (*object*): 

     - **Device Detail** (*object*): 

       - **Device ID** (*string*): 


       - **Display Name** (*object*): 

       - **Operating System** (*string*): Windows 10


       - **Browser** (*string*): Edge 80.0.361


       - **Is Compliant** (*object*): 

       - **Is Managed** (*object*): 

       - **Trust Type** (*object*): 

     - **Location** (*object*): 

       - **City** (*string*): Redmond


       - **State** (*string*): Washington


       - **Country Or Region** (*string*): US


       - **Geo Coordinates** (*object*): 

         - **Altitude** (*object*): 

         - **Latitude** (*number*): 47.68050003051758


         - **Longitude** (*number*): -122.12094116210938


     - **Applied Conditional Access Policies** (*array*): 

       - **ID** (*string*): 6701123a-b4c6-48af-8565-565c8bf7cabc


       - **Display Name** (*string*): Medium signin risk block


       - **Enforced Grant Controls** (*array*): 

         - **file_name** (*string*) - Required


         - **file** (*string*) - Required


       - **Enforced Session Controls** (*array*): 

         - **file_name** (*string*) - Required


         - **file** (*string*) - Required


       - **Result** (*string*): notEnabled