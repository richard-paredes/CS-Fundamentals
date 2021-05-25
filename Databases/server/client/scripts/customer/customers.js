let customer = null;
let selectedBooking = null;
let bookings = [];

const displayBookings = () => {
    document.querySelector('#input-bookings').removeAttribute('hidden');
    const bookingsTable = document.querySelector('#bookings-table');
    let bookingsHTML = "";
    bookings.map(booking => {
        // console.log(booking);
        bookingsHTML += `
        <tr key="${booking.book_ref}">
            <td>${booking.book_ref}</td>
            <td>${new Date(booking.book_date).toLocaleString()}</td>
            <td>${booking.tickets.length}</td>
            <td>$${(parseFloat(booking.payment.base_amount) + parseFloat(booking.payment.taxes) - parseFloat(booking.payment.discount)).toFixed(2)}
            <td>
                <button class="btn btn-outline-primary mr-2" data-toggle="modal" data-target="#edit-booking-modal" onclick="setBookingDetails(${booking.book_ref})">Details</button> 
                <button class="btn btn-primary ml-2" data-toggle="modal" data-target="#checkin-modal" onclick="populateCheckIn('${booking.book_ref}')">Check In</button>
            </td>
        </tr>
    `});
    bookingsTable.innerHTML = bookingsHTML;
};

const checkCheckInAvailability = (flight, ticket) => {
    return flight.status !== 'Cancelled'
        && flight.status !== 'Departed'
        && flight.status !== 'Arrived'
        && !ticket.flights.find(x => x.flight_id === flight.flight_id).is_waitlisted
        && !(ticket.boarding_passes.some(x => x.flight_id === flight.flight_id))
        && !(ticket.flights.some(x => !ticket.boarding_passes.some(y => y.flight_id === x.flight_id) && new Date(x.scheduled_departure) < new Date(flight.scheduled_departure)));
};

const getTicketFlightCheckInsHTML = (ticket) => {
    let detailsHTML = '';
    ticket.flights.forEach(flight => {
        const boarding_pass = ticket.boarding_passes.some(x => x.flight_id === flight.flight_id);
        // const can_checkin = flight.status = !ticket.flights.some(x => new Date(x.scheduled_departure).getTime() < new Date(flight.scheduled_departure).getTime());
        const can_checkin = checkCheckInAvailability(flight, ticket);
        if (!boarding_pass) {
            detailsHTML += `
                <div class="px-3 py-1 mb-1 alert-warning text-center border rounded">
                    <div class="">
                        <div class="badge d-block text-left">Departure: <span class="font-weight-bold">${flight.departure_airport} </span><span class="">@ ${new Date(flight.scheduled_departure).toLocaleString()}</span></div>
                        <div class="badge d-block text-left">Arrival: <span class="font-weight-bold">${flight.arrival_airport} </span><span class="">@ ${new Date(flight.scheduled_arrival).toLocaleString()}</span></div>
                        <div class="badge d-block text-left">Boarding: ${new Date(flight.boarding_time).toLocaleString()}</div>
                        <div class="badge d-block text-left">Status: 
                            <div class="badge ${flight.status === 'Cancelled' ? 'badge-danger' : 'badge-info'}">${flight.status.toUpperCase()}</div>
                        </div>
                    </div>
                    <button class="btn btn-sm btn-primary badge my-2" onclick="insertBoardingPass('${ticket.ticket_no}', '${flight.flight_id}')" ${!can_checkin && 'disabled'}>Get Boarding Pass</button>
                    ${flight.is_waitlisted ? `<div class="d-block badge my-1 badge-warning">WAITLISTED</div>` : ''}
                </div>
            `;
        }
    });
    return detailsHTML;
};

const getBaggageTagsHTML = (boarding_pass) => {
    let detailsHTML = '';
    boarding_pass.baggages.forEach(bag => {
        detailsHTML += `
            <div class="badge bg-dark text-white">
                <div>Type: ${bag.type}</div>
                <div>Tag: ${bag.baggage_id}</div>
            </div>
        `;
    });
    return detailsHTML;
};

