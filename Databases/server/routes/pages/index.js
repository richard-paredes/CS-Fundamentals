const express = require('express'),
    path = require('path'),
    router = express.Router({mergeParams:true});


router.get('/', async (req, res) => {
    
    return res.sendFile(path.join(__dirname + '/../../client/airlineweb.html'));
});

router.get('/customer', async (req, res) => {
    return res.sendFile(path.join(__dirname + '/../../client/pages/customer.html'));
});

router.get('/clerk', async(req, res) => {
    return res.sendFile(path.join(__dirname + '/../../client/pages/clerk.html'));
});

router.get('/admin', async (req, res) => {
    return res.sendFile(path.join(__dirname + '/../../client/pages/admin.html'));
});

module.exports = router;