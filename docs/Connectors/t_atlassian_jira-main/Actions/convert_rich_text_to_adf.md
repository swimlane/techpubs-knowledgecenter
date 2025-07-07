# Convert Rich text to ADF

**Description**: Converts rich text to Atlassian Document Format (ADF) to ensure compatibility with Jira applications.

## Inputs

- **rich_text** (object)
  - **summary** (string)
## Output

### Example

```json
[
  {
    "summary": {
      "version": 1,
      "type": "doc",
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "This is a test."
            },
            {
              "type": "text",
              "text": "This is a test.",
              "marks": [
                {
                  "type": "strong"
                }
              ]
            },
            {
              "type": "text",
              "text": "This is a test.",
              "marks": [
                {
                  "type": "em"
                }
              ]
            },
            {
              "type": "text",
              "text": "This is a test.",
              "marks": [
                {
                  "type": "textColor",
                  "attrs": {
                    "color": "#f1c40f"
                  }
                }
              ]
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "This is a test.",
              "marks": [
                {
                  "type": "textColor",
                  "attrs": {
                    "color": "#e03e2d"
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    "title": {
      "version": 1,
      "type": "doc",
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "this is test."
            }
          ]
        }
      ]
    },
    "praveen": {
      "version": 1,
      "type": "doc",
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "This is a demo case description, with Rich Text, to show that it works in Jira."
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "For "
            },
            {
              "type": "text",
              "text": "example, paragraphs",
              "marks": [
                {
                  "type": "strong"
                }
              ]
            },
            {
              "type": "text",
              "text": ", "
            },
            {
              "type": "text",
              "text": "colours, bolding",
              "marks": [
                {
                  "type": "textColor",
                  "attrs": {
                    "color": "#ba372a"
                  }
                }
              ]
            },
            {
              "type": "text",
              "text": ", etc.",
              "marks": [
                {
                  "type": "em"
                }
              ]
            }
          ]
        }
      ]
    },
    "gen": {
      "version": 1,
      "type": "doc",
      "content": []
    },
    "p1": {
      "version": 1,
      "type": "doc",
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "1"
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "2",
              "marks": [
                {
                  "type": "strong"
                }
              ]
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "3",
              "marks": [
                {
                  "type": "em"
                }
              ]
            }
          ]
        }
      ]
    },
    "p2": {
      "version": 1,
      "type": "doc",
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "4"
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "5",
              "marks": [
                {
                  "type": "strong"
                }
              ]
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "6",
              "marks": [
                {
                  "type": "em"
                }
              ]
            }
          ]
        }
      ]
    },
    "p3": {
      "version": 1,
      "type": "doc",
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "7"
            }
          ]
        }
      ]
    }
  }
]
```
### Output Parameters

- **summary** (object)
  - **version** (number)
  - **type** (string)
  - **content** (array)
    - **type** (string)
    - **content** (array)
      - **type** (string)
      - **text** (string)
      - **marks** (array)
        - **type** (string)
        - **attrs** (object)
          - **color** (string)
- **title** (object)
  - **version** (number)
  - **type** (string)
  - **content** (array)
    - **type** (string)
    - **content** (array)
      - **type** (string)
      - **text** (string)
- **praveen** (object)
  - **version** (number)
  - **type** (string)
  - **content** (array)
    - **type** (string)
    - **content** (array)
      - **type** (string)
      - **text** (string)
      - **marks** (array)
        - **type** (string)
- **gen** (object)
  - **version** (number)
  - **type** (string)
  - **content** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
- **p1** (object)
  - **version** (number)
  - **type** (string)
  - **content** (array)
    - **type** (string)
    - **content** (array)
      - **type** (string)
      - **text** (string)
      - **marks** (array)
        - **type** (string)
- **p2** (object)
  - **version** (number)
  - **type** (string)
  - **content** (array)
    - **type** (string)
    - **content** (array)
      - **type** (string)
      - **text** (string)
      - **marks** (array)
        - **type** (string)
- **p3** (object)
  - **version** (number)
  - **type** (string)
  - **content** (array)
    - **type** (string)
    - **content** (array)
      - **type** (string)
      - **text** (string)