const getTicketFlightBoardingPassesHTML = (ticket) => {
    let detailsHTML = '';
    ticket.boarding_passes.forEach(pass => {
        const flight = ticket.flights.find(x => x.flight_id === pass.flight_id);
        detailsHTML += `
            <div class="px-3 py-1 mb-1 alert-success text-center border rounded">
                <div class="">
                    <div class="badge d-block text-left">Departure: <span class="font-weight-bold">${flight.departure_airport} </span><span class="">@ ${new Date(flight.scheduled_departure).toLocaleString()}</span></div>
                    <div class="badge d-block text-left">Arrival: <span class="font-weight-bold">${flight.arrival_airport} </span><span class="">@ ${new Date(flight.scheduled_arrival).toLocaleString()}</span></div>
                    <div class="badge d-block text-left">Boarding: ${new Date(flight.boarding_time).toLocaleString()}</span></div>
                    <div class="badge d-block text-left">Departing Gate: ${flight.departure_gate}</div>
                    <div class="badge d-block text-left">Arrival Gate: ${flight.arrival_gate}</div>
                    <div class="badge d-block text-left">Baggage Claim: ${flight.baggage_claim}</div>
                    <div class="badge d-block text-left">Seat: ${pass.seat_no}</div>
                    <div class="badge d-block text-left">Status: <div class="badge ${flight.status === 'Cancelled' ? 'badge-danger' : 'badge-info'}">${flight.status.toUpperCase()}</div></div>
                    <div class="badge d-block text-left">Baggage:</div>
                    <div class="badge">
                        ${getBaggageTagsHTML(pass)}
                    </div>
                </div>
            </div>
        `
    });
    return detailsHTML
};

const populateCheckIn = (book_ref) => {
    selectedBooking = bookings.find(x => x.book_ref == book_ref);
    
    let innerHTML = '<div>'
    selectedBooking.tickets.forEach(ticket => 
        innerHTML += `
            <div class="bg-light p-3 my-2 border">
                <div class="row mb-3">
                    <div class="col-md-12">
                        <span class="font-weight-bold">${ticket.passenger.first_name}</span> <span class="font-weight-bold">${ticket.passenger.last_name}</span>
                    </div>
                </div>

                <div class="accordion" id="accordion">
                    <div class="card">
                        <div class="card-header" id="headingOne">
                            <h2 class="mb-0">
                                <button class="btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapseOne_${ticket.passenger.passenger_id}" aria-expanded="true" aria-controls="collapseOne_${ticket.passenger.passenger_id}">
                                Flight Check-In
                                </button>
                            </h2>
                        </div>
                        <div id="collapseOne_${ticket.passenger.passenger_id}" class="collapse" aria-labelledby="headingOne" data-parent="#accordion">
                            <div class="card-body">
                                <div class="d-flex justify-content-around flex-wrap">
                                    ${getTicketFlightCheckInsHTML(ticket)}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card-header" id="headingTwo">
                            <h2 class="mb-0">
                                <button class="btn btn-link btn-block text-left collapsed" type="button" data-toggle="collapse" data-target="#collapseTwo_${ticket.passenger.passenger_id}" aria-expanded="false" aria-controls="$collapseTwo_${ticket.passenger.passenger_id}">
                                    Boarding Passes
                                </button>
                            </h2>
                        </div>
                        <div id="collapseTwo_${ticket.passenger.passenger_id}" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
                            <div class="card-body">
                                <div class="d-flex justify-content-around flex-wrap">
                                    ${getTicketFlightBoardingPassesHTML(ticket)}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>`
    );
    innerHTML += '</div>'
    document.querySelector('#checkin-details').innerHTML = innerHTML;
};

