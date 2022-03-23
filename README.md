1. SERIALIZER CLASS 
- seriliaizer and deserialize instances into representations such as json
- are similar to django forms

*Method Based
create and update methods define how instances are created or modified when serializer.save is called
- just like django forms, it includes validation flags, required and max_length. this fields also define how serializer and brosable API is displayed
-TIP: replicates alot of info from model class, just change model to serializer

*MODEALSERIALIZERS
- similar to modelForm


2. REQUESTS AND RESPONSES
- Requests extends regular HttpRequest providing flexible request parsing
when using request.data, there is no need of explicitly tying request or response o=to a given datatype as it can handle multiple formats including json
- Respose is aa type of TemplateResponse takes unrendered content, determines the correct content type to return
- status module provides explicit status code rather than just numeric code


3. API WRAPPERS
-@api_view decorator is used when working with functions
APIView when working with class based api

-optional format suffixes can be added to url that explicitly refer to a given format e.g http://example.com/api/items/4.json as a url


4. CLASS-BASED VIEWS
- allow reuse of common functionality and keeps the code DRY


5.GENERIC BASED
provide a set of aready generated functionality classes that trim down views.py


6. AUTHENTICATION
- associates incoming requests with a set of identifying credentials i.e user or token
-place at top of the view before any other code is excuted setting request.user to an instance of contrib.auth, request.auth represents authentication token and any other additional info

-create user field in the model that will be used for authentication from auth.user
