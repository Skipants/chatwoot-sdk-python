# Exceptions

All SDK exceptions inherit from `ChatwootError`. The exception hierarchy maps directly to HTTP status codes so you can catch as broadly or narrowly as needed.

```
ChatwootError
└── ChatwootAPIError
    ├── ChatwootAuthError        (401)
    ├── ChatwootPermissionError  (403)
    ├── ChatwootNotFoundError    (404)
    └── ChatwootValidationError  (400/422)
```

::: chatwoot.exceptions