const getTicketFlightDetailsHTML = (ticket) => {
    let detailsHTML = ``;
    ticket.flights.forEach(flight => { 
        const canUpdate = flight.status !== 'Boarding' 
            && flight.status !== 'Cancelled'
            && flight.status !== 'Departed'
            && flight.status !== 'Arrived'
            && !(ticket.boarding_passes.some(x => x.flight_id === flight.flight_id)) ;
        detailsHTML += 
        `<div class="">
        <h6 class="mt-3">Flight: ${flight.departure_airport} to ${flight.arrival_airport}</h6>
            <div class="form-row">
                <div class="col-md-6">
                    <label for="checked-bags">Checked bags</label>
                    <div class="input-group mb-3">
                        ${
                            canUpdate ? `
                            <div class="input-group-prepend">
                                <span class="input-group-btn btn btn-outline-primary"
                                    onclick="baggageInputHandler('decrement', '#passenger_${ticket.passenger.passenger_id}_flight_${flight.flight_id}_checked_bags', 0)">&minus;</span>
                            </div>
                            ` : ''
                        }
                        <input type="number" id="passenger_${ticket.passenger.passenger_id}_flight_${flight.flight_id}_checked_bags" 
                            name="passenger_${ticket.passenger.passenger_id}_flight_${flight.flight_id}_checked_bags" 
                            readonly min="1" max="5" step="1" class="form-control text-center" value="${flight.checked_bags}" ${!canUpdate && 'disabled'}>
                        ${
                            canUpdate ? `
                            <div class="input-group-append">
                            <span class="input-group-btn btn btn-outline-primary"
                                onclick="baggageInputHandler('increment', '#passenger_${ticket.passenger.passenger_id}_flight_${flight.flight_id}_checked_bags', 3)">&plus;</span>
                            </div>
                            ` : ''
                        }
                    </div>
                </div>
                <div class="col-md-6">
                    <label for="carry-ons">Carry Ons</label>
                    <div class="input-group mb-3">
                        ${
                        canUpdate ? `
                        <div class="input-group-prepend">
                            <span class="input-group-btn btn btn-outline-primary"
                                onclick="baggageInputHandler('decrement', '#passenger_${ticket.passenger.passenger_id}_flight_${flight.flight_id}_carry_ons', 0)">&minus;</span>
                        </div>
                        ` : ''
                        }
                        <input type="number" id="passenger_${ticket.passenger.passenger_id}_flight_${flight.flight_id}_carry_ons" name="passenger_${ticket.passenger.passenger_id}_flight_${flight.flight_id}_carry_ons" 
                            readonly min="1" max="5" step="1" class="form-control text-center" value="${flight.carry_ons}">
                        ${
                        canUpdate ? `
                        <div class="input-group-append">
                            <span class="input-group-btn btn btn-outline-primary"
                                onclick="baggageInputHandler('increment', '#passenger_${ticket.passenger.passenger_id}_flight_${flight.flight_id}_carry_ons', 2)">&plus;</span>
                        </div>
                        ` : ''
                        }
                    </div>
                </div>
            </div>
            <div class="form-row">
                <div class="col-md-6">
                    <label for="fare_conditions">Seat Fare</label>
                    <select class="custom-select" id="passenger_${ticket.passenger.passenger_id}_flight_${flight.flight_id}_fare_conditions" name="passenger_${ticket.passenger.passenger_id}_flight_${flight.flight_id}_fare_conditions" required ${!canUpdate && 'disabled'}>
                        <option value="Economy" ${flight.fare_conditions === 'Economy' && 'selected'}>Economy ${(flight.is_waitlisted && flight.fare_conditions === 'Economy') ? '(Waitlisted)' :''}</option>
                        <option value="Business" ${flight.fare_conditions === 'Business' && 'selected'}>Business ${(flight.is_waitlisted && flight.fare_conditions === 'Business') ? '(Waitlisted)' :''}</option>
                        <option value="First" ${flight.fare_conditions === 'First' && 'selected'}>First ${(flight.is_waitlisted && flight.fare_conditions === 'First') ? '(Waitlisted)' :''}</option>
                    </select>
                </div>
            </div>
            <input type="hidden" name="passenger_${ticket.passenger.passenger_id}_flight_${flight.flight_id}_old_fare_conditions" value="${flight.fare_conditions}" />
            </div>
        `
    });
    return detailsHTML;
};

