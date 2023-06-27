# deta-proxy-api
Simple proxy cors

## usage
example fetch with axios
```javascript
const response = await axios.post("http://127.0.0.1:8000/proxy-api", {
  headers: {
    "Content-Type": "application/json"
  }, // header to pass in the url
  url: "http://your-api.com/path",
  methods: "your api methods [get, post, put, delete, patch, dll]",
  params: {}
})
```
