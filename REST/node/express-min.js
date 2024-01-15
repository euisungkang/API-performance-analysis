const express = require('express');

const data = require('../../model.json')

// Initialize App
const app = express();
app.use(express.json());

// Set PORT : 3000
const port = process.env.PORT || 3000;

// Run App
app.listen(port, () => {
    console.log("Server Listening on PORT:", port);
});

// get request
app.get("/rest_express", (req, res) => {
    return res.send(data)
});