const setBookingDetails = (book_ref) => {
    selectedBooking = bookings.find(x => x.book_ref == book_ref);
    let booked_flights = selectedBooking.tickets[0].flights;
    let innerHTML = `<div>`;
    
    if (booked_flights) {
        innerHTML += `
                <div>
                    <h6>Flight Details</h6>
        `;

        booked_flights.forEach(flight => 
            innerHTML += `
            <div class="px-3 py-1 mb-1 bg-warning rounded">
                <div class="badge d-block text-left">Departure: <span class="font-weight-bold">${flight.departure_airport} </span><span class="">@ ${new Date(flight.scheduled_departure).toLocaleString()}</span></div>
                <div class="badge d-block text-left">Arrival: <span class="font-weight-bold">${flight.arrival_airport} </span><span class="">@ ${new Date(flight.scheduled_arrival).toLocaleString()}</span></div>
                ${flight.includes_movie ? `<div class="badge d-block text-left text">Movie Included</div>` : ''}
                ${flight.includes_meal ? `<div class="badge d-block text-left text">Meal Included</div>` : ''}
                ${flight.allow_waitlist ? `<div class="badge d-block text-left text">Seat Waitlisting Enabled (performed automatically)</div>` : ''}
                <div class="badge d-block text-left">Status: <div class="badge ${flight.status === 'Cancelled' ? 'badge-danger' : 'badge-info'}">${flight.status.toUpperCase()}</div></div>
            </div>
            `
        );
        innerHTML += '</div>'
    }
    innerHTML += `
        <div>
            <h6>Payment Details</h6>
            <div class="px-3 py-1 mb-2 rounded" style="background-color:#ececec !important;">
                <div class="badge d-block text-left mb-1">Card Number: ${selectedBooking.payment.card_no}</div>
                <div class="badge d-block text-left">Price: $${parseFloat(selectedBooking.payment.base_amount).toFixed(2)}</div>
                <div class="badge d-block text-left">Discount: $${parseFloat(selectedBooking.payment.discount).toFixed(2)}</div>
                <div class="badge d-block text-left">Taxes: $${parseFloat(selectedBooking.payment.taxes).toFixed(2)}</div>
                <div class="badge d-block text-left border-top">Total: $${(parseFloat(selectedBooking.payment.base_amount) + parseFloat(selectedBooking.payment.taxes) - parseFloat(selectedBooking.payment.discount)).toFixed(2)}</div>
            </div>
        </div>
    </div>
    `;

    let ticketHTML = ``;
    selectedBooking.tickets.forEach(ticket => 
        ticketHTML += `
            <div class="bg-light p-3 my-2 border">
                <div class="form-row">
                    <div class="form-group col-md-6">
                        <label for="passenger_${ticket.passenger.passenger_id}_first_name">First Name</label>
                        <input type="text" class="form-control" name="passenger_${ticket.passenger.passenger_id}_first_name" value="${ticket.passenger.first_name}" onblur="onBlur(event)"/>
                    </div>
                    <div class="form-group col-md-6">
                        <label for="passenger_${ticket.passenger.passenger_id}_last_name">Last Name</label>
                        <input type="text" class="form-control" name="passenger_${ticket.passenger.passenger_id}_last_name" value="${ticket.passenger.last_name}" onblur="onBlur(event)"/>
                    </div>
                    <input type="hidden" name="passenger_${ticket.passenger.passenger_id}_ticket_no" value="${ticket.ticket_no}" />
                </div>
                <div>
                    ${getTicketFlightDetailsHTML(ticket)}
                </div>
            </div>`
    );

    innerHTML += `
        <div>
            <h6>Ticket Details</h6>
            <div class="mb-2 rounded">
                ${ticketHTML}
            </div>
        </div>
        <input type="hidden" name="book_ref" value="${selectedBooking.book_ref}" />
        <input type="hidden" name="payment_ref" value="${selectedBooking.payment.payment_ref}" />
        <input type="hidden" name="flight_ids" value="${booked_flights.map(x => x.flight_id).join(',')}"
    </div>
    `;
    if (selectedBooking.tickets.some(x => x.boarding_passes.length > 0) || selectedBooking.tickets.some(x => x.flights.some(y => y.status === 'Cancelled' || y.status === 'Departed' || y.status === 'Arrived'))) {
        document.querySelector('#booking-cancel-btn').setAttribute('disabled', 'true');
    } else {
        document.querySelector('#booking-cancel-btn').removeAttribute('disabled');
    }
    if (selectedBooking.tickets.every(x => x.boarding_passes.length === x.flights.length) || selectedBooking.tickets.some(x => x.flights.some(y => y.status === 'Cancelled' || y.status === 'Departed' || y.status === 'Arrived'))) {
        document.querySelector('#booking-save-btn').setAttribute('disabled', 'true');
    } else {
        document.querySelector('#booking-save-btn').removeAttribute('disabled');
    } 
    if (selectedBooking.tickets.some(x => x.flights.some(y => y.status === 'Cancelled'))) {
        document.querySelector('#refund-alert').removeAttribute('hidden')
    } else {
        document.querySelector('#refund-alert').setAttribute('hidden', 'true');
    }
    document.querySelector('#booking-selected-flight-details').innerHTML = innerHTML;
};

