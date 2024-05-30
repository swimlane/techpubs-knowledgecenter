Advanced Transformation Options
===============================

The table shows advanced transformation options, summary. and provides
easy to copy/paste examples. Want to write the code yourself?

You can use advanced transformations to write complex JSONata
expressions, which gives you significant flexibility to transform data
according to your needs. See `JSONata
Docs <https://docs.jsonata.org/overview.rstl>`__ to assist you in
writing expressions.

Text
^^^^

+---------------+-------------------------+-------------------------+
| Function      | Example Syntax          | Summary                 |
+===============+=========================+=========================+
| Append        | Returns an array        | $append([1,2],3) =>     |
|               | containing the values   | [1,2,3]                 |
|               | of the first array      |                         |
|               | followed by the values  |                         |
|               | of the second array. If |                         |
|               | either input is not an  |                         |
|               | array, returns an array |                         |
|               | containing the value of |                         |
|               | first input followed by |                         |
|               | the value of the second |                         |
|               | input.                  |                         |
+---------------+-------------------------+-------------------------+
| Regex         | **Note:** The flags to  | $r                      |
|               | use when evaluating the | egexContains("aabbcc53d |
|               | regular expression.     | dcc","[1-9][0-9]","im") |
|               | Supported flags are:    | => true                 |
|               | 'i' - ignore case, 'm'  | $r                      |
|               | - multiline match.      | egexContains("aabbcc03d |
|               | Determines if a string  | dcc","[1-9][0-9]","im") |
|               | contains at least one   | => false                |
|               | occurrence of a regular |                         |
|               | expression pattern.     |                         |
+---------------+-------------------------+-------------------------+
| Regex Match   | **Note:** The flags to  | $rege                   |
|               | use when evaluating the | xMatches("aabbcc53ddcc6 |
|               | regular expression.     | 8zz","[0-9][0-9]","im") |
|               | Supported flags are:    | => ["53", "68"]         |
|               | 'i' - ignore case, 'm'  |                         |
|               | - multiline match.      |                         |
|               | Finds occurrences of a  |                         |
|               | regular expression      |                         |
|               | pattern in a string and |                         |
|               | returns an array of     |                         |
|               | matched strings.        |                         |
+---------------+-------------------------+-------------------------+
| Regex Replace | **Note:** The flags to  | $regexRepl              |
|               | use when evaluating the | ace("aabbcc53ddcc68zz", |
|               | regular expression.     | "[0-9][0-9]","im","XY") |
|               | Supported flags are:    | => "aabbccXYddccXYzz"   |
|               | 'i' - ignore case, 'm'  |                         |
|               | - multiline match.      |                         |
|               | Finds occurrences of a  |                         |
|               | regular expression      |                         |
|               | pattern in a string and |                         |
|               | replaces each           |                         |
|               | occurrence with another |                         |
|               | string.                 |                         |
+---------------+-------------------------+-------------------------+
| Regex Split   | **Note:** The flags to  | $re                     |
|               | use when evaluating the | gexSplit("aabbcc53ddcc6 |
|               | regular expression.     | 8zz","[0-9][0-9]","im") |
|               | Supported flags are:    | => ["aabbcc", "ddcc",   |
|               | 'i' - ignore case, 'm'  | "zz"]                   |
|               | - multiline match.      |                         |
|               | Finds occurrences of a  |                         |
|               | regular expression      |                         |
|               | pattern in a string and |                         |
|               | splits the string into  |                         |
|               | an array of substrings  |                         |
|               | for each occurrence.    |                         |
+---------------+-------------------------+-------------------------+

 

Numbers
-------

+----------------------+----------------------+----------------------+
| Function             | Example Syntax       | Summary              |
+======================+======================+======================+
| Absolute Value       | Compute the absolute | $numericAbs(-1) => 1 |
|                      | value of a number.   |                      |
+----------------------+----------------------+----------------------+
| Calculate            | Evaluates a          | $eval("(52 +         |
|                      | mathematical         | 32)*(1/2)") => 8     |
|                      | expression.          |                      |
+----------------------+----------------------+----------------------+
| Ceil                 | Adjust a number      | $numericCeil(1234,   |
|                      | ceiling it.          | -1) => 1240          |
+----------------------+----------------------+----------------------+
| Floor                | Adjust a number      | $numericFloor(1234,  |
|                      | flooring it.         | -1) => 1230          |
+----------------------+----------------------+----------------------+
| Greater              | Check if the first   | $n                   |
|                      | number is greater    | umericGreaterThan(2, |
|                      | than the second.     | 7) => false          |
+----------------------+----------------------+----------------------+
| Greater Than or      | Check if the first   | $numericG            |
| Equal                | number is greater    | reaterThanOrEqual(7, |
|                      | than or equal to the | 7) => true           |
|                      | second.              |                      |
+----------------------+----------------------+----------------------+
| Less Than            | Check if the first   | $numericLessThan(2,  |
|                      | number is less than  | 7) => true           |
|                      | the second.          |                      |
+----------------------+----------------------+----------------------+
| Less Than or Equal   | Check if the first   | $numeri              |
|                      | number is less than  | cLessThanOrEqual(20, |
|                      | or equal to the      | 7) => false          |
|                      | second.              |                      |
+----------------------+----------------------+----------------------+
| Round                | Adjust a number      | $numericRound(123.6, |
|                      | rounding or flooring | 0) => 124            |
|                      | it.                  |                      |
+----------------------+----------------------+----------------------+

 

Arrays
------

+----------------------+----------------------+----------------------+
| Function             | Example Syntax       | Summary              |
+======================+======================+======================+
| Average Array        | Computes the mean    | $average([1,2,3]) => |
|                      | value of an array of | 2                    |
|                      | numbers.             |                      |
+----------------------+----------------------+----------------------+
| Avg                  | Average the values   | $arrayAvg([10, 30,   |
|                      | of an array of       | 40]) => 26.6666      |
|                      | numbers.             |                      |
+----------------------+----------------------+----------------------+
| AvgBy                | Average the values   | $arrayAvgBy([{       |
|                      | of a plucked         | “age”: 10 }, {       |
|                      | property of the      | “age”: 30 }, {       |
|                      | objects within an    | “age”: 40 }], “age”) |
|                      | array of objects.    | => 26.6666           |
+----------------------+----------------------+----------------------+
| Count Items in Array | Returns the total    | $count([1,2,3]) => 3 |
|                      | number of items in   |                      |
|                      | an array (i.e. array |                      |
|                      | length).             |                      |
+----------------------+----------------------+----------------------+
| CountIf              | Count all items of   | $arrayCountIf([43,   |
|                      | an array that are    | 43, 41, 100], 43) => |
|                      | equal to a specific  | 2                    |
|                      | value.               |                      |
+----------------------+----------------------+----------------------+
| CountIfBy            | Count all items of   | $arrayCountIfBy( [{  |
|                      | an array of objects  | “lastName”: “Doe” }, |
|                      | that contain a       | { “lastName”: “Test” |
|                      | plucked property     | }, { “lastName”:     |
|                      | equal to a specific  | “Doe” }],            |
|                      | value.               | “lastName”, “Doe” )  |
|                      |                      | => 2                 |
+----------------------+----------------------+----------------------+
| Filter               | Filter an array to   | $arrayFilter([1, 2,  |
|                      | the values that      | 3, 4, 5, 3], 3) =>   |
|                      | match a regular      | [3, 3]               |
|                      | expression, a        |                      |
|                      | specific value, or   |                      |
|                      | non-null value       |                      |
+----------------------+----------------------+----------------------+
| FilterBy             | Filter an array of   | $arrayFilterBy([{    |
|                      | objects to those     | “age”: 10 }, {       |
|                      | that contain a       | “age”: 30 }, {       |
|                      | property or deeply   | “age”: 40 }], “age”, |
|                      | nested property      | 10) => [{ “age”: 10  |
|                      | whose values match a | }]                   |
|                      | regular expression,  |                      |
|                      | a specific value, or |                      |
|                      | non-null value.      |                      |
+----------------------+----------------------+----------------------+
| Flatten              | Flatten an array     | $arrayFlatten([1, 2, |
|                      | containing           | [3, 4]]) => [1, 2,   |
|                      | potentially nested   | 3, 4]                |
|                      | arrays to a single   |                      |
|                      | array                |                      |
+----------------------+----------------------+----------------------+
| Get Item in Array    | Retrieves an item    | $a                   |
|                      | from an array at a   | rrayGetAt([1,2,3],0) |
|                      | specific index.      | => 1                 |
|                      |                      | $a                   |
|                      |                      | rrayGetAt([1,2,3],1) |
|                      |                      | => 2                 |
|                      |                      | $a                   |
|                      |                      | rrayGetAt([1,2,3],2) |
|                      |                      | => 3                 |
|                      |                      | $ar                  |
|                      |                      | rayGetAt([1,2,3],-1) |
|                      |                      | => 3                 |
|                      |                      | $ar                  |
|                      |                      | rayGetAt([1,2,3],-2) |
|                      |                      | => 2                 |
|                      |                      | $ar                  |
|                      |                      | rayGetAt([1,2,3],-3) |
|                      |                      | => 1                 |
+----------------------+----------------------+----------------------+
| Get Items in Array   | Retrieves the items  | $arraySl             |
| within Index Range   | of an array that     | ice([1,2,3,4,5],1,3) |
|                      | exist within a       | => [2,3]             |
|                      | specific range.      |                      |
+----------------------+----------------------+----------------------+
| Get Largest Number   | Retrieves the        | $max([1,2,3]) => 3   |
| in Array             | largest number in an |                      |
|                      | array of numbers.    |                      |
+----------------------+----------------------+----------------------+
| Get Smallest Number  | Retrieves the        | $min([1,2,3]) => 1   |
| in Array             | smallest number in   |                      |
|                      | an array of numbers. |                      |
+----------------------+----------------------+----------------------+
| Max                  | Find the maximum     | $arrayMax([10, 30,   |
|                      | value in an array of | 40]) => 40           |
|                      | numbers.             |                      |
+----------------------+----------------------+----------------------+
| Min                  | Find the minimum     | $arrayMin(10, 30,    |
|                      | value in an array of | 40]) => 10           |
|                      | numbers.             |                      |
+----------------------+----------------------+----------------------+
| MinBy                | Find the minimum     | $arrayMinBy([{       |
|                      | value of a plucked   | “age”: 10 }, {       |
|                      | property of the      | “age”: 30 }, {       |
|                      | objects within an    | “age”: 40 }], “age”) |
|                      | array of objects.    | => 10                |
+----------------------+----------------------+----------------------+
| PluckBy              | Extract the values   | $arrayPluckBy([{     |
|                      | of a property or     | “color”: “Brown”,    |
|                      | deeply nested        | “type”: “Dog” },{    |
|                      | property of the      | “color”: “Beige”,    |
|                      | objects within an    | “type”: “Cat”        |
|                      | array of objects     | }],”type”) =>        |
|                      |                      | [“Dog”,”Cat”]        |
+----------------------+----------------------+----------------------+
| Prepend              | Returns an array     | $array               |
|                      | containing the       | Prepend([1,2,3],[-1, |
|                      | values of the second | 0]) => [-1, 0, 1, 2, |
|                      | array followed by    | 3]                   |
|                      | the values of the    |                      |
|                      | first array. If      |                      |
|                      | either input is not  |                      |
|                      | an array, returns an |                      |
|                      | array containing the |                      |
|                      | value of second      |                      |
|                      | input followed by    |                      |
|                      | the value of the     |                      |
|                      | first input.         |                      |
+----------------------+----------------------+----------------------+
| Remove Items from    | Removes all          | $arrayRemoveIte      |
| Arrays               | instances of a value | m([1,2,3,3,4,5,6],3) |
|                      | from an array.       | => [1,2,4,5,6]       |
+----------------------+----------------------+----------------------+
| Sort                 | Sort the items of an | $arraySort([3, 4,    |
|                      | array of strings or  | 1], “desc”) => [4,   |
|                      | numbers by value.    | 3, 1]                |
+----------------------+----------------------+----------------------+
| SortBy               | Sort the items of an | $arraySortBy( [{     |
|                      | array of objects by  | “user”: { “name”:    |
|                      | the value of a       | “Foo” } }, { “user”: |
|                      | plucked property of  | { “name”: ”Bar” } }, |
|                      | the objects within   | { “user”: { “name”:  |
|                      | the array.           | “Around” } }],       |
|                      |                      | “user.name”, “asc” ) |
|                      |                      | => [{ “user”: {      |
|                      |                      | “name”: “Around” }   |
|                      |                      | }, { “user”: {       |
|                      |                      | “name”: “Bar” } }, { |
|                      |                      | “user”: { “name”:    |
|                      |                      | “Foo” } }]           |
+----------------------+----------------------+----------------------+
| Sum                  | Sum the values of an | $arraySum([10, 30,   |
|                      | array of numbers.    | 40]) => 80           |
+----------------------+----------------------+----------------------+
| SumBy                | Sum the values of a  | $arraySumBy([{       |
|                      | plucked property of  | “age”: 10 }, {       |
|                      | the objects within   | “age”: 30 }, {       |
|                      | an array of objects. | “age”: 40 }], “age”) |
|                      |                      | => 80                |
+----------------------+----------------------+----------------------+

 

Object Transformations
----------------------

+------------------+------------------------+------------------------+
| Function         | Example Syntax         | Summary                |
+==================+========================+========================+
| Get Value by Key | Retrieves the value of | $lookup({"hello":      |
|                  | a property from an     | "world"},"hello") =>   |
|                  | object.                | "world"                |
+------------------+------------------------+------------------------+
| Has By           | Check if an object     | $objectHasBy({ key: 1  |
|                  | contains a property or | }, “key”) => true      |
|                  | deeply nested          |                        |
|                  | property.              |                        |
+------------------+------------------------+------------------------+
| Is Equal         | Perform a deep         | $objectIsEqual({       |
|                  | comparison between two | “age”: 30, “name”:     |
|                  | values to determine if | “joe” }, { “age”: 30,  |
|                  | they are equivalent.   | “name”: “joe” }) =>    |
|                  |                        | true                   |
+------------------+------------------------+------------------------+
| Pick             | Create an object       | $objectPick({          |
|                  | composed of the picked | “person”: { “name”:    |
|                  | properties.            | “joe” }, “age”: 30 },  |
|                  |                        | “age”) => { “age”: 30  |
|                  |                        | }                      |
+------------------+------------------------+------------------------+
| Pluck By         | Extract the value of a | $objectPluckBy({       |
|                  | property or deeply     | “person”: { “name”:    |
|                  | nested property of an  | “joe” }, “age”: 30 },  |
|                  | object.                | “person.name”) =>      |
|                  |                        | “joe”                  |
+------------------+------------------------+------------------------+
| Remove           | Remove a property on   | $objectRemove({        |
|                  | an object.             | “name”: “John” },      |
|                  |                        | “name”) => {}          |
+------------------+------------------------+------------------------+

 

Date/Time
---------

+-------------------+-----------------------+-----------------------+
| Function          | Example Syntax        | Summary               |
+===================+=======================+=======================+
| Convert Date/Time | Converts a date/time  | "2023                 |
|                   | to ISO-8601, Unix     | -04-04T13:09:51.013Z" |
|                   | epoch, or a custom    | ~>                    |
|                   | format.               | $dateCon              |
|                   |                       | vert("ISO-8601",null) |
|                   | **Important!** If you | =>                    |
|                   | select **Custom**,    | "2023                 |
|                   | the Output Format     | -04-04T13:09:51.013Z" |
|                   | String field shows.   | "2023                 |
|                   | Click the **plus**    | -04-04T13:09:51.013Z" |
|                   | icon to select a      | ~> $dateConvert("Unix |
|                   | playbook property or  | (seconds)",null) =>   |
|                   | manually enter a      | 1680613791.032        |
|                   | custom format that    | "2023                 |
|                   | follows `luxon table  | -04-04T13:09:51.013Z" |
|                   | of                    | ~> $dateConvert("Unix |
|                   | tokens <h             | (milliseconds)",null) |
|                   | ttps://moment.github. | => 1680613791032      |
|                   | io/luxon/#/parsing?id | "2023                 |
|                   | =table-of-tokens>`__. | -04-04T13:09:51.013Z" |
|                   |                       | ~>                    |
|                   | For example:          | $da                   |
|                   | MM/dd/yyyy.           | teConvert("SQL",null) |
|                   |                       | => "2023-04-04        |
|                   |                       | 13:09:51.045"         |
|                   |                       | "2023                 |
|                   |                       | -04-04T13:09:51.013Z" |
|                   |                       | ~>                    |
|                   |                       | $dateC                |
|                   |                       | onvert("Custom","DD") |
|                   |                       | => "Apr 4, 2023"      |
+-------------------+-----------------------+-----------------------+
| Set Time Zones    | Converts a date/time  | "2023                 |
|                   | to a specific time    | -04-04T14:36:12.145Z" |
|                   | zone or offset.       | ~>                    |
|                   |                       | $dateSet              |
|                   |                       | TimeZone("UTC-05:00") |
|                   |                       | =>                    |
|                   |                       | "2023-04-0            |
|                   |                       | 4T09:36:12.145-05:00" |
+-------------------+-----------------------+-----------------------+

 

Strings
-------

+-----------------+------------------------+------------------------+
| Function        | Example Syntax         | Summary                |
+=================+========================+========================+
| Camel Case      | Convert a string to    | $                      |
|                 | camel case.            | stringCamelCase(“hello |
|                 |                        | world”) =>             |
|                 |                        | “helloWorld”           |
+-----------------+------------------------+------------------------+
| Capitalize      | Convert the first      | $s                     |
|                 | character of a string  | tringCapitalize(“hello |
|                 | to upper case and the  | world”) = “Hello       |
|                 | remaining to lower     | world”                 |
|                 | case.                  |                        |
+-----------------+------------------------+------------------------+
| Defang String   | Replaces and/or        | $strin                 |
|                 | surrounds certain      | gDefang("192.168.1.1") |
|                 | characters in a string | => "192[.]168.1.1"     |
|                 | to render it           |                        |
|                 | unactionable (e.g.     |                        |
|                 | non-clickable).        |                        |
+-----------------+------------------------+------------------------+
| Distinct        | Returns an array       | $distinct([1,2,3,1])   |
|                 | containing the unique  | => [1,2,3]             |
|                 | values of the input    |                        |
|                 | array (duplicate       |                        |
|                 | values removed).       |                        |
+-----------------+------------------------+------------------------+
| Ends With       | Check if a string ends | $stringEndsWith(“abc”, |
|                 | with another.          | “c”) => true           |
+-----------------+------------------------+------------------------+
| Eval Expression | Parse and evaluate a   | $s                     |
|                 | string containing      | tringEvalExpression(“[ |
|                 | literal JSON or a      | 1,$string(number),3]”, |
|                 | JSONata expression.    | { “number”: 2 }) =>    |
|                 |                        | [1,”'2”, 3]            |
+-----------------+------------------------+------------------------+
| Hash            | Compute that hash of a | $stringHash(“data”,    |
|                 | value.                 | “MD5”) =>              |
|                 |                        | “8d777f385d3           |
|                 |                        | dfec8815d20f7496026dc” |
+-----------------+------------------------+------------------------+
| Pad             | Pad a string on the    | $stringPad('abc', 8)   |
|                 | left and right sides   | => “ abc “             |
|                 | if it's shorter than   |                        |
|                 | length. Padding        |                        |
|                 | characters are         |                        |
|                 | truncated if they      |                        |
|                 | can't be evenly        |                        |
|                 | divided by length.     |                        |
+-----------------+------------------------+------------------------+
| Pad End         | Pad a string on the    | $stringPadEnd(“abc”,   |
|                 | right side if it's     | 5,”h’’) => “abchh”     |
|                 | shorter than length.   |                        |
|                 | Padding characters are |                        |
|                 | truncated if they      |                        |
|                 | can't be evenly        |                        |
|                 | divided by length.     |                        |
+-----------------+------------------------+------------------------+
| Pad Start       | Pad a string on the    | $stringPadStart(“abc”, |
|                 | left side if it's      | 5,”h’’) => “hhabc”     |
|                 | shorter than length.   |                        |
|                 | Padding characters are |                        |
|                 | truncated if they      |                        |
|                 | can't be evenly        |                        |
|                 | divided by length.     |                        |
+-----------------+------------------------+------------------------+
| Refang String   | Restores a defanged    | $stringR               |
|                 | string to its original | efang("192[.]168.0.1") |
|                 | value to re-render it  | => 192.168.0.1         |
|                 | actionable (e.g.       |                        |
|                 | clickable).            |                        |
+-----------------+------------------------+------------------------+
| Repeat          | Repeat a string N      | $stringRepeat(“abc”,   |
|                 | times.                 | 2) => “abcabc”         |
+-----------------+------------------------+------------------------+
| Split           | Finds occurrences a    | $stringSplit("hello    |
|                 | delimiter in a string  | world"," ") =>         |
|                 | and splits the string  | ["hello", "world"]     |
|                 | into an array of       |                        |
|                 | substrings for each    |                        |
|                 | occurrence.            |                        |
+-----------------+------------------------+------------------------+
| Starts With     | Check if a string      | $s                     |
|                 | starts with another.   | tringStartsWith(“abc”, |
|                 |                        | “a”) => true           |
+-----------------+------------------------+------------------------+
| Strip           | Remove all whitespace  | $stringStrip(“ hello   |
|                 | (tabs, spaces, and     | word ”) => “hello      |
|                 | newlines) from both    | word”                  |
|                 | the left and right     |                        |
|                 | side of text. Spaces   |                        |
|                 | in between words will  |                        |
|                 | not be removed         |                        |
+-----------------+------------------------+------------------------+
| UUID v4         | Generate a v4          | $stringUuidv4() =>     |
|                 | universally unique     | “be407787-14e1-4       |
|                 | identifier (UUID).     | 7d1-9b25-9eaa624f7a5f” |
+-----------------+------------------------+------------------------+

 

Hashing/Signing
---------------

+---------------------+----------------------+----------------------+
| Function            | Example Syntax       | Summary              |
+=====================+======================+======================+
| Decode from Base 64 | Converts a base      | $stringBase64Decode  |
|                     | 64-encoded value to  | ("SGVsbG8gV29ybGQh") |
|                     | a string using a     | => "Hello World!"    |
|                     | UTF-8 encoding       |                      |
|                     | scheme.              |                      |
+---------------------+----------------------+----------------------+
| Encode to Base 64   | Converts a string to | $strin               |
|                     | base 64              | gBase64Encode("Hello |
|                     | representation.      | World!") =>          |
|                     |                      | "SGVsbG8gV29ybGQh"   |
+---------------------+----------------------+----------------------+

 

Value Transformations
---------------------

+----------------------+----------------------+----------------------+
| Function             | Example Syntax       | Summary              |
+======================+======================+======================+
| From XML             | Parse an XML string. | $                    |
|                      |                      | valueFromXml(“<a/>”) |
|                      |                      | => {“a”: {}}         |
+----------------------+----------------------+----------------------+
| From YAML            | Parse a YAML string. | $valueFromYaml(      |
|                      |                      | “version:            |
|                      |                      | 1.0.                 |
|                      |                      | 0\\ndependencies:\\n |
|                      |                      | yaml:                |
|                      |                      | ^                    |
|                      |                      | 1.10.0\\npackage:\\n |
|                      |                      | exclude:\\n -        |
|                      |                      | .idea/\**\\n -       |
|                      |                      | .gitignore\\n” ) =>  |
|                      |                      | { “version”:         |
|                      |                      | “1.0.0”,             |
|                      |                      | “dependencies”: {    |
|                      |                      | “yaml”: “^1.10.0”},  |
|                      |                      | “package”:           |
|                      |                      | {“exclude”:          |
|                      |                      | [“.idea/\*\*”,       |
|                      |                      | “.gitignore”]}}      |
+----------------------+----------------------+----------------------+
| Is Array             | Check if value is an | $valueIsArray([1, 4, |
|                      | array.               | 4]) => true          |
+----------------------+----------------------+----------------------+
| Is Null Or Undefined | Check if value is    | $valueIsN            |
|                      | null or undefined.   | ullOrUndefined(null) |
|                      |                      | => true              |
+----------------------+----------------------+----------------------+
| Is Object            | Check if a value is  | $valueIsObject({})   |
|                      | an object.           | => true              |
+----------------------+----------------------+----------------------+
| Is String            | Check if value is a  | $v                   |
|                      | string.              | alueIsString(“data”) |
|                      |                      | => true              |
+----------------------+----------------------+----------------------+
| To CSV               | Serialize a value to | $valueToCsv([ {      |
|                      | CSV.                 | “eruid”: “batman”,   |
|                      |                      | “description”: “uses |
|                      |                      | technology” }, {     |
|                      |                      | “eruid”: “superman”, |
|                      |                      | “description”:       |
|                      |                      | “flies through the   |
|                      |                      | air” } ]) =>         |
|                      |                      | “eruid,descr         |
|                      |                      | iption\\nbatman,uses |
|                      |                      | technol              |
|                      |                      | ogy\\nsuperman,flies |
|                      |                      | through the air\\n”  |
+----------------------+----------------------+----------------------+
| To XML               | Serialize a value to | $valueToXml({ “a”:   |
|                      | XML.                 | {} }) => “<a/>”      |
+----------------------+----------------------+----------------------+
| To YAML              | Serialize a value to | $valueToYaml({       |
|                      | YAML.                | “version”: “1.0.0”,  |
|                      |                      | “dependencies”: {    |
|                      |                      | “yaml”: “^1.10.0” }, |
|                      |                      | “package”: {         |
|                      |                      | “exclude”:           |
|                      |                      | [“.idea/\*\*”,       |
|                      |                      | “.gitignore”] } })   |
|                      |                      | => “version:         |
|                      |                      | 1.0.                 |
|                      |                      | 0\\ndependencies:\\n |
|                      |                      | yaml:                |
|                      |                      | ^                    |
|                      |                      | 1.10.0\\npackage:\\n |
|                      |                      | exclude:\\n -        |
|                      |                      | .idea/\**\\n -       |
|                      |                      | .gitignore\\n”       |
+----------------------+----------------------+----------------------+
