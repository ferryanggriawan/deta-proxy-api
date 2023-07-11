# proxy api
Simple proxy cors

## Swagger docs
https://proxypass-1-a3415167.deta.app/docs

## usage
example fetch with axios
```javascript
const response = await axios.post("https://proxypass-1-a3415167.deta.app/proxy-api/json", {
  headers: {
    "Content-Type": "application/json"
  }, // header to pass in the url
  url: "http://your-api.com/path",
  methods: "your api methods [get, post, put, delete, patch, dll]",
  params: {}
})
```
