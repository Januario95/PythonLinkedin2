-- wrk script for hitting the GEO server
wrk.method = "POST"
wrk.headers["Content-Type"] = "application/json"
wrk.body = [[
{
  "src": {
    "lat": 34.3852712,
    "lng": -119.487444
  },
  "dest": {
    "lat": 37.7765072,
    "lng": -122.3942272
  }
}
]]
