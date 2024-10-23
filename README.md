# PRA5: ML Deployment

This repo is for a small fake news classifier hosted at
[planelle.us-east-2.elasticbeanstalk.com](http://planelle.us-east-2.elasticbeanstalk.com/)

## API documentation

### POST /is-fake

Returns a list of "REAL" or "FAKE" classes for the list of documents passed

#### Request body

```json
{
    "documents": [
        "Document 1 (fake)",
        "Document 2 (real)",
        ...
    ]
}
```

#### Response body

```json
{
    "results": [
        "FAKE",
        "REAL",
        ...
    ]
}
```

## Latency distribution

![Latency distribution box plot](Latency Box Plot.png)