const selectCustomer = async () => {
    try {
        const response = await fetch('/api/customers', {
            method: "GET",
            credentials: "include"
        });
        const json = await response.json();
        // console.log(customer_data);
        if (response.status === 200) {
            if (json && json.customers && json.bookings) {
                customer = json.customers[0];
                bookings = json.bookings;
                document.querySelector('#signup-button').setAttribute('hidden', 'true');
                document.querySelector('#login-button').setAttribute('hidden', 'true');
                document.querySelector('#logout-button').removeAttribute('hidden');
                displayBookings();
            }
        }
    } catch (err) {
        // console.log(err);
        handleError(err);
    }
};



const insertCustomer = async (event) => {
    try {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);

        var customer_details = {};
        formData.forEach((value, key) => {
            customer_details[key] = value;
        });

        const response = await fetch("/api/customers", {
            method: "POST",
            credentials: "include",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(customer_details)
        });
        const json = await response.json();
        if (response.status === 200) {
            location.reload();
        } else {
            handleError(json);
        }
    } catch (err) {
        // console.log(err.message);
        handleError(err);
    }
};

const insertBoardingPass = async (ticket_no, flight_id) => {
    try {
        const boarding_pass_details = {
            ticket_no: ticket_no,
            flight_id: flight_id
        };
        const response = await fetch(`/api/boardingpasses`, {
            method: "POST",
            credentials: "include",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(boarding_pass_details)
        });
        const json = await response.json();
        if (response.status === 200) {
            location.reload();
        } else {
            handleError(json);
        }
    } catch (err) {
        handleError(err);
    }
};

const editBooking = async (event) => {
    try {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        const passengers = [];
        let flight_ids = [];
        const booking_details = {};
        formData.forEach((value, key) => {
            if (key.startsWith('flight_ids')) {
                flight_ids = value.split(',');
            } else if (key.startsWith('passenger')) {
                let split_idx = key.slice(10).indexOf('_');
                let passenger_id = key.slice(10,10+split_idx);
                let passenger = passengers.find(x => x.passenger_id === passenger_id);
                if (!passenger) {
                    passenger = {
                        passenger_id: passenger_id,
                    };
                    passengers.push(passenger);
                }
                passenger[key.slice(10+split_idx+1)] = value;
            } else {
                booking_details[key] = value;
            }
        });

        booking_details['passengers'] = passengers;
        booking_details['flight_ids'] = flight_ids;
        // console.log(passengers);
        
        const response = await fetch(`/api/bookings/${selectedBooking.book_ref}`, {
            method: "PUT",
            credentials: "include",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(booking_details)
        });
        const json = await response.json();
        if (response.status === 200) {
            location.reload();
        } else {
            handleError(json);
        }
    } catch (err) {
        // console.log(err.message);
        handleError(err);
    }
};

const deleteBooking = async () => {
    try {
        const response = await fetch(`/api/bookings/${selectedBooking.book_ref}`, {
            method: "DELETE",
            credentials: "include"
        });
        const json = await response.json();
        if (response.status === 200) {
            location.reload();
        } else {
            handleError(json);
        }
    } catch (err) {
        // console.log(err.message);
        handleError(err);
    }
};

const loginCustomer = async (event) => {
    try {
        event.preventDefault();
        const customer_data = {};
        const formData = new FormData(event.currentTarget);
        formData.forEach((val, key) => customer_data[key] = val);

        const response = await fetch("/api/customers/login", {
            method: "POST",
            credentials: "include",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(customer_data)
        });
        const json = await response.json();
        if (response.status === 200) {
            location.reload();
        } else {
            handleError(json);
        }
    } catch (err) {
        handleError(err, 'Invalid customer login.');
    }
};

const logoutCustomer = async () => {
    try {
        const response = await fetch("/api/customers/logout", {
            method: "POST",
            credentials: "include"
        });
        const json = await response.json();
        if (response.status === 200) { 
            document.querySelector('#login-button').removeAttribute('hidden');
            document.querySelector('#logout-button').setAttribute('hidden', 'true');
            location.reload();
        } else {
            handleError(json);
        }
    } catch (err) {
        handleError(err)
    }
}

selectCustomer();