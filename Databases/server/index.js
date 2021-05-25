const express = require('express'),
  cors = require('cors'),
  cookieParser = require('cookie-parser')
  app = express(),
  pageRoutes = require('./routes/pages/index'),
  todoRoutes = require('./routes/api/todos'),
  flightRoutes = require('./routes/api/flights'),
  airportRoutes = require('./routes/api/airports'),
  aircraftRoutes = require('./routes/api/aircrafts'),
  customerRoutes = require('./routes/api/customers'),
  bookingRoutes = require('./routes/api/bookings'),
  boardingPassRoutes = require('./routes/api/boardingpasses'),
  db_config = require('./database/config/initialize');


const allowed_origins = ["http://localhost:5000", "http://localhost:5500", "http://127.0.0.1:5500"];

// middleware
app.use(cors({ origin: allowed_origins, credentials: true}));
app.use(express.json());      //req.body
app.use(cookieParser());
app.use("/scripts", express.static(__dirname + '/client/scripts'));
app.use("/styles", express.static(__dirname + '/client/styles'));

//ROUTES
app.use('/', pageRoutes);
app.use('/api/todos', todoRoutes);
app.use('/api/flights', flightRoutes);
app.use('/api/airports', airportRoutes);
app.use('/api/aircrafts', aircraftRoutes);
app.use('/api/customers', customerRoutes);
app.use('/api/bookings', bookingRoutes);
app.use('/api/boardingpasses', boardingPassRoutes)

// set up the server listening at port 5000 (the port number can be changed)
app.listen(5000, async () => {
  // The next line of code sets the schema to our group schema, but doesn't work well at the moment
  // await db_config.set_schema(); 
  
  // await db_config.initialize_database();
  // await db_config.seed_database();
  console.log("Server has started on http://localhost:5000");
});